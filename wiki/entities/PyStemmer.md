---
title: "PyStemmer"
type: entity
tags: [tokenization, ir, library, python, stemming]
sources: [dspy-rl-multihop-tutorial, dspy-multihop-search-tutorial]
last_updated: 2026-05-24
---

# PyStemmer

Python bindings to the **Snowball stemmer** family (Porter / Porter2 / Lancaster / Krovetz and language-specific stemmers). Imported as `Stemmer`; instantiated per-language: `Stemmer.Stemmer("english")`. C-backed for speed — the canonical low-cost stemmer paired with [[bm25s]] in lightweight in-process BM25 retrieval.

## API surface (from [[dspy-rl-multihop-tutorial|this wiki's first receipt]])

```python
import Stemmer
stemmer = Stemmer.Stemmer("english")
corpus_tokens = bm25s.tokenize(corpus, stopwords="en", stemmer=stemmer)
```

`Stemmer.Stemmer(language)` constructs a stemmer object; passed by reference into the tokenizer of choice ([[bm25s|`bm25s.tokenize`]] here). The stemmer reduces inflectional forms (`running → run`, `houses → house`) so that surface-form mismatches between query and document tokens don't drop the BM25 score.

## Position in the IR-tokenization landscape

| Component | Role |
|---|---|
| Lowercasing | Normalize case. |
| Tokenization | Split text into tokens. |
| Stopword removal | Drop high-frequency, low-information words. |
| **Stemming (PyStemmer)** | **Map inflected forms to a common base.** |
| Punctuation stripping | Remove non-alphanumeric tokens. |

The full pipeline is what [[bm25s|`bm25s.tokenize(corpus, stopwords="en", stemmer=Stemmer.Stemmer("english"))`]] does in one call.

## Connections

- [[bm25s]] — primary pairing.
- [[BM25]] — the ranking function PyStemmer-tokenized corpora are scored under.
- [[StopWord]] — sibling preprocessing step.
- [[Lemmatization]] — alternative normalization (full dictionary lookup rather than algorithmic rule application).
- [[dspy-rl-multihop-tutorial]] — first wiki receipt; paired with [[ArborGRPO]] / [[ResearchHop]].
- [[dspy-multihop-search-tutorial]] — second wiki receipt; paired with [[MIPROv2]] / [[Hop]] (same English-stemmer config).
- [[hands-on-llm-ch08-semantic-search-and-rag]] — sibling BM25 receipt using a different tokenizer (sklearn stopwords + punctuation strip, no stemmer).
