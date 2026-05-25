---
title: "Time to Publish"
type: concept
tags: [latency, metrics, inference, agents, cot]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Time to Publish

**The time from a user's query submission until the *first user-visible token* — distinguished from [[TTFT|TTFT]] when intermediate planning / tool-use tokens are hidden.** Introduced in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]] for [[ChainOfThought|CoT]] and agentic queries:

> *"It's important to note that the TTFT and TPOT values observed by users might differ from those observed by models, especially in scenarios involving CoT (chain-of-thought) or agentic queries where models generate intermediate steps not shown to users. Some teams use the metric time to publish to make it explicit that it measures time to the first token users see."*

## Why TTFT alone misleads in agentic workflows

Ch 9's scenario:

1. Model generates a **plan** (sequence of actions). Not shown to the user.
2. Model executes actions and logs their outputs. Not shown to the user.
3. Model generates the **final response** to show to the user.

From the model's perspective, the first token is generated in step 1. From the user's perspective, the first token is from step 3 — sometimes much later. **TTFT** measures the former; **time to publish** measures the latter.

For [[Agent|agentic]] applications with [[Planning|plans]] and [[ToolUse|tool calls]] before the final user-visible answer, time to publish is the metric that matches the actual user experience.

## When time to publish matters

- **[[ChainOfThought|CoT-prompted]] models** that produce hidden reasoning chains before the final answer.
- **[[Agent|Agents]]** that plan, act, observe, then respond.
- **Streaming-with-thinking** UIs that hide intermediate model output.
- **[[RAG]] pipelines** with multiple retrieval-then-generate stages.

## Relationship to other metrics

- **TTFT** — time to model-internal first token (could be a hidden plan).
- **Time to publish** — time to user-visible first token (after CoT / actions complete).
- **TPOT / [[TBT]]** — token cadence (independent of which metric is gating the first one).

In agentic systems, time to publish ≫ TTFT.

## Connections

- [[TTFT]] — the model-internal cousin.
- [[TPOT]] / [[TBT]] — steady-state cadence metrics, unaffected by this distinction.
- [[ChainOfThought]] — CoT produces hidden tokens between model-internal first token and user-visible first token.
- [[Agent]] / [[Planning]] / [[ToolUse]] — agentic workflows where the gap is largest.
- [[Goodput]] — SLO-based metric that should use time-to-publish when user UX matters.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
