---
title: "Four Pillars of Machine Learning"
type: concept
tags: [machine-learning, foundations, framework, mml]
sources: [mml-ch01-introduction-and-motivation, mml-book]
last_updated: 2026-06-04
---

# Four Pillars of Machine Learning

The central organizing metaphor of *[[mml-book|Mathematics for Machine Learning]]*, introduced in **Figure 1.1** (§1.2, p. 14): a temple in which a pediment labeled **Machine Learning** rests on **four pillars** — fundamental ML problems — that in turn stand on a two-tier foundation of **six mathematical disciplines**. Part I of the book lays the six foundations; Part II builds the four pillars on top of them.

## The four pillars (Part II)

The four pillars are the fundamental ML problems the book treats as *worked examples* of its mathematics (broadly ordered by ascending difficulty):

| Pillar | Chapter | Method used | Labels? | Output |
|---|---|---|---|---|
| **[[Regression]]** | Ch 9 — [[LinearRegression\|linear regression]] | MLE / [[BayesianLinearRegression\|Bayesian]] | yes ($y \in \mathbb{R}$) | real-valued |
| **[[DimensionalityReduction]]** | Ch 10 — [[PrincipalComponentAnalysis\|PCA]] | maximum variance / min reconstruction error | no | low-dim representation of $\boldsymbol{x} \in \mathbb{R}^D$ |
| **Density estimation** | Ch 11 — [[GaussianMixtureModel\|Gaussian mixture models]] | EM | no | a probability distribution over the data |
| **[[Classification]]** | Ch 12 — [[SupportVectorMachine\|support vector machines]] | margin maximization (convex QP) | yes ($y$ integer) | integer label |

Two of the four are *supervised* (regression and classification have labels $y$); two are *unsupervised* (dimensionality reduction and density estimation have no labels). Dimensionality reduction and density estimation differ in their goal: the former seeks a low-dimensional *representation*, the latter a *density model* of the data.

## The six foundations (Part I)

The pillars rest on two foundation rows (Figure 1.1):

- **Upper row** — [[VectorCalculus|Vector Calculus]] (Ch 5, gradients), [[ProbabilityAndDistributions|Probability & Distributions]] (Ch 6, uncertainty), [[ContinuousOptimization|Optimization]] (Ch 7, finding maxima/minima).
- **Lower row** — [[LinearAlgebra|Linear Algebra]] (Ch 2, vectors & matrices), [[AnalyticGeometry|Analytic Geometry]] (Ch 3, similarity & distance), [[MatrixDecomposition|Matrix Decomposition]] (Ch 4, factoring matrices).

The book emphasizes a *modular* design (§1.2, p. 13): foundational mathematics is separated from applications so the book can be read either **bottom-up** (foundations first, the mathematician's order) or **top-down** (drill down from an ML need to the math it requires). Part I chapters mostly build on previous ones; Part II chapters are only loosely coupled and can be read in any order, with many cross-pointers between the parts.

## Why this framing

The four pillars are deliberately a *small, representative* set — not an ML survey. They serve as concrete destinations that motivate every piece of Part I mathematics, so that foundational definitions (which "are quickly forgotten" when learned without motivation, §1.2, p. 13) acquire a clear purpose.

## Connections

- [[mml-ch01-introduction-and-motivation]] — Figure 1.1 and the two-part / two-reading-strategy framing.
- [[mml-book]] — the umbrella source page; this concept is the book's table of contents in metaphor form.
- [[MachineLearning]] — the four-pillars view is MML's structuring of the field.
- [[Regression]] / [[DimensionalityReduction]] / [[Classification]] / [[GaussianMixtureModel]] — the four pillars.
- [[LinearAlgebra]] / [[AnalyticGeometry]] / [[MatrixDecomposition]] / [[VectorCalculus]] / [[ProbabilityAndDistributions]] / [[ContinuousOptimization]] — the six foundations.
- [[Predictor]] / [[Training]] — the data / model / learning trichotomy each pillar instantiates.
