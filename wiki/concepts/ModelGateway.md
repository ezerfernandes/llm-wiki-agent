---
title: "Model Gateway"
type: concept
tags: [architecture, platform, model-api, ops, gateway]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Model Gateway

**A model gateway is the intermediate platform layer that gives an organization a single, secure, observable way to talk to many models — self-hosted and commercial — through one API.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]: *"A model gateway is an intermediate layer that allows your organization to interface with different models in a unified and secure manner."*

In Huyen's reference architecture, the gateway *replaces* the raw model-API box once an application is using more than one model (Figure 10-7). Once requests flow through it, the gateway becomes the natural place to attach cross-cutting concerns.

## Five responsibilities

1. **Unified interface** — wrap [[openai|OpenAI]], [[anthropic|Anthropic]], [[gemini|Gemini]], self-hosted models behind one shape. *"If a model API changes, you only need to update the gateway instead of updating all applications that depend on this API."*
2. **Access control and cost management** — *"instead of giving everyone who wants access to the OpenAI API your organizational tokens, which can be easily leaked, you give people access only to the model gateway."* Fine-grained per-user / per-application policies; cost caps; usage attribution.
3. **Fallback policies** — *"a model gateway can also be used to implement fallback policies to overcome rate limits or API failures (the latter is unfortunately common)."* Route to alternate model, retry after backoff, graceful degradation.
4. **Load balancing, logging, analytics** — *"since requests and responses are already flowing through the gateway, it's a good place to implement other functionalities."*
5. **Optionally caching + guardrails** — some gateways absorb these; *"some gateways even provide caching and guardrails."* Boundary with [[ExactCache|exact-cache]] and [[Guardrail|guardrail]] components is fluid.

## Named gateways (Ch 10)

[[Portkey]] AI Gateway, MLflow AI Gateway ([[MLflow]]), [[WealthsimpleLLMGateway|Wealthsimple's LLM Gateway]], [[TrueFoundry]], [[Kong]], [[Cloudflare]].

## Why it matters more than it looks

A gateway is *"relatively straightforward to implement"* — Huyen gives a ~30-line Flask sketch dispatching on `model_type` — yet it is the keystone for organizational discipline: API-key sprawl, cost run-aways, silent provider failures, and inconsistent observability all funnel through this seam. Without a gateway, every application becomes its own ad-hoc integration of those concerns.

## Boundary with the orchestrator

Ch 10 flags an explicit boundary tension: *"some orchestrator tools want to be gateways. In fact, so many tools seem to want to become end-to-end platforms that do everything."* The gateway specifically owns the *model API surface*; the orchestrator (e.g., [[LangChain]], [[LlamaIndex]]) owns the *pipeline chaining*. They overlap when an orchestrator absorbs the gateway role and vice versa.

## A note on tool gateways

> *"A similar abstraction layer, such as a tool gateway, can also be useful for accessing a wide range of tools. It's not discussed in this book since it's not a common pattern as of this writing."* — Ch 10

The tool-side equivalent exists as an idea but had not consolidated into a recognized pattern as of December 2024.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ModelRouter]] — paired component; routing decides *which model*, gateway handles *how to talk to it*.
- [[ModelAPI]] / [[ModelAPIProvider]] — what the gateway abstracts over.
- [[Guardrail]] / [[ExactCache]] — sometimes folded into the gateway.
- [[AIPipelineOrchestration]] — sibling layer with overlapping ambitions.
- [[Portkey]] / [[MLflow]] / [[WealthsimpleLLMGateway]] / [[TrueFoundry]] / [[Kong]] / [[Cloudflare]] — named implementations.
- [[FallbackPolicy]] — gateway-implemented retry/route-around strategy (see below).
