---
title: "Concatenation Merging"
type: concept
tags: [model-merging]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Concatenation Merging

A [[ModelMerging|model-merging]] primitive: **append parameters from constituent models end-to-end** rather than summing or stacking them. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], the merged component's parameter count equals the **sum** of the constituents' parameter counts.

Canonical example: merging two [[lora|LoRA]] adapters of ranks r₁ and r₂ via concatenation produces an adapter of rank **r₁ + r₂**.

## Why Ch 7 doesn't recommend it

> "Concatenation isn't recommended because it doesn't reduce the memory footprint compared to serving different models separately. Concatenation might give better performance, but the incremental performance might not be worth the number of extra parameters."

In short: concatenation **adds** parameters; the other merging primitives (summing, layer stacking) maintain or reduce parameter counts. The whole point of merging is usually to *consolidate* models — concatenation doesn't consolidate.

Ch 7's [[ChipHuyen|Huyen]] notes she "debated for a long time whether to include the concatenation technique in this book, and decided to include it for completeness."

## When concatenation might be the right choice

- When you specifically want to **preserve all constituent behaviors** without trading off one against another.
- When parameter count isn't a constraint and you want strictly additive composition.
- When the constituents truly contain disjoint information (rare in practice for finetunes of the same base).

## Connections

- [[ModelMerging]] — parent operation.
- [[lora|LoRA]] — the most common context for concatenation (combining multiple adapters).
- [[LinearCombinationMerging]] / [[LayerStacking]] — the recommended alternatives.
- [[ai-engineering-ch07-finetuning]] — primary source.
