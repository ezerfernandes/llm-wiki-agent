---
title: "Intent Classifier"
type: concept
tags: [agents, planning, routing, classification]
sources: [ai-engineering-ch06-rag-agents, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Intent Classifier

**Intent classifier** is the agent component that **predicts what the user is trying to do** with a query, used to (a) select the right tools for the request and (b) reject out-of-scope queries. Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]:

> *"Planning requires understanding the intention behind a task: what's the user trying to do with this query? An intent classifier is often used to help agents plan."*

## How it integrates with planning

Intent classification can be done by:

- **Another prompt** to the same or a different model.
- **A specialized classification model** trained for the task.

Either way, *"the intent classification mechanism can be considered another agent in your multi-agent system"* — Huyen's framing that the boundary between *single agent with sub-components* and *multi-agent system* is mostly notational.

## Routing example

For a customer-support agent:

| Intent | Tool routed to |
|---|---|
| Billing question | Payment-history retrieval |
| Password reset | Documentation retrieval |
| Refund request | Order-lookup + escalation |
| Out of scope | Polite rejection |

The IRRELEVANT class is load-bearing:

> *"Some queries might be out of the scope of the agent. The intent classifier should be able to classify requests as IRRELEVANT so that the agent can politely reject those instead of wasting FLOPs coming up with impossible solutions."*

## Why this matters more than it looks

Without an intent classifier, an agent's tool inventory must be presented in **full** in every prompt — every tool description for every query. With an intent classifier, the tool inventory can be **conditioned on intent** — only billing tools surface for billing queries. This is the cheapest scalability lever in production agent design.

## Connections

- [[Agent]] / [[Planning]] — the parent abstractions.
- [[ToolInventory]] — what intent classification routes against.
- [[multiagentsystems]] — Huyen frames the classifier as itself an agent.
- [[PromptDecomposition]] — the broader Ch 5 pattern this instantiates.
- [[UtteranceIntent]] — the [[CoSTORM|Co-STORM]] intent taxonomy that already exists in the wiki.
- [[ai-engineering-ch06-rag-agents]] — primary source.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 promotes the intent classifier from a Ch 6 *agent component* to the **core of the [[ModelRouter|model router]]** — the third architectural step in the production AI-app reference architecture.

### Three router roles Ch 10 names

1. **Query → solution dispatcher** — billing → payments lookup; technical → troubleshooting bot; out-of-scope → polite refusal.
2. **Next-action predictor** — *"should the model use a code interpreter or a search API next?"*
3. **Memory-tier selector** — choose between attached-document context, conversational history, or external web search.

### Implementation guidance Ch 10 adds

- Adapted small foundation models — **GPT-2, [[bert|BERT]], Llama 7B** — are common router base models.
- Some teams train **even smaller classifiers from scratch** when latency and cost dominate over coverage.
- The hard constraint: *"routers should be fast and cheap so that they can use multiples of them without incurring significant extra latency and cost."*

### Context-window adjustment

When the router routes to a model with a tight context limit but a downstream step expands the prompt (e.g., web search), the router must truncate or re-route. This is a router-specific orchestration concern absent from the Ch 6 framing.

### The canonical pipeline order

> *"Routing → retrieval → generation → scoring is a much more common AI application pattern."* — Ch 10

Pre-retrieval routing is more common than post-retrieval routing, though both exist.
