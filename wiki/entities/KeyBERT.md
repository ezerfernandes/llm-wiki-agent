---
title: "KeyBERT"
type: entity
tags: [library, python, nlp, keyword-extraction, embeddings, grootendorst]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# KeyBERT

Open-source Python package by [[MaartenGrootendorst|Maarten Grootendorst]] (2020) for **keyword and keyphrase extraction** using [[bert|BERT]]-style embeddings. Repository: `MaartenGr/KeyBERT`. Installable as `pip install keybert`. The methodology behind [[BERTopic]]'s [[KeyBERTInspired]] representation model.

## Algorithm

1. Embed the input document with a sentence-transformer.
2. Embed candidate phrases (e.g., n-grams extracted via [[BagOfWords|bag-of-words]] with a `CountVectorizer`).
3. Rank candidates by **cosine similarity** to the document embedding.
4. Optionally apply [[MaximalMarginalRelevance|MMR]] to diversify the top-K keywords.

## Quote (per *Hands-On LLMs* Ch 5)

*"KeyBERT extracts keywords from texts by comparing word and document embeddings through cosine similarity."* — Ch 5

## API sketch

```python
from keybert import KeyBERT
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), top_n=5)
```

## Why KeyBERT matters in the LLM stack

KeyBERT operationalizes the **embedding-as-substrate** thesis Ch 4 + Ch 5 develop: by embedding both documents and candidate keywords into a shared space, **keyword extraction becomes a cosine-similarity ranking problem** with no need for parser-based or syntactic-rule keyword extractors.

Same trick as:
- [[ZeroShotClassification|Zero-shot classification with label embeddings]] (Ch 4) — embed both documents and label descriptions.
- [[ZeroShotTopicModeling|Zero-shot topic modeling]] (Ch 5) — embed both documents and predefined topic names.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 primary mention.
- [[KeyBERTInspired]] — the BERTopic representation model inspired by KeyBERT.
- [[MaartenGrootendorst]] — author.
- [[CosineSimilarity]] — the underlying similarity metric.
- [[SentenceTransformers]] / [[Embedding]] — the embedding backbone.
- [[MaximalMarginalRelevance]] — the standard diversity step.
- [[BERTopic]] — companion package.
