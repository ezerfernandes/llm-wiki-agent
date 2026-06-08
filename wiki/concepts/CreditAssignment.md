---
title: "Credit Assignment"
type: concept
tags: [optimization, multi-stage, latent-variables]
sources: [2406.11695-mipro, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Credit Assignment

The problem of attributing a task-level reward / score back to **specific intermediate decisions** that produced it. Central to multi-stage learning whenever per-stage supervision is unavailable.

## In LM-program prompt optimization

The [[2406.11695-mipro|MIPRO paper]] names credit assignment as one of the **two key challenges** of [[PromptOptimization|prompt optimization]] for multi-stage [[LMProgram|LM programs]] (the other being the **proposal challenge**):

> *"The credit assignment challenge: our problem requires jointly optimizing over many distinct variables that parameterize the prompts of all modules. To allocate search effort, we must infer the impact of our configurations for each variable effectively."*

The paper studies three credit-assignment strategies:

1. **Greedy** — optimize one stage at a time (rejected in initial experiments — no accuracy gain, much worse wall-clock).
2. **Surrogate** — a [[BayesianOptimization|Bayesian model]] ([[TreeStructuredParzenEstimator|TPE]] via [[Optuna]]) infers joint contributions of per-module parameter choices from observed program scores. **MIPRO's choice.**
3. **History-based** — pass the proposer LM a history of past evaluations and rely on its in-context inference ([[OPRO]] / [[ModuleLevelOPRO]] style).

[[BootstrapDemonstrations|Bootstrap demonstrations]] is the **rejection-sampling** analog — high-scoring traces propagate labels to all per-module input/output pairs.

## In neural-network training (the original sense)

[[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]] frames credit assignment as the problem **[[Backpropagation|backpropagation]] solves**: determining which of thousands/millions of [[WeightMatrix|weights]] contributed to the final prediction error, and by how much. The chapter's factory-assembly-line analogy — tracing a defect backward station by station, each receiving feedback proportional to its contribution — maps onto the chain-rule multiplication that propagates the error signal backward, with the most-responsible connections making the largest adjustments.

## In reinforcement learning

The same vocabulary applies to RL (Sutton & Barto's *"temporal credit assignment"*). The wiki's RL-side anchor is [[grpo|GRPO]] and the family of policy-gradient methods. The [[2507.19457-gepa|GEPA paper]] presents the prompt-space alternative as **strictly more sample-efficient** in the LLM regime.

## Connections

- [[PromptOptimization]] — the parent task where credit assignment is one of two structural challenges.
- [[2406.11695-mipro|MIPRO]] — the surrogate-based solution.
- [[OPRO]] / [[ModuleLevelOPRO]] — the history-based solution.
- [[BootstrapDemonstrations]] — the rejection-sampling solution at the demo-collection layer.
- [[grpo|GRPO]] — the RL analog.
- [[LMProgram]] / [[CompoundAISystem]] — the multi-stage objects where credit assignment matters.
- [[Backpropagation]] / [[ChainRule]] / [[mlsysbook-ch05-neural-computation]] — the original neural-network sense backprop solves.
