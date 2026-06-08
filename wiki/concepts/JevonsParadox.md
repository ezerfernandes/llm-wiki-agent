---
title: "Jevons Paradox (Inference Demand)"
type: concept
tags: [serving, economics, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Jevons Paradox (Inference Demand)

William Stanley Jevons observed in 1865 that efficiency improvements in coal-powered steam engines *increased* total coal consumption by making steam power economically viable for previously-too-costly applications. The same dynamic governs **AI inference** ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]): each ~10× cost reduction opens application classes infeasible at the prior price point, expanding aggregate demand by *more* than the efficiency gain.

This is why cheaper inference reliably *increases*, not decreases, total GPU fleet demand — efficiency and demand are complements in AI, not substitutes. The chapter pairs it with **intelligence deflation**: public API input-token prices fell ~5.8× per 18 months (2020–2025), collapsing per-inference margins and making infrastructure efficiency the primary lever for economic viability.

## Connections

- [[CostPerInference]] — the per-inference economics this paradox operates on.
- [[CapacityPlanning]] — why aggregate fleet demand keeps rising despite efficiency gains.
- [[LLMServing]] — the token-price trajectory driving the dynamic.
- [[mlsysbook-ch13-model-serving]] — source.
