---
title: "BloombergGPT"
type: entity
tags: [model, llm, domain-specific, finance, bloomberg]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# BloombergGPT

A **50-billion-parameter domain-specific LLM** trained from scratch by Bloomberg in early 2023, designed for financial tasks and to be hosted in-house for sensitive-data use cases. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], cited by Wu et al. (2023):

- **Parameter count**: 50B.
- **Training compute**: 1.3 million A100 GPU hours.
- **Estimated cost**: $1.3M–$2.6M for compute alone (excluding data costs).
- **Released**: March 2023.

## Ch 7's cautionary framing

BloombergGPT is the chapter's headline example of a **domain-specific model getting outperformed by a stronger general-purpose model released the same month**.

In the same month BloombergGPT was published, [[openai|OpenAI]] released **GPT-4-0314**. Per Li et al. (2023):

| Model | FiQA sentiment (weighted F1) | ConvFinQA (accuracy) |
|---|---|---|
| GPT-4-0314 (zero-shot) | **87.15** | **76.48** |
| BloombergGPT | 75.07 | 43.41 |

GPT-4 won on both financial benchmarks **without any finance-specific training**. By 2024, mid-size models comparable to GPT-4 (Claude 3.5 Sonnet ~70B, Llama 3-70B-Instruct, Qwen2-72B-Instruct) were also available, and the latter two are open-weight and self-hostable.

## The lesson Huyen draws

> "Beware of the argument that general-purpose models don't work well for domain-specific tasks, and, therefore, you must finetune or train models for your specific tasks. As general-purpose models become more capable, they also become better at domain-specific tasks and can outperform the domain-specific models."

The corollary: domain-specific *pretraining* is usually a worse investment than domain-specific *finetuning on top of a general-purpose base*. Bloomberg may still benefit from BloombergGPT for their specific use cases (the benchmark results don't capture everything), and the team certainly gained training experience — but **it's not a recipe to copy**.

## Connections

- [[ai-engineering-ch07-finetuning]] — primary source.
- [[gpt4|GPT-4]] / [[Claude35Sonnet|Claude 3.5 Sonnet]] / [[Llama3]] / [[Qwen2]] — the general-purpose models that outperformed BloombergGPT.
- [[FineTuning]] — the alternative path Bloomberg could have taken.
- [[ChipHuyen]] — author who framed this as a cautionary tale.
- Bloomberg LP — the institution.
