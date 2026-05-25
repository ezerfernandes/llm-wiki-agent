---
title: "CoreNLP"
type: entity
tags: [tool, nlp, java, stanford, tokenization]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# CoreNLP

**Stanford CoreNLP** is the Stanford NLP Group's Java-based natural-language processing toolkit — named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[NLTK]] and [[spaCy]] as a classical NLP package providing **tokenization** for [[TermBasedRetrieval|term-based retrieval]] preprocessing.

## Position relative to [[NLTK]] and [[spaCy]]

| Library | Language | Strength |
|---|---|---|
| [[NLTK]] | Python | Educational; broad |
| [[spaCy]] | Python | Production; fast |
| **CoreNLP** | Java (Python bindings) | Deep linguistic features; Stanford-grade |

CoreNLP is the closest of the three to a **classical-NLP research toolkit**: rich coreference resolution, parsing, named-entity recognition. For pure-tokenization preprocessing the lighter [[spaCy]] is usually preferred; CoreNLP is chosen when downstream linguistic analysis is needed too.

## Connections

- [[NLTK]] / [[spaCy]] — peer NLP libraries.
- [[stanforduniversity]] — institutional home.
- [[TermBasedRetrieval]] — the retrieval family CoreNLP's tokenizers preprocess for.
- [[Tokenization]] — the core operation.
- [[ai-engineering-ch06-rag-agents]] — primary source.
