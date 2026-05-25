---
title: "Nie et al. 2026 (Iterative Generative Optimization)"
type: entity
tags: [paper-reference, prompt-optimization, survey]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Nie et al. 2026 — *Understanding the Challenges in Iterative Generative Optimization with LLMs*

Nie, Daull, Kuang, Akkiraju, Chaudhuri, Piasevoli, Rong, Yuan, Choudhary, Xiao, Fakoor, Swaminathan & Cheng (arXiv:2603.23994, 2026). Cited by [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] in the §4.2 discussion of why iterative optimization usually fails:

> *"Only 9% of surveyed agents use any automated optimization, attributing low adoption to hidden design choices that compound the noise problem we observe."*

Provides the **external corroborating signal** for Zhang et al.'s coin-flip finding: practitioners empirically avoid iterative prompt optimization at a rate consistent with the 49% sub-zero-shot failure rate observed in the controlled study.

Wiki entry held as a dangling reference / forward citation until the paper itself is ingested.

## Connections
- [[2604.14585-prompt-optimization-coin-flip]] — cites this paper in support of the iterative-optimization failure narrative.
- [[CoinFlipOptimization]] — the empirical phenomenon this survey's adoption statistic corroborates.
- [[PromptOptimization]] — parent task.
