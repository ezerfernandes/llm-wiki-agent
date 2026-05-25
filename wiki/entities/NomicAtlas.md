---
title: "Nomic Atlas"
type: entity
tags: [tool]
sources: [leh-ch05-supervised-fine-tuning, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

## What it is
Nomic AI's interactive atlas for embedding-based visualization and exploration of large datasets.

## In LLM Engineer's Handbook
Nomic AI's interactive web-based atlas for visualizing large datasets via 2-D projections of high-dimensional embeddings. Used in [[leh-ch05-supervised-fine-tuning]] (Figure 5.5) for topic-clustering exploration of instruction datasets; listed alongside BunkaTopics and Lilac as alternatives to Hugging Face's `text-clustering` pipeline.

## In *Hands-On LLMs* Ch 5

Nomic Atlas is mentioned as a contrasting visualization-and-exploration tool in the comparison with [[leh-ch05-supervised-fine-tuning|LEH Ch 5]]'s tooling list. [[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]] of *Hands-On LLMs* uses [[BERTopic]] (with [[Plotly]] and [[Datamapplot]] for visualization) rather than Nomic Atlas — but the same underlying embed → UMAP → cluster pipeline. Both tools target the same need (interactive cluster exploration); Nomic Atlas is hosted-web-first, BERTopic is Python-library-first.
