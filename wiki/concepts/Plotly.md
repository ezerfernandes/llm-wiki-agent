---
title: "Plotly"
type: concept
tags: [visualization, library, python, interactive, plotting]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Plotly

**Plotly** is an open-source interactive plotting library (with Python, R, and JavaScript bindings) used for browser-rendered, hover-enabled charts. In [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]] it is the rendering engine behind [[BERTopic]]'s `visualize_documents()` 2D scatter plot — each point is a document, color is the topic, and hovering reveals the document text. Ch 5 also uses Plotly for `visualize_barchart()` (top-keyword bars per topic) and `visualize_heatmap()` (inter-topic similarity).

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

The chapter pairs Plotly with a separate [[UMAP|UMAP `n_components=2`]] projection of the embeddings to surface the topic structure in 2D — distinct from the `n_components=5` projection used for [[HDBSCAN]] clustering. Hover labels combine the document title and topic, making the plot a fast exploratory inspection tool for clusters that c-TF-IDF alone cannot convey.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] — uses Plotly for its standard visualization methods.
- [[matplotlib]] — the static-plot complement used for cluster scatter plots.
- [[Datamapplot]] — the labeled-landscape companion used at chapter close.
- [[UMAP]] — the 2D projection that Plotly renders.
