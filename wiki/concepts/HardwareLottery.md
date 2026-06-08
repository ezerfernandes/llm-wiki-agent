---
title: "Hardware Lottery"
type: concept
tags: [benchmarking, hardware, bias, ml-systems, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Hardware Lottery

Coined by Sara Hooker (2021): the phenomenon where an ML model's success is dictated not only by its architecture and data but by **how well it aligns with the available hardware**. Some models win not because they are inherently superior but because they map naturally onto GPU/TPU parallelism; promising alternatives are systematically overlooked because they fit dominant silicon poorly.

Per [[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]], the canonical case is the [[Transformer|transformer]]: its dense matrix multiplications map perfectly to GPU [[TensorCore|Tensor Cores]], while graph neural networks and sparse mixture-of-experts models remain underexplored because they map poorly to current hardware. **For benchmarking, this means hardware-specific leaderboards systematically favor hardware-aligned architectures**, potentially obscuring algorithms that would dominate on different silicon. The chapter's multi-platform figure (CPU / GPU / EdgeTPU / DSP) makes this concrete: the "best" model depends entirely on the deployment target — a conclusion impossible to reach from single-platform benchmarks. Mitigation: benchmark across diverse hardware configurations so performance is not driven solely by platform compatibility.

## Connections

- [[TensorCore]] / [[GPU]] / [[GoogleTPU]] — the dominant hardware whose alignment confers the advantage.
- [[BenchmarkEngineering]] — the intentional sibling bias; both distort what leaderboards reward.
- [[Benchmarking]] — why multi-hardware evaluation is a fairness requirement.
- [[mlsysbook-ch12-benchmarking]] — source.
