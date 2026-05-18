---
title: "Distribution Shift"
type: concept
tags: [generalization, deployment, mlops, foundational]
sources: [d2l-linear-classification, madewithml-monitoring]
last_updated: 2026-05-16
---

# Distribution Shift

The phenomenon where training distribution $p_S(\mathbf x, y)$ differs from test/deployment distribution $p_T(\mathbf x, y)$. The single largest cause of ML deployment failures. Without restrictive assumptions on how $p_S$ and $p_T$ relate, learning a robust classifier is **impossible** ([[d2l-linear-classification]]).

## Taxonomy

[[d2l-linear-classification]] decomposes by which conditional is invariant:

| Shift type | What changes | What is fixed | Natural when |
|---|---|---|---|
| [[CovariateShift]] | $P(\mathbf x)$ | $P(y\mid\mathbf x)$ | $\mathbf x$ causes $y$ (image → species) |
| [[LabelShift]] | $P(y)$ | $P(\mathbf x\mid y)$ | $y$ causes $\mathbf x$ (disease → symptom) |
| [[ConceptShift]] | $P(y\mid\mathbf x)$ | (varies) | Labels are conventions (fashion, geography) |

A fourth category, **nonstationary distributions**, denotes slow continuous drift unaccounted for in retraining cadence — common but often mistaken for one of the above.

## Correction strategy

Both covariate and label shift admit **importance-weighted [[EmpiricalRiskMinimization|empirical risk minimization]]**: train with reweighted loss $\frac{1}{n}\sum_i \beta_i\, l(f(\mathbf x_i), y_i)$ where

- **Covariate shift**: $\beta_i = p(\mathbf x_i)/q(\mathbf x_i)$, estimated by training a [[LogisticRegression|logistic-regression]] domain classifier to distinguish source from target inputs.
- **Label shift**: $\beta_i = p(y_i)/q(y_i)$, estimated by inverting the validation-set confusion matrix: $\mathbf C\, p(\mathbf y) = \mu(\hat{\mathbf y})$.

Concept shift is hard to correct principally; usual remedy is continual fine-tuning on small fresh batches.

## Detection in production

The Made With ML monitoring stack ([[AlibiDetect]] / [[EvidentlyAI]] / [[TorchDrift]] / [[WhyLogs]]) operationalizes distribution-shift detection with KS, MMD, and chi-squared tests on input statistics, output distributions, or learned embeddings. Together with D2L's theory, the wiki now spans both the **principled-correction** and **operational-detection** sides of distribution shift.

## Connections

- [[CovariateShift]] / [[LabelShift]] / [[ConceptShift]] — the three principal shift types.
- [[EmpiricalRiskMinimization]] — generalized here to **weighted ERM** for shift correction.
- [[LogisticRegression]] — the binary classifier used to estimate covariate-shift importance weights.
- [[Generalization]] / [[GeneralizationGap]] — IID is the implicit no-shift assumption; this is what fails.
- [[AlibiDetect]] / [[EvidentlyAI]] / [[TorchDrift]] / [[WhyLogs]] — production drift-detection libraries.
- [[d2l-linear-classification]] / [[madewithml-monitoring]] — corpus anchors (theory + practice).
