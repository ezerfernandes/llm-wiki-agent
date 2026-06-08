---
title: "AI Compute Primitives"
type: concept
tags: [hardware, accelerators, compute-primitives, mac]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# AI Compute Primitives

**AI compute primitives** are the specialized functional blocks that accelerators build to exploit the small set of operations neural networks actually perform. The dominant operation across every layer type (fully connected, convolutional, attention) is the **multiply-accumulate (MAC)** — multiplying inputs by learned weights and accumulating — which consumes **>95% of execution time**.

## The three primitives ([[mlsysbook-ch11-hardware-acceleration]])

The processor-level nested loop of a dense layer exposes three recurring patterns, each justifying dedicated silicon:

1. **Vector operations** — element-wise, one-to-one transforms (activations, layer norm, pooling, embedding gather/scatter). Mapped to [[SIMD]]/[[SIMT]] units; the [[VectorProcessor|Cray-1]] pioneered the template in 1975.
2. **Matrix operations** — many-to-many transforms (layer transforms, attention, convolutions via im2col). Mapped to [[TensorCore|tensor cores]] (16×16 tiles, ~256 MACs per instruction) and [[SystolicArray|systolic arrays]].
3. **Special functions** — nonlinear transcendentals (exp, sqrt, sigmoid) handled by [[SpecialFunctionUnit|special function units]].

## Why it works

These patterns are regular (predictable data flow, no irregular branches), frequent, and stable across decades of architecture evolution — exactly the conditions that justify trading flexibility for raw throughput. CPUs reach ~100 GFLOP/s; accelerators built around these primitives reach 100,000+ GFLOP/s.

## See also
- [[TensorCore]] / [[SystolicArray]] — the matrix-primitive engines.
- [[SIMD]] / [[SIMT]] / [[VectorProcessor]] — the vector-primitive engines.
- [[SpecialFunctionUnit]] — the nonlinear-function engine.
- [[GEMM]] — the matrix primitive that dominates training time.
- [[mlsysbook-ch11-hardware-acceleration]] — the MAC pattern and the three-primitive taxonomy.
