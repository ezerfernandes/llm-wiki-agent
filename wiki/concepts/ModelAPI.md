---
title: "Model API"
type: concept
tags: [api, infrastructure, ai-engineering, serving]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Model API

The **user-facing interface** to an [[InferenceService|inference service]]. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "The interface users interact with is called the model API."

## Three flavors of model APIs

1. **Model providers** ([[openai|OpenAI]], [[anthropic|Anthropic]], [[google|Google]], [[Mistral]], [[Cohere]]) — first-party.
2. **Cloud service providers** ([[microsoft|Azure]], [[Amazon|AWS]], GCP) — host commercial models under partnership and host open-source models on their own infrastructure.
3. **Third-party API providers** ([[Databricks]] Mosaic, [[Anyscale]], etc.) — startups that host open-source models with optimizations and features.

Same model on different APIs can behave differently because of inference optimizations.

## OpenAI API as de facto standard

> "Many model developers try to make their models mimic the API of the most popular models. As of this writing, many API providers mimic OpenAI's API."

The chat-completions schema (`messages: [{role, content}]`, etc.) has become the swap-compatibility layer.

## What model APIs typically expose / hide

| Often exposed | Often limited / hidden |
|---|---|
| Text generation | [[Logprobs|Logprobs]] (limited or absent) |
| [[StructuredOutputs|Structured outputs]] / JSON mode | Intermediate activations |
| [[FunctionCalling|Function calling]] | Custom [[FineTuning|finetuning]] (varies) |
| Sampling params (temperature, top-p) | KV cache, full model weights |
| Moderation endpoints | Long-tail customization |

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[InferenceService]] / [[ModelAPIProvider]] — sibling concepts.
- [[Logprobs]] — frequently-restricted output worth fighting for.
- [[ModelBuildVsBuy]] — the build/buy decision filter.
- [[FineTuning]] / [[StructuredOutputs]] / [[FunctionCalling]] — functionality dimensions.
