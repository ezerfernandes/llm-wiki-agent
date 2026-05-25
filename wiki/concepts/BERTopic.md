---
title: "BERTopic"
type: concept
tags: [topic-modeling, clustering, embeddings, nlp, llm, framework, bertopic]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# BERTopic

**BERTopic** is a **modular topic-modeling framework** ([[2203.05794-bertopic|Grootendorst 2022, arXiv:2203.05794]]) authored by [[MaartenGrootendorst]] himself — the co-author of *Hands-On LLMs* and the flagship tool of [[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]. BERTopic combines **embedding-based clustering** with **class-based [[TFIDF|TF-IDF]] (c-TF-IDF)** topic representation; its central architectural commitment is **swappability** — *"You can think of this modularity as building with Lego blocks; each part of the pipeline is completely replaceable with another, similar algorithm."*

> Note: although the file is named `BERTopic.md` (matching the framework's own capitalization), it is a `concept` page describing the technique. BERTopic the Python package is also tracked as an entity at [[entities/BERTopic]].

## The two-stage pipeline

**Stage 1 — Clustering** (the [[TextClustering|text-clustering pipeline]]):
1. **Embed** documents with a [[SentenceTransformers|sentence-transformers]] model (default; replaceable). Ch 5 uses `thenlper/gte-small` (384-dim).
2. **Reduce dimensionality** with [[UMAP]] (default; replaceable with [[PCA]]). Ch 5: 384 → 5 dimensions.
3. **Cluster** with [[HDBSCAN]] (default; replaceable with [[KMeansClustering|k-means]]). Ch 5: `min_cluster_size=50`, `metric='euclidean'`, `cluster_selection_method='eom'` → 156 clusters + outlier bucket.

**Stage 2 — Topic representation**:
4. **Bag-of-words per cluster** via [[sklearn|scikit-learn]]'s `CountVectorizer` (concatenate documents in each cluster, count tokens).
5. **[[ClassBasedTFIDF|c-TF-IDF weighting]]** — reweight cluster-level term frequency by an IDF computed across clusters. Words frequent in one cluster but rare across clusters get high weight; cluster-spanning words (stopwords, generic domain vocab) get downweighted.

The result: each cluster becomes a **topic ranked by c-TF-IDF-weighted keywords**.

## Why modularity matters

Because the two stages are **largely independent** — *"with c-TF-IDF, we are not dependent on the models used in clustering the documents"* — any component can be swapped without re-running the others:

- **Don't want outliers?** Swap HDBSCAN for k-means.
- **Embedding model too slow?** Swap `gte-small` for any model in the [[MTEB]] catalog.
- **Want hierarchical topics?** Layer hierarchical merging on top of stage 1.
- **Want LLM-generated topic labels?** Add a [[GenerativeTopicLabeling|text-generation representation block]] after stage 2.

## Representation models (stage-2.5 reranking)

BERTopic's **representation models** are reranking blocks that operate on top of c-TF-IDF's initial keyword distribution. They run **once per topic** — not once per document — making them efficient at scale. *"If we have millions of documents and a hundred topics, the representation block only needs to be applied once for every topic instead of for every document."*

Three families demonstrated in Ch 5:

- **[[KeyBERTInspired]]** — embed candidate keywords, compute the average document embedding per topic, rerank keywords by cosine similarity. Modeled after [[KeyBERT]]. Strength: removes nearly all stopwords. Weakness: drops domain abbreviations the embedding model can't represent (e.g., *"nmt"* for neural machine translation).
- **[[MaximalMarginalRelevance|MMR]]** — iteratively select keywords that are **diverse from already-chosen keywords yet relevant to the topic**, controlled by a `diversity` parameter. Removes redundancy (e.g., *"summary"* / *"summaries"* / *"summarization"* → keep one).
- **[[GenerativeTopicLabeling|Generative text labeling]]** — prompt an LLM with `[DOCUMENTS]` (top 4 most-representative documents) + `[KEYWORDS]` (top c-TF-IDF keywords) → emit a short natural-language label. Demonstrated with [[FLANT5|Flan-T5-small]] (local) and [[ChatGPT|GPT-3.5-turbo]] (OpenAI API).

Multiple representation models can be **stacked or run side by side** to give multiple perspectives on the same topic.

## Output API

```python
from bertopic import BERTopic
topic_model = BERTopic(
    embedding_model=embedding_model, umap_model=umap_model,
    hdbscan_model=hdbscan_model, verbose=True
).fit(abstracts, embeddings)

topic_model.get_topic_info()                # per-topic table: ID, Count, Name, Representation
topic_model.get_topic(0)                    # ranked keywords with c-TF-IDF weights for topic 0
topic_model.find_topics("topic modeling")   # search topics by query (returns IDs + similarities)
topic_model.topics_[doc_index]              # the topic assigned to a specific document
topic_model.update_topics(docs, representation_model=...)  # rerun stage 2 with a different rep model
topic_model.reduce_outliers(...)            # reassign HDBSCAN's -1 outliers to topics
```

## Algorithmic variants

BERTopic supports many variants on the same modular base — see [[TopicModeling]] for the full list. The variants share stages 1–2 and customize stage 2+ (hierarchical merging, time-bucketing for dynamic topic modeling, anchor words for guided modeling, etc.).

## On the ArXiv NLP dataset

Ch 5's worked example: 44,949 cs.CL abstracts (1991–2024) from [[ArXivNLP|`maartengr/arxiv_nlp`]]. Selected topics:

| Topic | Count | Top Keywords | Theme |
|---|---|---|---|
| -1 | 14,520 | the, of, and, to | Outliers |
| 0 | 2,290 | speech, asr, recognition, end | Automatic speech recognition |
| 3 | 986 | translation, nmt, machine, neural | Neural machine translation |
| 22 | — | topic, topics, lda, latent, dirichlet | Topic modeling (where the BERTopic paper itself is filed) |
| 151 | 54 | prompt, prompts, optimization, prompting | Prompt engineering |
| 154 | 50 | backdoor, attacks, triggers | Adversarial attacks |

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[2203.05794-bertopic]] — the original paper.
- [[MaartenGrootendorst]] — BERTopic's author.
- [[TextClustering]] / [[TopicModeling]] — what BERTopic does.
- [[ClassBasedTFIDF]] — BERTopic's topic-representation weighting.
- [[KeyBERTInspired]] / [[MaximalMarginalRelevance]] / [[GenerativeTopicLabeling]] — representation blocks.
- [[KeyBERT]] — the keyword-extraction package KeyBERTInspired is based on.
- [[UMAP]] / [[HDBSCAN]] / [[SentenceTransformers]] / [[sklearn]] — the default pipeline components.
- [[LatentDirichletAllocation]] — the classical baseline contrasted with BERTopic.
- [[Plotly]] / [[Datamapplot]] / [[matplotlib]] — visualization libraries used.
- [[ReRanking]] — the abstraction representation models embody.
- [[ArXivNLP]] — Ch 5's worked dataset.
