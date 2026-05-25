---
title: "ImageBind"
type: concept
tags: [model, multimodal, embeddings]
sources: [ai-engineering-ch03-evaluation-methodology, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# ImageBind

**ImageBind** (Girdhar et al. 2023, [[meta|Meta]]) learns a **joint [[MultimodalEmbeddingSpace|embedding space]] across six different modalities**: text, images, audio, depth, thermal, and IMU (inertial-measurement-unit) data. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]: *"ImageBind (Girdhar et al., 2023) learns a joint embedding across six different modalities, including text, images, and audio."*

## What's novel

Most multimodal embeddings before ImageBind paired modalities one-to-one (text+image in [[CLIP]]; text+image+3D in [[ULIP]]). ImageBind learns **all six modalities into one shared space** without requiring all-pair training data — it uses *image* as the binding modality, anchoring text/audio/depth/thermal/IMU to it.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[MultimodalEmbeddingSpace]] — parent concept.
- [[CLIP]] / [[ULIP]] — sibling multimodal-embedding models.
- [[meta|Meta]] — authoring lab.
- [[Embedding]] — substrate concept.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 does not name ImageBind directly — its multimodal embedding focus is squarely on [[CLIP]]. The wiki records ImageBind here as the **six-modality successor** in the [[MultimodalEmbeddingSpace|multimodal-embedding-space]] lineage that Ch 9 walks the two-modality starting point of. Ch 9's opening framing — *"a model that is able to handle text and images (each of which is called a modality) is said to be multimodal"* — admits ImageBind's expansion to audio / depth / thermal / IMU as the natural generalization; the chapter explicitly notes *"in this chapter, however, we will mostly explore the modality of vision"* — flagging the deliberate scope-narrowing that distinguishes a pedagogical book chapter from ImageBind's research-paper coverage.
