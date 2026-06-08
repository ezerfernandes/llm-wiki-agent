---
title: "Reverse-Mode Automatic Differentiation"
type: concept
tags: [autograd, vector-calculus, deep-learning, optimization, foundational]
sources: [mml-ch05-vector-calculus, mml-book, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Reverse-Mode Automatic Differentiation

One of the two modes of [[AutomaticDifferentiation|automatic differentiation]] — and the mode that **is [[Backpropagation|backpropagation]]**. For a chain $x\to a\to b\to y$ the chain rule gives $\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}b}\frac{\mathrm{d}b}{\mathrm{d}a}\frac{\mathrm{d}a}{\mathrm{d}x}$. **Reverse mode** associates this product **right-to-left, reverse to the data flow** ([[mml-ch05-vector-calculus|MML Ch 5]] §5.6.2, Eq. 5.120):

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \left(\frac{\mathrm{d}y}{\mathrm{d}b}\frac{\mathrm{d}b}{\mathrm{d}a}\right)\frac{\mathrm{d}a}{\mathrm{d}x}.$$

Gradients are propagated *backward* through the graph, opposite to the direction of the forward computation. MML §5.6.2: *"Equation (5.120) would be the reverse mode because gradients are propagated backward through the graph, i.e., reverse to the data flow."*

## Why it dominates deep learning

Reverse mode computes the gradient of **one scalar output** with respect to **all inputs/parameters** in a single backward pass — cost scales with the number of *outputs* (here: one, the loss), not the (huge) number of parameters. MML §5.6.2: *"In the context of neural networks, where the input dimensionality is often much higher than the dimensionality of the labels, the reverse mode is computationally significantly cheaper than the [[ForwardModeAutodiff|forward mode]]."*

Formalized over a [[ComputationalGraph|computation graph]] $x_i=g_i(x_{\mathrm{Pa}(x_i)})$ (Eq. 5.143, with parents $\mathrm{Pa}(\cdot)$): set $\frac{\partial f}{\partial x_D}=1$ for the output, then accumulate backward via $\frac{\partial f}{\partial x_i}=\sum_{x_j:\,x_i\in\mathrm{Pa}(x_j)}\frac{\partial f}{\partial x_j}\frac{\partial g_j}{\partial x_i}$ (Eq. 5.145). The deep insight (MML Example 5.14): **computing the gradient costs about the same as computing the function**, even when the symbolic derivative looks far more complicated than the function.

## Systems consequence ([[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]])

Ch 7 makes the $\mathcal{O}(1)$-vs-$\mathcal{O}(P)$ asymmetry the central training claim: for a 100-million-parameter network, that is the difference between 100 million [[ForwardModeAutodiff|forward-mode]] passes and exactly one backward pass. The price is memory — reverse mode must store every forward activation until the backward pass consumes it (a "memory wave" peaking at backprop start; 3–4× model-weight memory for a transformer), which is why frameworks provide [[ActivationCheckpointing|activation checkpointing]] and [[GradientAccumulation|gradient accumulation]]. All major frameworks default to reverse mode for training (Baydin et al. 2018).

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.6.2 Eq. 5.120 canonical reference.
- [[mlsysbook-ch07-ml-frameworks]] — the systems cost (one backward pass vs $P$, the activation memory tax).
- [[ActivationCheckpointing]] / [[GradientAccumulation]] — the memory levers reverse mode forces.
- [[Backpropagation]] — reverse-mode AD *is* backprop (the NN training algorithm).
- [[AutomaticDifferentiation]] — the parent technique.
- [[ForwardModeAutodiff]] — the dual mode (cheaper when outputs ≫ inputs).
- [[ComputationalGraph]] — the DAG traversed in reverse.
- [[ChainRule]] — the rule it implements.
- [[Jacobian]] — reverse mode is iterated Jacobian-transpose-vector products.
- [[GradientDescent]] — consumes the gradients it produces.
