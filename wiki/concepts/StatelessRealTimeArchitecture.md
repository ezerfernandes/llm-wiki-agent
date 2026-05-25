---
title: "Stateless Real-Time Architecture"
type: concept
tags: [architecture, mlops, anti-pattern]
sources: [leh-ch01-understanding-llm-twin-concept]
last_updated: 2026-05-22
---

## Definition
A **stateless real-time ML architecture** is a serving pattern in which the client must ship the full feature state (user attributes, history, retrieved documents) in every request because the serving layer holds no feature state of its own. The *LLM Engineer's Handbook* explicitly labels this an anti-pattern because it forces the client to know how to access or compute features.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] uses two illustrative failure cases: a movie-recommender server that requires the client to send the user's name, age, watch history, etc. on every request, and a [[rag|RAG]] system that forces the client to fetch and pass retrieved documents alongside the query. The chapter calls this "an antipattern for the client application to know how to access or compute the features" — the abstraction has leaked, the client now needs database access, and feature versioning becomes a cross-cutting concern with no obvious owner.

## Key details
- Client owns feature computation; server is pure-function inference.
- Forces clients to talk directly to feature stores, vector DBs, or warehouses — leaking the data layer through the public API.
- Cannot guarantee feature consistency across clients.
- Conflicts with the [[FTIArchitecture|FTI]] principle that the inference pipeline owns retrieval and feature lookup.
- The book's chosen alternative wraps retrieval and feature lookup inside the inference pipeline (the FastAPI business microservice, in the LLM Twin's case).

## Connections
- [[FTIArchitecture]] — the pattern that replaces this anti-pattern.
- [[MonolithicBatchArchitecture]] — the first of the two anti-patterns the book rejects.
- [[MicroservicesArchitecture]] — the deployment topology that, done right, hides feature lookup behind the inference service boundary.
- [[FeatureStore]] — the abstraction the client should never need to talk to directly.
- [[RESTAPI]] — the protocol whose surface gets polluted by leaking feature state.
