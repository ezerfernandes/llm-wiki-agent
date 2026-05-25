---
title: "BERTopic (package)"
type: entity
tags: [library, python, topic-modeling, nlp, bertopic, grootendorst]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# BERTopic (Python package)

The open-source Python package implementing [[BERTopic|the BERTopic algorithm]] — [[MaartenGrootendorst|Maarten Grootendorst]]'s modular topic-modeling framework ([[2203.05794-bertopic|Grootendorst 2022, arXiv:2203.05794]]). Installable as `pip install bertopic`; repository: `MaartenGr/BERTopic`. The flagship tool of [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]].

## API surface

```python
from bertopic import BERTopic

topic_model = BERTopic(
    embedding_model=embedding_model,   # any sentence-transformers / custom model
    umap_model=umap_model,             # UMAP instance
    hdbscan_model=hdbscan_model,       # HDBSCAN instance (or k-means)
    verbose=True,
).fit(docs, embeddings)

topic_model.get_topic_info()           # topic table
topic_model.get_topic(topic_id)        # ranked keywords for a topic
topic_model.find_topics(query)         # semantic topic search
topic_model.update_topics(docs, representation_model=...)  # rerun rep step
topic_model.reduce_outliers(...)       # reassign -1 docs

# Visualization
topic_model.visualize_documents(titles, reduced_embeddings=...)
topic_model.visualize_barchart()
topic_model.visualize_heatmap(n_clusters=30)
topic_model.visualize_hierarchy()
topic_model.visualize_document_datamap(titles, ...)   # via datamapplot
```

## Submodules used in Ch 5

- `bertopic.representation.KeyBERTInspired` — keyword reranker.
- `bertopic.representation.MaximalMarginalRelevance` — diversity-vs-relevance keyword filter.
- `bertopic.representation.TextGeneration` — local-LLM topic labeling (e.g., Flan-T5).
- `bertopic.representation.OpenAI` — OpenAI-API topic labeling.

## Modularity in practice

Every BERTopic component is **swappable**. The pipeline tuple in Ch 5:

| Stage | Default | Replaceable with |
|---|---|---|
| Embedding | `sentence-transformers` | Any model returning vectors per doc |
| Dimensionality reduction | [[UMAP]] | [[PCA]], TruncatedSVD, no-op |
| Clustering | [[HDBSCAN]] | [[KMeansClustering|k-means]], BIRCH, online clusterers |
| Tokenization for BoW | `sklearn` `CountVectorizer` | Custom vectorizer |
| Topic-weighting | [[ClassBasedTFIDF|c-TF-IDF]] | Custom weighting |
| Representation | c-TF-IDF | [[KeyBERTInspired]], [[MaximalMarginalRelevance|MMR]], LLM, custom |

## Why BERTopic over Gensim's LDA

| | [[Gensim]] LDA | BERTopic |
|---|---|---|
| Topic discovery | Bag-of-words probabilistic | Embedding clustering |
| Captures semantic similarity | No | Yes |
| Auto-detects #topics | No (you set `K`) | Yes (HDBSCAN) |
| Outlier handling | None | Topic `-1` |
| Modularity | Limited | Lego-block |
| LLM integration | None | First-class |
| Visualization | Manual | Built-in Plotly + datamapplot |

## Connections

- [[BERTopic]] — the algorithm / framework page.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5's primary worked example.
- [[2203.05794-bertopic]] — the original paper.
- [[MaartenGrootendorst]] — author.
- [[KeyBERT]] — companion package.
- [[ClassBasedTFIDF]] / [[UMAP]] / [[HDBSCAN]] / [[SentenceTransformers]] / [[sklearn]] — pipeline components.
- [[Plotly]] / [[Datamapplot]] / [[matplotlib]] — visualization backends.
- [[HuggingFace]] — hosts the `maartengr/arxiv_nlp` dataset and the embedding / LLM models BERTopic uses.
- [[Gensim]] — the classical-NLP topic-modeling alternative (LDA).
