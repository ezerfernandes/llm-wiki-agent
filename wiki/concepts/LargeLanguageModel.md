---
title: "Large Language Model"
type: concept
tags: [llm, language-models, scale, foundation-models]
sources: [ai-engineering-ch01-intro, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Large Language Model

A scaled-up [[LanguageModel|language model]] trained via [[SelfSupervision|self-supervision]] on internet-scale text, large enough to perform a wide range of tasks via in-context learning and prompting. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], *"LLM is hardly a scientific term"* — the boundary between "language model" and "large language model" is determined by current expectations of scale rather than by a sharp technical definition.

## Historical milestones (Ch 1)

- **June 2018** — [[openai|OpenAI's]] first GPT, **117M parameters**. Considered large.
- **February 2019** — GPT-2, **1.5B parameters**. 117M now considered small.
- **At Ch 1's time of writing (2024)** — "a model with 100 billion parameters is considered large."
- **Implied trajectory** — what is "large" today will be "small" tomorrow.

## What scale required: self-supervision

The crucial enabler is **[[SelfSupervision|self-supervision]]**: language modeling can derive labels from the input itself (next token / masked token), unlike the supervised paradigm (e.g., [[AlexNet]]) that required manually labeled datasets like [[ImageNet]] ($50k to label 1M images). Self-supervision dissolves the data-labeling bottleneck — *any text on the internet* becomes training data — enabling parameter counts to scale.

## Parameters

> *"A parameter is a variable within an ML model that is updated through the training process. In general, though this is not always true, the more parameters a model has, the greater its capacity to learn desired behaviors."* — Ch 1

Note: Huyen treats "model weights" as synonymous with "model parameters" (including biases), reflecting standard 2024 usage.

## Why larger models need more data

> *"You can train a large model on a small dataset too, but it'd be a waste of compute. You could have achieved similar or better results on this dataset with smaller models."*

Compute-efficient training of large models requires data scaled commensurately — connecting to the [[ScalingLaws|Kaplan/Chinchilla scaling laws]] literature elsewhere in the wiki.

## LLM → Foundation Model

Once a language model is extended to other modalities (text + image + audio + video), Huyen prefers the term **[[FoundationModel|foundation model]]** — both because the modalities exceed language and because "foundation" emphasizes the build-upon-able role.

## Connections

- [[LanguageModel]] — the parent concept (statistical joint-probability model over tokens).
- [[FoundationModel]] — the umbrella term when modalities extend.
- [[SelfSupervision]] — the training paradigm.
- [[AutoregressiveLanguageModel]] — the dominant LLM type.
- [[maskedlanguagemodel]] — the non-generative variant (BERT).
- [[Tokenization]] / [[Tokenizer]] — input-unit construction.
- [[GPT4]] / [[ChatGPT]] / [[gemini]] / [[claudeopus47]] / [[bert]] / [[Mistral7BInstructV02]] — representative LLMs.
- [[scalinglaws]] / [[2001.08361-scaling-laws]] — quantitative scaling backbone.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

[[JayAlammar|Alammar]] and [[MaartenGrootendorst|Grootendorst]] explicitly adopt a **more permissive definition** of "large language model" than the [[ai-engineering-ch01-intro|Chip Huyen Ch 1]] framing — they include encoder-only [[RepresentationModel|representation models]] (e.g., [[bert|BERT]]) and sub-1B-parameter models in the LLM category:

> "The term LLM is not only reserved for generative models (decoder-only) but also representation models (encoder-only). ... 'Large' is arbitrary and what might be considered a large model today could be small tomorrow. There are currently many names for the same thing and to us, 'large language models' are also models that do not generate text and can be run on consumer hardware." — Ch 1

The two operational consequences:

1. **The book covers BERT-class encoder-only models under "LLM."** Chs 4 (classification), 5 (clustering), 8 (semantic search), and 11 (fine-tuning representation models) all use sub-1B encoder-only models as their primary worked artifact.

2. **The book uses [[Phi3Mini|Phi-3-mini]] (3.8B params) as its recurring generative LLM** — much smaller than the 100B+ models the [[ai-engineering-ch01-intro|Huyen framing]] anchors on. The book's stance: 3.8B is plenty for educational purposes and fits on a free Google Colab T4.

**This is a definitional difference, not a contradiction** — both books name the same models (BERT, GPT family, Llama, Mistral, Phi) but draw the "LLM" line in different places. The wiki preserves both framings.

The book also adopts the same scaling history Ch 1 of *AI Engineering* records: GPT-1 (June 2018) 117M params → [[GPT2|GPT-2]] (Feb 2019) 1.5B → [[GPT3|GPT-3]] (June 2020) 175B — *"more parameters greatly influence the capabilities and performance of language models."*
