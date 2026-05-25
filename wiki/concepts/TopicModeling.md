---
title: "Topic Modeling"
type: concept
tags: [unsupervised, nlp, topic-modeling, llm]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Topic Modeling

**Topic modeling** is the unsupervised discovery of **abstract themes ("topics")** in a corpus, *"where we want to discover (abstract) topics that appear in large collections of textual data."* A topic is traditionally represented by a ranked list of **keywords / keyphrases** (and, ideally, a single short label).

## Two eras

### Classical era — [[LatentDirichletAllocation|LDA]] (Blei, Ng & Jordan 2003)

Treats each topic as a **probability distribution over the vocabulary**. Operates on **bag-of-words features alone** — *"these approaches generally use a bag-of-words technique for the main features of the textual data, which does not take the context nor the meaning of words and phrases into account."* Each word in the vocabulary is scored against its relevance to each topic.

### Modern era — [[BERTopic]] (Grootendorst 2022)

Combines **embedding-based clustering** ([[TextClustering|sentence-transformers + UMAP + HDBSCAN]]) with **bag-of-words topic representation** ([[ClassBasedTFIDF|c-TF-IDF]]). The semantic / contextual signal from Transformer embeddings drives the **topic discovery** step; the bag-of-words representation drives the **topic explanation** step.

## The two stages of modern topic modeling (per *Hands-On LLMs* Ch 5)

[[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]] frames any modern topic model as:

1. **Find clusters of semantically similar documents** (the [[TextClustering|text-clustering pipeline]]).
2. **Represent each cluster as a topic** — extract keywords, optionally rerank via representation models, optionally generate short labels via LLMs.

A topic is the second stage's output: a ranked keyword list (e.g., `topic, topics, lda, latent, dirichlet` → *"topic modeling"*), optionally augmented with a short generative label (e.g., *"Advancements in Aspect-Based Sentiment Analysis"*).

## Variants supported by BERTopic

Ch 5 lists the algorithmic variants BERTopic supports on the same modular base:

- **[[GuidedTopicModeling|Guided topic modeling]]** — seed topics with anchor words.
- **[[SemiSupervisedTopicModeling|(Semi-)supervised topic modeling]]** — use partial labels.
- **[[HierarchicalTopicModeling|Hierarchical topic modeling]]** — topics organized as a tree.
- **[[DynamicTopicModeling|Dynamic topic modeling]]** — track topics over time.
- **[[MultimodalTopicModeling|Multimodal topic modeling]]** — text + images / audio.
- **Multi-aspect topic modeling** — multiple representations per topic.
- **[[OnlineTopicModeling|Online / incremental topic modeling]]** — stream updates.
- **[[ZeroShotTopicModeling|Zero-shot topic modeling]]** — match documents to predefined topic names.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[TextClustering]] — the input pipeline.
- [[BERTopic]] — the modern modular framework.
- [[LatentDirichletAllocation]] — the classical bag-of-words baseline.
- [[ClassBasedTFIDF]] — BERTopic's topic-keyword weighting.
- [[KeyBERTInspired]] / [[MaximalMarginalRelevance]] / [[GenerativeTopicLabeling]] — BERTopic's representation refinements.
- [[BagOfWords]] / [[TFIDF]] — the classical text-feature stack.
- [[Gensim]] — the canonical Python library for classical LDA.
- [[UnsupervisedLearning]] — parent paradigm.
- [[MaartenGrootendorst]] — BERTopic's author.
