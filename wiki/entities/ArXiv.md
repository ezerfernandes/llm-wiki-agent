---
title: "arXiv"
type: entity
tags: [preprint, open-access, scientific-publishing, dataset-source]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# arXiv

**arXiv** (`arxiv.org`) is the canonical open-access preprint repository for physics, mathematics, computer science, quantitative biology, statistics, and related fields. Founded by [[PaulGinsparg|Paul Ginsparg]] in 1991 at Los Alamos National Lab, now hosted by Cornell University. Almost every modern LLM / deep-learning paper appears on arXiv before (or instead of) formal publication.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5's worked-example dataset is **[[ArXivNLP|`maartengr/arxiv_nlp`]]** — 44,949 abstracts from arXiv's **Computation and Language (cs.CL)** category between 1991 and 2024 — used to walk the embed → UMAP → HDBSCAN → c-TF-IDF pipeline end-to-end. The chapter's sanity-check vignette is that the [[BERTopic]] paper's own abstract (also on arXiv: [[2203.05794-bertopic|2203.05794]]) is assigned to BERTopic's topic 22 (the "topic modeling" topic) in this very dataset.

arXiv categories are the de facto taxonomy used throughout the wiki: every paper page cites its arXiv ID (e.g., `1706.03762`, `2203.05794`, `2603.19247`).

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 worked dataset.
- [[ArXivNLP]] — the specific Hugging Face dataset derived from cs.CL.
- [[2203.05794-bertopic]] — the BERTopic paper hosted on arXiv.
- [[HuggingFace]] — distributor of `maartengr/arxiv_nlp`.
