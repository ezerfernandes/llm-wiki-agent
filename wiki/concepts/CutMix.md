---
title: "CutMix"
type: concept
tags: [ml-method, data-augmentation, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# CutMix

An image [[DataAugmentation|augmentation]] technique that **pastes a patch from one image into another and mixes the labels proportionally to patch area** (30% of image A replaced by B → a 70/30 label split) ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). It fixes [[Cutout]]'s weakness — zeroed regions waste pixel information — by filling the cut region with real content from a second image. Improves ImageNet top-1 by ~1% over baseline and improves occlusion robustness, providing stronger regularization than either [[Cutout]] or [[MixUp]] alone at identical compute cost.

## Connections

- [[DataAugmentation]] — parent; [[Cutout]] / [[MixUp]] — the techniques it improves on.
- [[mlsysbook-ch09-data-selection]] — source.
