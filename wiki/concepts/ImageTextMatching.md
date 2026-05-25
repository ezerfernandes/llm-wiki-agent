---
title: "Image-Text Matching"
type: concept
tags: [multimodal, classification, training-objective, vision-language]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Image-Text Matching

A **binary classification** training objective: given an (image, text) pair, predict whether they match (positive) or do not match (negative). The second of three [[QFormer|Q-Former]] stage-1 objectives in [[BLIP2|BLIP-2]] ([[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]).

> *"Image-text matching: A classification task to predict whether an image and text pair is positive (matched) or negative (unmatched)."*

Adds **discriminative supervision** on top of the contrastive objective: contrastive pulls aligned pairs together in embedding space; matching directly trains a classifier that determines pair compatibility. The two are complementary — contrastive shapes the embedding geometry, matching trains the readout that consumes that geometry.

## Position in Ch 9's three-objective Q-Former training

1. [[ImageTextContrastive|Image-text contrastive]]
2. **[[ImageTextMatching|Image-text matching]]** ← *this page*
3. [[ImageGroundedTextGeneration|Image-grounded text generation]]

*"These three objectives are jointly optimized to improve the visual representations that are extracted from the frozen ViT."*

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[BLIP2]] / [[QFormer]] — Ch 9's three-objective stage-1 training.
- [[ImageTextContrastive]] / [[ImageGroundedTextGeneration]] — sibling Q-Former objectives.
- [[ContrastiveLearning]] — the broader paradigm.
- [[BinaryClassification]] — the formal task category.
