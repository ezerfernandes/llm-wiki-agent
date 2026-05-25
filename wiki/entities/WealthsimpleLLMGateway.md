---
title: "Wealthsimple LLM Gateway"
type: entity
tags: [open-source, model-gateway, llmops, internal-tool]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Wealthsimple LLM Gateway

Open-source [[ModelGateway|model gateway]] built and released by Wealthsimple (Canadian fintech). Cited in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as one of the off-the-shelf gateway options:

> *"There are many off-the-shelf gateways. Examples include Portkey's AI Gateway, MLflow AI Gateway, Wealthsimple's LLM Gateway, TrueFoundry, Kong, and Cloudflare."* — Ch 10

## Significance

A notable instance of an **internal LLM gateway open-sourced by a non-AI company** — Wealthsimple is a regulated financial services company, and the gateway was originally built to manage organizational access to LLM APIs (audit trail, cost control, model-agnostic endpoints) under compliance constraints. Its release demonstrates that the model-gateway pattern is mature enough that production users are publishing reference implementations.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ModelGateway]] — the product category.
- [[Portkey]] / [[Kong]] / [[Cloudflare]] / [[TrueFoundry]] / [[MLflow]] — peer gateway products.
