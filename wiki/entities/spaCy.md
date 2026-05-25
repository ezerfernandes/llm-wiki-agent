---
title: "spaCy"
type: entity
tags: [tool, nlp, python, tokenization]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# spaCy

**spaCy** is a popular open-source Python NLP library — named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[NLTK]] and [[CoreNLP]] as a classical NLP package that offers **tokenization** functionalities for [[TermBasedRetrieval|term-based retrieval]] preprocessing.

## Position relative to [[NLTK]] and [[CoreNLP]]

| Library | Language | Strength |
|---|---|---|
| [[NLTK]] | Python | Educational; broad coverage; slower |
| **spaCy** | Python | Production-oriented; fast; modern API |
| [[CoreNLP]] | Java (Python bindings) | Stanford-developed; deep linguistic features |

For RAG / term-based-retrieval preprocessing — lowercasing, punctuation removal, stop-word elimination, n-gram detection — spaCy is the production default in modern Python pipelines.

## Connections

- [[NLTK]] / [[CoreNLP]] — peer NLP libraries.
- [[TermBasedRetrieval]] — the retrieval family spaCy's tokenizers preprocess for.
- [[Tokenization]] — the core operation.
- [[ai-engineering-ch06-rag-agents]] — primary source.
