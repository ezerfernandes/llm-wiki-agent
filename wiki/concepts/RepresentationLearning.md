---
title: "Representation Learning"
type: concept
tags: [deep-learning, foundational]
sources: [d2l-introduction]
last_updated: 2026-05-16
---

# Representation Learning

Per [[d2l-introduction]]: "representational learning focuses on how to automatically find the appropriate way to represent data." It's the umbrella that contains [[DeepLearning|deep learning]] as a special case — *multi-level* representation learning, in which the model learns **many layers of transformations** rather than a single handcrafted feature map.

## The chapter's framing

> "What differentiates deep learning is that the operations learned at each of the many layers of representations are learned jointly from data."

Classical ML pipelines have *one* layer of feature processing (handcrafted or shallow-learned) feeding into a shallow predictor. Deep learning has *many* layers, each producing its own representation, all jointly optimized by [[Backpropagation|backprop]] against the final loss. The hierarchy moves from low-level perceptual features (edges, phonemes, characters) up through abstract task-relevant features (object parts, syntactic structures, semantic relations).

## Why it matters

The chapter is explicit that this is *the* substantive advance: many-layered models "are capable of addressing low-level perceptual data in a way that previous tools could not." The previous tools — Canny edges, [[SIFT|SIFT features]] — *were* representations, just **not jointly optimized** with the downstream classifier and **not nested** beyond one or two levels.

## Connections

- [[DeepLearning]] — the specific multi-level instance.
- [[EndToEndTraining]] — the optimization principle that makes the joint multi-level training work.
- [[FeatureEngineering]] — the *manual* alternative this paradigm replaces.
- [[SelfSupervisedLearning]] — modern recipe for learning representations without task labels.
- [[TransferLearning]], [[FineTuning]] — what makes learned representations *portable* across tasks.
- [[d2l-introduction]] — corpus anchor of this framing.
