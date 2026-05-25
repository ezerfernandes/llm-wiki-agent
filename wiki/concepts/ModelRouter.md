---
title: "Model Router"
type: concept
tags: [architecture, routing, intent-classification, agents, cost-optimization]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Model Router

**A model router dispatches each incoming query to the appropriate downstream solution — a specific specialized model, a cheaper model for easy queries, a human operator, or a polite refusal.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]: *"Instead of using one model for all queries, you can have different solutions for different types of queries."*

A router is structurally an [[IntentClassifier|intent classifier]] plus a dispatch table. It is the **third** component Huyen adds to the reference AI-app architecture (after [[ContextConstruction|context construction]] and [[Guardrail|guardrails]]), paired with the [[ModelGateway|model gateway]].

## Why route

Three benefits named in Ch 10:

1. **Specialization** — *"one model specialized in technical troubleshooting and another specialized in billing"* can each beat a single generalist on its slice.
2. **Cost** — *"instead of using one expensive model for all queries, you can route simpler queries to cheaper models."*
3. **Out-of-scope rejection** — *"if the user asks who you would vote for in the upcoming election, a chatbot can respond with: 'As a chatbot, I don't have the ability to vote …'"* — without burning an API call.

## Beyond intent classification: next-action and memory routing

A router does not have to be limited to incoming queries:

- **Next-action prediction**: *"for an agent capable of multiple actions, a router can take the form of a next-action predictor: should the model use a code interpreter or a search API next?"*
- **Memory-tier selection**: *"for a model with a memory system, a router can predict which part of the memory hierarchy the model should pull information from."* The example: a user attaches a document mentioning Melbourne, then later asks about Melbourne — should the router fetch from the attached document or trigger a web search?

## Implementation

Ch 10 names two patterns:

- **Adapt a smaller foundation model** — GPT-2, [[bert|BERT]], or Llama 7B fine-tuned as an intent classifier.
- **Train a small classifier from scratch** — when latency and cost matter more than coverage.

The hard constraint: *"routers should be fast and cheap so that they can use multiples of them without incurring significant extra latency and cost."*

## Context-limit adjustment

When the router selects a model with a tight context window but later steps (e.g., web search) inflate the prompt, the router must either:

- Truncate the query's context to fit the originally chosen model, **or**
- Re-route to a larger-context model.

## Canonical pipeline order

> *"Routing → retrieval → generation → scoring is a much more common AI application pattern."* — Ch 10

Routing can happen *after* retrieval too (e.g., escalate to a human if the answer is poor), but the pre-retrieval position is more common.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ModelGateway]] — paired component; routing decides *which*, gateway handles *how to talk*.
- [[IntentClassifier]] — the standard implementation; Ch 6 origin.
- [[Agent]] / [[AgenticAI]] — agent next-action routing.
- [[CustomerServiceAgent]] — Ch 10's worked router example is a customer-support dispatcher.
- [[FalseRefusalRate]] — out-of-scope rejection is the routing-level analog.
- [[bert|BERT]] / GPT-2 / Llama 7B — common router base models.
