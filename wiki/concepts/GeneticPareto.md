---
title: "Genetic-Pareto"
type: concept
tags: [evolutionary-search, pareto-frontier, prompt-optimization, gepa]
sources: [2507.19457-gepa]
last_updated: 2026-05-22
---

# Genetic-Pareto

The full name **GEPA** expands to: **Ge**netic-**Pa**reto.

The naming compresses the algorithm's two architectural distinguishers vs both prior prompt optimizers and prior evolutionary methods:

- **Genetic.** A population of candidate prompts $\mathcal{P}$ evolved across iterations via mutation ([[ReflectivePromptMutation]]) and optional crossover ([[SystemAwareMerge]]). The lineage relationships are tracked (each child records its parent(s)).
- **Pareto.** Selection at each iteration draws from the *per-instance Pareto frontier* — every prompt that wins on at least one task instance — weighted by frequency on the frontier. This is the **quality-diversity** axis that prior prompt optimizers ([[MIPROv2]], TextGrad, APO) lacked.

## Why both, not either

Pure **genetic** evolution without Pareto selection (e.g. EvoPrompt) collapses onto whichever prompt has the highest mean score; diverse "winning" strategies get pruned. Pure **Pareto** selection without a directed mutation operator (e.g. random prompt perturbation) explores the frontier slowly. Combining LLM-driven directed mutation with Pareto-frontier selection produces both efficient exploration of the prompt space *and* preservation of diverse winning strategies.

The empirical evidence: holding mutation fixed and replacing Pareto-selection with top-1 (TextGrad) costs **−6.39%** aggregate; vs the +12.44% GEPA achieves, the Pareto component is responsible for roughly half the total gain.

## Lineage in evolutionary algorithms

The Pareto-selection mechanism is the **"illumination"** strategy of **Mouret & Clune (2015)** — adapted from quality-diversity robot-controller evolution to per-instance scoring of compound AI systems. The directed-mutation operator is the LLM-reflection analog of *fitness-aware mutation* in classical GAs — where classical GAs randomly perturb genes and let fitness select, GEPA reads the fitness signal *first* (via $\mu_f$) and uses an LLM to propose a perturbation directly targeted at the diagnosed weakness.

## Connections
- [[2507.19457-gepa]] — canonical source.
- [[GEPA]] — the optimizer; this concept page documents the name's etymology and architectural rationale.
- [[ReflectivePromptMutation]] — the genetic-mutation operator.
- [[SystemAwareMerge]] — the optional genetic-crossover operator.
- [[ParetoBasedCandidateSelection]] — the Pareto-selection rule.
- [[PromptOptimization]] — parent activity.
- [[GeneticAlgorithm|Genetic Algorithm]] — parent class.
