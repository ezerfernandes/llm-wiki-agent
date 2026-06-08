---
title: "Artificial Neuron"
type: concept
tags: [neural-networks, deep-learning, ml-systems, foundational]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Artificial Neuron

The basic unit of neural computation — a simplified mathematical abstraction of biological nervous activity (McCulloch & Pitts 1943). It maps biology to math in four stages: dendrites → **input vector** x, synapses → **weight vector** w (the learnable parameters where the model's "knowledge" lives), cell body → **linear sum** `z = Σ(xᵢ·wᵢ) + b`, and axon firing → **[[ActivationFunction|activation function]]** `a = f(z)`. Also called a node, unit, or [[MultilayerPerceptron|perceptron]].

Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], the neuron is the systems atom of deep learning: just as a transistor reveals how a processor works, the neuron reveals how a million-parameter network operates. The linear sum is a **dot product** — the operation hardware accelerators are built to execute at maximum throughput.

## Systems cost

- Each neuron over N inputs costs **N [[MultiplyAccumulate|multiply-accumulate (MAC)]] operations** and **2N+2 memory accesses** (load N inputs + N weights, plus bias and output).
- A layer of M neurons repeats this M times → **M×N MACs**, exactly the [[MatrixMultiplication|matrix multiply]] **xW** that hardware must execute.
- Replicated millions of times, these primitives create the arithmetic and bandwidth demands ([[MemoryWall|memory wall]]) that define modern AI infrastructure.

## Connections

- [[NeuralNetwork]] / [[MultilayerPerceptron]] — networks built from many neurons.
- [[ActivationFunction]] — the nonlinear `f(z)` (axon firing).
- [[WeightMatrix]] — how per-neuron weights organize into layer matrices.
- [[MultiplyAccumulate]] / [[MatrixMultiplication]] — the underlying arithmetic.
- [[DeepLearning]] — the paradigm composed from neurons.
- [[mlsysbook-ch05-neural-computation]] — biological-to-artificial mapping and systems cost.
