---
title: "Jacobi Decoding"
type: concept
tags: [inference, decoding, parallel-decoding, jacobi, optimization]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Jacobi Decoding

**The family of [[ParallelDecoding|parallel-decoding]] algorithms that use the [[JacobiAlgorithm|Jacobi method]] to iteratively refine K simultaneously-generated tokens** until they all satisfy coherence and consistency checks. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"This family of parallel decoding algorithms is also called Jacobi decoding."*

[[LookaheadDecoding|Lookahead decoding]] (Fu et al. 2024) is the primary instance Ch 9 names.

## The Jacobi connection

> *"The Jacobi method is an iterative algorithm where multiple parts of a solution can be updated simultaneously and independently."* — Ch 9 footnote

For solving a linear system, the Jacobi method updates each variable based on the previous iteration's values of all variables — parallelizable, but slower-converging than Gauss-Seidel. For parallel decoding, the analogy is: each of the K future tokens is generated based on the *previous iteration's* values of all K, then verified, then re-generated for failures.

## Why "Jacobi" matters

- **Parallelizable** — all K updates happen simultaneously, vs sequential autoregressive generation.
- **Iterative** — convergence isn't guaranteed in one pass; multiple iterations refine until verification passes.

## Connections

- [[ParallelDecoding]] — parent family.
- [[LookaheadDecoding]] — primary Jacobi-decoding instance.
- [[JacobiAlgorithm]] — the underlying iterative method.
- [[Medusa]] — sibling parallel-decoding family (uses tree attention, not Jacobi).
- [[SpeculativeDecoding]] — alternative decoding accelerator family.
- [[Decode]] — the sequential phase Jacobi decoding tries to parallelize.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
