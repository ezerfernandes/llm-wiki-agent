---
title: "GRPO"
type: concept
tags: [ml-method, rl-algorithm]
sources: [2512.04388-conductor, 2605.02572-long-horizon-llm-training, 2507.19457-gepa, dspy-tutorial-rl-papillon, dspy-rl-multihop-tutorial]
last_updated: 2026-05-24
---

# GRPO

Group Relative Policy Optimization (Shao et al., 2024). Critic-free policy-gradient method that uses Monte-Carlo advantages within grouped completions; reduces memory/compute relative to PPO and is the default RL backbone in modern reasoning LLM training (DeepSeek R1, the Conductor, and the long-horizon study all build on GRPO or its descendants like DAPO / GSPO / CISPO).

## In compound AI system optimization

GRPO is the **default weight-space RL baseline** for compound-AI-system optimization. [[2507.19457-gepa|GEPA (Agrawal et al., ICLR 2026)]] argues this is the wrong tool for sample-constrained settings: GRPO consumed **24,000 rollouts** on each of HotpotQA, IFBench, HoVer, PUPA, AIME-2025, LiveBench-Math (Qwen3 8B with LoRA), and [[GEPA]] outperformed it by **6% average and up to 20%** using **up to 35× fewer rollouts** (243–7,051 rollouts depending on benchmark). The headline contrast:

| Benchmark (Qwen3 8B) | GRPO (24,000 rollouts) | GEPA |
|---|---|---|
| HotpotQA | 43.33 | **62.33** |
| IFBench | 35.88 | **38.61** |
| HoVer | 38.67 | **52.33** |
| PUPA | 86.66 | **91.85** |
| AIME-2025 | **38.00** | 32.00 |
| LiveBench-Math | 51.26 | **51.95** |

Only AIME-2025 favored GRPO — math-reasoning is the regime where weight-space updates still extract more than prompt-only adaptation.

The paper's information-bandwidth argument: GRPO's scalar reward delivers $\sim 1$ bit per rollout; the same rollout's serialized natural-language trace carries kilobytes of fully-readable diagnostic content (compiler errors, judge rationales, reasoning chains) that an LLM reflection step can extract. The contradiction with GRPO's "more sample-efficient than PPO" claim is real but scope-limited — see [[2507.19457-gepa]] for the prompts-only vs weights caveat.

## In DSPy / multi-module compound-AI training

[[dspy-tutorial-rl-papillon|DSPy's `rl_papillon` tutorial]] and [[dspy-rl-multihop-tutorial|DSPy's `rl_multihop` tutorial]] expose GRPO as a first-class [[DSPyOptimizers|DSPy optimizer]] — `dspy.GRPO` / [[ArborGRPO]] — that extends the single-policy GRPO algorithm to **multi-module compound AI programs**. One scalar reward propagates back to a shared local LM serving every module in the program; a [[lora|LoRA]] adapter is the only thing that moves. Both tutorials use `loss_type="dapo"` ([[DAPO]] variant, *not* vanilla GRPO), `beta=0.00` (no [[KLPenalty|KL]] anchor), `learning_rate=1e-6`, rank-8 LoRA on all attention + MLP projections.

| Tutorial | Program | Reward type | Compute | Rollouts | Lift |
|---|---|---|---|---|---|
| [[dspy-tutorial-rl-papillon]] | [[PAPILLON]] (privacy delegation, 2 modules) | [[LLMJudge|LLM-judge composite]] `(quality + (1-leakage))/2` | 1.5B LM, 4× [[NVIDIA|H100]], ~3 h | 500 steps × 4 examples × 8 = 16,000 | 54.6 → 60.0 (composite) |
| [[dspy-rl-multihop-tutorial]] | [[ResearchHop]] (2-hop retrieval, 2 sub-modules) | Deterministic title-recall (gold ∩ retrieved) / |gold| | Qwen2.5-1.5B-Instruct, 4 GPUs (3 train + 1 inference), ~18 h | 1000 steps × 6 examples × 4 = **24,000 — same total budget [[2507.19457-gepa|GEPA paper]] gave its GRPO baseline** | 61.8 → 66.2 (recall) |

Both authors openly disclaim the approach as *"typically worse on cost/quality basis than"* prompt optimization ([[MIPROv2]] / [[SIMBA]] / [[GEPA]]) and frame the value as *"online RL over arbitrary LM programs for tiny LMs"* — the small-student-size regime where prompt-space optimization hits an underlying capability ceiling. The rl_multihop tutorial's 24,000-rollout budget **matches exactly the budget the [[2507.19457-gepa|GEPA paper]] gave its GRPO baseline that GEPA beat by 6% average and up to 20% on HoVer** — the wiki's strongest operational alignment with the GEPA paper's central contrast.

## Connections
- [[reinforcementlearning|ReinforcementLearning]]
- [[deepseekr1|DeepSeekR1]]
- [[DAPO]] — the clip-decoupled GRPO variant ArborGRPO uses by default.
- [[ArborGRPO]] — the DSPy optimizer that extends GRPO to multi-module programs.
- [[PAPILLON]] / [[PUPA]] / [[ResearchHop]] / [[HoVer]] — the wiki-canonical worked examples of multi-module GRPO.
- [[dspy-tutorial-rl-papillon]] — first DSPy GRPO tutorial (privacy-delegation task, LLM-judge reward).
- [[dspy-rl-multihop-tutorial]] — second DSPy GRPO tutorial (multi-hop retrieval, deterministic recall reward).
- [[2512.04388-conductor]]
- [[2605.02572-long-horizon-llm-training]]
- [[2507.19457-gepa]] — the paper that argues against GRPO for sample-constrained compound-AI-system prompt-space adaptation.
- [[GEPA]] — the prompt-space alternative.
- [[CompoundAISystem]] — the formalism both GRPO and GEPA target (GRPO updates $\Theta_\Phi$, GEPA updates $\Pi_\Phi$).
