---
title: "EL2N (Error L2-Norm)"
type: concept
tags: [ml-systems, data-selection, coreset, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# EL2N (Error L2-Norm)

A gradient/error-based [[CoresetSelection|coreset-scoring]] method (Paul et al. 2021) that scores each sample by the **L2 distance between the model's predicted probabilities and the one-hot label**, computed early in training ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). High EL2N = uncertain sample near the decision boundary = most informative for learning; low EL2N = easy, already-mastered sample.

Practicality rests on **proxy transferability**: scores from a small model trained for ~5 epochs (e.g. ResNet-18) guide selection for a much larger target (ResNet-50, 90 epochs). Most practitioners find EL2N-with-proxy the best balance of selection quality and cost; a 50% ImageNet coreset yields ~1.8× higher [[InformationComputeRatio|ICR]] for ~0.5 pp accuracy. Often paired with [[GraNd]] (gradient-norm scoring) and contrasted with [[ForgettingEvents|forgetting events]].

## Connections

- [[CoresetSelection]] — the parent technique; [[GraNd]] / [[ForgettingEvents]] — sibling scorers.
- [[InformationComputeRatio]] — the efficiency it improves.
- [[UncertaintySampling]] — shares the uncertainty-near-boundary intuition.
- [[mlsysbook-ch09-data-selection]] — source.
