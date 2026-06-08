---
title: "LiteLLM"
type: entity
tags: [framework, llm, provider-abstraction, python, oss, agentic-design-patterns]
sources: [dspy-language-models, agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# LiteLLM

**LiteLLM** ([github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)) is an open-source Python SDK from [BerriAI](https://www.berri.ai/) that provides a **unified, OpenAI-shaped client interface over dozens of LLM providers** — [[openai|OpenAI]], [[anthropic|Anthropic]], [[gemini|Google Gemini]], Vertex AI ([[google|GCP]]), [[Databricks]], [[microsoft|Azure]], [[Anyscale]], [[TogetherAI|Together AI]], [[Ollama]], [[SGLang]], and many more — selected via a `provider/model-name` string convention. The library handles per-provider authentication, request shaping, and response parsing, exposing the same `completion()` / `acompletion()` interface (and OpenAI's `chat.completions` shape) across all of them.

## Place in the wiki

LiteLLM surfaces on the wiki as **the upstream provider-abstraction layer underneath [[DSPy]]**. The [[dspy-language-models|DSPy Learn — Language Models]] page (page 3 of 13) is explicit that DSPy's `dspy.LM` client wrapper routes its calls through LiteLLM:

> *"DSPy supports dozens of LLM providers via LiteLLM. Just follow their instructions for whichever provider you want."*

LiteLLM is therefore the **substrate that makes [[DSPyProgrammingModel|DSPy's *swap-the-LM* portability claim]] true**: the `provider/model-name` string convention DSPy uses is LiteLLM's, the per-provider plumbing is LiteLLM's, and the OpenAI-compatible-endpoint escape hatch (`openai/your-model-name` + `api_base=...`) is LiteLLM's pattern.

## The OpenAI-compatible-endpoint pattern

LiteLLM's most-leveraged convention is its **OpenAI-compatible-endpoint** pattern: any provider that exposes an HTTP API matching OpenAI's `/v1/chat/completions` shape is reachable by prefixing the model string with `openai/` and setting `api_base` to the provider URL. [[SGLang]]'s self-hosted server relies on exactly this pattern; many third-party model-hosting services do too. The pattern is what gives the [[dspy-language-models|DSPy Language Models page]] its *catch-all* answer to "what about provider X that isn't in your list?"

## ADK model integration (Agentic Design Patterns Ch 16)

[[agentic-design-patterns-ch16-resource-aware|Ch 16 (Resource-Aware Optimization)]] names LiteLLM as [[GoogleADK|Google ADK]]'s escape hatch for **model flexibility**: ADK can use various [[gemini|Gemini]] models directly, *"or integration of other models through LiteLLM"* (`from google.adk.models.lite_llm import LiteLlm`). This is what lets an ADK [[DynamicModelSelection|dynamic-model-selection]] / [[ResourceAwareOptimization|resource-aware]] router dispatch across providers (not just the Gemini family) — the cross-provider role [[OpenRouter]] plays in the chapter's other example.

## Connections

- [[ResourceAwareOptimization]] / [[DynamicModelSelection]] — Ch 16: LiteLLM is how ADK reaches non-Gemini models for cost-aware routing.
- [[GoogleADK]] — integrates LiteLLM (`google.adk.models.lite_llm.LiteLlm`) for non-default models.
- [[OpenRouter]] — sibling unified-routing layer playing the same cross-provider role in Ch 16's other example.
- [[DSPy]] — primary consumer recorded on the wiki; [[DSPyLM|`dspy.LM`]] is a thin facade over LiteLLM.
- [[dspy-language-models]] — canonical source recording the DSPy-on-LiteLLM dependency.
- [[DSPyLM]] — the DSPy abstraction LiteLLM substantiates.
- [[openai|OpenAI]], [[anthropic|Anthropic]], [[gemini|Gemini]], [[google|Google]], [[Databricks]], [[microsoft|Microsoft]] (Azure), [[Anyscale]], [[TogetherAI|Together AI]], [[Ollama]], [[SGLang]] — providers spanned through LiteLLM.
