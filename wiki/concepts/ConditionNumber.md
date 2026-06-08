---
title: "Condition Number"
type: concept
tags: [optimization, numerical-linear-algebra, gradient-descent]
sources: [mml-ch07-continuous-optimization, mml-book]
last_updated: 2026-06-05
---

# Condition Number

Ratio $\kappa = \sigma_{\max}(\mathbf{A})/\sigma_{\min}(\mathbf{A})$ of the largest to smallest singular value (§4.5 / [[SingularValueDecomposition]]) — how much a linear system amplifies error. Large $\kappa$ ⇒ ill-conditioned ⇒ [[GradientDescent]] zigzags ⇒ need a [[Preconditioner]].

## From [[mml-ch07-continuous-optimization|MML Ch 7]]

[[mml-ch07-continuous-optimization|MML Ch 7]] §7.1.1 (Remark, p. 230): when gradient descent is applied to a linear system $\mathbf{A}\mathbf{x}=\mathbf{b}$, **the speed of convergence depends on $\kappa$**. The condition number "essentially measures the ratio of the most curved direction versus the least curved direction" — i.e. **poorly conditioned problems are long, thin valleys** (very curved one way, very flat the other). Plain GD then "zigzags as the gradients point nearly orthogonally to the shortest direction to a minimum point" (Fig. 7.3). The fix is to solve the **[[Preconditioner|preconditioned]]** system $\mathbf{P}^{-1}(\mathbf{A}\mathbf{x}-\mathbf{b})=\mathbf{0}$ where $\mathbf{P}^{-1}\mathbf{A}$ has a smaller $\kappa$ but $\mathbf{P}^{-1}$ stays cheap (Boyd & Vandenberghe 2004, ch. 9). [[Momentum]] mitigates the same pathology by leaky averaging.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.1.1 canonical reference.
- [[GradientDescent]] — convergence speed it governs.
- [[Preconditioner]] — reduces $\kappa$.
- [[Momentum]] — alternative remedy for ill-conditioning.
- [[SingularValueDecomposition]] — defines $\sigma_{\max},\sigma_{\min}$ (§4.5).
