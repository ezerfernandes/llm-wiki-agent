---
title: "Self-Querying"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline, leh-ch09-rag-inference-pipeline]
last_updated: 2026-05-22
---

## Definition
Pre-retrieval RAG step that uses an LLM to extract structured metadata filters from a natural-language query.

## In LLM Engineer's Handbook
Self-querying parses the user's natural-language query and extracts structured metadata fields (author name, tags, ID, date range, like count) that are then applied as filters during the subsequent vector search. Per [[leh-ch09-rag-inference-pipeline]] the LLM is prompted few-shot to return only the requested field value (or `none`); the value is attached as `query.author_id` (or similar), later picked up by [[FilteredVectorSearch]].
