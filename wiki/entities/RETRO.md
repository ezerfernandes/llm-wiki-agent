---
title: "RETRO"
type: entity
tags: [cs324, llm]
sources: [cs324-selective-architectures]
last_updated: 2026-06-04
---

RETRO (Retrieval-Enhanced Transformer) is a DeepMind language model that augments a Transformer with retrieval over an external datastore. A 7B-parameter RETRO model retrieves 32-token chunks from a roughly 2-trillion-token datastore, allowing it to rival the performance of far larger parameter-only language models.

## Connections
- [[RAG]] — RETRO is a retrieval-augmented generation architecture
- [[DenseRetrieval]] — retrieves chunks from a large external datastore
- [[cs324-selective-architectures]] — discussed in this CS324 lecture
