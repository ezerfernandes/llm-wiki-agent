---
title: "BetterTogether"
type: concept
tags: [dspy, optimizer, meta-optimizer, bootstrap, finetune, prompt-optimization]
sources: [2407.10930-better-together, dspy-optimizers, 2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# BetterTogether

**`dspy.BetterTogether`** is the [[DSPy]] **meta-optimizer** that **alternates prompt optimization and weight fine-tuning** over a compound LM program. Introduced as Algorithm 1 of [[2407.10930-better-together|Soylu, Potts & Khattab (2024)]] and released in DSPy as the **single-entry Meta-Optimizer family** of [[DSPyOptimizers|the catalog]].

## Algorithm

Given a compound system $\Phi_{\langle\Theta,\Pi\rangle}$ with module-level prompts $\Pi$ and LM weights $\Theta$, training set $X$, and metric $\mu$:

```
function BetterTogether(Φ_{⟨Θ,Π⟩}, X, μ):
  Π′  ← OptimizePrompts(Φ_{⟨Θ,Π⟩},  X, μ)
  Θ′  ← FinetuneWeights(Φ_{⟨Θ,Π′⟩}, X, μ)
  Π″  ← OptimizePrompts(Φ_{⟨Θ′,Π⟩}, X, μ)
  return Φ_{⟨Θ′, Π″⟩}
```

The canonical instantiation: `OptimizePrompts ← `[[BootstrapFewShotWithRandomSearch|`BootstrapFewShotRS`]] and `FinetuneWeights ← `[[BootstrapFinetune|`BootstrapFinetune`]]. Any of the three steps can be omitted, yielding the eight strategies in Table 1 of the paper.

## The two-direction motivation

The paper's hypothesis decomposes into two halves:

1. **Prompt-opt *before* fine-tune → better SFT dataset.** [[BootstrapFinetune|BFT]] builds its supervised dataset from program traces whose final output passes the metric. A prompt-optimized program produces **more passing traces** on the same training set, giving fine-tuning more (and higher-quality) supervision. The [[2407.10930-better-together|paper]]'s Iris-llama-2 cell demonstrates this hard-stop: vanilla zero-shot is 0% accurate, so Θ-only fine-tuning has **no traces** to learn from ("—" in the table) — but Π → Θ works because the prompt-opt step lifts the bootstrap into a usable regime.

2. **Prompt-opt *after* fine-tune → adjust to new weights.** A fine-tuned LM has a shifted prior; the prompts that were optimal for the prompted-only model are no longer optimal. Re-running prompt optimization against the *fine-tuned* model produces module-specific instructions and demos calibrated to the new weights.

## The eight-strategy grid

| Strategy | What it does |
|---|---|
| Vanilla | No optimization. |
| Π | Prompt-opt only. |
| Θ | Fine-tune only (vanilla bootstrap). |
| Π → Π | Repeated prompt-opt — controls for "more compute on the prompt axis." |
| Θ → Θ | Repeated fine-tune — controls for "more compute on the weight axis." |
| Π → Θ | BetterTogether: prompt-opt, then fine-tune. |
| Θ → Π | BetterTogether: fine-tune, then prompt-opt. |
| **Π → Θ → Π** | **Full BetterTogether (Algorithm 1)**. |

**The three BetterTogether strategies (last three) win in 7 of 9 (dataset, LM) cells**, with Π → Θ → Π the typical winner. The two repeated-same-axis baselines (Π→Π, Θ→Θ) **isolate the alternation effect** from "just more optimization compute."

## Position in the optimizer catalog

| Family | Optimizers | What's tuned |
|---|---|---|
| Few-Shot | `LabeledFewShot`, [[BootstrapFewShot]], [[BootstrapFewShotWithRandomSearch]], `KNNFewShot` | Demonstrations |
| Instruction | `COPRO`, [[MIPROv2]], `SIMBA`, [[GEPA]] | Instructions |
| Finetuning | [[BootstrapFinetune]] | LM weights |
| Program Transformation | `Ensemble` | Composition |
| **Meta-Optimizer** | **`BetterTogether`** (this page) | **Sequence of optimizers** |

BetterTogether is **the only meta-optimizer in the catalog** — it doesn't tune $\Pi$ or $\Theta$ directly; it **composes other optimizers** along a fixed three-step schedule. The DSPy [[BootstrapFinetune|BootstrapFinetune]] page explicitly names this composition pattern: *"You can run `dspy.MIPROv2` and use the produced program ... to `dspy.BootstrapFinetune` to get better results. This is partly the essence of `dspy.BetterTogether`."*

## Empirical results ([[2407.10930-better-together|Soylu et al. 2024]])

Three datasets × three LMs:

- **HotPotQA** (3-module CoT + frozen [[ColBERTv2]] retriever): gains **5–78%** over the better of prompts-only / weights-only.
- **GSM8K** (1-module CoT): gains **2.5–10%**.
- **Iris** (1-module CoT classification): gains **3.5–88%**.

Best single configurations (bold in Table 1): Π → Θ → Π wins on HotPotQA-mistral (37.6) and HotPotQA-llama-2 (34.8); Θ → Π wins on GSM8K-mistral (48.3) and Iris-mistral (66.7).

Per-task pattern:
- **HotPotQA** (largest gains; 3-module pipeline = most "compound" structure to exploit).
- **GSM8K** (smallest gains; 1-module CoT, little compound structure).
- **Iris** (largest *relative* gains; 50-example train set means prompt-opt is essential).

## Implementation notes

- **BFRS** for prompt steps: 6 candidate programs × up to 3 few-shot examples per module prompt; `BootstrapFewShotRS` with random search over generated subsets, scored by $\mu$ on a held-out validation split.
- **BFT** for the weight step: [[lora|LoRA]] rank 32, alpha 64, no dropout; bfloat16; 5 epochs; lr 1e-5; effective batch size 8; query+key self-attention layers only.
- **The vanilla-prompt substitution trick** inside BFT: each bootstrapped trace's optimized prompt is **replaced with the vanilla (zero-shot) prompt** before fine-tuning. The fine-tuned model thus learns to produce the metric-passing completions *without* the optimized prompts at inference. (See [[BootstrapFinetune#The training-at-runtime trick|BootstrapFinetune's training-at-runtime trick]] for the structurally identical Banking77 example.)
- **All modules in Φ share the same base LM** at initialization; LoRA adapts a single set of weights that every module then routes through.

## Why this matters

The [[CompoundAISystem|compound-AI-system]] framing has two learnable axes — $\Pi$ (prompts) and $\Theta$ (weights). Before this paper, the **DSPy** catalog had separate optimizers for each axis but **no published evidence** that running them together would beat running either alone. BetterTogether is the **first published bi-axial optimizer** for LM programs, and the result *"7 of 9 cells favor alternation"* is the empirical basis for the wiki's claim that **prompts and weights are complementary, not redundant** learning channels. The result also frames the [[2507.19457-gepa|GEPA (2026)]] question — *"can we replace the weight axis entirely with smarter prompt-only optimization?"* — which GEPA answers affirmatively in the *sample-constrained frontier-LM* regime.

## 2026 empirical caveat ([[2604.14585-prompt-optimization-coin-flip|Zhang et al. 2026]])

BetterTogether's $\Pi \to \Theta \to \Pi$ alternation rests on an **assumption of axis coupling**: that prompt-opt before fine-tune produces a higher-quality SFT dataset *because* the prompt and weight steps interact, and that prompt-opt after fine-tune adjusts prompts to the shifted prior *because* the fine-tuned LM behaves differently from the original. [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] do not directly test the $\Pi \times \Theta$ axis pair (they decompose two-agent feed-forward pipelines along the prompt × prompt axis pair instead), but their finding — **no significant cross-axis interaction** in any of six tested model×task conditions — generalizes naturally to the bi-axial question. An open follow-up: run the [[ANOVAVarianceDecomposition|ANOVA decomposition]] over the (prompt, weight) factor pair on one of BetterTogether's 9 cells; if $F_{\Pi \times \Theta} < 1$, then BetterTogether's *7-of-9-cells-win* may reflect a sum of independent main effects rather than alternation-specific gains.

## Connections

- [[2407.10930-better-together]] — the canonical paper introducing this algorithm.
- [[DSPy]] — the framework; `dspy.BetterTogether` ships as the Meta-Optimizer family.
- [[DSPyOptimizers]] — the catalog this optimizer sits at the top of.
- [[BootstrapFewShotWithRandomSearch]] — `OptimizePrompts` instantiation.
- [[BootstrapFinetune]] — `FinetuneWeights` instantiation.
- [[MIPROv2]] — alternative `OptimizePrompts` instantiation; the [[BootstrapFinetune]] page names the `MIPROv2 → BootstrapFinetune` composition as *"partly the essence of `dspy.BetterTogether`"*.
- [[CompoundAISystem]] — the formalism this algorithm operates on.
- [[GEPA]] — the next-generation prompt-only optimizer that, in the frontier-LM regime, outperforms even BetterTogether-style alternation.
- [[lora|LoRA]] — the PEFT method used in the weight step.
- [[hotpotqa|HotPotQA]] / [[GSM8K]] / [[Iris]] — the three benchmark tasks.
- [[FineTuning]] — the weight-axis regime.
- [[DilaraSoylu]] / [[ChristopherPotts]] / [[OmarKhattab]] — authors.
- [[2604.14585-prompt-optimization-coin-flip]] — empirical audit of the cross-axis coupling premise; introduces the [[ANOVAVarianceDecomposition|ANOVA]] test the bi-axial schedule should be evaluated against.
- [[AgentCoupling]] / [[JointOptimization]] / [[IndependentOptimization]] — concept tree for the coupling question BetterTogether's design assumes positively.
