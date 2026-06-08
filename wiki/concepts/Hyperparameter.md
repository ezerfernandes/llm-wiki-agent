---
title: "Hyperparameter"
type: concept
tags: [modeling, tuning, methodology]
sources: [mechanics-of-ml, mml-ch08-when-models-meet-data]
last_updated: 2026-06-04
---

# Hyperparameter

A model setting **chosen by the programmer rather than learned from the training data** — in contrast to [[TrainableParameters|parameters]], which are computed during fitting (e.g. a [[DecisionTrees|decision tree]]'s split structure). [[mechanics-of-ml|*The Mechanics of Machine Learning*]] gives the canonical examples: `k` in [[KNearestNeighbors|k-nearest neighbors]] and the number of trees in a [[RandomForests|Random Forest]].

Hyperparameters are tuned against a **[[TrainValTestSplit|validation set]]**, never the test set. The book recommends **sequential** tuning over exhaustive grid search for Random Forests: raise `n_estimators` until accuracy plateaus, then sweep `max_features` (~0.1–0.6) and `min_samples_leaf` (~1–15). On the bulldozer data this moved RMSLE 0.2469 → 0.2327.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.1.4 places hyperparameters as the high-level structural choices that control a model's flexibility — "the number of components to use or the class of probability distributions to consider" — and tuning them is exactly [[ModelSelection|model selection]] (§8.6), done for non-probabilistic models via [[NestedCrossValidation|nested cross-validation]] (§8.6.1). MML is explicit that the line is **pragmatic, not fundamental** (§8.1.4, Remark, p. 258): *"The distinction between parameters and hyperparameters is somewhat arbitrary, and is mostly driven by the distinction between what can be numerically optimized versus what needs to use search techniques. Another way to consider the distinction is to consider parameters as the explicit parameters of a probabilistic model, and to consider hyperparameters (higher-level parameters) as parameters that control the distribution of these explicit parameters."* The "chosen by the programmer, not learned" framing above is the search-required side of the first reading. In the §8.5.1 graphical-model view, a **hyperprior** literally places a distribution on the parameters of the first-layer priors — the second reading made graphical.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.1.4 parameters-vs-hyperparameters remark; §8.6 model selection.
- [[mechanics-of-ml]] — defines parameters vs hyperparameters; RF tuning recipe (Ch 9).
- [[TrainableParameters]] — the learned counterpart.
- [[TrainValTestSplit]] — hyperparameters are tuned on the validation set.
- [[RandomForests]] / [[KNearestNeighbors]] — sources of the book's example hyperparameters.
- [[CrossValidation]] — common protocol for hyperparameter selection.
