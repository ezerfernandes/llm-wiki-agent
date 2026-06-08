---
title: "Linear Programming"
type: concept
tags: [optimization, convex-optimization, linear-programming, duality, foundational]
sources: [mml-ch07-continuous-optimization, mml-book]
last_updated: 2026-06-05
---

# Linear Programming

The convex-optimization sub-class where **objective and constraints are all linear** ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.3.1, Eq. 7.39):

$$\min_{\mathbf{x}\in\mathbb{R}^d}\ \mathbf{c}^\top\mathbf{x}\quad\text{subject to}\quad\mathbf{A}\mathbf{x}\leq\mathbf{b},$$

with $\mathbf{A}\in\mathbb{R}^{m\times d}$ and $\mathbf{b}\in\mathbb{R}^m$ — $d$ variables, $m$ linear constraints. "Linear programs are one of the most widely used approaches in industry" ([[mml-ch07-continuous-optimization|MML Ch 7]] margin, p. 239). The feasible region is a convex polytope; because both objective and contour lines are linear, the optimum sits at a **vertex** of the polytope (Example 7.5, Fig. 7.9).

## The dual LP (via [[LagrangianDuality|Lagrangian duality]])

[[Lagrangian]]: $\mathfrak{L}(\mathbf{x},\boldsymbol\lambda)=\mathbf{c}^\top\mathbf{x}+\boldsymbol\lambda^\top(\mathbf{A}\mathbf{x}-\mathbf{b})=(\mathbf{c}+\mathbf{A}^\top\boldsymbol\lambda)^\top\mathbf{x}-\boldsymbol\lambda^\top\mathbf{b}$ (Eqs. 7.40–7.41) with $\boldsymbol\lambda\ge\mathbf{0}$. Setting $\partial_{\mathbf{x}}\mathfrak{L}=\mathbf{0}$ gives $\mathbf{c}+\mathbf{A}^\top\boldsymbol\lambda=\mathbf{0}$ (Eq. 7.42), so the dual function is $\mathfrak{D}(\boldsymbol\lambda)=-\boldsymbol\lambda^\top\mathbf{b}$ and the **dual program** (Eq. 7.43) is

$$\max_{\boldsymbol\lambda\in\mathbb{R}^m}\ -\mathbf{b}^\top\boldsymbol\lambda\quad\text{subject to}\quad\mathbf{c}+\mathbf{A}^\top\boldsymbol\lambda=\mathbf{0},\ \ \boldsymbol\lambda\geq\mathbf{0}.$$

This is **also a linear program**, but with $m$ variables. Convention: minimize the primal, maximize the dual. Choose to solve the primal ($d$ vars) or the dual ($m$ vars) depending on whether $d$ or $m$ is larger ([[mml-ch07-continuous-optimization|MML Ch 7]] p. 240).

## Algorithms

Solved by the **simplex** method (vertex-walking) or **interior-point** methods. (Exercise 7.5–7.6 of [[mml-ch07-continuous-optimization|MML Ch 7]] ask to write a problem in standard LP form and derive the dual.)

## Connections

- [[mml-ch07-continuous-optimization]] — §7.3.1 canonical reference.
- [[ConvexOptimization]] — LP is the all-linear special case.
- [[QuadraticProgramming]] — the quadratic-objective sibling.
- [[LagrangianDuality]] / [[Duality]] — source of the dual LP.
- [[Lagrangian]] — the function used to derive the dual.
</content>
