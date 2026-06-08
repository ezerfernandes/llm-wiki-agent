---
title: "Curriculum Learning"
type: concept
tags: [ml-method, data-selection, training, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Curriculum Learning

A [[DynamicDataSelection|dynamic-selection]] technique (Bengio et al. 2009) that structures the **order** in which data is presented — starting with easy examples and gradually introducing harder ones — instead of random shuffling ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). It acts as a continuation method for nonconvex optimization: easy examples give clean, consistent gradients that smooth the early loss landscape, while hard examples introduced too early produce noisy gradients that slow convergence or cause memorization.

Two components: a **difficulty scorer** (loss-based, teacher-confidence, domain heuristics, or self-paced) and a **pacing function** (e.g. linear warmup). From a systems view, [[InformationComputeRatio|ICR]] varies within a run — easy samples have high ICR early and near-zero ICR later — so phasing them out improves efficiency. Gains are **inversely proportional to data quality** and manifest as *faster convergence*, not higher final accuracy: CIFAR-10 ~23% fewer epochs, but ImageNet only ~11% (less redundant). Variants: anti-curriculum (hard first) and self-paced (model adjusts difficulty by its own loss).

## Connections

- [[DynamicDataSelection]] — parent stage; [[DataSelection]] — discipline.
- [[ActiveLearning]] — sibling dynamic technique (assumes unlabeled pool, not order).
- [[InformationComputeRatio]] — explains why easy-first ordering raises total efficiency.
- [[mlsysbook-ch09-data-selection]] — source.
