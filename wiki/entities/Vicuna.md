---
title: "Vicuna"
type: entity
tags: [model, llm, llama-finetune]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Vicuna

A series of open-source LLMs released in 2023 by LMSYS, the team behind the [[ChatbotArena|Chatbot Arena]]. **Finetuned from [[Llama]]** on ShareGPT-derived conversations. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], cited as one of the comparator models in the [[QLoRA]] / [[Guanaco]] Elo rankings:

| Model | Size | May 2023 GPT-4-judged Elo |
|---|---|---|
| Vicuna 13B | 26 GB | 974 ± 1 |
| Guanaco 13B | 10 GB | 916 ± 1 |
| Guanaco 65B | 41 GB | 1022 ± 1 |

Notable that Vicuna 13B beats Guanaco 13B at the same scale (Vicuna's full-precision FT vs Guanaco's 4-bit QLoRA), but Guanaco 65B dominates by going bigger at lower precision — the QLoRA value proposition in numbers.

## Beyond Ch 7

Vicuna also appears across the wiki in the medical-LLM context — e.g., [[2408.08849-ecg-chat|ECG-Chat]] uses Vicuna-13B as the base for ECG report generation under a constrained 8×V100 32GB budget. The Llama-2-based Vicuna lineage has been broadly adopted as a finetune-friendly base for specialized models.

## Connections

- [[Llama]] — the base family.
- [[Guanaco]] / [[QLoRA]] — the comparator family in Ch 7's tables.
- [[ChatbotArena]] — Vicuna's evaluation context.
- [[2408.08849-ecg-chat]] — medical application using Vicuna-13B.
- [[ai-engineering-ch07-finetuning]] — wiki source.
