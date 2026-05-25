---
title: "Model as a Service"
type: concept
tags: [ai-engineering, deployment, api, business-model]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Model as a Service

**The deployment pattern in which a foundation model is exposed via an API that receives user queries and returns model outputs.** Popularized by [[openai|OpenAI]] and other model providers. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], MaaS is one of the **three structural factors enabling [[AIEngineering|AI engineering]]** to emerge as a discipline.

> *"The model as a service approach popularized by OpenAI and other model providers makes it easier to leverage AI to build applications. In this approach, models are exposed via APIs that receive user queries and return model outputs. Without these APIs, using an AI model requires the infrastructure to host and serve this model. These APIs give you access to powerful models via single API calls."*

## Why MaaS unlocked AI engineering

Without MaaS, every team that wanted to use a foundation model had to:
1. Acquire model weights (often unavailable).
2. Provision GPU infrastructure to host them.
3. Build serving + monitoring + scaling.

MaaS collapses this to a single API call. Combined with the fact that **AI can also write the surrounding code** and **users can interact via plain English**, this drove the barrier to entry to near-zero — *"anyone, and I mean anyone, can now develop AI applications."*

## API convergence

> *"As model providers converge to the same API, it's becoming easier to swap one model API for another."*

This convergence has two consequences:
- **Good for buyers**: lower switching cost between providers.
- **Bad for providers**: model APIs commoditize, eroding differentiation. (Plays into the [[AIProductDefensibility|defensibility]] discussion — if model APIs commoditize, the moat must come from data or distribution.)

But Huyen warns: each model has its own quirks, strengths, and weaknesses. Swapping one model for another still requires reworking prompts, contexts, and evaluation pipelines — *without proper infrastructure for versioning and evaluation, the process can cause a lot of headaches.*

## MaaS economics

Inference cost has dropped sharply over time (see [[AIInvestmentBoom]]) — [[Scribd|Scribd's]] AI cost fell two orders of magnitude April 2022 → April 2023. This rapid price decay also creates risk: *"you may decide to build a model in-house because it seems cheaper than paying for model providers, only to find out after three months that model providers have dropped their prices in half, making in-house the expensive option."*

## Connections

- [[FoundationModel]] — the model class served via MaaS.
- [[AIEngineering]] — discipline MaaS enables.
- [[AIInvestmentBoom]] — the cost-decay trend MaaS rides.
- [[openai|OpenAI]] — MaaS originator.
- [[anthropic|Anthropic]] / [[google|Google]] / [[meta|Meta]] / [[Mistral7BInstructV02|Mistral]] — peer MaaS providers.
- [[AIProductDefensibility]] — MaaS commoditization is the central defensibility threat.
- [[ai-engineering-ch01-intro]] — primary source.
