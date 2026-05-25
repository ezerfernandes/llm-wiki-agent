---
title: "Query Routing"
type: concept
tags: [rag, retrieval, advanced-rag, routing, multi-source]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Query Routing

**Query routing** is the advanced-[[rag|RAG]] extension where the LLM is given access to **multiple data sources** and decides which source to query based on the question. Extends the retrieval surface from one corpus to many; the LLM-as-router selects the appropriate corpus per query.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names query routing in the **Advanced RAG Techniques** section:

> *"An additional enhancement is to give the model the ability to search multiple data sources. We can, for example, specify for the model that if it gets a question about HR, it should search the company's HR information system (e.g., Notion) but if the question is about customer data, that it should search the customer relationship management (CRM) (e.g., Salesforce)."* — Ch 8

## When to use query routing

Query routing is the right technique when an application spans **multiple disjoint corpora** with different access patterns, schemas, or update cadences:

- **Enterprise document RAG** — HR docs (Notion) vs customer data (Salesforce) vs financial reports (internal DB).
- **Multi-domain assistant** — code questions → docs, business questions → wiki, customer questions → CRM.
- **Tiered-cost retrieval** — cheap-and-fast first; route to expensive specialized index only if needed.

The routing decision is itself an LLM call (or a classifier, in earlier non-LLM implementations).

## Position in the Advanced-RAG continuum

Query routing is the **multi-data-source** point on Ch 8's delegation continuum:

| Technique | What's parameterized | Data sources |
|---|---|---|
| [[QueryRewriting]] | Query string | 1 |
| [[MultiQueryRAG]] | Number of queries | 1 |
| [[MultiHopRAG]] | Query sequence | 1 |
| **Query routing** | **Data source** | **N (one per query)** |
| [[AgenticRAG]] | All of the above | N (with read+write tool symmetry) |

Query routing is **structurally close to [[Agent|agentic]] tool selection** — the LLM is deciding *which tool to call* given the question; the tools happen to be retrieval over different corpora. The shift from query routing to full agentic RAG is **adding more action types** beyond just retrieval.

## Connections

- [[rag]] — the parent technique family.
- [[QueryRewriting]] / [[MultiQueryRAG]] / [[MultiHopRAG]] / [[AgenticRAG]] — sibling advanced-RAG techniques.
- [[Agent]] / [[ToolUse]] — the broader category query routing converges into.
- Customer relationship management (CRM) — Ch 8's named example data source (Salesforce).
- Notion — Ch 8's named example HR data source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
