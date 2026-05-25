---
title: "HotpotQA"
type: concept
tags: [concept, benchmark, qa, multi-hop]
sources: [2605.12357-delta-mem, 2507.19457-gepa, 2407.10930-better-together, 2406.11695-mipro, 2312.13382-dspy-assertions, 2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# HotpotQA

Multi-hop QA dataset (Yang et al., EMNLP 2018) requiring reasoning over multiple Wikipedia paragraphs. Two question types: **Bridge** (true multi-hop, where one fact bridges to another) and **Comparison** (compare attributes of two entities). Metrics: Exact Match (EM) and F1.

Used in [[2605.12357-delta-mem]] as a memory-heavy reasoning benchmark and — more revealingly — in the **no-context ablation**: with all explicit context removed, δ-mem's online state alone lifts overall EM from **0.08% → 6.48%** and F1 from **8.27% → 15.20%**; Bridge subset EM from 0.08% → 3.97%. The compact $8 \times 8$ state retains usable multi-hop signal.

## In [[2507.19457-gepa|GEPA]] (ICLR 2026)

HotpotQA is one of six core benchmarks. GEPA's largest cross-model-generalization gain is on HotpotQA — prompts optimized on Qwen3 8B and evaluated on GPT-4.1 Mini *without modification* gain **+27.67%** on HotpotQA. The optimized prompt for the second-hop query generator (paper Figure 2) is a multi-section declarative prose document — "Input Understanding / Purpose and Context / Key Observations and Lessons / How to Build the Query / Practical Strategy / Output" — that has no few-shot exemplars and is the paper's headline illustration of how rich reflectively-evolved instructions become.

| Optimizer | Qwen3 8B | GPT-4.1 Mini | GEPA-Qwen-Opt (Qwen-trained → GPT-4.1-eval) |
|---|---|---|---|
| Baseline | 42.33 | 38.00 | — |
| [[grpo|GRPO]] | 43.33 | — | — |
| [[MIPROv2]] | 55.33 | 58.00 | — |
| **GEPA** | 62.33 | **69.00** | **65.67** |
| **GEPA+Merge** | **64.33** | 65.67 | — |

## In [[2406.11695-mipro|Opsahl-Ong et al. (2024)]] — MIPRO

HotPotQA is one of seven tasks in the [[DSPyOptimizerBenchmark]]. The DSPy program is a **2-module multi-hop retrieval** pipeline (generate query → retrieve → generate query → retrieve → answer); Exact-Match metric; 500 train / 500 dev / 2000 test. The paper also introduces a conditional variant — [[HotPotQAConditional]] — that changes the answer format depending on entity type (person/date/place); on the conditional variant, MIPRO lifts the baseline from 6 → 23.3 test (~17 absolute points), the largest relative gain in the entire benchmark.

On vanilla HotPotQA, the paper's **demos-only baselines (Bootstrap RS / Bayesian Bootstrap) are not significantly beaten by MIPRO** — the paper attributes this to the final module being *"a relatively straightforward Q&A task that is likely in-distribution for many models"*. This is the **canonical exception** to MIPRO's Lesson 2 ("joint optimization is best overall").

## In [[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. (2024)]] — DSPy Assertions

HotPotQA is the **shared dataset** for all four task variants in the DSPy Assertions paper — [[MultiHopQA]] (2-hop CoT + retrieval + answer), [[LongFormQA]] (2-hop + cited-paragraph), [[QuizGen]] (HotPotQA Q→A pair into a JSON quiz), and [[TweetGen]] (HotPotQA Q→A pair into an engaging tweet). Open-domain "fullwiki" setting, hard-label subset; 300 train + 300 dev + 500 test per task; [[ColBERTv2]] retrieval over the 2017 Wikipedia abstracts dump.

On [[MultiHopQA]], adding two soft [[DSPySuggest|`dspy.Suggest`]] constraints (query length < 100; query distinct from prior hops) improves retrieval recall by **6.5–7.9%** and answer correctness by **3.4–14.4%** — the smallest pipeline-level intervention in the paper, and the first published demonstration that assertion-driven backtracking pays for itself on HotPotQA-style multi-hop retrieval.

## In [[2407.10930-better-together|Soylu, Potts & Khattab (2024)]] — BetterTogether

The most "compound" of the three BetterTogether benchmark tasks: a **3-module CoT pipeline** (`generate_query[0]` → retrieve via frozen [[ColBERTv2]] → `generate_query[1]` → retrieve → `generate_answer`). The largest gains in the paper land here — **5–78%** over the better of prompts-only or weights-only, with Π → Θ → Π winning on mistral-7b-instruct-v0.2 (37.6) and llama-2-7b-chat (34.8). 1000 train / 500 dev / 1500 test split.

## In [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] — The Coin-Flip Audit

HotpotQA is the *a priori* **"tight coupling"** prediction in Zhang et al.'s Study 1 — multi-hop reasoning seemingly requires Agent B (synthesizer) to build on Agent A's (decomposer's) specific decomposition. The [[ANOVAVarianceDecomposition|ANOVA decomposition]] of a $10 \times 10$ prompt grid evaluated on $n=30$ samples falsifies the prediction:

| Model | Q | A | B | A×B | Err |
|---|---|---|---|---|---|
| [[ClaudeHaiku45\|Haiku]] | 91.3 | 0.05* | **0.37*** | **0.18** | 8.1 |
| [[AmazonNovaLite\|Nova]] | 75.1 | 0.12 | 0.08 | **0.51** | 24.2 |

HotpotQA shows the **smallest interaction** in the entire study (0.18% Haiku, 0.51% Nova) — practitioners' intuition that multi-hop coupling drives [[JointOptimization|joint optimization]] is empirically wrong. On Haiku, Agent B dominates ($p < 0.001$); on Nova, neither agent's main effect is significant. **Question difficulty explains 75–91% of total variance** — vastly more than any prompt effect.

This is the canonical wiki example of [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]]'s claim *"even practitioners cannot predict coupling, making empirical measurement essential."*
