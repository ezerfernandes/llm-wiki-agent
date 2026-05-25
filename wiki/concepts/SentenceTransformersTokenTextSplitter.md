---
title: "SentenceTransformers Token Text Splitter"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## Definition
LangChain text splitter that respects a Sentence-Transformers model's max input length.

## In LLM Engineer's Handbook
`SentenceTransformersTokenTextSplitter` from [[LangChain]] splits text into chunks that fit a specific Sentence-Transformers model's `max_seq_length`. Per [[leh-ch04-rag-feature-pipeline]] it is stage 2 of `chunk_text` (after the character-based splitter) with `chunk_overlap=50` to guarantee each chunk fits the embedding model's input window.
