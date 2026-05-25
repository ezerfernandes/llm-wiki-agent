---
title: "Term-Based Retrieval"
type: concept
tags: [retrieval, search, ir, rag]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Term-Based Retrieval

**Term-based retrieval** (a.k.a. *lexical retrieval*) is the family of [[rag|RAG]] retrieval algorithms that score documents by **the occurrence and frequency of query terms in each document**, rather than by semantic similarity. The canonical members are [[TFIDF|TF-IDF]] and [[BM25]]; the canonical production system is [[Elasticsearch]] over a [[Lucene]] [[InvertedIndex|inverted index]].

## Why "term-based" instead of "sparse"

[[ChipHuyen|Huyen]] in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] explicitly rejects the literature's *sparse vs dense* division in favor of *term-based vs embedding-based*. The reason is [[SPLADE]] (Formal et al. 2021): SPLADE produces **sparse** embeddings (regularized to push most BERT-embedding values to 0), but its operations, strengths, and weaknesses match dense [[EmbeddingBasedRetrieval|embedding-based retrieval]] rather than term-based retrieval. *"Term-based versus embedding-based division avoids this miscategorization."*

## Strengths and weaknesses

| Dimension | Term-based |
|---|---|
| Query speed | Much faster than [[EmbeddingBasedRetrieval|embedding-based]] |
| Out-of-the-box performance | Strong baseline — [[AravindSrinivas]] (Perplexity CEO): *"Making a genuine improvement over BM25 or full-text search is hard."* |
| Failure mode | Term ambiguity — querying *"transformer architecture"* returns documents about the electric device or the movie |
| Cost | Much cheaper — no embedding generation, simpler index storage |
| Improvement headroom | Limited — *"fewer components you can tweak"* |

## Tokenization is non-trivial

Term-based retrieval's hidden subtlety is **tokenization** — multi-word terms like *"hot dog"* lose meaning if split into individual words. Mitigations: treat common n-grams as terms; lowercase; remove punctuation; eliminate stop words. Classical NLP packages ([[NLTK]], [[spaCy]], [[CoreNLP]]) ship these tokenization functions; modern term-based solutions like [[Elasticsearch]] handle them automatically.

## Connections

- [[rag]] — the application family term-based retrieval serves.
- [[BM25]] — the dominant term-based scorer.
- [[TFIDF]] — the foundational scorer BM25 generalizes.
- [[InvertedIndex]] — the data structure term-based retrieval queries against.
- [[Elasticsearch]] / [[Lucene]] — canonical implementations.
- [[EmbeddingBasedRetrieval]] — the semantic-search alternative.
- [[HybridSearch]] — combines term-based and embedding-based; production standard.
- [[SPLADE]] — the *sparse-embedding* counterexample that motivates Huyen's term-vs-embedding division.
- [[ai-engineering-ch06-rag-agents]] — primary source for Huyen's framing.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 uses the informal *"keyword search"* / *"lexical search"* vocabulary for the same family.
- [[SparseRetrieval]] — the wiki's Ch 8-aliased page (sparse-vs-dense framing).

## Vocabulary note

The same architectural family has **two concept pages** in the wiki — each named for a different framing tradition:

| Page | Framing | Source |
|---|---|---|
| **[[TermBasedRetrieval]]** (this page) | Term-vs-embedding | [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] |
| **[[SparseRetrieval]]** | Sparse-vs-dense vector geometry | [[hands-on-llm-ch08-semantic-search-and-rag|Ch 8]] |

Huyen explicitly prefers the term-vs-embedding division because [[SPLADE]] produces sparse-but-semantic embeddings that don't fit cleanly into sparse-vs-dense; Ch 8 uses the simpler sparse-vs-dense informally. The two pages back-link to each other for resolution clarity.
