---
title: "Commercial Model"
type: concept
tags: [model-class, proprietary, api, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Commercial Model

A proprietary model **accessed only via the developer's API**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Commercial models are only accessible via APIs licensed by the model developers."

## What it costs (and saves) you

| You give up | You get |
|---|---|
| Inspection, freezing, customization | Strongest models, easier scaling |
| Data inside your network | Often-better functionality (function calling, structured outputs) |
| [[Logprobs|Logprobs]] (usually) | Less DevOps overhead |
| Long-term version stability | Vendor-managed updates |

## The hidden risks

- **Version drift.** GPT-3.5/GPT-4 performance changed significantly between March and June 2023 (Chen et al. 2023). [[Voiceflow]] lost 10% intent-classification accuracy on the 0301→1106 migration; [[GoDaddy]]'s chatbot improved on the same migration. Same update, opposite effects.
- **Provider can ban you / your industry / your country.** Italy briefly banned OpenAI in 2023.
- **Provider can go out of business.**
- **Over-censoring.** Proprietary models err safe — useful for general apps, blocking for some ([[Convai]]'s 3D NPCs needed to grab objects; commercial models refused).

## Worked example

> "GPT-4 is available through both OpenAI and Azure APIs. There might be slight differences in the performance of the same model provided through different APIs, as different APIs might use different techniques to optimize this model."

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[OpenSourceModel]] / [[OpenWeight]] / [[OpenModel]] — sibling categories.
- [[ModelAPI]] / [[InferenceService]] / [[ModelAPIProvider]] — what you interact with.
- [[ModelBuildVsBuy]] — the decision framing.
- [[Voiceflow]] / [[GoDaddy]] / [[Convai]] — case studies on version drift and over-censoring.
