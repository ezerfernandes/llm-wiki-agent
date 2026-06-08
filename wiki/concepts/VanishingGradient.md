---
title: "Vanishing Gradient"
type: concept
tags: [optimization, neural-networks, foundational]
sources: [madewithml-baselines, d2l-multilayer-perceptrons, d2l-optimization, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Vanishing Gradient

A training pathology in deep [[NeuralNetwork|networks]] where gradients shrink toward zero as they propagate backward through layers, stalling learning in early layers. Caused by repeated multiplication of small Jacobian / activation-derivative factors during [[Backpropagation|backprop]] ([[d2l-multilayer-perceptrons]] §Vanishing and Exploding Gradients).

## Mechanism

For an $L$-layer network the gradient of the output w.r.t. early parameters is a product of $L-l$ matrices:

$$\partial_{\mathbf{W}^{(l)}}\mathbf{o} = \underbrace{\mathbf{M}^{(L)} \cdots \mathbf{M}^{(l+1)}}_{\text{Jacobian product}} \mathbf{v}^{(l)}.$$

If the Jacobians have spectral radius $< 1$ on average, the product *shrinks exponentially* in depth. With saturating activations ([[Sigmoid|sigmoid]] derivative ≤ 0.25, [[Tanh|tanh]] derivative ≤ 1), the shrinkage compounds quickly.

## Where it bites hardest

- **Deep MLPs / CNNs with sigmoid or tanh hidden units** — historical motivation for the [[ReLU]] switch.
- **Vanilla [[RNN|RNNs]] across long sequences** — the time-unrolled gradient is the same kind of product; [[LSTM]] / [[GRU]] gating + cell-state addition explicitly counter this.

## Mitigations

- **[[ReLU]] activations** — derivative is 0 or 1, no per-layer shrinkage.
- **[[HeInitialization|He]] / [[XavierInitialization|Xavier]] initialization** — keeps activation and gradient variance constant across layers in expectation.
- **Skip / residual connections** (ResNet) — add identity paths so the gradient has a direct route.
- **[[BatchNormalization]]** — rescales activations layer-by-layer.
- **Architectural choices**: [[LSTM]] / [[GRU]] cell-state additivity; [[Transformer]] residual + LayerNorm stack.

## Connections

- [[d2l-multilayer-perceptrons]] — §Vanishing and Exploding Gradients (canonical exposition).
- [[ExplodingGradient]] — symmetric pathology in the other direction.
- [[Backpropagation]] — the Jacobian product is the mechanism.
- [[ReLU]] / [[Sigmoid]] / [[Tanh]] — activations that influence per-layer shrinkage.
- [[XavierInitialization]] / [[HeInitialization]] — initialization remedies.
- [[WeightInitialization]] — parent concept.
- [[LSTM]] / [[RNN]] — sequence-model setting where it dominated history.
- [[BatchNormalization]] — orthogonal mitigation.
- [[mlsysbook-ch05-neural-computation]] — quantifies it as a *systems constraint*: 0.25^10 ≈ 10⁻⁶ (10-layer sigmoid), 0.25^20 ≈ 10⁻¹² (20-layer) — "a mathematical impossibility" invisible in logs (loss plateaus or goes NaN); ReLU + residual connections were the two architectural breakthroughs.
