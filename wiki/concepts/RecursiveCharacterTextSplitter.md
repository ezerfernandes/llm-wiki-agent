---
title: "Recursive Character Text Splitter"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## Definition
LangChain text splitter that recursively splits text by a list of separators.

## In LLM Engineer's Handbook
`RecursiveCharacterTextSplitter` from [[LangChain]] splits text by trying separators in order (e.g. `["\n\n"]`) and falling back to smaller granularities until each chunk fits the configured `chunk_size`. [[leh-ch04-rag-feature-pipeline]] uses it as stage 1 of the generic `chunk_text` function.
