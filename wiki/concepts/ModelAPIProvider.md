---
title: "Model API Provider"
type: concept
tags: [api, organization-class, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Model API Provider

An organization that exposes a [[ModelAPI|model API]] backed by an [[InferenceService|inference service]]. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], three categories:

1. **Model providers** — develop their own models, then expose them via API. Examples: [[openai|OpenAI]], [[anthropic|Anthropic]], [[google|Google]], [[Mistral]], [[Cohere]].
2. **Cloud service providers** — partner with model developers (e.g., Azure hosts GPT-4) and/or host open-source models. Examples: [[microsoft|Azure]], [[Amazon|AWS]], GCP.
3. **Third-party API providers** — specialized startups that host open-source models with their own optimizations. Examples: [[Databricks]] Mosaic, [[Anyscale]].

## Why third-party providers exist

> "API providers might be more motivated to provide better APIs with better pricing. … For commercial model providers, models are their competitive advantages. For API providers that don't have their own models, APIs are their competitive advantages."

Third parties compete on API quality, pricing, latency, and added features. The downside is that early-stage API providers may have unreliable SLAs.

## Private deployment variant

> "There are also commercial API providers that can deploy their services within your private networks. In this discussion, I treat these privately deployed commercial APIs similarly to self-hosted models."

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[ModelAPI]] / [[InferenceService]] — sibling concepts.
- [[ModelBuildVsBuy]] — the decision they compete in.
- [[openai|OpenAI]] / [[anthropic|Anthropic]] / [[google|Google]] / [[Mistral]] / [[Cohere]] — model-provider examples.
- [[microsoft|Azure]] / [[Amazon|AWS]] / [[Databricks]] / [[Anyscale]] — cloud and third-party examples.
