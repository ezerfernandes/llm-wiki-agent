---
title: "Voiceflow"
type: entity
tags: [company, conversational-ai, chatbot, case-study]
sources: [ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Voiceflow

Conversational-AI platform. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Migrating from GPT-3.5-turbo-0301 to GPT-3.5-turbo-1106 led to a 10% drop in Voiceflow's intent classification task."

## Significance

Voiceflow's experience is one half of Ch 4's canonical **"same model update, opposite effects"** anecdote — paired with [[GoDaddy]]'s improvement on the same migration. Together they argue that *"the best model overall might not be the best model for your application."*

It's also evidence for the broader claim that **[[CommercialModel|commercial model]] versioning can quietly break production apps** — *"your prompts might stop working as expected and you have no idea."*

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[GoDaddy]] — paired counter-case study.
- [[CommercialModel]] — the model class whose version drift caused the regression.
- [[openai|OpenAI]] — the model provider in question.
- [[Evaluation]] — the discipline that catches this.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 reuses the **same Voiceflow incident** as a worked example of [[SilentModelUpdate|silent model update]] / [[DriftDetection|drift]]:

> *"[[Voiceflow]] reported a 10% performance drop when switching from the older GPT-3.5-turbo-0301 to the newer GPT-3.5-turbo-1106."* — Ch 10

In Ch 10's framing, the incident isn't (just) a [[CommercialModel|commercial-model versioning]] hazard — it's a **drift-detection** case showing why production AI apps need continuous offline eval against the live model. The same evaluation signal that Ch 4 used to argue *"the best model overall might not be the best for your app"* becomes, in Ch 10, the *monitoring* signal that catches behavior change behind a stable API.
