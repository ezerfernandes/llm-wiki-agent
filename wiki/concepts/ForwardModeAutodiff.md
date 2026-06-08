---
title: "Forward-Mode Automatic Differentiation"
type: concept
tags: [autograd, vector-calculus, deep-learning, foundational]
sources: [mml-ch05-vector-calculus, mml-book, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Forward-Mode Automatic Differentiation

One of the two modes of [[AutomaticDifferentiation|automatic differentiation]]. For a chain of intermediate variables $x\to a\to b\to y$, the chain rule gives $\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}b}\frac{\mathrm{d}b}{\mathrm{d}a}\frac{\mathrm{d}a}{\mathrm{d}x}$. **Forward mode** associates this product **left-to-right, with the data flow** ([[mml-ch05-vector-calculus|MML Ch 5]] §5.6.2, Eq. 5.121):

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}b}\left(\frac{\mathrm{d}b}{\mathrm{d}a}\frac{\mathrm{d}a}{\mathrm{d}x}\right).$$

Gradients flow from input to output, in the same direction as the forward computation. The two modes differ only in *the order of multiplication* (matrix multiplication is associative, so both give the same answer) — but the order determines computational cost.

## Forward vs reverse: when each wins

Forward mode propagates derivatives **with respect to one input** through the whole graph in one pass — cost scales with the number of *inputs*. [[ReverseModeAutodiff|Reverse mode]] (= [[Backpropagation|backpropagation]]) propagates derivatives **of one output** backward — cost scales with the number of *outputs*.

- **Forward mode is cheaper when outputs ≫ inputs** (few inputs, many outputs).
- **Reverse mode is cheaper when inputs ≫ outputs** — the neural-network regime, where a high-dimensional parameter/input vector maps to a *scalar* loss. MML §5.6.2: *"In the context of neural networks, where the input dimensionality is often much higher than the dimensionality of the labels, the reverse mode is computationally significantly cheaper than the forward mode."*

This is why deep learning uses reverse mode (backprop) almost exclusively, and why MML focuses on it.

## Systems view from [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 implements forward mode with **[[DualNumbers|dual numbers]]** (each value augmented with its derivative; ~2× compute per input) and stresses its *constant memory* (only the value, one derivative, temporaries) — making it suitable for embedded/real-time/memory-bandwidth-limited settings. But for a model with $P$ parameters it multiplies total compute by $P$, so it is *never* used for training; it keeps niche uses with **few inputs, many outputs**: sensitivity analysis (how one pixel change affects the prediction) and feature importance. PyTorch/JAX expose it via `jacfwd`.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.6.2 Eq. 5.121 canonical reference.
- [[mlsysbook-ch07-ml-frameworks]] — dual-number implementation; constant-memory niche uses.
- [[DualNumbers]] — the mechanism forward mode uses.
- [[AutomaticDifferentiation]] — the parent technique.
- [[ReverseModeAutodiff]] — the dual mode (= backprop).
- [[Backpropagation]] — reverse mode applied to NN training.
- [[ComputationalGraph]] — the DAG both modes traverse.
- [[ChainRule]] — the rule both modes implement.
