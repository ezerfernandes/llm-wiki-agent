---
title: "Semi-Supervised Learning"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, labeling, ml-method]
sources: [mlsysbook-ch04-data-engineering, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Semi-Supervised Learning

A labeling-efficiency strategy that uses structural assumptions to **propagate labels from a small labeled set to a larger unlabeled corpus**, reducing the human annotation burden (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). It sits between traditional (fully manual) supervision and [[WeakSupervision|weak supervision]] in the [[AIAssistedLabeling|AI-assisted labeling]] hierarchy.

In practice it underlies **pre-annotation** workflows — an AI model trained on a small labeled seed generates preliminary labels that humans verify and correct, cutting manual effort 50–80% for many computer-vision tasks. It addresses the label-scarcity bottleneck common in domains like medical imaging where large unlabeled repositories exist but expert annotation is the constraint.

## Connections

- [[AIAssistedLabeling]] — the parent decision hierarchy.
- [[WeakSupervision]] / [[ActiveLearning]] / [[TransferLearning]] — sibling label-efficiency strategies.
- [[DataLabeling]] — the stage it accelerates.
- [[DynamicDataSelection]] — [[mlsysbook-ch09-data-selection|Ch 9]] frames SSL as a dynamic-selection technique reaching 80–95% of supervised accuracy with 10–20% of labels via [[PseudoLabeling]], [[ConsistencyRegularization]], label propagation, and [[FixMatch]] (200× label efficiency on CIFAR-10).
- [[mlsysbook-ch04-data-engineering]] / [[mlsysbook-ch09-data-selection]] — sources.
