---
title: "Frankenmerging"
type: concept
tags: [model-merging, model-composition]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Frankenmerging

Community nickname for **[[LayerStacking|layer stacking]]** as a [[ModelMerging|model merging]] technique — taking layers from different models and stacking them into a single Frankenstein-style composite. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], also called *passthrough merging*.

Canonical instance: **[[Goliath120B]]** (alpindale, 2023) — 72 layers from each of two finetuned Llama-2-70B models stitched together into a 120B model. The community embrace of the term predates its formal study.

See [[LayerStacking]] for the full treatment.

## Connections

- [[LayerStacking]] — the formal name.
- [[ModelMerging]] — parent operation.
- [[Goliath120B]] — the early high-profile example.
- [[ai-engineering-ch07-finetuning]] — primary source.
