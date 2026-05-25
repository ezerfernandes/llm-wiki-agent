---
title: "NLTK"
type: entity
tags: [tool, nlp, python]
sources: [madewithml-mlops-preprocessing, madewithml-mlops-exploratory-data-analysis, ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# NLTK

Python natural-language toolkit. Provides stop-word lists, tokenizers, and lemmatization used during text preprocessing in [[madewithml-mlops-preprocessing]] and [[madewithml-mlops-exploratory-data-analysis]].

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 names NLTK alongside [[spaCy]] and [[CoreNLP]] as classical NLP packages that provide **tokenization functionalities** for [[TermBasedRetrieval|term-based retrieval]] preprocessing:

> *"Classical NLP packages, such as NLTK (Natural Language Toolkit), spaCy, and Stanford's CoreNLP, also offer tokenization functionalities."*

Tokenization sits at the foundation of term-based retrieval — splitting *"hot dog"* badly into *"hot"* and *"dog"* (losing the bigram meaning) is exactly the failure NLTK's n-gram-aware tokenizers help avoid. In modern Python pipelines, [[spaCy]] has largely displaced NLTK for production use, but NLTK remains the educational default and is still a common dependency in research code.
