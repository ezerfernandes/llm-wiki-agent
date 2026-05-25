---
title: "AlphaGeometry"
type: concept
tags: [dataset-engineering, synthetic-data, deepmind, math]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# AlphaGeometry

**[[googledeepmind|DeepMind]]'s Olympiad-level geometry model (Trinh et al. 2024), trained on 100 million synthetic problems.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], AlphaGeometry is the headline example of [[RuleBasedDataSynthesis|rule-based / procedural data synthesis]] producing world-class reasoning capability.

## Scale

| Metric | Value |
|---|---|
| Synthetic training examples | **100 million** geometry problems |
| Domain | International Math Olympiad-level geometry |
| Synthesis method | Procedural (templates + grammar over geometry axioms) |
| Performance | Olympiad-level (compared to top human contestants) |

## Why it matters

AlphaGeometry demonstrates that **purely procedural synthesis (no LLM in the loop) can produce 100M-scale training data** of provable correctness for a domain with well-formalized rules. Geometry is verifiable; problems are constructible; solutions are checkable — the perfect synthesis target.

This makes AlphaGeometry the inverse case to LLM-generated data: when the domain has formal verifiability, [[RuleBasedDataSynthesis|rules]] beat [[AIPoweredDataSynthesis|AI-generation]] for both scale and correctness.

## Connections

- [[RuleBasedDataSynthesis]] — parent technique.
- [[DataSynthesis]] — parent category.
- [[googledeepmind|DeepMind]] — the lab.
- [[AlphaProof]] — sibling DeepMind math-reasoning project.
- [[MetaMath]] — sibling math-data success (LLM-generated, not rule-based).
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
