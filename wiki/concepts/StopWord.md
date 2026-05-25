---
title: "Stop Word"
type: concept
tags: [tokenization, ir, retrieval, bm25, text-processing]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Stop Word

**Stop words** are high-frequency function words (*"the"*, *"a"*, *"is"*, *"of"*, *"and"*, *"to"*) that carry little discriminative information for retrieval and are **removed during tokenization** for sparse / lexical retrievers like [[BM25]].

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8's BM25 worked example shows stop-word removal explicitly:

```python
from sklearn.feature_extraction import _stop_words
import string

def bm25_tokenizer(text):
    tokenized_doc = []
    for token in text.lower().split():
        token = token.strip(string.punctuation)
        if len(token) > 0 and token not in _stop_words.ENGLISH_STOP_WORDS:
            tokenized_doc.append(token)
    return tokenized_doc
```

The four operations in the tokenizer are the classical IR pipeline:

1. **Lowercase** (`text.lower()`) — normalize case.
2. **Tokenize** (`.split()`) — whitespace tokenization.
3. **Strip punctuation** (`token.strip(string.punctuation)`).
4. **Remove stop words** (`token not in ENGLISH_STOP_WORDS`).

Without stop-word removal, [[BM25]] would over-weight matches on frequent low-information terms and produce noisier rankings.

## Position in the IR pipeline

Stop-word removal sits in the **tokenization** layer of [[SparseRetrieval|sparse retrieval]] / [[TermBasedRetrieval|term-based retrieval]]:

| Stage | Operation |
|---|---|
| Lowercase | Reduce case variance |
| Strip punctuation | Reduce surface variance |
| **Stop-word removal** | **Remove low-IDF terms** |
| Stem / lemmatize | Reduce morphological variance (optional) |
| BM25 / TF-IDF scoring | Compute query-document similarity |

[[DenseRetrieval|Dense retrieval]] does **not** typically remove stop words — the embedding model has learned which tokens carry signal, and stop-word removal would break the model's pretraining-time tokenization assumptions.

## The stop-word lists

There is no single canonical stop-word list. Common choices:

- **sklearn's `ENGLISH_STOP_WORDS`** — Ch 8's worked example uses this (318 words).
- **NLTK's `english` stopwords** — different word list (179 words).
- **spaCy's stop words** — yet another list (326 words).
- **Lucene / Elasticsearch's `_english_`** — production default for many search engines.

The differences matter at the margin (some lists include *"would"* and *"could"*, some don't; some include *"film"* in domain-specific lists). For research it's worth being explicit about which list is in use.

## When to skip stop-word removal

- **Phrase queries** — *"to be or not to be"* loses all signal if stop words are removed.
- **Code search** — *"this"*, *"new"*, *"return"* are semantically loaded in code; the stop-word list should not be the English natural-language list.
- **Dense retrieval** — as noted above.

## Connections

- [[BM25]] — the canonical sparse retriever Ch 8 demonstrates with stop-word removal.
- [[TFIDF]] — the term-frequency scorer that benefits from stop-word removal.
- [[Tokenization]] — the parent operation.
- [[sklearn]] — the library Ch 8's worked example uses.
- [[SparseRetrieval]] / [[TermBasedRetrieval]] — the retrieval family.
- [[DenseRetrieval]] — the complementary family that does not remove stop words.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
