---
title: "GPT"
type: entity
tags: [model-family, llm, openai]
sources: [leh-ch01-understanding-llm-twin-concept, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

## What it is
GPT (Generative Pre-trained Transformer) is [[openai|OpenAI]]'s family of decoder-only large language models — GPT-1 (2018, 117M), GPT-2 (2019, 1.5B), GPT-3 (2020, 175B), GPT-3.5, GPT-4, GPT-4o, GPT-4o-mini, GPT-5.1, and successors. The original GPT-1 paper ([[AlecRadford|Radford]] et al., 2018, *"Improving Language Understanding by Generative Pre-Training"*) established the decoder-only-Transformer template that all subsequent LLMs inherit. The models are accessed through OpenAI's hosted API and (for some variants) via a fine-tuning interface.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] names GPT as one of three LLM families (alongside [[Mistral]] and [[Llama]]) the LLM Twin's training pipeline must support — provided the model exposes programmatic and fine-tuning access. The book's broader stance: GPT-the-API is a legitimate base; ChatGPT-the-product is the rejected foil because its UI hides infrastructure, makes outputs irreproducible across sessions, and obscures hallucination rates.

## Connections
- [[openai]] — model provider.
- [[ChatGPT]] — consumer product built on GPT; rejected for personalized-content generation.
- [[Llama]] / [[Mistral]] — sibling model families the LLM Twin training pipeline must also support.
- [[GPT3]] / [[GPT4]] / [[GPT51]] — specific GPT-family checkpoints discussed elsewhere in the wiki.
- [[AlecRadford]] — first author of GPT-1 and GPT-2.
- [[GenerativeModel]] / [[CompletionModel]] — the model class GPT defines.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 traces the GPT lineage as the canonical **decoder-only [[GenerativeModel|generative model]]** thread:

> "Similar to the encoder-only architecture of BERT, a decoder-only architecture was proposed in 2018 to target generative tasks. This architecture was called a Generative Pre-trained Transformer (GPT) for its generative capabilities (it's now known as GPT-1 to distinguish it from later versions). ... GPT-1 was trained on a corpus of 7,000 books and Common Crawl, a large dataset of web pages. The resulting model consisted of 117 million parameters." — Ch 1

The scale evolution Ch 1 records:

| Model | Year | Parameters | Source |
|---|---|---|---|
| GPT-1 | 2018 | 117M | Radford et al. 2018 |
| GPT-2 | 2019 | 1.5B | Radford et al. 2019 (*"Language models are unsupervised multitask learners"*) |
| GPT-3 | 2020 | 175B | Brown et al. 2020 (*"Language models are few-shot learners"*) |

*"If everything remains the same, we expect more parameters to greatly influence the capabilities and performance of language models. Keeping this in mind, we saw larger and larger models being released at a steady pace."* — Ch 1
