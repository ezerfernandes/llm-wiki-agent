---
title: "Adafactor"
type: concept
tags: [cs324, llm]
sources: [cs324-training]
last_updated: 2026-06-04
---

Adafactor is a memory-efficient optimizer that stores factored row and column second-moment statistics instead of full per-parameter moments, drastically reducing optimizer-state memory. It was used to train T5.

## Connections
- [[Adam]] — the optimizer it economizes on
- [[T5]] — trained with Adafactor
- [[cs324-training]] — discussed in this CS324 lecture
