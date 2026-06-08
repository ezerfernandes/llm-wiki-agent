---
title: "Label Shift"
type: concept
tags: [distribution-shift, generalization, mlops]
sources: [d2l-linear-classification, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Label Shift

The form of [[DistributionShift|distribution shift]] in which the **label marginal** $P(y)$ changes between training and test time while the **class-conditional input distribution** $P(\mathbf x\mid y)$ stays fixed. The natural assumption when $y$ causes $\mathbf x$ — diagnosing diseases from symptoms is the canonical example: the prevalence of diseases may change over time, but each disease still produces the same symptom distribution.

## Why it's tractable in deep learning

Per [[d2l-linear-classification]]: label shift "involves manipulating objects that look like labels (often low-dimensional), as opposed to objects that look like inputs, which tend to be high-dimensional in deep learning." Importance weights live in $k$-dimensional simplex space (one per class), so estimation is far easier than in [[CovariateShift|covariate shift]].

## Correction by importance-weighted ERM

$$
\int l(f(\mathbf x), y)\, p(\mathbf x\mid y)\,p(y)\, d\mathbf x\,dy = \int l(f(\mathbf x), y)\, q(\mathbf x\mid y)\,q(y)\, \frac{p(y)}{q(y)}\, d\mathbf x\,dy
$$

so reweight training example $(\mathbf x_i, y_i)$ by $\beta_i = p(y_i)/q(y_i)$ and minimize weighted [[EmpiricalRiskMinimization|empirical risk]].

## Estimating the target label distribution

Trick from [[d2l-linear-classification]]: even though we cannot label the target data, we can estimate $p(\mathbf y)$ from **mean model outputs at test time** via the confusion matrix.

1. Compute the validation-set confusion matrix $\mathbf C \in \mathbb R^{k\times k}$, where $c_{ij}$ = fraction of validation predictions where true label was $j$ and the model predicted $i$.
2. At test time, average model predictions: $\mu(\hat{\mathbf y})_i$ = fraction of test predictions where model output class $i$.
3. Solve the linear system $\mathbf C\, p(\mathbf y) = \mu(\hat{\mathbf y})$; if the classifier is reasonably accurate, $\mathbf C$ is invertible and $p(\mathbf y) = \mathbf C^{-1}\mu(\hat{\mathbf y})$.
4. Compute $\beta_i = p(y_i)/q(y_i)$ from the estimated $p$ and the directly-observed $q$.

Assumptions: classifier is reasonably accurate on the source distribution; target data contains only categories seen in training; label-shift assumption itself holds (the strongest of the three).

## Degenerate co-occurrence with covariate shift

When labels are deterministic functions of inputs, both label-shift and [[CovariateShift|covariate-shift]] assumptions hold simultaneously. In such cases label-shift methods are still preferred because operating on low-dimensional label space is far more sample-efficient.

## Connections

- [[DistributionShift]] — parent taxonomy.
- [[CovariateShift]] / [[ConceptShift]] / [[ConceptDrift]] — sibling shift types.
- [[mlsysbook-ch04-data-engineering]] — Reddi's *Machine Learning Systems* Ch 4: label shift ($p(y)$ changes, $p(x\mid y)$ fixed) is detectable *without* ground truth by tracking model output distributions (e.g., seasonal disease prevalence, new product categories).
- [[EmpiricalRiskMinimization]] — what gets reweighted.
- [[Softmax]] / [[CrossEntropyLoss]] — what the underlying classifier is trained with.
- [[d2l-linear-classification]] — corpus anchor (Section *Label Shift Correction*).
