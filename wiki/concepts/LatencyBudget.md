---
title: "Latency Budget"
type: concept
tags: [serving, inference, latency, slo, mlsysbook]
sources: [mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Latency Budget

The **time capital allocated to a request, strictly bounded by the end-to-end SLO** — a *zero-sum* constraint system where any millisecond spent on serialization, network, or queuing directly subtracts from the budget available for model inference ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]).

The central pitfall it corrects: engineers assume the model gets the whole budget; in practice **the model often gets <50%**, the rest going to DNS/TLS/load-balancing/serialization/preprocessing. The ResNet-50 breakdown (≈10.1 ms): JPEG decode 3 ms (30%), resize+normalize 1.5 ms, CPU→GPU 0.5 ms, **forward pass 5 ms (~50%)**, postprocess 0.1 ms. After TensorRT cuts inference to 2 ms, preprocessing dominates at ~63%. Unlike average latency (which hides variance), a latency budget is a *hard bound that must hold for the slowest requests* (p99).

Practical use: instrument each phase, then spend engineering effort proportional to measured time consumed (a 50%-of-latency phase deserves more attention than a 5% one), and use architectural changes (GPU preprocessing, batching) to *shift* work between phases. For batching, allocate ~20–30% of the SLO to batching wait, capping the window at $T_{\text{max}} = 0.3 \times L_{\text{lat,SLO}}$.

## Connections

- [[AmdahlsLaw]] — quantifies the ceiling: a 10× model speedup on a 50%-non-model budget yields only ~1.8× end-to-end.
- [[QueuingTheory]] / [[LittlesLaw]] — the wait component of the budget under concurrent load.
- [[TailLatency]] — tail SLOs must budget the *full* batching window, not the average.
- [[ServiceLevelObjective]] — the bound that defines the budget.
- [[DynamicBatching]] — consumes the wait portion; window/2 average wait.
- [[ModelServing]] / [[InferenceOptimization]] — the practice and discipline.
- [[mlsysbook-ch13-model-serving]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14's worked 100 ms P99 budget shows model inference is only ~45% of end-to-end, so a 2× model speedup yields only ~1.3× end-to-end (Amdahl/D·A·M).
- [[mlsysbook-ch16-conclusion]] — the conclusion makes this the **Latency Budget Invariant** (#12 of the [[ThirteenQuantitativeInvariants|thirteen]]): $T_{p99}(x)\le L_{budget}$ — "throughput is optimized within the latency envelope, never at its expense." It anchors the point that mean latency is misleading (a reference distribution puts P99 at 40× the mean) and that the [[MobileNetV2]] mobile journey is governed by a hard P99 < 50 ms constraint.

