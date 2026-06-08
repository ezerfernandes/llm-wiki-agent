---
title: "Taylor Series"
type: concept
tags: [vector-calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book, d2l-appendix-mathematics]
last_updated: 2026-06-04
---

# Taylor Series

A representation of a function $f$ as an infinite sum of derivative-weighted polynomial terms ([[mml-book]] §5.1.1, Def 5.4):

$$T_\infty(x) := \sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k.$$

The truncation to degree $n$ is the **Taylor polynomial** $T_n(x)$ — an *approximation* of $f$ near $x_0$.

## Multivariate Taylor

For $f:\mathbb{R}^D\to\mathbb{R}$, the second-order Taylor expansion at $\mathbf{x}_0$ is ([[mml-book]] §5.8):

$$f(\mathbf{x}_0 + \boldsymbol\delta) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)\boldsymbol\delta + \tfrac{1}{2}\boldsymbol\delta^\top \nabla^2 f(\mathbf{x}_0)\,\boldsymbol\delta.$$

First-order Taylor = [[Linearization]] (the local linear approximation of $f$ near $\mathbf{x}_0$). The first-order term is the [[Jacobian]]; the second-order term is the [[Hessian]] $\nabla^2 f$.

## Where Taylor surfaces in ML

- **[[LaplaceApproximation]]**: second-order Taylor of $\log p(\boldsymbol\theta\mid\mathcal{D})$ at the MAP estimate gives the Gaussian approximation to the posterior — variance comes from $-\nabla^2$ of the log-posterior (the Fisher information).
- **Newton's method**: optimization step $\boldsymbol\theta\leftarrow\boldsymbol\theta - [\nabla^2 f]^{-1}\nabla f$ uses the second-order Taylor approximation to find a quadratic-model minimum.
- **Gauss-Newton / Levenberg-Marquardt**: nonlinear least squares = repeated linearization (first-order Taylor) of the residuals.
- **Score matching / diffusion**: log-density gradients live in the first-order Taylor remainder of $\log p$.

## Polynomials are *exact* Taylor

[[mml-book]] §5.1 Example 5.3: the degree-$n$ Taylor polynomial of a degree-$n$ polynomial equals the original polynomial — the Taylor expansion is exact, not an approximation. This is the "obvious" sanity check.

## From [[mml-ch05-vector-calculus|MML Ch 5]]

**Univariate (§5.1.1).** Def 5.4 (Eq. 5.8) gives $T_\infty(x)=\sum_{k=0}^\infty\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$ for smooth $f\in\mathcal{C}^\infty$; at $x_0=0$ this is the **Maclaurin series**, and if $f=T_\infty$ then $f$ is **analytic**. The degree-$n$ truncation is the [[TaylorPolynomial|Taylor polynomial]] $T_n$ (Def 5.3). A Taylor series is a special **power series** $\sum a_k(x-c)^k$ (Eq. 5.28). MML Example 5.4 recovers $\cos x=\sum(-1)^k\frac{x^{2k}}{(2k)!}$ and $\sin x=\sum(-1)^k\frac{x^{2k+1}}{(2k+1)!}$ from the Maclaurin series of $\sin x+\cos x$ (Fig. 5.4: $T_{10}$ already matches $f$ on $[-4,4]$).

**Multivariate (§5.8).** Def 5.7 (Eq. 5.151): for $f:\mathbb{R}^D\to\mathbb{R}$ with $\boldsymbol\delta:=\mathbf{x}-\mathbf{x}_0$, $f(\mathbf{x})=\sum_{k=0}^\infty\frac{D_\mathbf{x}^k f(\mathbf{x}_0)}{k!}\boldsymbol\delta^k$, where both $D_\mathbf{x}^k f$ and $\boldsymbol\delta^k$ are $k$th-order [[Tensor|tensors]] and $\boldsymbol\delta^k$ is the $k$-fold outer product (Eqs. 5.153–5.155; $\boldsymbol\delta^2=\boldsymbol\delta\boldsymbol\delta^\top$). The low-order terms: $k=0$ is $f(\mathbf{x}_0)$; $k=1$ is $\nabla_\mathbf{x}f(\mathbf{x}_0)\boldsymbol\delta$ ([[Linearization]]); $k=2$ is $\frac{1}{2}\boldsymbol\delta^\top\mathbf{H}(\mathbf{x}_0)\boldsymbol\delta$ (the [[Hessian]] quadratic form, Eqs. 5.156–5.159). MML Example 5.15 expands $f(x,y)=x^2+2xy+y^3$ at $(1,2)$ — the degree-3 expansion reproduces the polynomial exactly. (Marginals show numpy `einsum` implementations of the tensor terms.)

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.1.1 (univariate) + §5.8 (multivariate) canonical references.
- [[mml-book]] — umbrella source.
- [[TaylorPolynomial]] — the degree-$n$ truncation.
- [[PartialDerivative]] — building block.
- [[Jacobian]] / [[Gradient]] — first-order coefficient (multivariate).
- [[Hessian]] — second-order coefficient (multivariate).
- [[Linearization]] — first-order truncation.
- [[LaplaceApproximation]] — second-order Taylor of a log-density.
- [[remarkable-limits]] — algebrica.org's limit-based intro to differentiation.
