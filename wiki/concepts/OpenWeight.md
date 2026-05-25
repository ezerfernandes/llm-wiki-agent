---
title: "Open Weight"
type: concept
tags: [model-class, license, open-source, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Open Weight

A model whose **weights are publicly available, but training data is not**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "To signal whether the data is also open, the term 'open weight' is used for models that don't come with open data, whereas the term 'open model' is used for models that come with open data."

## The current state

> "As of this writing, the vast majority of open source models are open weight only."

Why model developers hide training data:
- **Legal exposure** — training data inspection can open them to lawsuits.
- **Competitive advantage** — data curation is one of the differentiators.

Huyen uses *"open source"* loosely to refer to all weight-public models in the book, but flags this as contested terminology.

## Practical implications

- You **can** run, finetune, quantize, and serve the model.
- You **can't** retrain from scratch with the original data.
- You **can't** audit training data for IP/copyright/contamination concerns.
- You **can't** know precisely what biases or contamination might be baked in.

## Position

[[OpenWeight]] ⊂ [[OpenSourceModel]] (broad definition) ⊃ [[OpenModel]] (strict, with training data).
The fourth axis is [[CommercialModel]] (no weights public, API-only).

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[OpenSourceModel]] / [[OpenModel]] / [[CommercialModel]] — sibling categories.
- [[ModelLicense]] / [[LlamaLicense]] — the license layer that constrains use.
- [[ModelBuildVsBuy]] — the decision this enables.
- [[meta|Meta]] / [[Mistral]] / [[Cohere]] / [[google|Google]] (Gemma) — companies that release open-weight models.
