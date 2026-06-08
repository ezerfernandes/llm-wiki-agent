---
title: "Difference Quotient"
type: concept
tags: [calculus, vector-calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book]
last_updated: 2026-06-04
---

# Difference Quotient

The average slope of a function $f$ over an interval — the slope of the **secant line** through two points on its graph ([[mml-ch05-vector-calculus|MML Ch 5]] §5.1, Def. 5.1, Eq. 5.3):

$$\frac{\delta y}{\delta x} := \frac{f(x+\delta x) - f(x)}{\delta x}.$$

It is the rate of change of $f$ between $x$ and $x+\delta x$. As $\delta x\to 0$ the secant rotates into the **tangent**, and the difference quotient becomes the [[derivatives|derivative]] $\frac{\mathrm{d}f}{\mathrm{d}x}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$ ([[mml-ch05-vector-calculus|MML Ch 5]] Def. 5.2, Eq. 5.4) — i.e. the difference quotient *defines* the derivative (Fig. 5.2 mind map: "Difference quotient — defines → Partial derivatives").

## Why it matters

- **Foundation of all differentiation.** Every derivative, [[PartialDerivative|partial derivative]] (the multivariate version, Eq. 5.39), [[Gradient|gradient]], and [[Jacobian]] in the chapter is ultimately a difference-quotient limit.
- **Gradient checking** ([[mml-ch05-vector-calculus|MML Ch 5]] §5.2.2 Remark): because the partial derivative *is* a limit of difference quotients, you can numerically verify an analytic gradient implementation with a finite-difference approximation (small $h\approx 10^{-4}$) and check the relative error is below $\sim 10^{-6}$. This is the standard sanity check before trusting a hand-coded gradient or a custom autograd op.
- Distinct from the **finite-difference numerical gradient** that [[AutomaticDifferentiation|automatic differentiation]] explicitly improves on: AD computes the *exact* gradient (up to machine precision), avoiding the truncation/round-off tradeoff of choosing $h$.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.1 Def 5.1 canonical reference.
- [[derivatives]] — the limit of the difference quotient.
- [[PartialDerivative]] — the multivariate difference-quotient limit (one coordinate at a time).
- [[Gradient]] / [[Jacobian]] — built from those partials.
- [[AutomaticDifferentiation]] — exact gradients vs the finite-difference approximation.
