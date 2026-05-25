---
title: "Multimodal Topic Modeling"
type: concept
tags: [topic-modeling, bertopic, multimodal, vision]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Multimodal Topic Modeling

A [[BERTopic]] variant where documents include **multiple modalities** (text + image, text + audio, etc.) and the embedding step uses a **multimodal embedding model** (e.g., [[CLIP|CLIP]] for text + image) so the clustering pipeline operates across modalities.

Named in [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]] as one of BERTopic's algorithmic variants.

## Use cases

- **Image-caption corpora** — discover themes across both text and visual content.
- **Product catalogs** — cluster items by both description and product photo.
- **Multimodal social media** — posts with text + images.

## Mechanism

Replace the [[SentenceTransformers|sentence-transformers]] embedding step with a multimodal encoder (CLIP / BLIP / multimodal CLIP variants); the rest of the [[BERTopic]] pipeline ([[UMAP]] → [[HDBSCAN]] → [[ClassBasedTFIDF|c-TF-IDF]]) is unchanged. [[ClassBasedTFIDF|c-TF-IDF]] operates on text tokens only, so the topic representation step still produces text keywords for each multimodal cluster.

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] / [[TopicModeling]] — parent.
- [[CLIP]] — typical multimodal embedding backbone.
- [[Multimodal]] — parent paradigm (forward-references [[hands-on-llm-ch09-multimodal-llms|Ch 9]]).
