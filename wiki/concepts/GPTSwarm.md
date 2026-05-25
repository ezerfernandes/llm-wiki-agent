---
title: "GPTSwarm"
type: concept
tags: [prompt-optimization, joint-optimization, agent-graph, compound-ai-system]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# GPTSwarm

**GPTSwarm** (Zhuge, Wang, Kirsch, Faccio, Khizbullin & Schmidhuber, ICML 2024) treats **agent graphs as optimizable structures** — a [[CompoundAISystem|compound AI]] joint-optimization framework where the topology and the per-agent prompts are searched together. Sibling to [[TextGrad]] and [[DSPy]]/[[MIPROv2]] in the joint-optimization tool family.

## Position

GPTSwarm is one of three canonical joint optimizers [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] cite as relying on the (now-falsified) **Assumption B**: that agent prompts interact and require joint search.

The empirical case against the assumption:

- $A \times B$ interaction non-significant in 6/6 model×task conditions ($p > 0.52$, $F < 1.0$).
- 0.18–2.15% of total variance.
- Joint and independent optima are adjacent or identical.

For two-agent feed-forward pipelines on mid-tier models, GPTSwarm's joint-graph search reduces to per-node search at the same budget.

## Where coupling might re-emerge

GPTSwarm's agent-graph framing is one of the **untested architectures** [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] predict could exhibit coupling:

- Deeper pipelines (3+ agents) accumulate interaction opportunities.
- Cyclic / feedback-loop topologies (which GPTSwarm explicitly supports) may produce coupling absent in feed-forward two-agent pipelines.
- Structured-data communication between agents (JSON, code) may amplify coupling.

The [[ANOVAVarianceDecomposition|ANOVA pretest]] generalizes to GPTSwarm-style agent graphs: practitioners should measure their specific topology before assuming the joint-optimization premise holds.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — the empirical audit.
- [[TextGrad]] / [[DSPy]] / [[Helix]] — sibling joint optimizers.
- [[JointOptimization]] — the optimization mode GPTSwarm implements.
- [[CompoundAISystem]] — the formal target.
- [[AgentCoupling]] — the structural property GPTSwarm assumes.
- [[ANOVAVarianceDecomposition]] — the measurement.
- [[PromptOptimization]] — parent task.
