---
title: "Image-Text Contrastive Learning"
type: concept
tags: [multimodal, contrastive, training-objective, vision-language]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Image-Text Contrastive Learning

A training objective that **aligns paired (image, text) embeddings to maximize their mutual information**, while pushing unpaired examples apart. The foundation of [[CLIP]]'s training recipe and the first of three [[QFormer|Q-Former]] stage-1 objectives in [[BLIP2|BLIP-2]] ([[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]).

> *"Image-text contrastive learning: This task attempts to align pairs of image and text embeddings such that they maximize their mutual information."*

## Position in Ch 9's three-objective Q-Former training

In [[BLIP2|BLIP-2]]'s stage-1 Q-Former training, three objectives are **jointly optimized** on (image, caption) pairs:

1. **[[ImageTextContrastive|Image-text contrastive]]** ← *this page*
2. **[[ImageTextMatching|Image-text matching]]**
3. **[[ImageGroundedTextGeneration|Image-grounded text generation]]**

*"These three objectives are jointly optimized to improve the visual representations that are extracted from the frozen ViT. In a way, we are trying to inject textual information into the embeddings of the frozen ViT so that we can use them in the LLM."*

## Relation to [[CLIP]]'s training

[[CLIP]] uses image-text contrastive learning as its **sole training objective**; [[BLIP2|BLIP-2]] augments it with matching + generation to produce visual representations that are more useful as soft prompts for an LLM (not just as retrieval embeddings).

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[CLIP]] — uses this as its sole training objective.
- [[BLIP2]] / [[QFormer]] — Ch 9's three-objective stage-1 training.
- [[ImageTextMatching]] / [[ImageGroundedTextGeneration]] — sibling Q-Former objectives.
- [[ContrastiveLearning]] — the parent paradigm.
- [[CosineSimilarity]] — the standard score function.
- [[NoiseContrastiveEstimation]] — the loss-form ancestor.
