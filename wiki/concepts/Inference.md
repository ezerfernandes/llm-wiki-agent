---
title: "Inference"
type: concept
tags: [neural-networks, deployment, ml-systems, latency]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Inference

The operational phase in which a trained network applies its frozen weights to new inputs via the **[[ForwardPropagation|forward pass]] only** — no backward pass, no gradient or optimizer state, no weight updates. Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], the network architecture is identical to [[Training|training]]; the difference is entirely in computational and memory orchestration.

## Inference vs training priorities

| | Training | Inference |
|---|---|---|
| Optimizes for | Throughput | **Latency** |
| Batch | Large, fixed | Variable / single |
| Passes | Forward + backward | Forward only |
| Memory | Weights + gradients + [[OptimizerState|optimizer state]] + activations | Weights + transient activations (reusable) |
| Hardware | High-memory GPUs | NPUs (2–4 W), edge accelerators, quantized cloud instances |

For the MNIST MLP, training needs **~4× the memory** of single-sample inference (see [[Backpropagation]]).

## Inference-only optimizations

Because parameters are frozen and computation is predictable: aggressive **activation-buffer reuse / in-place ops** (each layer's activations exist only until the next layer computes), precise memory alignment, SIMD/cache tuning, batching for 10–32× throughput, and **reduced precision** ([[Quantization]] to FP16/INT8). Postprocessing (softmax, confidence thresholds, error handling) returns to *traditional* CPU computing and can dominate end-to-end latency.

## Connections

- [[Training]] — the contrasting phase.
- [[ForwardPropagation]] — the only pass inference runs.
- [[BatchSize]] / [[Quantization]] / [[Logits]] — inference optimizations.
- [[Latency]] / [[InferenceOptimization]] / [[BatchInference]] / [[OnlineInference]] — deployment framings.
- [[mlsysbook-ch05-neural-computation]] — source.
