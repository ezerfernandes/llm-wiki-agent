---
title: "Binarization & Ternarization (Extreme Quantization)"
type: concept
tags: [quantization, model-compression, tinyml, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Binarization & Ternarization (Extreme Quantization)

**The most aggressive [[Quantization|quantization]] regime, reserved for deployments where even INT8/INT4 cannot meet the memory/energy budget.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]]:

- **Binarization** — constrains weights/activations to two values (±1 or 0/1). Drastically shrinks model size and accelerates inference on specialized binary-network hardware, but severely limits expressiveness; binary weights reach only ~51% on ImageNet.
- **Ternarization** — three values (−1, 0, +1), packed into 2-bit storage; the zero enables sparsity while keeping more representational power than pure binary.

Both achieve 16–32× size reduction but need custom hardware and the [[StraightThroughEstimator|Straight-Through Estimator]] + [[QuantizationAwareTraining|QAT]] to handle non-differentiable quantization and mitigate accuracy loss. Lives in the keyword-spotting / [[TinyML]] regime where ~256 KB SRAM makes extreme compression existential.

## Connections

- [[Quantization]] — the extreme low-bit end of the precision spectrum.
- [[StraightThroughEstimator]] / [[QuantizationAwareTraining]] — required to train binary/ternary nets.
- [[TinyML]] — the deployment regime that demands it.
- [[mlsysbook-ch10-model-compression]] — source.
