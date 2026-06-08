---
name: ShortcutLearning
title: "Shortcut Learning"
type: concept
tags: [responsible-ai, generalization, evaluation, robustness]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Shortcut Learning

When a model "exploits the easiest statistical signal available" — learning the data-generating process (artifacts, acquisition patterns, prevalence) rather than the true underlying phenomenon. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], the **hospital shortcut** war story (Zech et al. 2018; Lapuschkin et al. 2019) is canonical: Mount Sinai pneumonia models trained on one hospital's chest X-rays performed worse on NIH and Indiana University scans because hospital-specific artifacts created shortcuts that did not transfer — "the model has learned the data-generating process, not necessarily the disease process."

Defense: external validation across sites and [[Explainability|interpretability]] tools ([[SaliencyMap|saliency maps]]) as quality-assurance gates, not presentation polish.

## Connections
- [[Explainability]] / [[SaliencyMap]] — tools that expose shortcuts.
- [[DistributionShift]] — why shortcuts fail on new sites (population mismatch).
- [[AlgorithmicBias]] — shortcuts often encode demographic disparities.
- [[mlsysbook-ch15-responsible-engineering]] — source.
