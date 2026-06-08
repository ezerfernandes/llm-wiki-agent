---
title: "MixUp"
type: concept
tags: [ml-method, data-augmentation, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# MixUp

An image [[DataAugmentation|augmentation]] technique (Zhang et al. 2018) that **blends two images and their labels linearly**, creating entirely synthetic training examples that regularize learning ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). One of the advanced augmentations alongside [[Cutout]] (random rectangular masks) and [[CutMix]] (patch-pasting between images). As a heavy CPU augmentation it can become the pipeline bottleneck, motivating [[DataEchoing|data echoing]].

## Connections

- [[DataAugmentation]] — parent; [[Cutout]] / [[CutMix]] — sibling advanced augmentations.
- [[DataEchoing]] — addresses the CPU cost of heavy augmentations like MixUp.
- [[mlsysbook-ch09-data-selection]] — source.
