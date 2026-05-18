---
title: "Empirical Risk Minimization"
type: concept
tags: [foundational, learning-theory, optimization]
sources: [pml1-murphy, mml-book, d2l-linear-regression, d2l-linear-classification]
last_updated: 2026-05-16
---

# Empirical Risk Minimization (ERM)

The canonical recipe for supervised learning: pick parameters $\hat{\boldsymbol\theta}$ that minimize the **average loss on the training set**.

$$
\hat{\boldsymbol\theta} = \arg\min_{\boldsymbol\theta}\;\mathcal{L}(\boldsymbol\theta) = \arg\min_{\boldsymbol\theta}\;\frac{1}{N}\sum_{n=1}^{N}\ell\big(y_n,\,f(\mathbf{x}_n;\boldsymbol\theta)\big)
$$

[[pml1-murphy]] §1.2.1.4 introduces ERM as the operational definition of "training" or "model fitting." Different loss functions $\ell$ recover most of supervised learning:

| Loss $\ell$ | Recovers |
|---|---|
| Zero-one $\mathbb{I}(y\neq\hat y)$ | Misclassification rate (§1.2.1.4) |
| Quadratic $(y-\hat y)^2$ | Mean Squared Error / least squares (§1.2.2) |
| Negative log-likelihood $-\log p(y\|f(\mathbf{x};\boldsymbol\theta))$ | [[MaximumLikelihoodEstimation\|MLE]] (§1.2.1.6) |
| Cross-entropy | MLE for categorical outputs |
| $\ell_1$ residual | Robust regression (Ch 11) |

## The gap ERM doesn't close

ERM minimizes loss on the *training* sample. The actual quantity of interest is the **population risk** $\mathcal{L}(\boldsymbol\theta; p^*) = \mathbb{E}_{p^*(\mathbf{x},y)}[\ell(y, f(\mathbf{x};\boldsymbol\theta))]$. Their difference is the [[GeneralizationGap]]. A driver that gets the training loss to zero by memorization is *overfitting*; a model with the right [[InductiveBias]] generalizes (§1.2.3).

The standard mitigation is train/validation/test partition with model selection on the validation set, plus regularization (Ch 4, Ch 11) and Bayesian methods (Ch 4.5.2, Ch 5.2.2).

## Role in this wiki

- Underlies every supervised-learning method in [[pml1-murphy]] Parts II–IV.
- The RL-stage and pretraining-stage interventions in the Corpus II 2026 papers ([[2604.21590-agenticqwen]], [[2601.21343-self-improving-pretraining]], [[2605.02572-long-horizon-llm-training]]) are all ERM variants with carefully engineered loss functions / data distributions.
- [[2605.12966-agentic-ai-to-agi]]'s [[AverageTrap]] is *exactly* an ERM-pathology argument: weighted-average ERM across heterogeneous task manifolds pays a quadratic per-task-divergence penalty.

## Cross-reference: [[mml-book]] §8.2

[[mml-book]] reaches the same definition from the mathematical-foundations side. The four design choices in §8.2 — (i) hypothesis class of functions, (ii) loss function for training, (iii) regularization to construct predictors that perform well on unseen data, (iv) search procedure over the space of models — mirror Murphy's framing, and use ERM as the introductory route to [[SupportVectorMachine|SVMs]] in [[mml-book]] Ch 12. The two corpora agree: ERM is the operational definition of supervised learning before any probabilistic framing.

## Weighted ERM for distribution shift

[[d2l-linear-classification]] generalizes ERM to **weighted empirical risk minimization** as the principled correction for [[DistributionShift|distribution shift]]:

$$
\min_f \frac{1}{n}\sum_{i=1}^n \beta_i\, l(f(\mathbf x_i), y_i)
$$

where importance weights $\beta_i$ depend on the assumed shift type:

| Shift | Weight | Estimation |
|---|---|---|
| [[CovariateShift]] | $\beta_i = p(\mathbf x_i)/q(\mathbf x_i)$ | Logistic-regression domain classifier |
| [[LabelShift]] | $\beta_i = p(y_i)/q(y_i)$ | Confusion-matrix inversion |
| [[ConceptShift]] | (no principled $\beta$) | Continual fine-tuning |

The crucial covariate-shift caveat: the correction only works when $q(\mathbf x) > 0$ wherever $p(\mathbf x) > 0$ — otherwise importance weights are infinite and the correction breaks.

## Connections

- [[pml1-murphy]] — §1.2.1.4.
- [[mml-book]] — §8.2 canonical reference (alternative framing).
- [[d2l-linear-classification]] — extends ERM to **weighted ERM** under distribution shift.
- [[MaximumLikelihoodEstimation]] — ERM with NLL loss.
- [[GeneralizationGap]] — what ERM fails to control on its own.
- [[DistributionShift]] / [[CovariateShift]] / [[LabelShift]] / [[ConceptShift]] — the shift taxonomy that weighted ERM addresses.
- [[NoFreeLunchTheorem]] — why ERM needs an inductive bias to generalize.
- [[AverageTrap]] — heterogeneous-task ERM pathology.
- [[Abduction]] — model selection (over hypothesis classes) as an abductive step on top of ERM.
