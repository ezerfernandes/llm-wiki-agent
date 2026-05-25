---
title: "Topic Clustering"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

## Definition
Automatic grouping of similar documents via embeddings + dimensionality reduction + clustering.

## In LLM Engineer's Handbook
Automatic grouping of similar texts into thematic clusters. Standard pipeline: embed with sentence-transformers, reduce dimensionality with UMAP, cluster with DBSCAN/HDBSCAN, auto-label with an LLM. Per [[leh-ch05-supervised-fine-tuning]] tools include Hugging Face's `text-clustering` pipeline, [[NomicAtlas]], BunkaTopics, and Lilac. Used for instruction-dataset exploration.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 is the wiki's **full pedagogical walkthrough** of the same pipeline LEH Ch 5 named in passing. Where LEH Ch 5 listed Hugging Face's `text-clustering`, [[NomicAtlas]], BunkaTopics, and Lilac as tooling, *Hands-On LLMs* Ch 5 names [[BERTopic]] (Grootendorst's own framework) — a different tooling choice for the same underlying pipeline. The chapter runs the pipeline end-to-end on **44,949 cs.CL abstracts** from [[ArXivNLP|`maartengr/arxiv_nlp`]]:

1. Embed with [[GTESmall|`thenlper/gte-small`]] (384-dim sentence-transformer; chosen via [[MTEB]] clustering column).
2. Reduce with [[UMAP]] (384 → 5 dimensions; `min_dist=0.0`, `metric='cosine'`).
3. Cluster with [[HDBSCAN]] (`min_cluster_size=50`; produces 156 clusters incl. outlier topic `-1`).
4. Label clusters with c-TF-IDF + optional [[KeyBERTInspired]] / [[MaximalMarginalRelevance|MMR]] / [[GenerativeTopicLabeling|LLM-based]] refinements.

See [[TextClustering]] for the canonical concept page mirroring this walkthrough.

## Connections

- [[leh-ch05-supervised-fine-tuning]] — tooling-list mention.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — full walkthrough.
- [[TextClustering]] — the deeper concept page covering the same pipeline.
- [[BERTopic]] — Ch 5's chosen framework.
- [[NomicAtlas]] / Hugging Face `text-clustering` — LEH-named tooling alternatives.
- [[UMAP]] / [[HDBSCAN]] / [[SentenceTransformers]] / [[ClassBasedTFIDF]] — pipeline components.
