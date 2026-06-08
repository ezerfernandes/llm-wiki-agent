---
title: "Green AI"
type: concept
tags: [ml-systems, sustainability, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Green AI

The pursuit of energy- and carbon-efficient machine learning. In [[mlsysbook-ch09-data-selection|Reddi Ch 9]], [[DataSelection|data selection]] is framed as the **most direct lever for Green AI**: training a large language model can emit hundreds of metric tons of CO₂, and halving the dataset halves training energy with no accuracy trade-off if done correctly (since fewer samples means proportionally fewer forward/backward passes and gradient updates). This makes data-side optimization — [[DataDeduplication|deduplication]], [[CoresetSelection|coresets]] — an environmental as well as economic win, complementing model-side ([[ModelCompression|compression]]) and hardware-side efficiency.

## Connections

- [[DataSelection]] — the most direct lever for reducing training energy.
- [[IronLawOfMLSystems]] — energy tracks the operation count $O$ that data selection cuts.
- [[ModelCompression]] — the complementary algorithm-side efficiency lever.
- [[mlsysbook-ch09-data-selection]] — source.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 elevates Green AI (vs. "Red AI") to a first-class responsibility metric: Schwartz et al. 2020's 300,000× compute-growth figure, FLOP reporting alongside accuracy, GPT-3-scale training ≈ >500 t CO₂e, and "each 1% efficiency gain ≈ 1 car-year" removed.
