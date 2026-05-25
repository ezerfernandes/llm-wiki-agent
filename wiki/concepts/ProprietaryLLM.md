---
title: "Proprietary LLM"
type: concept
tags: [llm, closed-source, api, deployment]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Proprietary LLM

LLMs whose **weights and architecture are kept private** — accessed only through an [[API|application programming interface]] (API) hosted by the model provider. Defined in *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]) as the counterpart to [[OpenSourceLLM|open-source LLMs]]:

> "Closed source LLMs are models that do not have their weights and architecture shared with the public. They are developed by specific organizations with their underlying code being kept secret. ... These proprietary models are generally backed by significant commercial support and have been developed and integrated within their services." — Ch 1

## Canonical examples cited in Ch 1

- **[[openai|OpenAI's]] [[GPT4|GPT-4]]** — accessed via OpenAI API or [[ChatGPT]].
- **[[anthropic|Anthropic's]] Claude** — accessed via Anthropic API or claude.ai.

## Trade-offs (per Ch 1)

**Advantages:**
- *"The user does not need to have a strong GPU to use the LLM. The provider takes care of hosting and running the model and generally has more computing available."*
- *"There is no expertise necessary concerning hosting and using the model, which lowers the barrier to entry significantly."*
- *"These models tend to be more performant than their open source counterparts due to the significant investment from these organizations."*

**Disadvantages:**
- *"It can be a costly service. The provider manages the risk and costs of hosting the LLM, which often translates to a paid service."*
- *"Since there is no direct access to the model, there is no method to fine-tune it yourself."* — though some providers offer paid fine-tuning APIs.
- *"Your data is shared with the provider, which is not desirable in many common use cases, such as sharing patient data."*

## Access pattern

Ch 1's Figure 1-31 shows the standard pattern: a Python client (`from openai import OpenAI`) issues HTTPS requests; the provider serves the request from their internal infrastructure; only the output text crosses back. *"To use ChatGPT in Python you can use OpenAI's package to interface with the service without directly accessing it."* — Ch 1

## When to choose proprietary

Per Ch 1's implicit reasoning:
- **Quality matters more than cost** — frontier proprietary models often lead benchmarks.
- **Low-volume / unpredictable use** — pay-per-call beats running idle hardware.
- **No GPU expertise / no local GPU** — the provider absorbs operational cost.
- **Data privacy is not a hard constraint** — sensitive-data use cases push toward open + local.

## Connections

- [[OpenSourceLLM]] — the counterpart category.
- [[ChatGPT]] / [[GPT4]] / [[claudeopus47|Claude]] — example proprietary LLMs.
- [[openai]] / [[anthropic]] / [[google]] — proprietary LLM providers.
- [[API]] / [[ModelAsAService]] — the access pattern.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
