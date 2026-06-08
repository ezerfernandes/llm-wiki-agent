---
title: "Overfitting"
type: concept
tags: [theory, training]
sources: [madewithml-training, d2l-linear-regression, d2l-multilayer-perceptrons, mml-ch08-when-models-meet-data, mml-ch09-linear-regression]
last_updated: 2026-06-04
---

# Overfitting

When a model fits training noise rather than signal, harming generalization. Symptoms: training error low (often near zero) but validation error significantly higher — a large [[GeneralizationGap]]. The diagnostic mirror image of [[Underfitting]].

[[d2l-linear-regression]] §3.6 frames the canonical demo: a polynomial of degree $d \geq n$ achieves zero training error on *any* $n$-example dataset, including pure noise. Memorization, not learning.

## Modern caveat from [[d2l-linear-regression]]

"Note that overfitting is not always a bad thing. In deep learning especially, the best predictive models often perform far better on training data than on holdout data. Ultimately, we usually care about driving the generalization error lower, and only care about the gap insofar as it becomes an obstacle to that end." This foreshadows the **double-descent** phenomenon in overparameterized regimes (LLMs, modern DNNs).

## Deep-learning regime ([[d2l-multilayer-perceptrons]])

Modern over-parametrized networks can perfectly fit **arbitrary labels** (including random ones), yet they still generalize on real data. The classical "complexity → overfitting" mental model breaks down: increasing capacity (depth, width, training epochs) can actually *reduce* test error past the interpolation threshold — the [[DoubleDescent|double-descent]] curve in the [[InterpolationRegime|interpolation regime]]. [[Dropout]], [[EarlyStopping|early stopping]], and [[WeightDecay|weight decay]] are still useful, but the theoretical rationale shifts from "constraining capacity" to "encoding compatible inductive biases."

## Mitigations

- **More data** — most reliable; reduces overfitting risk monotonically.
- **[[Regularization]]** — [[WeightDecay|$\ell_2$ weight decay]], [[Lasso|$\ell_1$]], [[Dropout]], early stopping.
- **Reduce capacity** — fewer parameters, smaller polynomial degree, smaller network.
- **Proper [[TrainValTestSplit]]** + [[ModelSelection]] on validation, not test.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] gives two complementary definitions. **§8.2.3 (risk view):** for a fixed predictor, overfitting occurs when the training [[EmpiricalRisk|empirical risk]] $\mathbf{R}_{\text{emp}}(f,\mathbf{X}_{\text{train}},\mathbf{y}_{\text{train}})$ *under-estimates* the [[ExpectedRisk|expected risk]] $\mathbf{R}_{\text{true}}(f)$ — "having very small average loss on the training set but large average loss on the test set," tending to occur "when we have little data and a complex [[HypothesisClass|hypothesis class]]" (Mitchell 1997). The diagnostic: since we estimate $\mathbf{R}_{\text{true}}$ by the test risk, a test risk *much larger* than the training risk indicates overfitting (margin, via [[CrossValidation|cross-validation]], §8.2.4). **§8.3.3 ([[ModelFitting|model-fitting]] view):** overfitting is when the model class $M_{\boldsymbol\theta}$ is *too rich* (e.g. 7th-order polynomials for linear data) — overfit models "use all [their] modeling power to reduce the training error" and on noisy data "find some useful signal in the noise itself," causing enormous problems away from the training data (Fig. 8.8a; overfit models typically have *many* parameters). The symmetric failure is [[Underfitting|underfitting]] (too-poor class, few parameters, Fig. 8.8b). Mitigations: [[Regularization|regularization]] (§8.2.3), priors / [[MAPEstimation|MAP]] (§8.3.2). MLE in particular overfits "in the 'small' data regime" (§8.3.2 Remark).

## From [[mml-ch09-linear-regression|MML Ch 9]] (the polynomial-degree case study)

[[mml-ch09-linear-regression|MML Ch 9]] §9.2.2 is the canonical worked demonstration. Fitting [[PolynomialRegression|polynomials]] of increasing degree $M$ to $N=10$ points by [[MaximumLikelihoodEstimation|MLE]] (Fig. 9.5): low $M$ underfits; $M=N-1=9$ **interpolates every training point** but oscillates wildly between them; the extreme $M=N-1$ case is degenerate (otherwise the linear system would be underdetermined with infinitely many MLEs). Quantitatively (Fig. 9.6, via [[RMSE]] on a 200-point test set): **training error never increases with $M$**, but **test error is minimized at $M=4$** and explodes from $M=6$ onward — the U-shaped generalization curve. The diagnosis: MLE makes parameter magnitudes blow up under overfitting (Bishop 2006), motivating [[MAPEstimation|MAP]] / a prior (§9.2.3) and [[Regularization|regularization]] (§9.2.4) as mitigations. [[BayesianLinearRegression|Bayesian linear regression]] (§9.3) goes further, exposing the "huge" predictive uncertainty of overfit high-degree models rather than committing to a single bad fit.

## Connections

- [[mml-ch09-linear-regression]] — §9.2.2 polynomial-degree overfitting case study (Figs. 9.5–9.6, best $M=4$).
- [[mml-ch08-when-models-meet-data]] — §8.2.3 (risk view) + §8.3.3 (model-fitting view); the empirical-vs-expected-risk diagnostic.

- [[d2l-linear-regression]] — §3.6 canonical reference; polynomial-fitting demo.
- [[d2l-multilayer-perceptrons]] — modern deep-learning regime.
- [[DoubleDescent]] / [[InterpolationRegime]] — over-parametrized phenomena.
- [[Dropout]] / [[EarlyStopping]] — deep-learning regularizers.
- [[Underfitting]] — symmetric failure mode.
- [[GeneralizationGap]] — the gap-vs-validation diagnostic.
- [[Regularization]] / [[WeightDecay]] — primary mitigations.
- [[CrossValidation]] — what model selection should use.
