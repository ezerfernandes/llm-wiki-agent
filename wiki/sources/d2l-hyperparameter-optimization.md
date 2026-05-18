---
title: "Dive into Deep Learning — Hyperparameter Optimization"
type: source
tags: [textbook, d2l, hpo, hyperparameter-optimization, random-search, hyperband, successive-halving, multi-fidelity]
date: 2026-05-16
source_file: raw/d2l-en/chapter_hyperparameter-optimization/
---

## Summary

[[AaronKlein|Klein]], [[MatthiasSeeger|Seeger]] & [[CedricArchambeau|Archambeau]] ([[Amazon]])'s five-section guest chapter on **[[HyperparameterOptimization|hyperparameter optimization (HPO)]]** — D2L's only chapter cast entirely as **black-box optimization**. Builds HPO from scratch (`HPOSearcher` / `HPOScheduler` / `HPOTuner` API), implements [[RandomSearch]] from a SciPy `loguniform` config space, distributes it asynchronously via [[SyneTune]], introduces [[MultiFidelityOptimization|multi-fidelity HPO]] with [[SuccessiveHalving]] ([[Jamieson|Jamieson & Talwalkar 2016]] / [[Karnin|Karnin et al. 2013]]) and pivots to **[[ASHA|asynchronous successive halving]]** ([[LishaLi|Li et al. 2018]]) — the algorithm that promotes configurations the moment any $\eta$ observations land on a rung, eliminating the synchronization barrier that makes synchronous SH bad on heterogeneous workers. Closes by positioning [[NeuralArchitectureSearch|NAS]] and [[AutoML]] as natural HPO extensions.

## Key Claims

- **HPO as black-box global optimization.** The performance of a learning algorithm is a function $f:\mathcal{X}\to\mathbb{R}$ from hyperparameter space to validation loss. Goal: $\mathbf{x}_\star\in\arg\min_{\mathbf{x}\in\mathcal{X}} f(\mathbf{x})$ with no usable gradient (hypergradients [[Maclaurin|Maclaurin et al. 2015]] / [[Franceschi|Franceschi et al. 2017] are not competitive yet) and noisy observations $y\sim f(\mathbf{x})+\epsilon$, $\epsilon\sim\mathcal{N}(0,\sigma)$.
- **Configuration space is structured and bounded.** Each [[Hyperparameter|hyperparameter]] has a type (`float` / `integer` / `categorical`) and a closed range with a prior — typically *uniform* for linear-scale (e.g. momentum) and *log-uniform* for parameters spanning orders of magnitude (e.g. learning rate $10^{-6}$ to $10^{-1}$). Conditional hyperparameters (number of units in layer $l$ exists only if depth $\geq l+1$) require structured spaces beyond $\mathbb{R}^d$.
- **[[RandomSearch|Random search]] is the universal baseline.** Sample independently from the prior until a budget is exhausted; return the best observation. Simple, applies to any space with a prior, trivially parallelizable. *"Random search is one of the most frequently used HPO algorithms."*
- **Random search beats grid search on effective-low-dim problems** ([[JamesBergstra|Bergstra]] & [[YoshuaBengio|Bengio]] 2012). When validation error depends strongly on a small subset of the hyperparameters, the curse of dimensionality penalizes grid search; random search "somewhat mitigates" it.
- **Random-search shortcomings motivate model-based and multi-fidelity methods.** Random search (a) does not adapt the sampling distribution based on past observations, and (b) spends the same budget on every config regardless of early performance. These two failures define the two improvement axes: **searcher** ([[BayesianOptimization]]) and **scheduler** ([[SuccessiveHalving]] / [[ASHA]] / [[Hyperband]]).
- **The searcher / scheduler / tuner API.** Every HPO algorithm decomposes into two primitives: **searching** (`HPOSearcher.sample_configuration` — choose what to evaluate next) and **scheduling** (`HPOScheduler.suggest` — decide when / how many resources). An `HPOTuner` runs the loop, tracking the [[Incumbent|incumbent]] (best config so far) and [[AnyTimePerformance|any-time performance]] as `cumulative_runtime` vs `incumbent_trajectory`. This is the API used by [[SyneTune]], [[RayTune]] and [[Optuna]].
- **[[BayesianOptimization|Bayesian optimization]] dominates random search after enough trials** ([[JasperSnoek|Snoek]] et al. 2012). With identical wall-clock budgets, BO and random search are comparable through the first ~1000 seconds; afterwards BO's surrogate-model exploitation pulls ahead. Comparing HPO algorithms requires averaging over many seeds because both training stochasticity and algorithmic randomness contribute.
- **Asynchronous parallel random search achieves linear speed-up.** With $K$ workers, asynchronous random search reaches the same performance $K\times$ faster wall-clock than sequential — because each new configuration is independent of past observations, no synchronization or coordination is needed. Synchronous schemes pay an idle-time penalty from stragglers (configs with more layers / filters take longer).
- **[[MultiFidelityOptimization|Multi-fidelity HPO]] reduces *total compute*, not just wall-clock.** Expand the objective to $f(\mathbf{x},r)$ with $r\in[r_\text{min}, r_\text{max}]$ a *resource budget* (epochs, training-subset size, CV folds). Assume $f(\mathbf{x},r)$ decreases with $r$ and cost $c(\mathbf{x},r)$ increases. Use cheap low-fidelity evaluations as proxies; stop poorly-performing configs early.
- **[[SuccessiveHalving|Successive halving]]** ([[Jamieson|Jamieson & Talwalkar 2016]] / [[Karnin|Karnin et al. 2013]]). Start $N=\eta^K$ configs at $r_\text{min}$ epochs. After each rung $r_i=r_\text{min}\eta^i$, keep the top $1/\eta$, train them on $r_{i+1}=r_i\eta$ epochs. Only one config reaches $r_\text{max}$. The rung set is $\{r_\text{min}, r_\text{min}\eta, \dots, r_\text{max}\}$; D2L uses $r_\text{min}=2$, $\eta=2$, $r_\text{max}=10$.
- **[[ASHA|Asynchronous successive halving (ASHA)]]** ([[LishaLi|Li]] et al. 2018) eliminates synchronous SH's idle-time problem by **promoting configs as soon as $\eta$ observations exist on the current rung**. This produces suboptimal initial promotions (since rungs are incomplete), but in practice the cost is small because (a) hyperparameter rankings are fairly consistent across rungs, and (b) rungs grow as the run progresses. If no config can be promoted, start a fresh trial at $r_\text{min}$.
- **HPO extends to [[NeuralArchitectureSearch|NAS]] and [[AutoML]].** NAS — finding entire architectures — is HPO with discrete architectural choices; AutoML automates the full ML pipeline (preprocessing → model → HPO). NAS is even more expensive than classical HPO ([[d2l-convolutional-modern]] / [[NeuralArchitectureSearch]] independently flag NAS's GPU-day costs).

## Key Quotes

> "Hyperparameter optimization (HPO) algorithms are designed to tackle this problem in a principled and automated fashion, by framing it as a global optimization problem. The default objective is the error on a hold-out validation dataset, but could in principle be any other business metric." — §hyperopt-intro

> "Random search is one of the most frequently used HPO algorithms. It does not require any sophisticated implementation and can be applied to any configuration space as long as we can define some probability distribution for each hyperparameter." — §hyperopt-intro

> "While random search is very simple, it is the better alternative to grid search, which simply evaluates a fixed set of hyperparameters. Random search somewhat mitigates the curse of dimensionality, and can be far more efficient than grid search if the criterion most strongly depends on a small subset of the hyperparameters." — §hyperopt-intro

> "Asynchronous random search exhibits a linear speed-up, in that a certain performance is reached $K$ times faster if $K$ trials can be run in parallel." — §rs-async

> "The main idea of ASHA is to promote configurations to the next rung level as soon as we collected at least $\eta$ observations on the current rung level. This decision rule may lead to suboptimal promotions … On the other hand, we get rid of all synchronization points this way. In practice, such suboptimal initial promotions have only a modest impact on performance." — §sh-async

## Connections

- [[AaronKlein]] / [[MatthiasSeeger]] / [[CedricArchambeau]] — chapter authors ([[Amazon]]); core developers of [[SyneTune]] and key contributors to the open-source HPO / [[AutoML]] community.
- [[Amazon]] — chapter institutional affiliation; [[SyneTune]] is an Amazon-developed library.
- [[HyperparameterOptimization]] — the umbrella concept this chapter establishes within D2L; supersedes the earlier sparse [[HyperparameterTuning]] page in technical depth.
- [[RandomSearch]] / [[GridSearch]] — the chapter's HPO baselines; [[JamesBergstra]] & [[YoshuaBengio]] 2012 prove random search dominates grid on effective-low-dim problems.
- [[BayesianOptimization]] — the model-based searcher class compared against random search in `hyperopt-api`; [[JasperSnoek]] et al. 2012 is the canonical reference.
- [[SuccessiveHalving]] / [[Hyperband]] / [[ASHA]] — the multi-fidelity scheduler family; [[Jamieson]] / [[Karnin]] / [[LishaLi]] are the originating authors.
- [[MultiFidelityOptimization]] / [[BlackBoxOptimization]] — the conceptual axes the chapter occupies; HPO is presented as black-box because of the no-gradient + noisy-observation constraints, multi-fidelity because the resource $r$ can be cheapened.
- [[SyneTune]] — Amazon's HPO library used in `rs-async` and `sh-async`; D2L's preferred distributed backend.
- [[RayTune]] / [[Optuna]] — alternative open-source HPO libraries with the same searcher/scheduler decomposition; cited in `hyperopt-api`.
- [[NeuralArchitectureSearch]] / [[AutoML]] — HPO's natural extensions; AutoML aims to automate the full ML pipeline; NAS replaces / augments human-designed architectures via HPO over architectural choices.
- [[d2l-optimization]] — the *learnable*-parameter optimization chapter; HPO chapter is its non-learnable-parameter complement (the two together cover *all* of the optimization landscape D2L addresses).
- [[d2l-multilayer-perceptrons]] / [[d2l-convolutional-modern]] — define the hyperparameters (learning rate / batch size / regularization / depth / width / activation) this chapter searches over.
- [[CrossValidation]] / [[ModelSelection]] — the chapter's exercises flag that using the test set as the validation set is the model-selection sin [[d2l-linear-classification]]'s §generalization-basics warns against; proper HPO requires train / validation / test splits.

## Contradictions

- None direct. *Mild tension* with [[NeuralArchitectureSearch]]'s framing in [[d2l-convolutional-modern]]: that chapter positions NAS as the *foil* for the design-space approach (criticizes NAS's compute cost); the HPO chapter positions NAS as a natural extension of HPO with the same compute-cost caveat. Both views coexist — NAS is expensive *because* HPO is expensive, and the design-space alternative is one (cheaper) response.
- Slight pedagogical tension with the [[d2l-linear-regression]] / [[d2l-multilayer-perceptrons]] practice of fixing hyperparameters without principled search — the HPO chapter is implicitly the chapter that *should have come earlier* in the curriculum. D2L places it after the modeling chapters because HPO is treated as an advanced topic; the chapter itself acknowledges this with the exercise asking the reader to revisit the [[FashionMNIST]] validation-set practice from earlier chapters.
