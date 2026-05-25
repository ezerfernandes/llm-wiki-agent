---
title: "Class-Based TF-IDF (c-TF-IDF)"
type: concept
tags: [bag-of-words, tf-idf, topic-modeling, bertopic]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Class-Based TF-IDF (c-TF-IDF)

**Class-based TF-IDF (c-TF-IDF)** is the topic-keyword weighting scheme at the heart of [[BERTopic]] ([[2203.05794-bertopic|Grootendorst 2022]]). It reframes classical [[TFIDF|TF-IDF]] — designed to score *documents* against a *query* — for the topic-modeling setting where we want to score *words* against a *cluster of documents*.

## The reframing

Classical [[TFIDF|TF-IDF]] operates **per document**:
- **TF** = frequency of term `t` in document `D`.
- **IDF** = log-ratio of total documents to documents containing `t`.

c-TF-IDF operates **per cluster** (treating each cluster as if it were a single mega-document):
- **c-TF** = frequency of term `t` in cluster `C` (concatenate all documents in `C` and count tokens).
- **IDF** = *"calculated by taking the logarithm of the average frequency of all words across all clusters divided by the total frequency of each word."* (per Ch 5)

Each term's c-TF in a cluster is multiplied by this cross-cluster IDF, giving each term a **c-TF-IDF score per cluster** — high scores indicate terms that are **frequent inside the cluster** but **rare across other clusters**.

## What c-TF-IDF achieves (per *Hands-On LLMs* Ch 5)

*"BERTopic uses a class-based variant of term frequency–inverse document frequency (c-TF-IDF) to put more weight on words that are more meaningful to a cluster and put less weight on words that are used across all clusters."*

The IDF reweighting **downweights stopwords** (*"the"*, *"of"*, *"and"* — appear in every cluster) and **domain-spanning vocabulary** (*"model"*, *"data"*, *"paper"* in an NLP corpus — appear in every cluster) without an explicit stopword list. It **upweights cluster-distinguishing terms** (*"asr"* / *"acoustic"* for the speech recognition cluster, *"nmt"* / *"bleu"* for the neural machine translation cluster).

## Implementation

BERTopic uses [[sklearn|scikit-learn]]'s `CountVectorizer` to compute the bag-of-words representation per cluster, then applies the cross-cluster IDF reweighting. *"Each cluster is considered a topic that has a specific ranking of the corpus's vocabulary."*

## Why c-TF-IDF beats LDA on modern data

[[LatentDirichletAllocation|LDA]] uses bag-of-words for **both topic discovery and topic representation** — and topic discovery is where bag-of-words is weakest (synonyms get treated as orthogonal, context is lost). [[BERTopic]] uses **Transformer embeddings** for topic discovery (capturing semantic similarity) and **only uses bag-of-words for topic representation** (where its interpretability shines). c-TF-IDF is the **bridge** between the two — it lets BERTopic surface human-readable keyword lists per cluster while the cluster boundaries themselves come from embedding-space density.

## Decoupling property

A major architectural consequence: *"with c-TF-IDF, we are not dependent on the models used in clustering the documents."* The c-TF-IDF representation can be computed for **any** clustering — change the embedding model, change UMAP parameters, change HDBSCAN parameters, and c-TF-IDF still produces interpretable topic keywords on the resulting clusters.

## Example output

For the [[ArXivNLP|ArXiv NLP]] dataset, topic 0's top c-TF-IDF terms:

```
('speech', 0.028), ('asr', 0.019), ('recognition', 0.013), ('end', 0.010),
('acoustic', 0.009), ('speaker', 0.007), ('audio', 0.007), ('the', 0.006),
('error', 0.006), ('automatic', 0.006)
```

Note that *"the"* still appears with a non-zero weight — c-TF-IDF reduces but does not eliminate stopword presence. [[KeyBERTInspired]] and [[MaximalMarginalRelevance|MMR]] representation models (see [[BERTopic]]) further clean these up.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[2203.05794-bertopic]] — the original BERTopic paper.
- [[TFIDF]] — the classical TF-IDF this generalizes.
- [[BagOfWords]] / [[BERTopic]] — the dependency stack.
- [[sklearn]] / `CountVectorizer` — the implementation primitive.
- [[KeyBERTInspired]] / [[MaximalMarginalRelevance]] — representation models that refine c-TF-IDF's output.
- [[LatentDirichletAllocation]] — the classical-era alternative to c-TF-IDF for topic representation.
- [[MaartenGrootendorst]] — the author of c-TF-IDF + BERTopic.
