---
title: "Image Encoder"
type: concept
tags: [multimodal, encoder, vision]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Image Encoder

The component of a multimodal model that **converts an image into a numerical embedding (or sequence of embeddings)**. Across the modern multimodal stack, the canonical image encoder is a [[VisionTransformer|Vision Transformer (ViT)]] (sometimes a [[CNN|CNN]] in older systems).

Introduced as a named-role abstraction in [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]: *"CLIP uses a text encoder to embed text and an image encoder to embed images."* In [[BLIP2|BLIP-2]] the image encoder is the **frozen [[VisionTransformer|ViT]]** that feeds the trainable [[QFormer|Q-Former]].

## Where it appears

| Model | Image encoder | Role |
|---|---|---|
| [[CLIP]] | ViT (trained jointly with text encoder) | Produces image embeddings in joint text-image vector space. |
| [[BLIP2|BLIP-2]] | Frozen ViT | Produces visual features the [[QFormer|Q-Former]] bridges to a frozen LLM. |
| [[LLaVA15|LLaVA-v1.5]] | Frozen [[CoCa]]-style ViT | Produces visual features the 2-layer MLP projector bridges to the LLM. |
| [[2408.08849-ecg-chat|ECG-Chat]] | Frozen [[ECGEncoder|1d-ViT]] | The same pattern extended to a physiological-signal modality. |

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source for the named role.
- [[VisionTransformer]] — the dominant image-encoder architecture.
- [[PatchEmbedding]] — the ViT-specific image-tokenization primitive.
- [[CLIP]] / [[BLIP2]] / [[LLaVA15]] — models that all have an image encoder.
- [[MultimodalLLM]] — the broader pattern category.
- [[MultimodalEmbeddingSpace]] — what an image encoder + text encoder pair produces.
- [[ECGEncoder]] — the same role for a non-visual modality.
