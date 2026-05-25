---
title: "Generative Model"
type: concept
tags: [llm, decoder, generation, taxonomy]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Generative Model

In *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]), [[JayAlammar|Alammar]] and [[MaartenGrootendorst|Grootendorst]] use **generative model** as the umbrella term for **decoder-only** Transformer models that focus on **generating text** rather than producing fixed embeddings. The canonical lineage: [[GPT|GPT-1]] (2018) → [[GPT2|GPT-2]] (2019) → [[GPT3|GPT-3]] (2020) → [[GPT4|GPT-4]] (2023) → [[ChatGPT]] and successors. Open-weights peers include the [[Llama]] family, [[Mistral]] family, and [[Phi3Mini|Phi-3]] / [[microsoft|Microsoft's]] Phi family.

## Definition (from Ch 1)

> "Generative models focus primarily on generating text and typically are not trained to generate embeddings." — Ch 1

The chapter explicitly distinguishes this from **[[RepresentationModel|representation models]]** (encoder-only, e.g., [[bert|BERT]]) — both are Transformer-based; what differs is what they're optimized to produce.

The book uses a visual convention throughout: generative models are drawn in **pink with a small chat icon** (to indicate generative capabilities).

## Why decoder-only

The Transformer's decoder uses **masked (causal) [[selfattention|self-attention]]** — each position can attend only to itself and earlier positions, never future ones. This is exactly what's needed to train a model to predict the next token: without masking, the model could trivially look up the answer.

A decoder-only Transformer trained on next-token prediction over internet-scale text becomes a **completion machine**:

> "Generative LLMs, as sequence-to-sequence machines, take in some text and attempt to autocomplete it." — Ch 1

The chapter coins the **[[CompletionModel|completion-model]]** framing for this — generative LLMs are completion machines, and many higher-level tasks (translation, summarization, classification, coding) can be expressed as completion tasks.

## Scale history (per Ch 1)

| Model | Year | Parameters | Training data |
|---|---|---|---|
| [[GPT|GPT-1]] | 2018 | 117M | 7,000 books + [[CommonCrawl|Common Crawl]] |
| [[GPT2|GPT-2]] | 2019 | 1.5B | WebText (Reddit-link-filtered Common Crawl) |
| [[GPT3|GPT-3]] | 2020 | 175B | Common Crawl + curated sources, 300B tokens |

The chapter notes: *"more parameters greatly influence the capabilities and performance of language models."* This is the empirical observation that motivated the scaling-laws line of research (see [[scalinglaws]]).

## From base model to chatbot

Ch 1 introduces the **[[FoundationModel|base / foundation model]] → [[InstructModel|instruct / chat model]]** distinction:

> "Generative LLMs ... take in some text and attempt to autocomplete it. Although a handy feature, their true power shone from being trained as a chatbot. Instead of completing a text, what if they could be trained to answer questions? By fine-tuning these models, we can create instruct or chat models that can follow directions." — Ch 1

This is the [[pretraining]] → [[FineTuning|fine-tuning]] two-step training paradigm the chapter formalizes later.

## Context length

A defining property of generative models is **[[ContextLength|context length / context window]]** — the maximum number of tokens the model can process. *"A large context window allows entire documents to be passed to the LLM. Note that due to the autoregressive nature of these models, the current context length will increase as new tokens are generated."* — Ch 1

## Position in the LLM taxonomy

Per Ch 1, the book deliberately uses "large language model" to cover *both* generative and representation models — but **generative model is the prototypical, most-commonly-meant LLM in 2024 usage**:

> "These generative decoder-only models, especially the 'larger' models, are commonly referred to as large language models (LLMs)." — Ch 1

## Connections

- [[RepresentationModel]] — the encoder-only sibling category Ch 1 pairs it with.
- [[GPT|GPT-1]] / [[GPT2|GPT-2]] / [[GPT3|GPT-3]] / [[GPT4|GPT-4]] / [[ChatGPT]] — the canonical OpenAI lineage.
- [[Llama]] / [[Mistral]] / [[Phi3Mini]] — open-weights peers.
- [[CompletionModel]] — the framing for what generative models do.
- [[InstructModel]] — the chat / instruction-tuned variant.
- [[FoundationModel]] / [[pretraining]] / [[FineTuning]] — the training paradigm.
- [[ContextLength]] — the defining capacity property.
- [[transformer|Transformer]] — the underlying architecture (decoder stack only).
- [[AutoregressiveLanguageModel]] — the technical name for the next-token-prediction paradigm.
- [[selfattention|Masked self-attention]] — the mechanism that makes decoder-only training work.
- [[LanguageAI]] — the umbrella.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
