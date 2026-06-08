---
title: "API"
type: concept
tags: [software, interface, integration]
sources: [hands-on-llm-ch01-introduction-to-llms, fuzzingbook-24-api-fuzzer]
last_updated: 2026-06-06
---

# API

**Application Programming Interface** — the set of definitions and protocols through which one piece of software communicates with another. In the LLM context, *the* API typically means a **REST / HTTPS API exposed by a model provider** for sending prompts and receiving generated text without direct access to model weights.

## In *Hands-On LLMs* Ch 1

Ch 1 introduces the API concept specifically as the access pattern for [[ProprietaryLLM|proprietary LLMs]]:

> "You can access these models through an interface that communicates with the LLM, called an API (application programming interface). ... For instance, to use ChatGPT in Python you can use OpenAI's package to interface with the service without directly accessing it." — Ch 1

This is the practical alternative to running weights locally — the user sends a payload, the provider returns generated text, and the model itself remains on the provider's servers.

## From The Fuzzing Book — Fuzzing APIs
[[fuzzingbook-24-api-fuzzer|Ch 24]] uses *API* in the other common sense — a **library's functions** (e.g. `urllib`'s `urlparse()`, or `math.sqrt`) as opposed to a remote service. It targets the API *directly* via [[APIFuzzing|API fuzzing]]: rather than feeding system input to a whole program, it synthesizes function-call code (`urlparse("<url>")`) from a [[Grammar|grammar]] and runs it. This is faster and more flexible than system-level fuzzing, at the cost of possible false alarms when a call violates an API's implicit preconditions. [[CallSequenceFuzzing|Call-sequence]] variants exercise such an API across several calls.

## Connections

- [[ProprietaryLLM]] — the model class accessed via API.
- [[ModelAsAService]] — the broader business model.
- [[openai|OpenAI]] / [[anthropic|Anthropic]] — providers of major LLM APIs.
- [[ChatGPT]] / [[GPT4]] / [[claudeopus47|Claude]] — example API-accessed models.
- [[HuggingFace]] — also exposes inference APIs (Hugging Face Inference API).
- [[REST]] — the predominant API style for LLM providers.
- [[APIFuzzing]] / [[CallSequenceFuzzing]] — testing a *library's* API by synthesizing and running function calls ([[fuzzingbook-24-api-fuzzer|Ch 24]]).
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 introduces the term.
- [[fuzzingbook-24-api-fuzzer]] — Ch 24 fuzzes a library API at the function level.
