---
title: "Multi-Query RAG"
type: concept
tags: [rag, retrieval, query-rewriting, advanced-rag]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Multi-Query RAG

**Multi-query RAG** is the advanced-[[rag|RAG]] extension where one user question is decomposed into **multiple parallel queries**, each retrieving its own context, and the union of contexts is passed to the LLM for grounded generation. The technique extends [[QueryRewriting|query rewriting]] from one-in / one-out to one-in / many-out.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names multi-query RAG in the **Advanced RAG Techniques** section:

> *"The next improvement we can introduce is to extend the query rewriting to be able to search multiple queries if more than one is needed to answer a specific question."* — Ch 8

The canonical worked example:

> *"User Question: 'Compare the financial results of Nvidia in 2020 vs. 2023'"*
> 
> Rewritten as **two parallel queries**:
> - Query 1: *"Nvidia 2020 financial results"*
> - Query 2: *"Nvidia 2023 financial results"*
> 
> *"We then present the top results of both queries to the model for grounded generation."*

## When to use multi-query

Multi-query is the right technique when the user's question **mentions multiple distinct facts to retrieve** that are unlikely to co-occur in any single document:

- Comparisons between entities (Nvidia 2020 vs 2023).
- Multi-aspect questions (*"What is X, and how does Y compare?"*).
- Multi-entity questions (*"Tell me about A, B, and C"*).

A single retrieval over the user's verbatim query will tend to pick a single document discussing one of the entities, missing the others.

## Position in the Advanced-RAG continuum

Ch 8 frames advanced RAG as a delegation-increasing continuum:

| Technique | Query structure |
|---|---|
| [[QueryRewriting]] | One question → one rewritten query |
| **Multi-query RAG** | **One question → N parallel queries** |
| [[MultiHopRAG]] | One question → N sequential queries (each depends on prior results) |
| [[QueryRouting]] | One question → routed to specific data source |
| [[AgenticRAG]] | One question → LLM-as-agent over multi-source + multi-action workspace |

Multi-query is the **parallel-decomposition** point on the continuum; multi-hop is the **sequential** point.

## The no-search option

Ch 8 adds a small but load-bearing detail: *"An additional small improvement here is to also give the query rewriter the option to determine if no search is required and if it can directly generate a confident answer without searching."*

This makes the query rewriter a **router-of-sorts** — it decides:
- One query → standard query rewriting.
- Multiple queries → multi-query RAG.
- No query → bare LLM completion.

The decision is itself an LLM call.

## Connections

- [[rag]] — the parent technique family.
- [[QueryRewriting]] — the technique multi-query extends.
- [[MultiHopRAG]] — the sequential-decomposition complement.
- [[QueryRouting]] — the multi-data-source extension.
- [[AgenticRAG]] — the most-delegated point on the continuum.
- [[CohereChat]] — the Cohere endpoint with built-in query rewriting / multi-query support.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
