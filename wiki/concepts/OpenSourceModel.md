---
title: "Open Source Model"
type: concept
tags: [model-class, license, open-source, terminology]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Open Source Model

A **contested term**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "The term 'open source model' has become contentious. Originally, open source was used to refer to any model that people can download and use. … However, some people argue that since a model's performance is largely a function of what data it was trained on, a model should be considered open only if its training data is also made publicly available."

## Huyen's working definition

In *AI Engineering*, Huyen uses *open source* **broadly** — any model whose weights are made public, regardless of training-data availability or license. Stricter usage would reserve "open source" for [[OpenModel|fully open]] models (weights + data).

> "Some people argue that the term open source should be reserved only for fully open models. In this book, for simplicity, I use open source to refer to all models whose weights are made public, regardless of their training data's availability and licenses."

## The taxonomy

| Class | Weights | Training data | License restrictions |
|---|---|---|---|
| **[[OpenModel|Open model]]** | Public | Public | Often permissive (Apache 2.0, MIT) |
| **[[OpenWeight|Open weight]]** | Public | Private | Varies (Llama 2/3 Community License, etc.) |
| **[[CommercialModel|Commercial model]]** | Private | Private | API-only, terms of service |

## The performance-gap argument

Ch 4 makes a structural argument about why open-source models will lag commercial:

> "If you have the strongest model available, would you rather open source it for other people to capitalize on it, or would you try to capitalize on it yourself? It's a common practice for companies to keep their strongest models behind APIs and open source their weaker models."

The MMLU gap is closing (Labonne chart, Figure 4-7), but Huyen argues the incentive structure prevents full parity.

## Why use open source then

The a16z 2024 study (Figure 4-8 in Ch 4) identifies **control and customizability** as the two top enterprise reasons for choosing open source. [[Convai]]'s NPC system is a worked example — commercial models refused to give characters physical abilities (*"As an AI model, I don't have physical abilities"*), so they finetuned open-source instead.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[OpenWeight]] / [[OpenModel]] / [[CommercialModel]] — sibling categories.
- [[ModelLicense]] / [[LlamaLicense]] — the constraint layer.
- [[ModelBuildVsBuy]] — the decision framing.
- [[a16z]] — source of the "why open source" enterprise study.
- [[Convai]] — case study for finetuning open-source for use-case fit.
