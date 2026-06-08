---
title: "Pseudo-labeling"
type: concept
tags: [ml-method, semi-supervised, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Pseudo-labeling

A [[SemiSupervisedLearning|semi-supervised]] technique: train on labeled data, use the model's own **high-confidence predictions on unlabeled data as ground-truth labels**, then retrain on both ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Its effectiveness depends on a virtuous cycle (accurate predictions on easy examples expand the training set, improving the model). The failure mode is symmetric — incorrect pseudo-labels reinforce errors through **confirmation bias** — making the **confidence threshold** a critical systems parameter: too low compounds label noise, too high wastes useful data. Combined with [[ConsistencyRegularization|consistency regularization]] in methods like [[FixMatch]].

## Connections

- [[SemiSupervisedLearning]] — parent paradigm; [[ConsistencyRegularization]] / [[FixMatch]] — companions.
- [[ActiveLearning]] — alternative that asks humans rather than self-labels.
- [[mlsysbook-ch09-data-selection]] — source.
