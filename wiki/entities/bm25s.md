---
title: "bm25s"
type: entity
tags: [retrieval, library, python, bm25, ir]
sources: [dspy-rl-multihop-tutorial, dspy-multihop-search-tutorial]
last_updated: 2026-05-24
---

# bm25s

Python library implementing the [[BM25]] ranking function with **sparse-matrix-backed scoring** for fast in-process retrieval over million-document corpora. Pip-installable as `pip install -U bm25s`; pairs canonically with [[PyStemmer|`PyStemmer`]] for snowball-stemmed tokenization.

## API surface (from [[dspy-rl-multihop-tutorial|this wiki's first receipt]])

```python
import bm25s, Stemmer

stemmer = Stemmer.Stemmer("english")
corpus_tokens = bm25s.tokenize(corpus, stopwords="en", stemmer=stemmer)
retriever = bm25s.BM25(k1=0.9, b=0.4)
retriever.index(corpus_tokens)

# at query time
tokens = bm25s.tokenize(query, stopwords="en", stemmer=stemmer, show_progress=False)
results, scores = retriever.retrieve(tokens, k=k, n_threads=1, show_progress=False)
```

- **`bm25s.tokenize(...)`** does lowercase + tokenize + stopword removal + optional stemming, returning token-ID matrices.
- **`bm25s.BM25(k1=..., b=...)`** constructs the ranker. The tutorial uses **`k1=0.9, b=0.4`** — looser term-frequency saturation and gentler length normalization than the BM25 defaults (`k1≈1.2, b≈0.75`).
- **`.index(corpus_tokens)`** builds the inverted index — operates in-memory on the tokenized corpus.
- **`.retrieve(tokens, k=, n_threads=)`** returns `(doc_indices, scores)` arrays.

## Position in the wiki's BM25-implementation landscape

| Library | Wiki-corpus receipt | Notes |
|---|---|---|
| **`bm25s`** | [[dspy-rl-multihop-tutorial]], [[dspy-multihop-search-tutorial]] | Pure-Python, sparse-matrix-backed, pairs with [[PyStemmer]]. Two DSPy tutorials now reuse the same `bm25s.BM25(k1=0.9, b=0.4)` + 2017 Wikipedia abstracts stack — one upstream of [[ArborGRPO]] training ([[ResearchHop]]), one upstream of [[MIPROv2]] optimization ([[Hop]]). |
| `rank_bm25.BM25Okapi` | [[hands-on-llm-ch08-semantic-search-and-rag]] | Reference Python implementation; classical IR tokenizer. |
| [[ColBERTv2]] | [[dspy-tutorial-rag-as-agent]] / [[dspy-custom-module]] | Not BM25 — dense late-interaction; named here for retriever-family contrast. |
| [[Elasticsearch]] / [[Lucene]] | [[ai-engineering-ch06-rag-agents]] | Production-grade BM25 implementations. |

`bm25s` is the **lightweight in-process choice** for tutorial-scale retrieval — no Elasticsearch / Qdrant / Lucene server required, indexing happens in Python at import time. The tradeoff is that the index must fit in process memory (5M Wikipedia abstracts in the tutorial fits comfortably). The two DSPy receipts share the same retriever config (`k1=0.9, b=0.4`, English stemmer, 2017 Wikipedia snapshot) but pair it with **opposite optimizer families** (prompt-space [[MIPROv2]] vs weight-space [[ArborGRPO]]) — strong evidence that `bm25s` is the default DSPy lightweight retrieval substrate, optimizer-agnostic.

## Connections

- [[BM25]] — the ranking function this library implements.
- [[PyStemmer]] — paired tokenization helper.
- [[dspy-rl-multihop-tutorial]] — first wiki receipt; pairs `bm25s` with [[ArborGRPO]] RL training over [[ResearchHop]].
- [[dspy-multihop-search-tutorial]] — second wiki receipt; pairs `bm25s` with [[MIPROv2]] prompt-optimization over [[Hop]].
- [[DSPy]] — host framework in both receipts.
- [[ArborGRPO]] / [[MIPROv2]] — the two DSPy optimizers shown using the bm25s retriever as a frozen retrieval substrate.
- [[HoVer]] — the benchmark indexed against.
- [[wiki.abstracts.2017]] — the 5M-doc corpus indexed in the tutorial.
- [[ColBERTv2]] — alternative DSPy retriever (dense, hosted) used in prior DSPy retrieval tutorials.
