---
title: "System Aware Merge"
type: concept
tags: [prompt-optimization, evolutionary-search, crossover, gepa]
sources: [2507.19457-gepa]
last_updated: 2026-05-22
---

# System Aware Merge

[[2507.19457-gepa|GEPA]]'s **crossover operator**, complementary to [[ReflectivePromptMutation|reflective prompt mutation]]. The headline variant **GEPA+Merge** invokes Merge in addition to mutation; pure GEPA does not.

## Operation

Given two candidate prompt sets $\Pi_{\Phi_a}, \Pi_{\Phi_b}$ from *distinct ancestral lineages* in the candidate pool $\mathcal{P}$:

1. For each module $j \in \{1, \ldots, |M|\}$, identify which lineage evolved module $j$'s prompt further (i.e. has a more recent / higher-scoring update).
2. Construct $\Pi_{\Phi'}$ by taking $\pi_j$ from whichever lineage evolved it further, for each $j$.
3. If a module evolved in $\Phi_a$ but not $\Phi_b$, take it from $\Phi_a$; vice versa.

The product is a candidate that **combines the best-of-each-module across lineages** — a Mendelian crossover at the module level.

## Why it works conditionally

Crossover requires *complementary* lineages — distinct evolutionary paths that improved different modules. [[ParetoBasedCandidateSelection|Pareto-based selection]] is what produces the diverse lineages in the first place; with single-best-candidate selection there's only one lineage and Merge is a no-op.

The paper's empirical findings (Table 1, Table 2):

| Model | GEPA | GEPA+Merge | Δ |
|---|---|---|---|
| Qwen3 8B (aggregate) | 54.85 | 52.40 | **−2.45 (degradation)** |
| GPT-4.1 Mini (aggregate) | 65.22 | 66.36 | **+1.14** |
| GPT-4.1 Mini HotpotQA | 69.00 | 65.67 | −3.33 |

Per-task variability is large — Merge can help by +5% on one task and hurt by −3% on another. The paper attributes the Qwen3 regression to budget allocation: same hyperparameters across models, Merge invoked before lineages diverged enough to be productively merged. Adaptive scheduling of Merge invocation is **explicitly named as future work**.

## When to use

Paper's heuristic: invoke Merge "when the optimization tree has evolved sufficiently different lineages" — operationally, when the per-module update histories of two candidates have minimal overlap. Without an adaptive scheduler, fixed-budget GEPA+Merge works best on tasks where Pareto-selection has already produced diverse lineages (typically larger benchmarks with > ~50 instances).

## Position in the evolutionary-prompt-optimizer family

| Optimizer | Mutation | Crossover |
|---|---|---|
| EvoPrompt (Guo et al. 2024) | LLM-driven | random pair |
| Rainbow Teaming (Samvelyan et al. 2024) | quality-diversity | implicit (archive recombination) |
| **GEPA** | reflective LM | none |
| **GEPA+Merge** | reflective LM | **module-aware (Merge)** |
| AlphaEvolve / OpenEvolve | code-level | random pair |

## Connections
- [[2507.19457-gepa]] — canonical source.
- [[GEPA]] — the optimizer; Merge is the crossover variant.
- [[ReflectivePromptMutation]] — the complementary operator.
- [[ParetoBasedCandidateSelection]] — produces the diverse lineages Merge can exploit.
- [[CompoundAISystem]] — multi-module structure that makes module-aware merge meaningful.
- [[PromptOptimization]] — broader activity.
