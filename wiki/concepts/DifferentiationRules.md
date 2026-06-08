---
title: "Differentiation Rules"
type: concept
tags: [calculus, vector-calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book]
last_updated: 2026-06-04
---

# Differentiation Rules

The algebraic rules for differentiating combinations of functions, so derivatives of complicated expressions reduce to derivatives of their parts.

## Univariate ([[mml-ch05-vector-calculus|MML Ch 5]] §5.1.2, Eqs. 5.29–5.32)

Denoting $f'=\frac{\mathrm{d}f}{\mathrm{d}x}$:

| Rule | Formula |
|---|---|
| **Product** | $(f(x)g(x))' = f'(x)g(x) + f(x)g'(x)$ |
| **Quotient** | $\left(\dfrac{f(x)}{g(x)}\right)' = \dfrac{f'(x)g(x) - f(x)g'(x)}{(g(x))^2}$ |
| **Sum** | $(f(x)+g(x))' = f'(x) + g'(x)$ |
| **[[ChainRule\|Chain]]** | $(g\circ f)'(x) = g'(f(x))\,f'(x)$ |

Worked example (MML Example 5.5): $h(x)=(2x+1)^4$ with $f=2x+1$, $g(f)=f^4$ gives $h'(x)=g'(f)f'(x)=4f^3\cdot 2=8(2x+1)^3$.

## Multivariate ([[mml-ch05-vector-calculus|MML Ch 5]] §5.2.1, Eqs. 5.46–5.48)

The same rules hold for $\mathbf{x}\in\mathbb{R}^n$, **but the order matters** — gradients are now vectors/matrices and matrix multiplication is non-commutative:

$$\frac{\partial}{\partial\mathbf{x}}(f(\mathbf{x})g(\mathbf{x})) = \frac{\partial f}{\partial\mathbf{x}}g(\mathbf{x}) + f(\mathbf{x})\frac{\partial g}{\partial\mathbf{x}}, \qquad \frac{\partial}{\partial\mathbf{x}}(f+g) = \frac{\partial f}{\partial\mathbf{x}} + \frac{\partial g}{\partial\mathbf{x}}, \qquad \frac{\partial}{\partial\mathbf{x}}(g\circ f) = \frac{\partial g}{\partial f}\frac{\partial f}{\partial\mathbf{x}}.$$

The multivariate [[ChainRule|chain rule]] is the workhorse — written as a left-to-right product of [[Jacobian|Jacobians]] (which is clean precisely because MML uses the [[Gradient|row-vector / numerator-layout convention]]).

## Standard elementary derivatives

$\frac{\mathrm{d}}{\mathrm{d}x}C=0$; $\frac{\mathrm{d}}{\mathrm{d}x}x^n=nx^{n-1}$ (MML derives this from the [[DifferenceQuotient|difference quotient]] in Example 5.2); $\frac{\mathrm{d}}{\mathrm{d}x}e^x=e^x$; $\frac{\mathrm{d}}{\mathrm{d}x}\ln x=x^{-1}$; $\frac{\mathrm{d}}{\mathrm{d}x}\sin x=\cos x$; $\frac{\mathrm{d}}{\mathrm{d}x}\cos x=-\sin x$.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.1.2 + §5.2.1 canonical reference.
- [[ChainRule]] — the most important rule; basis of [[Backpropagation|backprop]].
- [[derivatives]] — the underlying operator and standard derivatives.
- [[DifferenceQuotient]] — where the rules ultimately come from.
- [[Gradient]] / [[Jacobian]] — the multivariate operands.
