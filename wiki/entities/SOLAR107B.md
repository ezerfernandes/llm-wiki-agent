---
title: "SOLAR 10.7B"
type: entity
tags: [model, depthwise-scaling, model-upscaling]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# SOLAR 10.7B

A 10.7-billion-parameter LLM created by [[Kim2023SOLAR|Kim et al. (2023)]] using **[[DepthwiseScaling|depthwise scaling]]** from a single 32-layer 7B pre-trained model. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], the canonical worked example of [[ModelUpscaling|model upscaling]] via layer stacking.

## The recipe

1. Start with the original 32-layer 7B pre-trained model (a Mistral / Llama-family base).
2. Make a copy of the model.
3. **Sum 16 of the layers** (collapsing 32 of the duplicated layers down to 16) and **stack the rest**.
4. Result: 32 × 2 − 16 = **48 layers**, ~10.7B parameters.
5. Further train this upscaled model toward the target performance.

## Why it matters

- **Demonstrates upscaling at LLM scale** — earlier upscaling work was mostly at CNN scales.
- **Reuses pre-training compute** — the 10.7B model didn't need to be trained from scratch.
- **Open-source and reproducible** — released by Upstage AI.

## Strong empirical results

At release (late 2023), SOLAR 10.7B was competitive with much larger models on common benchmarks, validating that depthwise scaling produces models with quality commensurate with their parameter count rather than their starting parameter count.

## Limitations

- Required further finetuning after stacking (the merged layers weren't trained to work together).
- The recipe doesn't trivially scale further — you can't keep depthwise-scaling indefinitely without quality loss.

## Connections

- [[DepthwiseScaling]] / [[LayerStacking]] / [[ModelMerging]] / [[ModelUpscaling]] — the techniques used.
- [[Kim2023SOLAR]] — the paper.
- Upstage AI — the originating organization.
- [[ai-engineering-ch07-finetuning]] — wiki source.
