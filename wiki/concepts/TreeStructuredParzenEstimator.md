---
title: "Tree-Structured Parzen Estimator"
type: concept
tags: [bayesian-optimization, hyperparameter-tuning, surrogate-model, optuna]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# Tree-Structured Parzen Estimator

**TPE** — Bergstra et al. 2011's [[BayesianOptimization|Bayesian]] surrogate-model approach to [[HyperparameterOptimization|HPO]]. Rather than fitting a single $p(y\mid x)$ regression model (as a [[GaussianProcess|GP]] would), TPE models the *conditional distributions* of the inputs $x$ split by the objective value $y$:

$$p(x \mid y) = \begin{cases} \ell(x) & \text{if } y < y^* \\ g(x) & \text{if } y \geq y^* \end{cases}$$

Both $\ell$ and $g$ are estimated by Parzen-window (kernel-density) estimators built from past observations. The acquisition function is **Expected Improvement** which, under the TPE factorization, reduces to maximizing $\ell(x)/g(x)$ — choose configurations more likely under the "good" half of past observations than the "bad" half.

## The "tree-structured" qualifier

TPE's defining feature is its **support for hierarchical / conditional search spaces**: parameter $a$'s validity depends on the value of parameter $b$. TPE handles this by modeling the joint as a tree of conditional distributions and routing density estimation along the tree. Hierarchical search spaces are the norm in [[NeuralArchitectureSearch|NAS]] and pipeline-style search problems.

## Role in [[MIPROv2|MIPRO]]

The [[2406.11695-mipro|MIPRO paper]] uses **[[Optuna]]'s multivariate TPE implementation** (Falkner et al. 2018 — BOHB) to build a Bayesian surrogate over the joint space of per-module (instruction, demo-set) tuples in the [[LMProgram|LM program]] $\Phi$. The multivariate variant *"models joint contributions between parameter choices, allowing us to jointly optimize over your program's variables"* — which is the structural feature MIPRO needs for **[[CreditAssignment|credit assignment]]** across modules (Lesson 3 of the paper).

The TPE surrogate is what gives MIPRO its **mini-batch tolerance**: TPE-based optimization is robust to noise, so MIPRO can evaluate candidate programs on small mini-batches (size $B$) rather than the full training set at each iteration, amortizing the LM-call budget.

## Limitation noted by the [[2406.11695-mipro|MIPRO paper]]

The surrogate *"only allows for optimization over a fixed set of proposals. Learnings from past evaluations cannot be used to improve the proposals themselves."* This is the **specific gap** that [[2507.19457-gepa|GEPA (2026)]] addresses with reflective prompt mutation, which generates new proposals from evaluation traces.

## Connections

- [[BayesianOptimization]] — TPE is one of the surrogate families used in BO; sibling to [[GaussianProcess|GP]] and random-forest surrogates.
- [[Optuna]] — the open-source HPO framework that ships TPE; [[MIPROv2|MIPRO]]'s implementation calls into it.
- [[HyperOpt]] — Bergstra's original TPE library.
- [[2406.11695-mipro]] — the canonical wiki anchor for TPE-in-LLM-program-optimization.
- [[MIPROv2|MIPRO]] — the LM-program optimizer using TPE as its search engine.
- [[d2l-hyperparameter-optimization]] — the [[d2l-preface|D2L]] chapter that establishes the broader [[BayesianOptimization|BO]] framework.
