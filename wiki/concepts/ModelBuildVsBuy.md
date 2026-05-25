---
title: "Model Build vs Buy"
type: concept
tags: [model-selection, ai-engineering, decision-framework, methodology]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Model Build vs Buy

The recurring **"use a model API vs host an open-source model yourself"** decision. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "An evergreen question for companies when leveraging any technology is whether to build or buy. Since most companies won't be building foundation models from scratch, the question is whether to use commercial model APIs or host an open source model yourself."

This decision *"can significantly reduce your candidate model pool"* — it's typically the first filter in the [[ModelSelectionWorkflow|model-selection workflow]].

## The seven axes (Ch 4)

| Axis | API tilt | Self-host tilt |
|---|---|---|
| **Data privacy** | — | If you can't send data outside your org ([[Samsung]] ChatGPT leak; [[Zoom]] 2023 ToS backlash) |
| **Data lineage & copyright** | Commercial contracts can shield you | Fully open models let you audit training data |
| **Performance** | Strongest models are commercial | Open is catching up, but always behind frontier |
| **Functionality** | Scaling, [[FunctionCalling|function calling]], [[StructuredOutputs|structured outputs]] out of the box | [[Logprobs|Logprobs]], intermediate outputs, custom [[FineTuning|finetuning]] |
| **Cost** | API cost (predictable) | Engineering + compute cost (scales better at high volume) |
| **Control, access, transparency** | Rate limits; risk of losing access; opaque updates | Freeze, inspect, customize, [[Quantization|quantize]] |
| **On-device** | Impossible | The only option |

## The four-step workflow this feeds

1. Filter on **hard attributes** ([[HardModelAttribute]]) — including build/buy.
2. Narrow with public benchmarks / [[Leaderboard|leaderboards]].
3. Run private experiments via [[EvaluationPipeline|your evaluation pipeline]].
4. Monitor in production.

## Same model, different APIs

A subtle complication: the same model on different APIs can perform differently because each API may apply different inference optimizations. *"GPT-4 is available through both OpenAI and Azure APIs. There might be slight differences in the performance of the same model provided through different APIs."* Test on every API you might use.

## Cost crossover

> "At a certain scale, a company that is bleeding its resources using APIs might consider hosting their own models. However, hosting a model yourself requires nontrivial time, talent, and engineering effort. … APIs are expensive, but engineering can be even more so."

## The mimicry signal

> "You want a model that … follows a standard API, which makes it easier to swap models. … As of this writing, many API providers mimic OpenAI's API."

OpenAI's API has become the *de facto* swap-compatibility interface.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[ModelSelectionWorkflow]] — four-step parent process.
- [[OpenWeight]] / [[OpenSourceModel]] / [[OpenModel]] / [[CommercialModel]] — the model-class taxonomy this decision filters over.
- [[ModelLicense]] / [[LlamaLicense]] — what makes some models commercially usable.
- [[InferenceService]] / [[ModelAPI]] / [[ModelAPIProvider]] — what you're choosing between.
- [[HardModelAttribute]] / [[SoftModelAttribute]] — the attribute typology.
- [[a16z]] — 2024 study on enterprise reasons for open source.
- [[Samsung]] / [[Zoom]] / [[Convai]] / [[Voiceflow]] / [[GoDaddy]] — chapter case studies.
