---
title: "Code Llama"
type: entity
tags: [model, code-model, llama, meta]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Code Llama

A family of code-specialized LLMs created by [[meta|Meta]] (Rozière et al. 2024) by **finetuning Llama 2 with multiple specialized finetuning techniques**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], Code Llama is the chapter's worked example of:

- **[[LongContextFinetuning|Long-context finetuning]]** — extended max context from **4,096 → 16,384 tokens** to fit longer code files.
- **[[InfillingFinetuning|Infilling finetuning]]** — trained to fill in the middle of code given prefix + suffix context, supporting in-editor code-completion.
- **Stacked specialization** — multiple finetuning techniques applied in sequence on the same base.

Ch 7's Figure 7-1 (adapted from the Rozière et al. paper, CC BY 4.0) shows the multi-stage Code Llama training pipeline from the Llama 2 base.

## Why Ch 7 highlights Code Llama

- **Demonstrates that one base model can support multiple finetuning specializations** simultaneously.
- **Long-context finetuning works at scale** — a 4× context-length extension via finetuning, not pre-training from scratch.
- **Instruction finetuning + infilling finetuning + long-context finetuning** combine cleanly without one undoing the others.

## Variants

- **Code Llama** (base) — 7B / 13B / 34B / 70B.
- **Code Llama - Python** — Python-specialized variant.
- **Code Llama - Instruct** — instruction-tuned variant.

## Connections

- [[InfillingFinetuning]] / [[LongContextFinetuning]] / [[FineTuning]] — the techniques used.
- [[Llama]] — the base family.
- [[meta|Meta]] — the originating institution.
- [[ai-engineering-ch07-finetuning]] — wiki source.
