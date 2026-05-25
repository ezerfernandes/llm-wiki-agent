---
title: "Image-Grounded Text Generation"
type: concept
tags: [multimodal, generation, training-objective, vision-language]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Image-Grounded Text Generation

A training objective that **generates text conditioned on an input image** — the generative complement to the contrastive and matching objectives. The third of three [[QFormer|Q-Former]] stage-1 objectives in [[BLIP2|BLIP-2]] ([[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]).

> *"Image-grounded text generation: Trains the model to generate text based on information extracted from the input image."*

This is the objective that **directly couples the visual features to the language-decoding capability** the Q-Former needs to produce visual representations useful as soft prompts for the downstream LLM. The other two objectives (contrastive + matching) shape the embedding geometry; this objective trains the visual representation to **produce text**.

## Position in Ch 9's three-objective Q-Former training

1. [[ImageTextContrastive|Image-text contrastive]]
2. [[ImageTextMatching|Image-text matching]]
3. **[[ImageGroundedTextGeneration|Image-grounded text generation]]** ← *this page*

*"These three objectives are jointly optimized to improve the visual representations that are extracted from the frozen ViT. In a way, we are trying to inject textual information into the embeddings of the frozen ViT so that we can use them in the LLM."*

## Relation to [[ImageCaptioning|image captioning]]

[[ImageCaptioning|Image captioning]] is the **downstream inference task** that image-grounded text generation enables — captioning is what BLIP-2 *does* with a trained image-grounded-generation-capable Q-Former plus a frozen LLM.

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[BLIP2]] / [[QFormer]] — Ch 9's three-objective stage-1 training.
- [[ImageTextContrastive]] / [[ImageTextMatching]] — sibling Q-Former objectives.
- [[ImageCaptioning]] — the downstream inference task this objective enables.
- [[SoftVisualPrompt]] — the runtime output mechanism the trained representation feeds.
