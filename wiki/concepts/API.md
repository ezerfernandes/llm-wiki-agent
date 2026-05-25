---
title: "API"
type: concept
tags: [software, interface, integration]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# API

**Application Programming Interface** — the set of definitions and protocols through which one piece of software communicates with another. In the LLM context, *the* API typically means a **REST / HTTPS API exposed by a model provider** for sending prompts and receiving generated text without direct access to model weights.

## In *Hands-On LLMs* Ch 1

Ch 1 introduces the API concept specifically as the access pattern for [[ProprietaryLLM|proprietary LLMs]]:

> "You can access these models through an interface that communicates with the LLM, called an API (application programming interface). ... For instance, to use ChatGPT in Python you can use OpenAI's package to interface with the service without directly accessing it." — Ch 1

This is the practical alternative to running weights locally — the user sends a payload, the provider returns generated text, and the model itself remains on the provider's servers.

## Connections

- [[ProprietaryLLM]] — the model class accessed via API.
- [[ModelAsAService]] — the broader business model.
- [[openai|OpenAI]] / [[anthropic|Anthropic]] — providers of major LLM APIs.
- [[ChatGPT]] / [[GPT4]] / [[claudeopus47|Claude]] — example API-accessed models.
- [[HuggingFace]] — also exposes inference APIs (Hugging Face Inference API).
- [[REST]] — the predominant API style for LLM providers.
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 introduces the term.
