---
title: "Neural Search"
type: concept
tags: [search, retrieval, embeddings, reranking, nlp]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Neural Search

**Neural search** is the family of information-retrieval systems that use **neural-network-derived embeddings** (rather than keyword overlap or hand-crafted lexical signals) to rank candidate documents against a query. A typical neural-search pipeline embeds both the query and a corpus of documents into a shared vector space, retrieves the **top-K nearest neighbours** by [[CosineSimilarity|cosine similarity]] or another vector distance, and then **reranks** that small candidate set with a more expensive model (often a [[CrossEncoder|cross-encoder]] or generative LLM).

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 forward-references neural search when describing [[BERTopic]]'s **representation-model abstraction**: *"this idea of reranking an initial set of results is a main staple in neural search, a subject that we cover in Chapter 8."* Ch 5's representation models — [[KeyBERTInspired]], [[MaximalMarginalRelevance|MMR]], and [[GenerativeTopicLabeling|LLM-based labeling]] — are reranking blocks layered on top of [[ClassBasedTFIDF|c-TF-IDF]]'s initial keyword distribution; the same pattern (*"generate cheap candidates broadly, refine expensively on a small set"*) is the central design principle of neural search at the document-retrieval level.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 forward-reference.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 (forward-referenced) is the neural-search chapter proper.
- [[ReRanking]] — the core operation neural search depends on.
- [[SemanticSearch]] — the most common umbrella term for neural-search-based retrieval.
- [[Embedding]] / [[SentenceEmbedding]] — the substrate.
- [[rag]] — neural search is the retrieval half of retrieval-augmented generation.
- [[CrossEncoder]] — a common reranker architecture.
