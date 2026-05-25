---
title: "Cloudflare"
type: entity
tags: [company, cdn, infrastructure, model-gateway, edge]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Cloudflare

Internet infrastructure and CDN company; cited in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as one of the off-the-shelf [[ModelGateway|model-gateway]] vendors.

> *"There are many off-the-shelf gateways. Examples include Portkey's AI Gateway, MLflow AI Gateway, Wealthsimple's LLM Gateway, TrueFoundry, Kong, and Cloudflare."* — Ch 10

## The "AI Gateway" product

Cloudflare's **AI Gateway** sits in front of LLM API calls and provides analytics, caching, rate limiting, and request logging — leveraging Cloudflare's edge network as the gateway substrate. Like [[Kong]], it represents the convergence of *general API/infrastructure vendors* into the model-gateway niche.

## Position

Cloudflare's appearance alongside specialist gateways (Portkey, Wealthsimple) signals that the model-gateway role is **infrastructure-shaped**, not LLM-specific — many of the operational concerns (rate limit, fallback, logging, security) are old problems the existing API-gateway stack already solves.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ModelGateway]] — the AI-app product category.
- [[Kong]] / [[Portkey]] / [[TrueFoundry]] / [[MLflow]] / [[WealthsimpleLLMGateway]] — peer gateway products.
