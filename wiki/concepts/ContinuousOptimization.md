---
title: "Continuous Optimization"
type: concept
tags: [optimization, foundational]
sources: [mml-ch07-continuous-optimization, mml-book]
last_updated: 2026-06-05
---

# Continuous Optimization

Numerical minimization of differentiable objectives over **continuous** variables in $\mathbb{R}^D$ (as opposed to *combinatorial* optimization over discrete variables): [[GradientDescent]], [[Momentum]], [[StochasticGradientDescent]], [[LagrangeMultipliers]], [[ConvexOptimization]]. The optimization engine for training every ML model in [[mml-book]] Part II.

## From [[mml-ch07-continuous-optimization|MML Ch 7]]

[[mml-ch07-continuous-optimization|MML Ch 7]] closes Part I (Mathematical Foundations) and splits the field three ways (mind map Fig. 7.1):

- **Unconstrained** (§7.1) — solve $\min_{\mathbf{x}} f(\mathbf{x})$ for differentiable $f$ with no closed form via [[GradientDescent|gradient descent]], its [[Momentum|momentum]] and [[StochasticGradientDescent|stochastic]] variants, tuned by the [[LearningRate|step-size]] and shaped by the [[ConditionNumber|condition number]].
- **Constrained** (§7.2) — handle $g_i(\mathbf{x})\le0$ / $h_j(\mathbf{x})=0$ via [[LagrangeMultipliers|Lagrange multipliers]], the [[Lagrangian]], and [[LagrangianDuality|Lagrangian duality]] ([[KKTConditions|KKT conditions]]).
- **[[ConvexOptimization|Convex]]** (§7.3) — the special class (convex objective + convex feasible set) where **every local minimum is a global minimum** and [[Duality|strong duality]] holds; includes [[LinearProgramming|linear]] and [[QuadraticProgramming|quadratic]] programming and the [[ConvexConjugate|Legendre–Fenchel transform]].

Two foundational assumptions: $f$ is **differentiable** (gradient available everywhere; the gradient points *uphill*, recall [[mml-ch05-vector-calculus|Ch 5]]) and, by ML convention, we **minimize**. The chapter feeds forward to Ch 9 (regression), Ch 10 (PCA), Ch 11 (GMM), and Ch 12 ([[SupportVectorMachine|SVM]]).

## Connections

- [[mml-ch07-continuous-optimization]] — canonical deep dive.
- [[GradientDescent]] / [[Momentum]] / [[StochasticGradientDescent]] — unconstrained methods.
- [[LagrangeMultipliers]] / [[Lagrangian]] / [[LagrangianDuality]] — constrained machinery.
- [[ConvexOptimization]] / [[Convexity]] — the tractable special case.
