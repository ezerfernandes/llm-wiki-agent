---
title: "Small-to-Big Retrieval"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## Definition
Pre-retrieval indexing strategy decoupling embedding scope from prompt scope.

## In LLM Engineer's Handbook
Small-to-big indexing embeds a small text span for retrieval precision while carrying a larger surrounding window in metadata for generation context. Per [[leh-ch04-rag-feature-pipeline]], this decouples retrieval precision from generation context, avoiding the noise of embedding overlong text.
