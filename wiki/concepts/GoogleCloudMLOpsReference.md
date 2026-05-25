---
title: "Google Cloud MLOps Reference Architecture"
type: concept
tags: [architecture, mlops, cloud]
sources: [leh-ch01-understanding-llm-twin-concept]
last_updated: 2026-05-22
---

## Definition
The **Google Cloud MLOps reference architecture** is Google's production-ready blueprint for end-to-end ML operations, comprising roughly twenty interconnected components (data ingestion, feature store, experiment tracking, training, evaluation, registry, serving, monitoring, governance, etc.). It is the foil against which the *LLM Engineer's Handbook* positions its lighter-weight [[FTIArchitecture|FTI pattern]].

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] acknowledges the Google Cloud reference as production-grade but rejects it for the LLM Twin: with ~20 moving pieces it is too complex to start small and grow from, intimidating for teams without a dedicated platform engineering function, and an obstacle to the data-centric/model-agnostic posture the book recommends. The chapter uses it to make the case that the FTI pattern is a better starting point — fewer abstractions, but still extensible toward the Google-style maturity once the product is validated.

## Key details
- Approximately 20 components covering data, training, serving, monitoring, governance, and lineage.
- Considered production-ready for large-scale enterprises.
- Treated as an aspirational endpoint, not a starting point.
- Book's critique: "It's not really approachable when you want to start small and grow your system as needed."

## Connections
- [[FTIArchitecture]] — the lighter alternative the book uses as its starting blueprint.
- [[MLOps]] — the discipline both architectures operationalize.
- [[google]] — publisher of the reference.
- [[GoogleCloudVertexAI]] — the productized stack that materializes the reference for Google Cloud users.
- [[LLMOps]] — the next-layer-up discipline the LLM Twin focuses on.
