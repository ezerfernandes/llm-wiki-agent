---
title: "EvoPrompt"
type: concept
tags: [prompt-optimization, evolutionary, llm]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# EvoPrompt

**Evolutionary Prompt Optimization** (Guo et al. 2024, arXiv:2309.08532). Combines LLMs with evolutionary algorithms — an LM acts as the mutation/crossover operator over a population of prompts; fitness is the task metric.

The [[2406.11695-mipro|MIPRO paper]] groups EvoPrompt with [[OPRO]] and [[APE]] as the single-prompt prior work that Algorithm 1 generalizes to multi-stage settings.

## Connections

- [[APE]] / [[OPRO]] — single-prompt antecedents.
- [[2406.11695-mipro|MIPRO]] — the multi-stage generalization.
- [[GeneticPareto|GEPA]] — the **closer relative**: GEPA also uses an evolutionary structure but adds reflective LM-driven mutation + Pareto-based selection.
- [[PromptOptimization]] — parent task.
