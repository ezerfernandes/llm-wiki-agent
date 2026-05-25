---
title: "TabMWP (Tabular Math Word Problems)"
type: concept
tags: [benchmark, math, tabular, reasoning]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# TabMWP

**TabMWP** (Tabular Math Word Problems; Lu et al. 2022) is a math-word-problem benchmark with **tabular input** — questions that require parsing a table and performing arithmetic over its contents. Named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[ScienceQA]] as one of the two benchmarks on which [[Chameleon]] demonstrates **+17% accuracy** improvement over [[GPT|GPT-4]] alone.

## Why it favors capability-extension tools

Per Lu et al. (quoted in Ch 6), TabMWP is the **tool-task affinity** counterpoint to [[ScienceQA]]: ScienceQA favors [[KnowledgeAugmentation|knowledge-retrieval]] tools; TabMWP favors [[CapabilityExtension|capability-extension]] tools, especially calculators and code interpreters. The tabular-math substrate exercises arithmetic and structured-data parsing — exactly the model deficiencies capability-extension addresses.

## Position relative to [[ScienceQA]]

| Benchmark | What it tests | Favored tool category | Chameleon gain |
|---|---|---|---|
| [[ScienceQA]] | Multimodal science QA | [[KnowledgeAugmentation]] | +11.37% |
| **TabMWP** | Tabular math word problems | [[CapabilityExtension]] | **+17%** |

The pair together establishes the **tool-task affinity** principle.

## Connections

- [[Chameleon]] — the agent that scored the +17% gain.
- [[ScienceQA]] — sibling benchmark.
- [[CapabilityExtension]] / [[CodeInterpreter]] — the tool category most relevant to TabMWP.
- [[ai-engineering-ch06-rag-agents]] — primary source.
