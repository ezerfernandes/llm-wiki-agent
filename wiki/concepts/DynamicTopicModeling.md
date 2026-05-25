---
title: "Dynamic Topic Modeling"
type: concept
tags: [topic-modeling, bertopic, temporal, time-series]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Dynamic Topic Modeling

**Dynamic topic modeling** tracks how topics **evolve over time** — discovering both stable themes and themes that wax / wane across time buckets. In [[BERTopic]] (per *Hands-On LLMs* Ch 5) it is implemented as a variant of the base pipeline: cluster documents once globally, then compute **per-time-bucket [[ClassBasedTFIDF|c-TF-IDF]]** representations so each topic gets a time-indexed keyword evolution.

## Why "dynamic"

Classical [[LatentDirichletAllocation|LDA]]-based dynamic topic models (Blei & Lafferty 2006) had their own probabilistic machinery. BERTopic's dynamic variant is **conceptually simpler**: clusters are fixed; only the c-TF-IDF representation per cluster changes across time buckets.

## Use cases

- **News-topic tracking** — how does the *"economy"* topic shift over years?
- **Research-trend analysis** — for the [[ArXivNLP|ArXiv NLP]] dataset (1991–2024), how do *"machine translation"* keywords shift from statistical → neural → transformer?
- **Social-media monitoring** — emerging vs declining themes.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] / [[TopicModeling]] — parent.
- [[ClassBasedTFIDF]] — the time-bucketed weighting.
- [[ArXivNLP]] — natural fit (timestamped abstracts).
