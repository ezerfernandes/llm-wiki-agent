---
title: "ArXiv NLP (maartengr/arxiv_nlp)"
type: entity
tags: [dataset, nlp, arxiv, huggingface, clustering, topic-modeling]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# ArXiv NLP (`maartengr/arxiv_nlp`)

`maartengr/arxiv_nlp` is a [[HuggingFace|Hugging Face]] dataset curated by [[MaartenGrootendorst|Maarten Grootendorst]] containing **44,949 paper abstracts** from [[ArXiv|arXiv's]] **Computation and Language (cs.CL)** category between **1991 and 2024**. The dataset is the worked example for [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]] — clustering and topic-modeling NLP research itself.

## Structure

```python
from datasets import load_dataset
dataset = load_dataset("maartengr/arxiv_nlp")["train"]
abstracts = dataset["Abstracts"]   # list[str]
titles    = dataset["Titles"]      # list[str]
```

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 runs the embed (gte-small, 384-dim) → [[UMAP]] (384→5) → [[HDBSCAN]] (`min_cluster_size=50`) → [[ClassBasedTFIDF|c-TF-IDF]] pipeline on the full 44,949 abstracts and finds **156 clusters** (155 topics + outlier topic `-1` containing 14,520 abstracts). Selected topics include automatic speech recognition (topic 0, 2,290 docs), medical NLP (topic 1, 1,403 docs), sentiment / aspect-based analysis (topic 2, 1,156 docs), neural machine translation (topic 3, 986 docs), and — as the chapter's sanity-check vignette — **topic 22 (topic modeling)**, the topic to which BERTopic's own arXiv abstract is assigned.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[ArXiv]] — the parent preprint repository.
- [[HuggingFace]] — the distribution platform.
- [[MaartenGrootendorst]] — dataset curator.
- [[BERTopic]] — the framework run against this dataset in Ch 5.
- [[GTESmall]] — the embedding model used.
- [[UMAP]] / [[HDBSCAN]] — the clustering pipeline applied.
