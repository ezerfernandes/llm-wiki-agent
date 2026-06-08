---
title: "Model Selection"
type: concept
tags: [learning-theory, methodology, foundational, ai-engineering]
sources: [mml-book, mml-ch08-when-models-meet-data, d2l-linear-regression, ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2026-06-04
---

# Model Selection

The problem of choosing among competing model classes / hyperparameter configurations ([[mml-book]] §8.6).

## What it's *not*

Model selection is **not** parameter estimation. Parameter estimation (MLE / MAP / Bayesian) optimizes parameters *within* a chosen model class. Model selection picks the *class itself* — polynomial degree, network depth, number of GMM components, regularization strength, kernel type, etc.

## The standard recipes

- **Held-out validation set**: fit each candidate on the training set, score on the validation set, pick the best. Then re-fit the winner on training + validation, evaluate on the (untouched) test set.
- **$k$-fold cross-validation** ([[mml-book]] §8.2.4): partition the training data into $k$ folds; train on $k-1$ folds, validate on the held-out fold; average. Reduces variance vs single-split validation.
- **Nested cross-validation** (§8.6.1): outer loop estimates generalization error; inner loop selects hyperparameters. Critical when reporting performance on a small dataset — single-loop CV that's *also* the model-selection criterion overfits to the validation folds.
- **Marginal likelihood / evidence** $p(\mathcal{D})$: the principled Bayesian alternative — integrate over parameters and compare model classes by $p(\mathcal{D}\mid\mathcal{M})$. Used in [[BayesianLinearRegression]] for polynomial-degree selection.
- **Information criteria**: AIC, BIC, MDL — approximations to marginal likelihood that penalize parameter count.

## Why model selection is *abduction*, not induction

[[mml-book]] §8.2 frames the whole learning procedure as [[Abduction|abduction]] — inference to the best explanation. Within a model class, parameter estimation is inductive. *Across* model classes, the choice itself is abductive — the modeler is picking the explanation framework that best accounts for the data while respecting Occam's razor.

## Hyperparameter vs parameter

[[mml-book]] §8.1.4 (p. 258): "*The distinction between parameters and hyperparameters is somewhat arbitrary, and is mostly driven by the distinction between what can be numerically optimized versus what needs to use search techniques.*" The pragmatic test: gradient methods optimize parameters; grid search / random search / Bayesian optimization optimize hyperparameters.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.6 treats model selection as choosing the high-level structural decisions that control flexibility (polynomial degree, mixture-component count, net architecture, SVM kernel, PCA latent dim, learning-rate schedule — §8.6.4). It develops three routes:

- **[[NestedCrossValidation|Nested cross-validation]]** (§8.6.1) — the non-probabilistic route; inner loop selects, outer loop estimates generalization (Fig. 8.13, Eq. 8.39), plus higher-order statistics like the standard error $\sigma/\sqrt{K}$.
- **[[BayesianModelSelection|Bayesian model selection]]** (§8.6.2) — frame it as *hierarchical inference*. For a finite model set $M=\{M_1,\dots,M_K\}$, place a prior $p(M)$; the generative process is $M_k\sim p(M)$, $\boldsymbol\theta_k\sim p(\boldsymbol\theta\,|\,M_k)$, $\mathcal{D}\sim p(\mathcal{D}\,|\,\boldsymbol\theta_k)$ (Eqs. 8.40–8.42; Fig. 8.15). The **model posterior** $p(M_k\,|\,\mathcal{D})\propto p(M_k)\,p(\mathcal{D}\,|\,M_k)$ (Eq. 8.43) *no longer depends on the parameters* — they are integrated out into the **[[MarginalLikelihood|model evidence / marginal likelihood]]** $p(\mathcal{D}\,|\,M_k)=\int p(\mathcal{D}\,|\,\boldsymbol\theta_k)p(\boldsymbol\theta_k\,|\,M_k)\,d\boldsymbol\theta_k$ (Eq. 8.44). Under a uniform model prior, the MAP model $M^*=\arg\max_{M_k}p(M_k\,|\,\mathcal{D})$ (Eq. 8.45) is just the maximum-evidence model. The marginal likelihood **automatically embodies [[OccamsRazor|Occam's razor]]** (no held-out set required, not prone to overfitting) and underlies the **[[BayesFactor|Bayes factor]]** (§8.6.3) for pairwise comparison.
- **Information criteria** (§8.6.4) — for MLE-focused selection: **[[AkaikeInformationCriterion|AIC]]** $\log p(\mathbf{x}\,|\,\boldsymbol\theta)-M$ (Eq. 8.48) and **[[BayesianInformationCriterion|BIC]]** $\approx\log p(\mathbf{x}\,|\,\boldsymbol\theta)-\frac12 M\log N$ (Eq. 8.49), the latter penalizing complexity more heavily. The automatic Occam's razor penalizes *function* complexity, not literally parameter count (Rasmussen & Ghahramani 2001).

## Connection to Corpus II / V

- **[[madewithml-mlops-tuning]]** is the applied counterpart: [[RayTune]] + [[HyperOpt]] + [[ASHA]] for hyperparameter search, with [[NestedCrossValidation]] mentioned as the right outer protocol.
- **[[2605.08083-autotts]]** can be read as *automated model selection* over a controller-program space — the Explorer searches the space of TTS controllers, validating each on an offline replay environment.

## Connections

- [[mml-book]] — §8.6 canonical reference.
- [[CrossValidation]] — existing wiki concept.
- [[HyperparameterTuning]] — existing wiki concept.
- [[Abduction]] — philosophical framing.
- [[NoFreeLunchTheorem]] — why model selection requires a prior over model classes.
- [[Overfitting]] — what model selection guards against.
- [[BayesianLinearRegression]] — marginal-likelihood route to model selection.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Chip Huyen's *AI Engineering* repurposes "model selection" for the **foundation-model engineering** setting — where the question is not "what polynomial degree?" but "what foundation model for my application?" The classical ML-theory framing on this page is the parent concept; the AI-engineering specialization adds three structural ideas:

1. **[[ModelSelectionWorkflow|Four-step workflow]]** — filter on [[HardModelAttribute|hard attributes]] → narrow with [[Leaderboard|leaderboards]] → run private experiments via [[EvaluationPipeline|your evaluation pipeline]] → monitor in production. Iterative.
2. **[[HardModelAttribute|Hard]] vs [[SoftModelAttribute|soft]] attributes** — license, training data, model size, your privacy policy → hard (filter); accuracy, toxicity, factual consistency → soft (optimize within filter).
3. **[[ModelBuildVsBuy|Build-vs-buy]] as the first filter** — seven axes: data privacy, data lineage, performance, functionality, cost, control, on-device. This single decision can cut your candidate pool by an order of magnitude.

> "At the end of the day, you don't really care about which model is the best. You care about which model is the best for your applications."

Huyen also distinguishes **per-technique re-application**: model selection runs many times during development, with different priorities depending on whether you're prompt-engineering (start with the strongest model overall) vs finetuning (start small, grow within hardware limits).

The classical-ML and AI-engineering treatments of model selection share the *abductive* structure — both are inference-to-the-best-explanation given evidence. The AI-engineering treatment adds [[ParetoOptimization|Pareto optimization]] across multiple cost/quality axes that classical model selection often collapses into a single validation score.
