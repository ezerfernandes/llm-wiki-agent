---
title: "Model Upscaling"
type: concept
tags: [model-merging, model-composition]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Model Upscaling

The study of **how to create larger models using fewer resources** — usually by composing or stacking layers from an existing pre-trained model rather than training a bigger model from scratch. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Sometimes, you might want a bigger model than what you already have, presumably because bigger models give better performance. For example, your team might have originally trained a model to fit on your 40 GB GPU. However, you obtained a new machine with 80 GB, which allows you to serve a bigger model. Instead of training a new model from scratch, you can use layer stacking to create a larger model from the existing model."

## Common recipes

- **[[DepthwiseScaling|Depthwise scaling]]** — duplicate + selectively sum layers to make a deeper model. Used to build [[SOLAR107B|SOLAR 10.7B]] from a 7B.
- **[[SparseUpcycling|Sparse upcycling]]** — duplicate layers + add a router → produce a [[MixtureOfExperts|MoE]] from a dense checkpoint.
- **Width-wise scaling** — less common in 2024; duplicate channels per layer rather than layers themselves.
- **[[ModelMerging|Merging multiple finetunes]]** of the same base — produces a same-size but more-capable model, technically not "upscaling" by parameter count but achieves similar quality goals at lower cost.

## When upscaling beats training from scratch

- You already have a strong pre-trained smaller model.
- Pre-training compute is the bottleneck, not finetuning compute.
- You want to reuse the dense base's learned features as a head start.
- You don't need a from-scratch architecture (upscaling can't fundamentally change the architecture).

## When it doesn't

- You want a different architecture, not just more parameters.
- Your base model's training data is mismatched to the new use case (upscaling preserves the data lineage).
- The new model size needs different scaling-law-derived hyperparameters that a naively-upscaled model won't follow.

## Connections

- [[ModelMerging]] / [[LayerStacking]] — the operational categories upscaling lives inside.
- [[DepthwiseScaling]] / [[SparseUpcycling]] — the two main recipes.
- [[SOLAR107B]] — the canonical depthwise-scaling product.
- [[MixtureOfExperts]] — the natural output of sparse upcycling.
- [[ScalingLaws]] — the theory that determines how much you can usefully upscale.
- [[ai-engineering-ch07-finetuning]] — primary source.
