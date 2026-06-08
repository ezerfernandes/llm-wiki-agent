---
title: "Selection Inequality"
type: concept
tags: [ml-systems, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Selection Inequality

The systems condition that gates every [[DynamicDataSelection|dynamic data-selection]] technique ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]):

$$T_{\text{selection}} + T_{\text{train}}(D_{\text{subset}}) < T_{\text{train}}(D_{\text{total}})$$

Selection is **not free** — it adds a new term to the [[IronLawOfMLSystems|iron law]]. If the scoring function $f(x)$ requires a forward pass of a large model, selection cost can exceed training cost and produce negative ROI. Worked example: scoring 1M images with a full ResNet-50 (~2.8 hr) can negate a 10% coreset, whereas a ResNet-18 proxy (~0.6 hr) preserves ~90% of savings. **Rule of thumb: selection time should stay below ~10% of full-training time.** Mitigations: small proxy models, cached embeddings, [[FAISS]] ANN indices.

## Connections

- [[DynamicDataSelection]] / [[DataSelection]] — what it gates.
- [[IronLawOfMLSystems]] — the equation it extends.
- [[InformationComputeRatio]] — a 2× ICR gain ≈ 2× hardware throughput, but only if the inequality holds.
- [[FAISS]] — infrastructure that keeps $T_{\text{selection}}$ low.
- [[mlsysbook-ch09-data-selection]] — source.
