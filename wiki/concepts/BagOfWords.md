---
title: "Bag-of-Words"
type: concept
tags: [nlp, representation, pre-neural, sparse, foundational]
sources: [hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Bag-of-Words

A classical, pre-neural technique for representing unstructured text as a fixed-dimensional numerical vector. First mentioned around the 1950s; popularized in the 2000s as the dominant text-vectorization scheme for [[NLP|NLP]] classification and retrieval before dense word embeddings ([[Word2Vec|word2vec]], 2013) displaced it for representation learning.

## Construction (per *Hands-On LLMs* Ch 1)

1. **[[Tokenization|Tokenize]]** the input text — *"the process of splitting up the sentences into individual words or subwords (tokens)."* The simplest method is whitespace splitting; the chapter notes that *"some languages, like Mandarin, do not have whitespaces around individual words"* — a foundational motivation for subword tokenization.
2. **Build a vocabulary** — the union of all unique tokens across the corpus.
3. **Vectorize each document** — for each document, count how often each vocabulary word appears, producing a vector whose length equals the vocabulary size and whose entries are token counts. *"As a result, a bag-of-words model aims to create representations of text in the form of numbers, also called vectors or vector representations."*

## Properties

- **Sparse.** Most documents use a small fraction of the vocabulary → vectors are dominated by zeros.
- **Order-insensitive.** The "bag" loses positional information — *"to the bag, a sentence is nothing more than an almost literal bag of words."* Two sentences with identical word multisets but different word orders receive identical vectors.
- **Semantics-blind.** Synonyms have unrelated vectors; *"cat"* and *"feline"* score zero similarity unless they happen to share other tokens via context. This semantic blindness is the explicit motivation for [[Word2Vec|word2vec]] in the next section of Ch 1.
- **Document-level granularity.** Bag-of-words produces **document embeddings** — Ch 1's [[Embedding]] taxonomy contrasts this with word2vec's *word-level* embeddings.

## Why the book still teaches it

> "Although bag-of-words is a classic method, it is by no means completely obsolete. In Chapter 5, we will explore how it can still be used to complement more recent language models." — Ch 1

Modern uses include feature engineering for traditional ML classifiers, lightweight retrieval baselines ([[BM25|BM25]] is conceptually a weighted bag-of-words), and ensemble / fallback components in hybrid search systems.

## Variants and extensions

- **TF-IDF** — weight raw counts by inverse document frequency to deemphasize common words.
- **N-grams** — extend the vocabulary to include word bigrams / trigrams to recover some local order.
- **BM25** — probabilistic ranking function on top of TF-IDF; the canonical sparse-retrieval baseline still used in hybrid retrieval (see [[BM25]]).

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 fulfils Ch 1's forward-reference: bag-of-words is the foundation of **[[ClassBasedTFIDF|class-based TF-IDF (c-TF-IDF)]]**, the [[BERTopic]] topic-representation scheme. The chapter uses [[sklearn|scikit-learn]]'s `CountVectorizer` to build the bag-of-words representation **per cluster** (concatenating all documents in a cluster into a single mega-document) before applying the c-TF-IDF reweighting. This is the operational answer to *"how can bag-of-words still be used to complement modern language models?"* — embed for clustering, then bag-of-words for **interpretable cluster-level keyword extraction**.

## Connections

- [[Tokenization]] — the first step of bag-of-words construction.
- [[Word2Vec]] — the dense-embedding successor that addressed bag-of-words's semantic blindness.
- [[WordEmbedding]] / [[Embedding]] — the dense replacement.
- [[BM25]] — a probabilistic bag-of-words variant still used in retrieval.
- [[ClassBasedTFIDF]] — BERTopic's cluster-level bag-of-words variant.
- [[LanguageAI]] — the umbrella; bag-of-words is Ch 1's pre-neural starting point.
- [[NLP]] — the discipline that produced and used bag-of-words for decades.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 operationalizes Ch 1's forward-reference via c-TF-IDF.
