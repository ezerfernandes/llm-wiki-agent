---
title: "Sliding-Window Chunking"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## Definition
Chunking with overlap between adjacent chunks so boundary context is preserved.

## In LLM Engineer's Handbook
Sliding-window chunking introduces overlap between consecutive text chunks so context near boundaries is preserved in at least one chunk. [[leh-ch04-rag-feature-pipeline]] highlights this as critical for legal, scientific, customer-support, and medical text where information spans sections; default `chunk_overlap=50` characters in the chapter's `chunk_text` implements it.
