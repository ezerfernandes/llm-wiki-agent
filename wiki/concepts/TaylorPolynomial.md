---
title: "Taylor Polynomial"
type: concept
tags: [calculus, vector-calculus, approximation, foundational]
sources: [mml-ch05-vector-calculus, mml-book]
last_updated: 2026-06-04
---

# Taylor Polynomial

The degree-$n$ truncation of the [[TaylorSeries|Taylor series]] — a *polynomial approximation* of a function $f$ near an expansion point $x_0$.

**Univariate** ([[mml-ch05-vector-calculus|MML Ch 5]] §5.1.1, Def. 5.3, Eq. 5.7):

$$T_n(x) := \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k,$$

where $f^{(k)}(x_0)$ is the $k$th derivative of $f$ at $x_0$ and $\frac{f^{(k)}(x_0)}{k!}$ are the coefficients (using the convention $t^0:=1$).

**Multivariate** ([[mml-ch05-vector-calculus|MML Ch 5]] §5.8, Def. 5.8, Eq. 5.152): for $f:\mathbb{R}^D\to\mathbb{R}$ with $\boldsymbol\delta:=\mathbf{x}-\mathbf{x}_0$,

$$T_n(\mathbf{x}) = \sum_{k=0}^n \frac{D_\mathbf{x}^k f(\mathbf{x}_0)}{k!}\boldsymbol\delta^k,$$

where $D_\mathbf{x}^k f(\mathbf{x}_0)$ is the $k$th (total) derivative tensor and $\boldsymbol\delta^k$ is the $k$-fold outer product (a $k$th-order [[Tensor|tensor]]).

## Approximation vs exact

- In general $T_n$ *approximates* $f$ in a neighborhood of $x_0$ and improves with $n$ (Fig. 5.4: $T_0,T_1,T_5,T_{10}$ of $\sin x+\cos x$ — higher order = better, more global fit; $T_{10}$ already matches $f$ on $[-4,4]$).
- For a **polynomial** $f$ of degree $k$, the Taylor polynomial of degree $n\geq k$ is an **exact** representation (all higher derivatives vanish). MML's two sanity checks: Example 5.3 ($f(x)=x^4$, $T_6$ at $x_0=1$ reassembles to $x^4$ exactly) and Example 5.15 ($f(x,y)=x^2+2xy+y^3$, the degree-3 multivariate Taylor expansion at $(1,2)$ reproduces $f$ exactly).

## Low-order terms have names

- **$T_1$ = [[Linearization|linearization]]**: $f(\mathbf{x})\approx f(\mathbf{x}_0)+\nabla f(\mathbf{x}_0)\boldsymbol\delta$ (first-order, Eq. 5.148).
- **$T_2$** adds the [[Hessian]] quadratic term $\frac{1}{2}\boldsymbol\delta^\top\mathbf{H}(\mathbf{x}_0)\boldsymbol\delta$ — the basis of Newton's method and the [[LaplaceApproximation|Laplace approximation]].

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.1.1 Def 5.3 + §5.8 Def 5.8 canonical references.
- [[TaylorSeries]] — the $n\to\infty$ limit.
- [[Linearization]] — the degree-1 case.
- [[Hessian]] — the degree-2 coefficient (multivariate).
- [[Jacobian]] / [[Gradient]] — the degree-1 coefficient (multivariate).
- [[Tensor]] — the $\boldsymbol\delta^k$ outer-product terms.
