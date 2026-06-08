---
title: "Probing"
type: concept
tags: [cs324, llm]
sources: [cs324-adaptation]
last_updated: 2026-06-04
---

Probing is an adaptation method that freezes a pretrained encoder and trains only a lightweight prediction head on top of its representations. It is used both to adapt models cheaply and to analyze what information the frozen representations encode.

## Connections
- [[FineTuning]] — contrasts by updating all weights
- [[BERT]] — encoder commonly probed
- [[cs324-adaptation]] — discussed in this CS324 lecture
