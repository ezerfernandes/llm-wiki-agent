---
name: SaliencyMap
title: "Saliency Map"
type: concept
tags: [interpretability, explainability, computer-vision, attribution]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Saliency Map

A post-hoc [[Explainability|explainability]] technique that highlights which input regions (typically pixels) most influenced a model's prediction. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], saliency maps are presented as a **quality-assurance gate**, not "presentation polish": in the Mount Sinai hospital-shortcut case (Zech et al. 2018; Lapuschkin et al. 2019) they exposed that pneumonia detectors keyed on hospital-specific artifacts rather than disease pathology ([[ShortcutLearning|shortcut learning]]).

## Connections
- [[Explainability]] — the broader capability.
- [[SHAP]] / [[LIME]] — alternative attribution methods.
- [[ShortcutLearning]] — the failure saliency maps reveal.
- [[mlsysbook-ch15-responsible-engineering]] — source.
