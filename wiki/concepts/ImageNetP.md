---
title: "ImageNet-P"
type: concept
tags: [benchmark, robustness, computer-vision]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# ImageNet-P

**Hendrycks & Dietterich (2019) robustness benchmark: ImageNet sequences with gradual perturbations to test prediction stability.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], the sibling benchmark to [[ImageNetC|ImageNet-C]].

While ImageNet-C tests **classification correctness** under corruption, ImageNet-P tests **prediction stability** as perturbations change smoothly — a model whose top-1 prediction flips with small input changes is unstable, even if it's still "correct" most of the time.

## Connections

- [[ImageNetC]] — sibling benchmark.
- [[Perturbation]] — the construction technique.
- [[ImageNet]] — source dataset.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
