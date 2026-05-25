---
title: "Re-Ranking"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline, leh-ch09-rag-inference-pipeline, ai-engineering-ch06-rag-agents, hands-on-llm-ch05-text-clustering-topic-modeling, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

## Definition
Post-retrieval RAG step that rescores top-K candidates with a stronger model (typically a cross-encoder).

## In LLM Engineer's Handbook
Re-ranking rescores retrieved candidates with a more accurate model — usually a [[CrossEncoder]] — and keeps the top K for prompt augmentation. [[leh-ch04-rag-feature-pipeline]] and [[leh-ch09-rag-inference-pipeline]] use `cross-encoder/ms-marco-MiniLM-L-4-v2` (wrapped in a [[Singleton]] `CrossEncoderModelSingleton`). Aggressive top-K trimming via re-ranking fights the [[lostinthemiddle]] LLM bias.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] names reranking as one of four production retrieval-optimization tactics (alongside [[ChunkingStrategy]], [[QueryRewriting]], and [[ContextualRetrieval]]). She develops two patterns beyond the LLM Engineer's Handbook treatment:

**Time-weighted reranking** — *"Documents can also be reranked based on time, giving higher weight to more recent data. This is useful for time-sensitive applications such as news aggregation, chat with your emails (e.g., a chatbot that can answer questions about your emails), or stock market analysis."*

**Context reranking vs search reranking** — *"Context reranking differs from traditional search reranking in that the exact position of items is less critical. In search, the rank (e.g., first or fifth) is crucial. In context reranking, the order of documents still matters because it affects how well a model can process them. Models might better understand documents at the beginning and end of the context [[NeedleInAHaystack|(NIAH)]], but as long as a document is included, the impact of its order is less significant compared to search ranking."*

The structural read: search reranking is **rank-precision-sensitive**; RAG reranking is **inclusion-and-position-sensitive**. The Ch 6 framing fits Huyen's broader thesis that RAG retrieval is not search — it's context construction.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 explicitly **generalizes the reranking pattern beyond retrieval**: *"this idea of reranking an initial set of results is a main staple in neural search, a subject that we cover in Chapter 8."* [[BERTopic]]'s **representation models** ([[KeyBERTInspired]], [[MaximalMarginalRelevance|MMR]], [[GenerativeTopicLabeling|LLM-based labeling]]) are reranking blocks layered on top of [[ClassBasedTFIDF|c-TF-IDF]]'s initial keyword distribution. The structural insight: **reranking is the abstraction of "generate cheap candidates broadly, refine expensively on a small set,"** applied to either retrieval (Ch 6 / LEH Ch 4 / Ch 8 forward-reference) or topic representation (Ch 5).

Key efficiency claim from Ch 5: reranking the topic-keyword distribution runs **once per topic** (≈100), not once per document (≈millions) — *"the representation block only needs to be applied once for every topic instead of for every document."* This is the same per-candidate efficiency property that motivates cross-encoder reranking on top of bi-encoder retrieval.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 dedicates its **second main section** to reranking — *"an easier way to incorporate language models is as a final step inside their search pipeline."* The chapter's framing is **reranking is the lightest-touch LLM-add to an existing search system**:

> *"This step is tasked with changing the order of the search results based on relevance to the search query. This one step can vastly improve search results and it's in fact what Microsoft Bing added to achieve the improvements to search results using BERT-like models."* — Ch 8

**The headline efficacy claim** (the wiki's canonical reranker-lift number):

> *"On a multilingual benchmark like [[MIRACL]], a reranker can boost performance from 36.5 to 62.8, measured as [[NDCG|nDCG@10]] (more on evaluation later in this chapter)."* — Ch 8

This is **almost a 2× lift** from adding a reranker on top of [[BM25|BM25]] — quantitative anchor for "what reranking is worth."

**The mechanism — [[CrossEncoder|cross-encoder]]:**

> *"One popular way of building LLM search rerankers is to present the query and each result to an LLM working as a cross-encoder. This means that a query and possible result are presented to the model at the same time allowing the model to view both these texts before it assigns a relevance score ... All of the documents are processed simultaneously as a batch yet each document is evaluated against the query independently."* — Ch 8

**The reference architecture — [[MonoBERT|monoBERT]]:** *"This method is described in more detail in a paper titled 'Multi-stage document ranking with BERT' and is sometimes referred to as monoBERT."*

**The classification-problem framing:**

> *"This formulation of search as relevance scoring basically boils down to being a classification problem. Given those inputs, the model outputs a score from 0–1 where 0 is irrelevant and 1 is highly relevant. This should be familiar from our classification discussions in Chapter 4."* — Ch 8

Ch 8 explicitly back-references [[hands-on-llm-ch04-text-classification|Ch 4]] — the same supervised-classification-head pattern that powered [[TwitterRoBERTa]] for sentiment now powers monoBERT for relevance.

### Worked managed-API receipt

```python
# Single-stage: rerank all 15 documents
results = co.rerank(query=query, documents=texts, top_n=3, return_documents=True)
# Two-stage: BM25 first stage → rerank top 10 → return top 3
bm25_hits = bm25.get_scores(...)
docs = [texts[hit['corpus_id']] for hit in bm25_hits]
results = co.rerank(query=query, documents=docs, top_n=top_k, return_documents=True)
```

See [[CohereRerank]] for the full primitive.

### Open-source path

Ch 8 names [[SentenceTransformers]] as the open-source alternative: *"If you want to locally set up retrieval and reranking on your own machine, then you can use the Sentence Transformers library."* The library's *"Retrieve & Re-Rank"* documentation section is the canonical reference; common rerankers include `cross-encoder/ms-marco-MiniLM-L-6-v2` and [[BAAI]]'s `bge-reranker-base`.
