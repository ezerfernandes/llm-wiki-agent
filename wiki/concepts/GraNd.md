---
title: "GraNd (Gradient Normed)"
type: concept
tags: [ml-systems, data-selection, coreset, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# GraNd (Gradient Normed)

A gradient-based [[CoresetSelection|coreset-scoring]] method (Paul et al. 2021) that scores each sample by its **gradient norm early in training** ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). High-norm samples lie near the decision boundary and contribute the most learning signal; low-norm samples are redundant. Cost is $\mathcal{O}(\text{epochs}\times D)$ and, like [[EL2N]], it relies on **proxy transferability** (small-model scores predict large-model importance). On CIFAR-10, GraNd/EL2N selection matches full-dataset accuracy with ~50% of samples.

## Connections

- [[CoresetSelection]] — parent; [[EL2N]] / [[ForgettingEvents]] — sibling scorers.
- [[InformationComputeRatio]] — gradient-based selection raises ICR ~1.8× over random.
- [[mlsysbook-ch09-data-selection]] — source.
