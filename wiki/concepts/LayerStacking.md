---
title: "Layer Stacking"
type: concept
tags: [model-merging, model-composition, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Layer Stacking

A [[ModelMerging|model-merging]] primitive where you **take layers from one or more models and stack them on top of each other**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], also known as **passthrough** or **frankenmerging** in the community. Unlike summing-based merging, layer stacking can produce **novel architectures and parameter counts** by composing pieces of different models.

## What you can build (Ch 7)

- **Frankenmerges** — take layer i from model A, layer j from model B, etc. Canonical example: **[[Goliath120B]]** (alpindale, 2023) — built by stacking 72 of 80 layers from each of two finetuned Llama-2-70B models (Xwin and Euryale) into a single 120B model.
- **[[MixtureOfExperts|MoE models]] via [[SparseUpcycling|sparse upcycling]]** ([[Komatsuzaki2022SparseUpcycling|Komatsuzaki et al., 2022]]) — replicate certain layers N times and add a router; you've created an MoE from a dense checkpoint. Ch 7's most theoretically interesting layer-stacking application.
- **[[ModelUpscaling|Model upscaling]] via [[DepthwiseScaling|depthwise scaling]]** ([[Kim2023SOLAR|Kim et al., 2023]]) — used to build [[SOLAR107B|SOLAR 10.7B]] from a 32-layer 7B base. The recipe: copy the base, sum some layers, stack the rest → 48-layer 10.7B model.
- **[[MixtureOfAgents]]** ([[TogetherAI]], 2024) — six weaker open-source models combined via layer stacking + routing → comparable to [[gpt54|GPT-4o]] on some benchmarks.

## When further finetuning is needed

> "Unlike the merging by summing approach, the merged models resulting from layer stacking typically require further finetuning to achieve good performance." — Ch 7

This is because the stacked layers were never trained to work together. The depthwise-scaling and sparse-upcycling recipes both end with a finetuning step on the stacked model.

## Depthwise scaling worked example ([[SOLAR107B|SOLAR 10.7B]])

1. Copy the original 32-layer 7B pre-trained model.
2. Choose which layers to *sum* (merge two-into-one) vs. which to *stack* (keep both copies). For SOLAR: 16 layers summed → final 32 × 2 − 16 = **48 layers**.
3. Further train this upscaled 48-layer model toward the target performance.

Result: a 10.7B model that didn't require training from scratch.

## Connections

- [[ModelMerging]] — parent operation.
- [[Goliath120B]] — frankenmerge example.
- [[SOLAR107B]] — depthwise-scaling example.
- [[SparseUpcycling]] / [[MixtureOfExperts]] — MoE construction via layer stacking.
- [[ModelUpscaling]] / [[DepthwiseScaling]] — broader use case.
- [[MixtureOfAgents]] — multi-model frankenmerge.
- [[Frankenmerging]] — alternate name for layer stacking.
- [[Komatsuzaki2022SparseUpcycling]] / [[Kim2023SOLAR]] — citations.
- [[ai-engineering-ch07-finetuning]] — primary source.
