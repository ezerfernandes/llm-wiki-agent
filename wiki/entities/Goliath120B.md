---
title: "Goliath-120B"
type: entity
tags: [model, frankenmerge, llama-2]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Goliath-120B

A 120-billion-parameter model created in 2023 by community user **alpindale** by **[[Frankenmerging|frankenmerging]] two finetuned Llama-2-70B models** (Xwin and Euryale). Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "One early success of frankenmerging is Goliath-120B (alpindale, 2023), which was merged from two finetuned Llama 2-70B models, Xwin and Euryale. It took 72 out of 80 layers from each model and merged them together."

## The recipe

- Take Xwin (70B finetune of Llama 2) and Euryale (another 70B finetune).
- Take 72 of 80 layers from each (overlapping middle layers from both, plus all unique outer layers).
- [[LayerStacking|Stack]] them into a 120B model.
- (Optionally further finetune.)

## Why it's significant in Ch 7

- **Early proof point** that frankenmerging produces working models, not just gibberish.
- **Community-driven, not lab-driven** — a single hobbyist built a 120B-class model from two existing 70B models, using only model-merging tooling (no GPUs required for the merge itself).
- **Anticipated the model-merging boom** on Hugging Face's Open LLM Leaderboard, where merged models came to dominate.

## Limitations

- Quality wasn't competitive with frontier proprietary models at the time.
- Required substantial inference hardware (120B params).
- Subsequent merging techniques (TIES, DARE, SLERP) eventually produced higher-quality merges at smaller scales.

## Connections

- [[Frankenmerging]] / [[LayerStacking]] / [[ModelMerging]] — the techniques used.
- [[Llama]] — the base model family.
- [[ai-engineering-ch07-finetuning]] — wiki source.
