---
title: "Automatic Differentiation"
type: concept
tags: [autograd, vector-calculus, deep-learning, foundational]
sources: [mml-ch05-vector-calculus, mml-book, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Automatic Differentiation

Algorithmic computation of exact gradients via the [[ChainRule]] over a recorded computational graph. **[[ReverseModeAutodiff|Reverse-mode AD]]** = [[Backpropagation]]; **[[ForwardModeAutodiff|forward-mode AD]]** is its dual. [[mml-book]] §5.6.

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.6.2 gives the canonical definition: *"backpropagation is a special case of a general technique in numerical analysis called automatic differentiation. We can think of automatic differentiation as a set of techniques to numerically (in contrast to symbolically) evaluate the exact (up to machine precision) gradient of a function by working with intermediate variables and applying the chain rule."*

### Three things AD is *not* confused with

- **Symbolic differentiation** — AD does not manipulate algebraic expressions; the explicit symbolic derivative (MML Eq. 5.110) is far uglier than the function (5.109), yet AD never forms it.
- **Numerical finite differences** — AD is *exact* up to machine precision, not a [[DifferenceQuotient|difference-quotient]] approximation with a step-size/round-off tradeoff.
- It works on **intermediate variables**, decomposing the function into elementary arithmetic ops (+, ×) and elementary functions ($\sin,\cos,\exp,\log$), then applying the chain rule op-by-op.

### Two modes (§5.6.2, Eqs. 5.119–5.121)

For $x\to a\to b\to y$, the chain-rule product $\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}b}\frac{\mathrm{d}b}{\mathrm{d}a}\frac{\mathrm{d}a}{\mathrm{d}x}$ can be associated two ways:

- **[[ReverseModeAutodiff|Reverse mode]]** (Eq. 5.120): $\left(\frac{\mathrm{d}y}{\mathrm{d}b}\frac{\mathrm{d}b}{\mathrm{d}a}\right)\frac{\mathrm{d}a}{\mathrm{d}x}$ — gradients flow backward, reverse to the data; = [[Backpropagation|backprop]]. Cheaper when **inputs ≫ outputs** (the NN regime).
- **[[ForwardModeAutodiff|Forward mode]]** (Eq. 5.121): $\frac{\mathrm{d}y}{\mathrm{d}b}\left(\frac{\mathrm{d}b}{\mathrm{d}a}\frac{\mathrm{d}a}{\mathrm{d}x}\right)$ — gradients flow with the data, left to right. Cheaper when **outputs ≫ inputs**.

### Formalization (Eqs. 5.143–5.145)

AD works over a [[ComputationalGraph|computation graph]] $x_i=g_i(x_{\mathrm{Pa}(x_i)})$ (input vars $x_1..x_d$, intermediates $x_{d+1}..x_{D-1}$, output $x_D$). Forward propagation is Eq. 5.143; backpropagation of the gradient is Eq. 5.145, $\frac{\partial f}{\partial x_i}=\sum_{x_j:\,x_i\in\mathrm{Pa}(x_j)}\frac{\partial f}{\partial x_j}\frac{\partial g_j}{\partial x_i}$. **Key result** (Example 5.14): computing the gradient costs roughly the same as computing the function. AD applies even to general computer programs (not just math functions), though `for`/`if` control structures need care. MML cites Baydin et al. (2018) for an ML-focused AD survey.

## Systems view from [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 reframes AD as the *differentiation problem* — one of three problems every framework must solve — and shifts focus from the math to the **systems engineering**: "The framework's role is not to perform calculus but to manage the bookkeeping at scale." The load-bearing claim is the [[ReverseModeAutodiff|reverse-mode]] asymmetry: a network has one scalar loss but $P$ parameters, so [[ForwardModeAutodiff|forward mode]] needs $P$ passes (using [[DualNumbers|dual numbers]]) while reverse mode computes all $P$ gradients in one backward pass at constant ~2–3× overhead. The dominant cost is **memory**: reverse mode must store every forward activation (3–4× model-weight memory for a transformer), motivating [[ActivationCheckpointing|activation checkpointing]] and [[GradientAccumulation|gradient accumulation]]. Ch 7 also contrasts [[Autograd|tape-based]] (PyTorch) vs transform-based ([[JAX]]) AD implementations.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.6.2 canonical reference.
- [[mlsysbook-ch07-ml-frameworks]] — the systems engineering of AD (memory, tape vs transform, frameworks).
- [[DualNumbers]] — the forward-mode mechanism; [[ActivationCheckpointing]] — the memory lever.
- [[Backpropagation]] — the reverse-mode special case.
- [[ReverseModeAutodiff]] / [[ForwardModeAutodiff]] — the two modes.
- [[ComputationalGraph]] — the DAG of intermediate variables AD traverses.
- [[ChainRule]] — the rule applied op-by-op.
- [[DifferenceQuotient]] — the finite-difference approximation AD improves on.
- [[Autograd]] — framework implementations (PyTorch, JAX, TensorFlow).
