---
title: "Sparse Retrieval"
type: concept
tags: [retrieval, search, rag, lexical, ir, bm25, sparse]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Sparse Retrieval

**Sparse retrieval** is the search family that scores documents by **the occurrence and frequency of query terms in each document** rather than by semantic similarity — representing documents and queries as **high-dimensional sparse term-frequency vectors** (most entries zero, one entry per vocabulary term that appears). The canonical members are [[TFIDF|TF-IDF]] and [[BM25]]; the canonical production system is [[Elasticsearch]] over a [[Lucene]] [[InvertedIndex|inverted index]].

This is the **alias [[hands-on-llm-ch08-semantic-search-and-rag|Ch 8 of *Hands-On LLMs*]] uses informally** when contrasting *"dense retrieval"* with *"keyword search"* / *"lexical search"*. The wiki keeps both vocabularies: this page is the **sparse-vs-dense framing**, [[TermBasedRetrieval]] is the **term-vs-embedding framing** [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] uses.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 runs sparse retrieval as the **direct comparison baseline** for dense retrieval on the *Interstellar* corpus, using [[BM25|`rank_bm25.BM25Okapi`]]:

```python
from rank_bm25 import BM25Okapi
from sklearn.feature_extraction import _stop_words
import string

def bm25_tokenizer(text):
    tokenized_doc = []
    for token in text.lower().split():
        token = token.strip(string.punctuation)
        if len(token) > 0 and token not in _stop_words.ENGLISH_STOP_WORDS:
            tokenized_doc.append(token)
    return tokenized_doc

tokenized_corpus = [bm25_tokenizer(passage) for passage in texts]
bm25 = BM25Okapi(tokenized_corpus)

def keyword_search(query, top_k=3, num_candidates=15):
    bm25_scores = bm25.get_scores(bm25_tokenizer(query))
    # ... ranking + return
```

On *"how precise was the science"*, BM25 returns the **wrong** answer (*"Interstellar is a 2014 epic science fiction film..."*) at rank 1 because of the surface-keyword overlap on *"science"*. This is Ch 8's canonical motivating contrast for **why dense retrieval matters when keyword search exists**.

## When sparse retrieval is the right answer

Sparse retrieval is **the production default for exact-phrase queries** — error codes, product names, technical identifiers, named entities. The dense-retrieval failure mode is *"absorbed into a continuous space where exact-match signal is lost"*; sparse retrieval is the natural complement.

This is why [[HybridSearch|hybrid search]] (sparse + dense, in sequence or in parallel) is the production-default Ch 8 advocates.

## Note on terminology

The literature is divided between:

- **Sparse vs dense** (used by Ch 8 of *Hands-On LLMs*, [[SentenceTransformers]] docs, much of the IR literature) — emphasizes the vector geometry (mostly-zero vs mostly-nonzero).
- **Term-based vs embedding-based** (used by [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]) — emphasizes the scoring mechanism. Huyen prefers this division because [[SPLADE]] produces sparse-but-semantic embeddings that don't fit the sparse-vs-dense framing.

The wiki maintains both pages so each vocabulary resolves cleanly: this page (sparse / dense) and [[TermBasedRetrieval]] (term / embedding).

## Connections

- [[TermBasedRetrieval]] — the wiki's other name for the same concept (per [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]).
- [[BM25]] — the dominant sparse-retrieval scorer.
- [[TFIDF]] — the foundational scorer BM25 generalizes.
- [[DenseRetrieval]] / [[EmbeddingBasedRetrieval]] — the complementary family.
- [[HybridSearch]] — the production-default combination.
- [[InvertedIndex]] / [[Elasticsearch]] / [[Lucene]] — canonical implementations.
- [[StopWord]] — sparse retrieval typically removes high-frequency function words during tokenization.
- [[SPLADE]] — the sparse-but-semantic counterexample that motivates Huyen's term-vs-embedding framing.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
