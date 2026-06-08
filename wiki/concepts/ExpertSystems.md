---
title: "Expert Systems"
type: concept
tags: [ai-history, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Expert Systems

The AI era (roughly 1970s–1980s) that pivoted from general logic to **capturing deep domain expertise as IF-THEN production rules.** Covered in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the era that hit the **knowledge-acquisition bottleneck**.

The canonical exemplar is **MYCIN** (1976), which diagnosed blood infections and outperformed junior doctors on specific tests. But extracting implicit expert intuition into formal rules proved slow, error-prone, and contradictory: knowledge elicitation consumed **70–80% of total project time** (Feigenbaum's bottleneck, named 1982) and roughly **60% of expert-system initiatives failed**. Unlike compute bottlenecks that yield to faster hardware, this one was bound by the serial bandwidth of human experts — the original "does not scale" constraint that motivated the data-driven paradigm.

The collapse of the Lisp Machine market triggered the **second [[AIWinter|AI winter]]** (1987–1993).

## Connections

- [[SymbolicAI]] — the predecessor era (logic bottleneck).
- [[AIWinter]] — the funding collapse that followed.
- [[BitterLesson]] — the pattern this failure validates: hand-injected knowledge does not scale.
- [[FeatureEngineering]] — the next bottleneck (statistical learning era).
- [[mlsysbook-ch01-introduction]] — source.
