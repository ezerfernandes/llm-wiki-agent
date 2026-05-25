---
title: "Cohere Embed"
type: entity
tags: [api, endpoint, cohere, embedding, dense-retrieval, search]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Cohere Embed

The `co.embed` endpoint of the [[Cohere]] managed API — produces text embeddings with an **explicit `input_type` parameter** that distinguishes documents (indexed once) from queries (embedded at query time). Ch 8 of *Hands-On LLMs* uses it as the chapter's **managed dense-retrieval substrate**.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

The signature minimal-API receipt:

```python
# Embed documents at index time
response = co.embed(
    texts=texts,
    input_type="search_document",
).embeddings
embeds = np.array(response)
print(embeds.shape)  # (15, 4096) — 15 sentences × 4,096-dim vectors

# Embed query at query time
query_embed = co.embed(
    texts=[query],
    input_type="search_query",
).embeddings[0]
```

## The dual-input-type signal

The `input_type="search_document"` vs `"search_query"` distinction is **the API-level operationalization** of the **query-document asymmetry** Ch 8 names as the second of two dense-retrieval caveats:

> *"Are a query and its best result semantically similar? Not always. This is why language models need to be trained on question-answer pairs to become better at retrieval."*

Cohere's API surface the asymmetric training directly — the same model produces **different embeddings** for the same string depending on whether it's a document being indexed or a query being matched. The `input_type` switch is how the caller signals which side of the asymmetry they're on.

## Position in Cohere's managed-RAG stack

`co.embed` is the **first endpoint** in Cohere's three-endpoint managed-RAG path: [[CohereEmbed|`co.embed`]] → [[CohereRerank|`co.rerank`]] → [[CohereChat|`co.chat`]]. Ch 8 walks all three sequentially on the *Interstellar* corpus.

## Connections

- [[Cohere]] — parent API provider.
- [[CohereChat]] / [[CohereRerank]] — sibling endpoints.
- [[EmbeddingBasedRetrieval]] / [[DenseRetrieval]] — the technique family.
- [[SemanticSearch]] — the application.
- [[FAISS]] — the index Ch 8 stores the resulting embeddings in.
- [[VectorDatabase]] — the production storage layer alternative.
- [[MTEB]] — the benchmark Cohere's embed models compete on.
- [[FineTuning]] — the query-document asymmetry is created by question-answer-pair fine-tuning (Ch 10's topic).
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
