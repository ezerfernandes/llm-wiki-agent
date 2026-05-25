---
title: "Minimum Viable Product (MVP)"
type: concept
tags: [product-design, methodology]
sources: [leh-ch01-understanding-llm-twin-concept]
last_updated: 2026-05-22
---

## Definition
A **Minimum Viable Product (MVP)** is the smallest, simplest version of a product that delivers the core value to early users and lets the team validate hypotheses about the problem and the solution before investing in full-scope engineering.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] devotes a section to MVP scoping for the [[LLMTwin]]: the authors deliberately constrain the MVP to four crawled data sources (LinkedIn, Medium, Substack, GitHub), an open-source LLM fine-tuned on that data, a [[VectorDatabase]] populated for [[rag|RAG]], LinkedIn-post generation, and a thin web UI for source configuration. The chapter argues MVP scoping is what enables the FTI architectural choices that follow — without a clear "what" you cannot decide which corners to cut in the "how."

## Key details
- MVP scoping is presented as a "Why / What / How" planning lens — the *What* of the LLM Twin.
- The book repeatedly invokes "batch first, streaming later" and "logical feature store, not specialized" as MVP-mindset compromises that defer complexity until validated by usage.
- An MVP is not a prototype: it is shipped, exercised by users, and measured.

## Connections
- [[LLMTwin]] — the running MVP the book scopes.
- [[ProductDesign]] — the broader discipline MVP scoping serves.
- [[SystemsDesign]] — the "How" stage that follows the MVP "What."
- [[FTIArchitecture]] — the architectural pattern chosen partly because it fits an MVP budget while remaining extensible.
- [[LogicalFeatureStore]] — an MVP-mindset substitution for a specialized feature store.
