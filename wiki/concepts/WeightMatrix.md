---
title: "Weight Matrix"
type: concept
tags: [neural-networks, deep-learning, parameters, matrix-multiplication]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Weight Matrix

The organization of a layer's learnable weights into a matrix for efficient batched computation. Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], a layer with n input features and m neurons has weights `W ∈ ℝ^{n×m}`, where each column holds the weights for one neuron. The layer's linear step is then the [[MatrixMultiplication|matrix multiply]] `Z = AW + b` — turning M separate [[ArtificialNeuron|neuron]] dot products into a single [[GEMM]] kernel.

Weights are where the model's "knowledge" is stored. A key systems property: neural-network "memory" is **distributed across all weights** rather than stored at specific addresses, so every prediction reads a large fraction of the parameters and every training step coordinates updates across the whole network — the tension between storage capacity and access bandwidth behind the [[MemoryWall|memory wall]].

For the MNIST 784→128→64→10 net, the first weight matrix alone is 784×128 = 100,352 weights — Layer 1 dominates the parameter budget because deeper layers compress toward the 10-class output. See [[ModelSize]] for the full memory accounting.

## Connections

- [[ArtificialNeuron]] — per-neuron weights aggregated into the matrix.
- [[MatrixMultiplication]] / [[GEMM]] — the operation weight matrices feed.
- [[ModelSize]] — parameter-count and memory implications.
- [[Backpropagation]] — computes the weight gradient `A^(ℓ-1)ᵀ · ∂L/∂Z`.
- [[MemoryWall]] — distributed-weight bandwidth tension.
- [[mlsysbook-ch05-neural-computation]] — source.
