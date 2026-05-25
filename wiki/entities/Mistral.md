---
title: "Mistral"
type: entity
tags: [company, model-family, llm, open-weight, france]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch02-tooling-and-installation, leh-ch08-inference-optimization, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch09-multimodal-llms]
last_updated: 2024-12-04
---

## What it is
Mistral AI is a French AI lab known for releasing competitive open-weight LLMs (Mistral 7B, Mixtral 8x7B, Mistral Small/Medium/Large) and the matching paid API. The "Mistral" name is used for both the company and the family of base models.

## In LLM Engineer's Handbook
Ch. 1 ([[leh-ch01-understanding-llm-twin-concept]]) names Mistral as one of the three LLM families ([[Mistral]], [[Llama]], [[GPT]]) the training pipeline must be able to swap between for the LLM Twin. Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Mistral among the foundation models hosted on [[AmazonBedrock]]. Ch. 8 ([[leh-ch08-inference-optimization]]) uses `mistralai/Mistral-7B-Instruct-v0.3` to demonstrate FlashAttention-2 (`attn_implementation="flash_attention_2"`).

## Connections
- [[Mistral7BInstructV02]] — specific model entity page already in the wiki.
- [[Mixtral8x7B]] — Mistral's MoE flagship; canonical Ch 2 worked example.
- [[Llama]] / [[GPT]] — peer LLM families.
- [[meta]] / [[openai]] — competitor LLM publishers.
- [[HuggingFace]] — primary distribution channel for Mistral weights.
- [[AmazonBedrock]] — hosts Mistral models as a managed API.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 features **[[Mixtral8x7B|Mixtral 8x7B]]** as **the canonical worked example for [[MixtureOfExperts|MoE]] sparsity**:

- 8 experts × 7B params = 56B nominally → **46.7B total** (shared params) → **12.9B active per token** (2 of 8 experts active per layer).
- Cost and speed match a 12.9B dense model despite 46.7B total params.

Per Ch 1, Mixtral's **vocabulary is 32,000 tokens** (vs GPT-4's 100,256) — partially explaining the cost / speed advantage.

Mistral is one of three "well-funded startups" Ch 1 names as having the resources to develop FMs from scratch (alongside [[openai|OpenAI]] and [[anthropic|Anthropic]]).

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 surfaces Mistral in three roles:

1. **Apache 2.0 license** — *"Mistral-7B were released under Apache 2.0"* — making it one of the **most permissively-licensed** strong open-weight models. Contrast with [[meta|Meta]]'s custom [[LlamaLicense|Llama Community License]] (which has a 700M MAU cap and bans distillation).
2. **Distillation policy change** — *"Mistral didn't allow [using model outputs to train other models] originally but later changed its license. As of this writing, the Llama licenses still don't allow it."* Ch 4 uses Mistral as the positive example of a license loosening over time.
3. **Provider + API hybrid** — Mistral is one of the model providers that *"open source some models and provide APIs for some."* Same dual strategy as [[Cohere]].

Per Ch 4's incentive-structure footnote: *"Both Mistral and Cohere have open source models, but they also have APIs. At some point, inference services on top of Mistral and Cohere models become their competitors."* This frames Mistral's open-source strategy as both a community commitment and a competitive risk to its own API business.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 names Mistral as one of four representative **[[OpenSourceLLM|open-weights LLM]] families**:

> "Cohere's Command R, the Mistral models, Microsoft's Phi, and Meta's Llama models are all examples of open models." — Ch 1

The book's [[OpenSourceLLM|open-vs-proprietary]] framing positions Mistral on the "open models you can download and run locally" side of the spectrum.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 names **Mistral 7B as the LLM backbone of [[Idefics2|Idefics 2]]** — Hugging Face's efficient adapter-style multimodal LLM cited alongside [[BLIP2|BLIP-2]] and [[LLaVA15|LLaVA]] as a contemporary visual LLM: *"Idefics 2, an efficient visual LLM based on the Mistral 7B LLM."* This is Mistral's wiki debut in a **multimodal** context — Mistral's role here is the open-weights text-LLM substrate that a vision adapter is bolted onto, the same architectural role [[meta|Meta]]'s OPT-2.7b plays inside BLIP-2.
