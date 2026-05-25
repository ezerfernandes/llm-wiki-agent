---
title: "TF-IDF"
type: concept
tags: [retrieval, search, ir, rag]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# TF-IDF

**TF-IDF** (Term Frequency × Inverse Document Frequency) is the foundational [[TermBasedRetrieval|term-based retrieval]] scoring function: a document's relevance to a query is the sum, over each query term, of (a) how often the term appears in the document and (b) how rare the term is across the corpus.

## The two ingredients

- **Term Frequency (TF)**: `f(t, D)` — count of term `t` in document `D`. *"The more a term appears in a document, the more relevant this document is to this term."*
- **Inverse Document Frequency (IDF)**: `IDF(t) = log(N / C(t))` where `N` is the total document count and `C(t)` is the number of documents containing `t`. *"The more documents contain a term, the less informative this term is."* In a 10-document corpus where 5 contain the term, `IDF = 10/5 = 2`.

## The score

For query `Q` with terms `t_1, ..., t_q`:

$$\text{Score}(D, Q) = \sum_{i=1}^{q} \text{IDF}(t_i) \times f(t_i, D)$$

## Why stop words and *for*, *at*, *the* are penalized

Common words appear in almost every document → their `C(t) ≈ N` → `IDF ≈ log(1) = 0`. They contribute nothing to the score. *"You want to focus on more informative terms like vietnamese and recipes, not for and at."*

## Why naive TF-IDF was generalized to [[BM25]]

Naive TF-IDF lets term frequency grow unboundedly with document length — a 10,000-word document is more likely to mention any given term than a 100-word document. [[BM25]] fixes this by **saturating term frequency** (the `k1` parameter) and **normalizing by document length** (the `b` parameter), which is why BM25 is the production default and naive TF-IDF is mostly historical.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 endorses **TF-IDF + [[LogisticRegression|logistic regression]]** as the **classical baseline** every modern LLM-based classifier should be compared against: *"it is highly advised to compare these examples against classic, but strong baselines such as representing text with TF-IDF and training a logistic regression classifier on top of that."* The chapter does not run this baseline itself but recommends it as the discipline-setting comparison.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 introduces the **class-based variant** of TF-IDF — see [[ClassBasedTFIDF|c-TF-IDF]]. Where classical TF-IDF computes the score for a `(document, term)` pair, c-TF-IDF computes the score for a `(cluster, term)` pair: term frequency is summed **across all documents in the cluster**, and IDF is computed across **clusters** rather than across documents. The IDF formula sketched in Ch 5: *"the logarithm of the average frequency of all words across all clusters divided by the total frequency of each word."* This is a different application surface from Ch 6 RAG retrieval — Ch 5 uses c-TF-IDF for **topic representation** in [[BERTopic]] rather than document retrieval.

## Connections

- [[BM25]] — the saturating, length-normalized successor.
- [[ClassBasedTFIDF]] — the per-cluster variant used by BERTopic.
- [[TermBasedRetrieval]] — the family TF-IDF anchors.
- [[InvertedIndex]] — the data structure that makes TF-IDF tractable at scale.
- [[Elasticsearch]] — production system.
- [[rag]] — the modern application surface.
- [[BagOfWords]] — the underlying representation.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch04-text-classification]] — TF-IDF + logistic-regression baseline recommendation.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 introduces the class-based variant.
