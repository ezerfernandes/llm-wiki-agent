---
title: "OpenRouter"
type: entity
tags: [organization, llm-routing, infrastructure, api-aggregator]
sources: [2603.19247-prompt-optimization-jailbreaking]
last_updated: 2026-05-22
---

# OpenRouter

Provider-aggregation routing layer for LLM APIs. Single API surface that fans out to multiple frontier and open-weights model providers. Conceptual sibling to [[LiteLLM]]; both reduce per-provider client logic to a unified call.

## In this wiki

- [[2603.19247-prompt-optimization-jailbreaking]] — used for inference against all four target models (Qwen-3 8B, LLaMA-4 Maverick, Gemini 2.5 Pro, Claude 4.5 Sonnet) at $T = 0.7$ with max 5,000 tokens (retry bumps to 8,000). The single routing layer is what makes the cross-vendor red-teaming experiment tractable.

## Connections

- [[LiteLLM]] — sibling provider-abstraction layer (used by [[DSPy]] for the same purpose).
- [[DSPy]] — the framework consuming OpenRouter in the source paper.
- [[2603.19247-prompt-optimization-jailbreaking]] — primary wiki source.
