---
title: "Continual Learning"
type: concept
tags: [concept, llm]
sources: [2604.27707-agentic-memory-is-a-memo, ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Continual Learning

Family of weight-update methods for streaming experience. Xu et al. note the community has largely ceded the agentic setting to retrieval-based approaches; closing the consolidation gap requires bringing CL methods back to LLM agents.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

[[ChipHuyen|Huyen]] reframes [[InContextLearning|in-context learning]] as **a form of continual learning** — but **without weight updates**:

> "In-context learning allows a model to incorporate new information continually to make decisions, preventing it from becoming outdated. ... With in-context learning, you can include the new JavaScript changes in the model's context, allowing the model to respond to queries beyond its cut-off date. This makes in-context learning a form of continual learning." — Ch 5

This is **the alternative path** to the Xu et al. critique: rather than reviving weight-update CL methods for agents, treat the prompt itself as the continual-learning substrate. The trade-offs differ: in-context-learning-as-CL is bounded by [[ContextLength|context length]] and doesn't compound across sessions without [[rag|RAG]] / memory tooling; weight-update CL persists but requires gradient updates.

Both approaches address the same underlying problem: a model trained at time T must answer questions about events after T.
