---
title: "Dive into Deep Learning — Preliminaries"
type: source
tags: [textbook, d2l, preliminaries, tensors, linear-algebra, calculus, probability, autograd]
date: 2026-05-16
source_file: raw/d2l-en/chapter_preliminaries/
---

## Summary

The [[d2l-preface|D2L]] *Preliminaries* chapter — the seven-section "survival skills" prerequisite for the rest of the book. Covers (i) [[NDArray|n-dimensional arrays / tensors]] (`ndarray.md`); (ii) [[pandas]] data preprocessing (`pandas.md`); (iii) [[LinearAlgebra]] from scalars to matrix multiplication and norms (`linear-algebra.md`); (iv) [[Calculus]] — derivatives, [[PartialDerivative|partial derivatives]], [[Gradient|gradients]], [[ChainRule|chain rule]] (`calculus.md`); (v) [[Autograd|automatic differentiation]] (`autograd.md`); (vi) [[probability|probability and statistics]] (`probability.md`); (vii) API lookup via `dir`/`help` (`lookup-api.md`). Each section is multi-framework: same exercises in [[MXNet]] / [[PyTorch]] / [[TensorFlow]] / [[JAX]], selectable via the `d2lbook.tab` notebook switch.

## Key Claims

- **Tensor = N-dim array generalizing scalars (0th-order) / vectors (1st-order) / matrices (2nd-order)**. All four frameworks expose a near-identical NumPy-like API for `arange` / `zeros` / `ones` / `randn` / `reshape` / indexing / slicing / `cat`. The tensor class adds two "killer features" over [[NumPy]]'s ndarray: [[Autograd|automatic differentiation]] and GPU acceleration.
- **[[Broadcasting]]** lets elementwise operations work on shape-mismatched tensors when axes of length 1 can be stretched — a $3\times1$ + $1\times2$ produces a $3\times2$ result. Same rules as NumPy.
- **In-place updates matter for training**: `Y = X + Y` allocates new memory; `Y[:] = X + Y` or `X += Y` does not. Parameters get updated millions of times — wasted allocations are a leak risk and a speed hit. PyTorch/MXNet share memory with NumPy on conversion; JAX arrays are immutable (use `.at[].set()`).
- **CSV + [[pandas]] is the default ingestion path**: `pd.read_csv` → split into `inputs, targets` via `iloc` → `pd.get_dummies(inputs, dummy_na=True)` for categorical (treats `NaN` as a category) → `fillna(inputs.mean())` for numerical → `.to_numpy(dtype=float)` → wrap in framework tensor. Imputation vs deletion are the two missing-value heuristics.
- **Linear-algebra hierarchy**: scalar ($\mathbb{R}$) ⊂ vector ($\mathbb{R}^n$, 1st-order tensor) ⊂ matrix ($\mathbb{R}^{m\times n}$, 2nd-order) ⊂ higher-order tensor. The chapter distinguishes **order** (number of axes) from **dimensionality** (length along an axis) to avoid the overloaded word "dimension". Images = 3rd-order ($H\times W\times C$); batches of images = 4th-order ($B\times H\times W\times C$).
- **Hadamard product $\mathbf{A}\odot\mathbf{B}$ ≠ matrix multiplication**. Elementwise (`A * B`) is quadratic time; matmul (`A @ B`, `torch.mm`, `tf.matmul`) is cubic. Matrix–vector product $\mathbf{A}\mathbf{x}$ is the row-wise [[DotProduct|dot product]] and underlies every neural-network forward pass.
- **Norms** are functions $\|\cdot\|:V\to\mathbb{R}$ obeying absolute homogeneity + triangle inequality + positive-definiteness. The $\ell_2$ (Euclidean) norm = $\sqrt{\sum x_i^2}$; the $\ell_1$ (Manhattan) norm = $\sum|x_i|$, less sensitive to outliers; general $\ell_p$ = $(\sum|x_i|^p)^{1/p}$. For matrices, the **Frobenius norm** $\|\mathbf{X}\|_F = \sqrt{\sum x_{ij}^2}$ is the $\ell_2$ of the flattened matrix and is computationally cheap; the **spectral norm** is harder but matters for adversarial robustness.
- **Derivative as instantaneous rate of change**: $f'(x) = \lim_{h\to 0} (f(x+h)-f(x))/h$. The chapter visualizes this empirically by halving $h$ and watching $f'(1) = 2$ emerge for $f(x) = 3x^2 - 4x$. Standard rules: constant, power, $e^x$, $\ln x$, plus sum / product / quotient / constant-multiple.
- **Partial derivatives generalize to multivariate functions**. The [[Gradient|gradient]] $\nabla_\mathbf{x} f(\mathbf{x}) = [\partial f/\partial x_1, \ldots, \partial f/\partial x_n]^\top$ is the column-vector of partials (D2L uses the column-vector convention — opposite of [[mml-book|MML]]'s row-vector convention). Key identities: $\nabla_\mathbf{x} \mathbf{A}\mathbf{x} = \mathbf{A}^\top$; $\nabla_\mathbf{x} \mathbf{x}^\top\mathbf{A}\mathbf{x} = (\mathbf{A}+\mathbf{A}^\top)\mathbf{x}$; $\nabla_\mathbf{x} \|\mathbf{x}\|^2 = 2\mathbf{x}$.
- **[[ChainRule]] is the load-bearing identity**: for $y = f(g(x))$, $dy/dx = (dy/du)(du/dx)$. Multivariate version: $\nabla_\mathbf{x} y = \mathbf{A}\,\nabla_\mathbf{u} y$ where $\mathbf{A}$ is the Jacobian of $\mathbf{u}$ wrt $\mathbf{x}$. This is *why* [[LinearAlgebra]] is integral to deep learning — gradient evaluation = vector–matrix product traversal.
- **Autograd builds a computational graph during the forward pass and walks it backwards via the chain rule = [[Backpropagation]]**. PyTorch: `x.requires_grad_(True)` → forward → `y.backward()` → read `x.grad`. TensorFlow: `with tf.GradientTape() as t:` → `t.gradient(y, x)`. JAX: `grad(f)(x)` — functional, not stateful. MXNet: `autograd.record()` scope + `y.backward()`. **Earliest autograd reference: Wengert 1964; modern backprop ideas: Speelpenning 1980, Griewank 1989.**
- **Autograd handles Python control flow** (while/if). The graph is realized *per execution*, so `backward()` always works even when iteration count depends on data. For non-scalar `y`, frameworks reduce-via-sum before differentiating (true [[Jacobian]] requires `vmap` or explicit Jacobian APIs). `detach()` / `stop_gradient` removes a subgraph from the gradient flow without erasing the graph leading to it.
- **PyTorch *accumulates* gradients across `backward()` calls**; MXNet, TensorFlow, JAX overwrite. Hence `x.grad.zero_()` is mandatory between PyTorch optimization steps. This footgun is unique to PyTorch but is exploited deliberately for multi-objective sums.
- **Probability has two competing interpretations**: **frequentist** (long-run relative frequency, applies only to repeatable events) and **Bayesian** (degree of belief, applies also to non-repeatable events; admits subjective priors). Kolmogorov's 1933 axioms apply to both: $P(\mathcal{A})\geq 0$, $P(\mathcal{S})=1$, countable additivity for disjoint events.
- **[[BayesTheorem|Bayes' theorem]] derived from product rule**: $P(A,B) = P(B|A)P(A) = P(A|B)P(B) \Rightarrow P(A|B) = P(B|A)P(A)/P(B)$. The chapter walks through the canonical HIV-test example, deriving posterior $P(H=1\mid D_1=1)\approx 0.1306$ from $P(D_1=1\mid H=1)=1$, $P(D_1=1\mid H=0)=0.01$, prevalence $P(H=1)=0.0015$. A second independent test brings it to 0.99 — illustrating chained Bayesian updates.
- **Independence, conditional independence, and "explaining away"**: $A\perp B \iff P(A,B)=P(A)P(B)$. Two variables independent in general can become *dependent* when conditioning on a common effect (broken bones vs lung cancer, conditional on hospitalization); two dependent variables can become *independent* when conditioning on a common cause (shoe size vs reading level, conditional on age).
- **Law of large numbers + central limit theorem** govern the convergence of sample frequencies to true probabilities at rate $O(1/\sqrt n)$. Simulating 10,000 fair-coin tosses visibly converges to 0.5.
- **API discovery via `dir(module)` and `help(function)`** is the recommended documentation strategy — paired with the official framework docs (mxnet.apache.org / pytorch.org/docs / tensorflow.org/api_docs).

## Key Quotes

> "There is no point in acquiring data without some way to store it, so to start, let's get our hands dirty with $n$-dimensional arrays, which we also call *tensors*." — `ndarray.md`, opener

> "The tensor class is the main interface for storing and manipulating data in deep learning libraries." — `ndarray.md`, Summary

> "Norms capture various notions of the magnitude of a vector (or matrix), and are commonly applied to the difference of two vectors to measure their distance apart." — `linear-algebra.md`, Discussion

> "The chain rule states that $\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}$. […] This is one of the key reasons why linear algebra is such an integral building block in building deep learning systems." — `calculus.md`, Chain Rule

> "Fortunately all modern deep learning frameworks take this work off our plates by offering *automatic differentiation* (often shortened to *autograd*). As we pass data through each successive function, the framework builds a *computational graph* that tracks how each value depends on others. To calculate derivatives, automatic differentiation works backwards through this graph applying the chain rule. The computational algorithm for applying the chain rule in this fashion is called *backpropagation*." — `autograd.md`, opener

> "Probabilities are *theoretical* quantities that underly the data generating process. […] Statistics are *empirical* quantities that are computed as functions of the observed data." — `probability.md`, §A Simple Example

> "Two random variables $A$ and $B$ are *conditionally independent* given a third variable $C$ if and only if $P(A, B \mid C) = P(A \mid C)P(B \mid C)$. Interestingly, two variables can be independent in general but become dependent when conditioning on a third." — `probability.md`, §Multiple Random Variables

## Connections

- [[d2l-preface]] — parent textbook; the Preliminaries are Ch 2.
- [[d2l-introduction]] — Ch 1 (broad survey); Preliminaries delivers the mathematical/code prerequisites it foreshadows.
- [[d2l-notation]] — defines the symbol conventions Preliminaries uses ($x$, $\mathbf{x}$, $\mathbf{X}$, $\mathsf{X}$, $\partial$, $\nabla$, $P$, $\mathbb{E}$, $\|\cdot\|_p$, $\langle\cdot,\cdot\rangle$).
- [[d2l-installation]] — must precede; this chapter assumes the `d2l` conda env is active.
- [[D2LPackage]] — `from d2l import torch as d2l` is used in calculus.md / probability.md for plotting helpers.
- [[AstonZhang]] / [[ZacharyLipton]] / [[MuLi]] / [[AlexanderSmola]] — authors.
- [[Tensor]] / [[NDArray]] — the core data structure.
- [[NumPy]] — ndarray progenitor; tensor classes are NumPy-shaped.
- [[Broadcasting]] — shape-aligning rule for elementwise ops.
- [[pandas]] / [[DataFrame]] / [[CSVFormat]] / [[CategoricalData]] — data-preprocessing toolkit.
- [[LinearAlgebra]] / [[scalar]] / [[DotProduct]] / [[InnerProduct]] — vector / matrix / norm material.
- [[Norm]] — $\ell_1$, $\ell_2$, $\ell_p$, Frobenius.
- [[Calculus]] / [[derivatives]] / [[PartialDerivative]] / [[Gradient]] / [[Jacobian]] / [[Hessian]] / [[ChainRule]] — calculus material.
- [[Autograd]] / [[Backpropagation]] / [[AutomaticDifferentiation]] — section 5.
- [[probability]] / [[ProbabilitySpace]] / [[RandomVariable]] / [[BayesTheorem]] / [[JointProbability]] / [[ConditionalProbability]] / [[StatisticalIndependence]] — section 6.
- [[PyTorch]] / [[TensorFlow]] / [[JAX]] / [[MXNet]] — the four parallel framework tracks.
- [[CUDA]] — implicit infrastructure for the "GPU acceleration" claim.
- [[mml-book]] — covers the same mathematical material with deeper derivations; D2L points at MML for "if you want more linear algebra." Row-vector vs column-vector gradient convention differs (flagged on [[Gradient]] / [[PartialDerivative]]).
- [[pml1-murphy]] — Murphy's probability chapters parallel `probability.md` with more depth on frequentist–Bayesian tension.
- [[islr-seventh-printing]] — covers the probability primer with R labs instead of multi-framework Python.

## Contradictions

- **Gradient convention**: D2L uses the **column-vector convention** ($\nabla_\mathbf{x} f \in \mathbb{R}^n$, Eq. unnumbered in `calculus.md`, §"Partial Derivatives and Gradients"), opposite to [[mml-book|MML]]'s row-vector convention (MML §5.2 Eq. 5.40). Both are correct; flagged on [[Gradient]] and [[PartialDerivative]]. Cross-corpus reading requires a mental transpose.
- No direct *factual* contradictions with prior sources. Reinforces [[probability]] / [[BayesTheorem]] / [[Tensor]] / [[Autograd]] / [[Broadcasting]] / [[pandas]] / [[Norm]] / [[Gradient]] / [[Jacobian]] / [[ChainRule]] across multiple corpora (MML, Murphy, ISLR, PyData, D2L).
