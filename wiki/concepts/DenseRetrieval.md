---
title: "Dense Retrieval"
type: concept
tags: [retrieval, search, rag, embeddings, vector-search, semantic-search]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Dense Retrieval

**Dense retrieval** is the [[rag|RAG]] / search-pipeline family that **embeds both queries and documents into a shared dense vector space and returns the documents whose embeddings are nearest to the query embedding** in that space. Ch 8 of *Hands-On LLMs* uses *"dense retrieval"* as the canonical name; the same family is called [[EmbeddingBasedRetrieval|embedding-based retrieval]] (per [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]) or [[SemanticSearch|semantic search]] (the user-facing name). The three names point at the same architectural family.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names dense retrieval as **the first of the three categories of LLM-augmented search** (alongside [[ReRanking|reranking]] and [[rag|RAG]]):

> *"Dense retrieval systems rely on the concept of embeddings, the same concept we've encountered in the previous chapters, and turn the search problem into retrieving the nearest neighbors of the search query (after both the query and the documents are converted into embeddings)."*

The worked example is the **15-sentence Wikipedia article on the film *Interstellar*** embedded via [[Cohere]] `co.embed(input_type="search_document")` (4,096-dim vectors), indexed via [[FAISS|`faiss.IndexFlatL2`]], and queried via `co.embed(input_type="search_query")` + `index.search(query_embed, k)`. On query *"how precise was the science"*, the system correctly returns *"It has also received praise from many astronomers for its scientific accuracy and portrayal of theoretical astrophysics"* as the top hit — **a result no keyword search can produce** because the correct sentence shares no words with the query.

## The dense-vs-sparse contrast

Ch 8's canonical demonstration runs **dense retrieval and [[BM25|BM25]] side-by-side on the same corpus** to show the failure modes of pure keyword search. On *"how precise was the science"*:

| Retriever | Top result | Correct? |
|---|---|---|
| **Dense (Cohere `co.embed` + FAISS L2)** | *"praise from astronomers for scientific accuracy and ... astrophysics"* | ✓ |
| **[[BM25]] (`rank_bm25.BM25Okapi`)** | *"Interstellar is a 2014 epic science fiction film..."* | ✗ — over-weights the word *"science"* |

> *"Notice that this wouldn't have been possible if we were only doing keyword search because the top result did not include the same keywords in the query."*

## Three caveats Ch 8 names

1. **Out-of-distribution queries still return results.** *"What is the mass of the moon?"* against the *Interstellar* corpus returns the film's worldwide-gross sentence as the nearest neighbor. Mitigation: a **[[SimilarityThreshold|similarity threshold]]** to filter low-confidence retrievals.

2. **Exact-phrase matching is a [[BM25]] strength, not a dense-retrieval strength.** *"That's one reason why **hybrid search**, which includes both semantic search and keyword search, is advised instead of relying solely on dense retrieval."* This establishes [[HybridSearch|hybrid search]] as the production default.

3. **Domain transfer is hard.** *"If you train a retrieval model on internet and Wikipedia data, and then deploy it on legal texts (without having enough legal data as part of the training set), the model will not work as well in that legal domain."*

## The query-document asymmetry

Ch 8 codifies the **query-document asymmetric semantic distance**:

> *"Are a query and its best result semantically similar? Not always. This is why language models need to be trained on question-answer pairs to become better at retrieval."*

[[CohereEmbed|Cohere's `co.embed`]] API surfaces this directly via `input_type="search_document"` vs `"search_query"` — the **same model produces different embeddings** for the same string depending on whether it's a document or a query. Deferred treatment for Ch 10 (embedding-model fine-tuning).

## The chunking decision

Long documents must be **[[Chunking|chunked]]** before embedding. Ch 8's design space is the two-bucket axis:

- **One vector per document** — embed slice (title / opening) or aggregate (average chunk embeddings). Loses information.
- **Multiple vectors per document** — sentence / paragraph / overlapping / LLM-driven. Better coverage; more vectors.

See [[Chunking]] / [[ChunkingStrategy]] for the full design space.

## Connections

- [[rag]] — the application family.
- [[EmbeddingBasedRetrieval]] — the wiki's other name for the same concept (per [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]).
- [[SemanticSearch]] — the user-facing name.
- [[SparseRetrieval]] / [[TermBasedRetrieval]] / [[BM25]] — the complementary family.
- [[HybridSearch]] — the production-default combination.
- [[ReRanking]] — the standard post-step.
- [[Chunking]] / [[ChunkingStrategy]] — the load-bearing index-time decision.
- [[FAISS]] / [[Annoy]] / [[VectorDatabase]] — the storage substrate.
- [[ApproximateNearestNeighbor]] — the speed mechanism for large-scale dense retrieval.
- [[SimilarityThreshold]] — the OOD-query mitigation.
- [[CohereEmbed]] — the worked managed-API embedding endpoint in Ch 8.
- [[SentenceTransformers]] / [[BGESmallEnV15]] — the open-weights alternative.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
