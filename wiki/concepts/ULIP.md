---
title: "ULIP"
type: concept
tags: [model, multimodal, embeddings, 3d]
sources: [ai-engineering-ch03-evaluation-methodology, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# ULIP

**ULIP** — *Unified representation of Language, Images, and Point clouds* (Xue et al. 2022) — extends the [[CLIP]] paradigm by adding **3D point clouds** as a third modality. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]: *"ULIP (unified representation of language, images, and point clouds), (Xue et al., 2022) aims to create unified representations of text, images, and 3D point clouds."*

## Why 3D point clouds matter

Adding point clouds enables:
- Zero-shot 3D shape classification from text or image queries.
- Cross-modal 3D shape retrieval.
- Bridging vision-language models to robotics / AR / autonomous-driving pipelines that consume LIDAR or depth-sensor data.

## Position

ULIP sits between [[CLIP]] (two modalities, 2021) and [[ImageBind]] (six modalities, 2023) in the multimodal-embedding lineage.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[MultimodalEmbeddingSpace]] — parent concept.
- [[CLIP]] / [[ImageBind]] — sibling multimodal-embedding models.
- [[Embedding]] — substrate concept.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 does not name ULIP directly; its multimodal-embedding focus stays on [[CLIP]] as the two-modality reference model. The wiki records ULIP here as the **three-modality intermediate** between [[CLIP]] (2021, two modalities) and [[ImageBind]] (2023, six modalities) in the lineage Ch 9 walks the starting point of.
