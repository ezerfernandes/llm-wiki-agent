---
title: "Spectral Norm"
type: concept
tags: [linear-algebra, norm, svd, matrix-algebra]
sources: [mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Spectral Norm

**Definition 4.23** ([[mml-book]] §4.6): for $\mathbf{x}\in\mathbb{R}^n\setminus\{\mathbf{0}\}$, the *spectral norm* of a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ is

$$\|\mathbf{A}\|_2 := \max_{\mathbf{x}}\frac{\|\mathbf{A}\mathbf{x}\|_2}{\|\mathbf{x}\|_2}.$$

It measures **how long any vector $\mathbf{x}$ can at most become when multiplied by $\mathbf{A}$** — i.e. the maximum stretch factor of the linear map. It is the matrix operator norm induced by the Euclidean ($\ell_2$) vector [[Norm|norm]].

## Largest singular value

**Theorem 4.24** ([[mml-book]] §4.6): the spectral norm of $\mathbf{A}$ equals its **largest singular value**:

$$\|\mathbf{A}\|_2 = \sigma_1.$$

(Proof is Exercise 4.12.) This is intuitive from the [[SingularValueDecomposition|SVD]]: $\mathbf{A}=\mathbf{U}\boldsymbol\Sigma\mathbf{V}^\top$ with orthogonal $\mathbf{U},\mathbf{V}$ preserves length, so the maximum stretch is the largest diagonal entry $\sigma_1$ of $\boldsymbol\Sigma$.

## Notational note

The subscript "2" on the *matrix* norm $\|\mathbf{A}\|_2$ echoes the subscript on the *vector* Euclidean norm $\|\mathbf{x}\|_2$ (§3.1) — same symbol, **different object** (operator norm of a matrix vs Euclidean length of a vector). MML flags this overload explicitly.

## Role in Eckart–Young

The spectral norm is the norm in which the truncated SVD is the optimal [[LowRankApproximation|low-rank approximation]]: the [[EckartYoung|Eckart–Young theorem]] (Thm 4.25) gives $\|\mathbf{A}-\widehat{\mathbf{A}}(k)\|_2=\sigma_{k+1}$, the first discarded singular value.

## Related: condition number

The ratio of largest to smallest singular value, $\kappa=\sigma_{\max}/\sigma_{\min}$, is the [[ConditionNumber|condition number]] ([[mml-book]] §7.1.1) — it controls gradient-descent convergence and numerical stability of linear solves.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.6 canonical reference (Def. 4.23, Thm 4.24).
- [[SingularValueDecomposition]] — $\|\mathbf{A}\|_2=\sigma_1$, the largest singular value.
- [[EckartYoung]] / [[LowRankApproximation]] — the spectral norm is the metric of approximation optimality.
- [[Norm]] — the vector $\ell_2$ norm that induces this operator norm.
- [[ConditionNumber]] — $\sigma_{\max}/\sigma_{\min}$, built from the same singular values.
</content>
