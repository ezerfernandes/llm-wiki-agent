---
title: "Q-Former (Querying Transformer)"
type: concept
tags: [multimodal, architecture, bridge, vision-language, blip-2]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Q-Former (Querying Transformer)

The **trainable bridge** between a frozen image encoder and a frozen LLM in [[BLIP2|BLIP-2]] (Li et al. 2023). The single component that BLIP-2 trains — the [[VisionTransformer|ViT]] image encoder and the LLM stay frozen. Introduced in [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]] as the wiki's first concrete bridge architecture for an adapter-style [[MultimodalLLM|multimodal LLM]].

## Why a bridge

*"Creating a multimodal language model from scratch requires significant computing power and data ... BLIP-2 bridges the vision-language gap by building a bridge, named the Querying Transformer (Q-Former), that connects a pretrained image encoder and a pretrained LLM."* — the compute-efficiency thesis that justifies the adapter pattern.

## Two-module shared-attention architecture

The Q-Former mimics both sides it connects:

1. **Image Transformer** — interacts with the frozen [[VisionTransformer|ViT]] for feature extraction.
2. **Text Transformer** — interacts with the LLM.

The two modules **share their attention layers**. This is the structural device that lets the Q-Former learn a representation that is simultaneously image-shaped and text-shaped.

## Two-stage training

### Stage 1 — Joint visual-text representation learning

(image, caption) pairs go through the frozen ViT → Q-Former Image Transformer; captions go through the Q-Former Text Transformer. The two are trained jointly on three contrastive-like objectives:

1. **[[ImageTextContrastive|Image-text contrastive learning]]** — align paired (image, text) embeddings to maximize their mutual information.
2. **[[ImageTextMatching|Image-text matching]]** — binary classification: is this (image, text) pair matched or unmatched?
3. **[[ImageGroundedTextGeneration|Image-grounded text generation]]** — generate text conditioned on the image.

*"These three objectives are jointly optimized to improve the visual representations that are extracted from the frozen ViT. In a way, we are trying to inject textual information into the embeddings of the frozen ViT so that we can use them in the LLM."*

### Stage 2 — Soft visual prompting

*"The learnable embeddings derived from step 1 now contain visual information in the same dimensional space as the corresponding textual information. The learnable embeddings are then passed to the LLM. In a way, these embeddings serve as soft visual prompts that condition the LLM on the visual representations that were extracted by the Q-Former."*

A **fully-connected linear projection layer** sits between the Q-Former and the LLM *"to make sure that the learnable embeddings have the same shape as the LLM expects."*

## Relation to LLaVA-style projectors

[[LLaVA15|LLaVA-v1.5]] simplifies the Q-Former to a **2-layer MLP projector** while keeping the frozen-encoder-frozen-LLM-only-train-the-bridge stance. [[Idefics2]] uses yet a different bridge. The Q-Former is the most expressive of the three (it is a multi-module transformer); the 2-layer MLP is the most lightweight; the Idefics-2 design sits between them. The shared goal across all three is the same: *"project visual features from the input images to language embeddings such that they can be used as the input for an LLM."*

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[BLIP2]] — the model that introduces the Q-Former.
- [[SoftVisualPrompt]] — the Q-Former's stage-2 output role.
- [[VisionTransformer]] — the frozen feature-extractor side.
- [[ImageTextContrastive]] / [[ImageTextMatching]] / [[ImageGroundedTextGeneration]] — the three stage-1 objectives.
- [[LLaVA15]] — the successor with a simplified projector.
- [[Idefics2]] — a contemporary alternative bridge.
- [[MultimodalLLM]] — the architectural family Q-Former-style bridges instantiate.
- [[ContrastiveLearning]] — the parent paradigm of the stage-1 objectives.
