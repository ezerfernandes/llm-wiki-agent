---
title: "Snowballing Hallucination"
type: concept
tags: [hallucination, llm, failure-mode]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Snowballing Hallucination

A specific [[Hallucination|hallucination]] pattern named by **Zhang et al. (2023)** and cited in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "After making an incorrect assumption, a model can continue hallucinating to justify the initial wrong assumption."

## The amplifying effect

The most striking part of Zhang et al.'s finding is that **initial wrong assumptions can cause the model to make mistakes on questions it would otherwise answer correctly**. Ch 2's worked example: an initial incorrect assumption can cause the model to claim that 9677 is divisible by 13, even if it knows this isn't true in isolation.

## Mechanism: tied to [[SelfDelusion|self-delusion]]

Snowballing hallucination is a direct consequence of the [[SelfDelusion|self-delusion]] mechanism (Ortega et al., DeepMind 2021): the model treats its own generated text as ground-truth context for subsequent generation. Once a wrong assertion is in the context, the model justifies it.

## Engineering responses

- **[[StopGeneration|Early stopping / cut-loop detection]]** — if the model is going in circles or contradicting itself, terminate.
- **Re-prompt with cleaner context** — strip the hallucinated assertion from history.
- **[[SelfVerification|Self-verification / self-consistency over multiple chains]]** — sample multiple reasoning chains and look for the one that doesn't snowball.
- **[[rag|RAG / retrieval-augmented generation]]** — ground generation in retrieved facts so the model has less freedom to invent.

## Connections
- [[SelfDelusion]] — the underlying mechanism.
- [[Hallucination]] — parent phenomenon.
- [[InternalKnowledgeMismatch]] — the complementary hallucination hypothesis.
- [[AutoregressiveLanguageModel]] — the architecture where snowballing is mechanically possible.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[selfconsistency]] — the test-time-compute defense.
- [[rag]] — the grounding defense.
