---
title: "Nested Cross-Validation"
type: concept
tags: [resampling, model-selection, evaluation]
sources: [mml-book, mml-ch08-when-models-meet-data]
last_updated: 2026-06-04
---

# Nested Cross-Validation

Two **nested levels of $K$-fold [[CrossValidation|cross-validation]]**: the **inner loop selects** the model/hyperparameters, the **outer loop estimates** the generalization error of that selection ([[mml-book]] §8.6.1, Fig. 8.13). It is the honest [[ModelSelection|model-selection]] protocol when reporting performance on small data — a single CV loop that is *also* the model-selection criterion overfits to the validation folds.

## The two levels

- **Inner level** — estimates the performance of a particular model/hyperparameter choice on an internal **validation set**. The inner loop estimates the expected validation error $\mathbb{E}_{\mathcal{V}}[\mathbf{R}(\mathcal{V}\,|\,M)]\approx\frac{1}{K}\sum_{k=1}^K\mathbf{R}(\mathcal{V}^{(k)}\,|\,M)$ ([[mml-book]] §8.6.1, Eq. 8.39), where $\mathbf{R}(\mathcal{V}\,|\,M)$ is the empirical risk (e.g. RMSE) on the validation set for model $M$.
- **Outer level** — estimates generalization performance for the **best** model chosen by the inner loop, on a held-out **test set**.

To keep the two straight: the set used to estimate final generalization is the **test set**; the set used to choose the best model is the **validation set**.

## What it buys you

Beyond the mean generalization estimate, CV yields **higher-order statistics** — e.g. the **standard error** $\sigma/\sqrt{K}$ ($K$ experiments; $\sigma$ = std-dev of the per-experiment risk), an estimate of how uncertain the mean estimate is ([[mml-book]] §8.6.1, margin, p. 284). Once the model is chosen, evaluate the final performance on the test set.

## Cost

Nesting multiplies the training runs (inner $\times$ outer folds $\times$ candidate models/hyperparameters), which is exactly the exponential blow-up §8.2.4 warns about when multiple complexity/regularization hyperparameters must be searched. Like plain CV it is **embarrassingly parallel**.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.6.1 canonical reference (Fig. 8.13, Eq. 8.39).
- [[mml-book]] — §8.6.1.
- [[CrossValidation]] — the single-loop building block.
- [[ModelSelection]] — what nested CV serves; the inner loop *is* model selection.
- [[Hyperparameter]] — what the inner loop tunes.
- [[Generalization]] — what the outer loop estimates.
- [[Overfitting]] — what single-loop CV-as-selection-criterion silently does.
