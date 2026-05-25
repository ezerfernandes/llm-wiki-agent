---
title: "Llama License"
type: concept
tags: [license, meta, llama, open-weight]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Llama License

[[meta|Meta]]'s **Community License** family for the Llama models — Llama 2 Community License Agreement, Llama 3 Community License Agreement. Discussed at length in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] as the canonical example of how a major model release uses a **custom license**, not a standard open-source one.

## Two material restrictions

1. **MAU cap.** *"Llama-2 and Llama-3 specify that applications with more than 700 million monthly active users require a special license from Meta."* This is *"similar to the Elastic License that forbids companies from offering the open source version of Elastic as a hosted service and competing with the Elasticsearch platform."*
2. **No output-based training.** *"As of this writing, the Llama licenses still don't allow [using model outputs to train other models]."* This blocks [[knowledgedistillation|distillation]] and [[DataSynthesis|synthetic-data]] pipelines that use Llama as a teacher. [[Mistral]] originally had the same restriction but later relaxed it; Llama has not.

## Why these restrictions matter

- The 700M MAU cap targets cloud providers (AWS / Azure / GCP) and would-be hosted-LLM competitors — not enterprise users.
- The distillation ban means you can't legally train a small model to mimic Llama for commercial deployment.

## Position

The most-discussed specific case of [[ModelLicense|model licensing]] in Ch 4 — the chapter uses Llama to illustrate every concern at once (custom license, MAU cap, distillation ban).

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[ModelLicense]] — parent concept.
- [[meta|Meta]] — authoring organization.
- [[OpenWeight]] — Llama's actual model class.
- [[knowledgedistillation|Knowledge Distillation]] — what the license blocks.
