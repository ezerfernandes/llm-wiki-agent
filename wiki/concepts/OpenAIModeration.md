---
title: "OpenAI Moderation Endpoint"
type: concept
tags: [api, safety, moderation, openai]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# OpenAI Moderation Endpoint

A **content-moderation API** by [[openai|OpenAI]] that classifies input/output text against OpenAI's harm taxonomy. Cited by [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] as one of the canonical [[Safety|safety]] taxonomies (alongside Meta's [[LlamaGuard]] paper).

## Position

> "Different safety solutions have different ways of categorizing harms — see the taxonomy defined in OpenAI's content moderation endpoint and Meta's Llama Guard paper (Inan et al., 2023)."

OpenAI exposes this as a free moderation endpoint companies can call before showing user inputs to the model or model outputs to users. It's the **moderation tool** OpenAI ships alongside its commercial models to keep usage safe.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[openai|OpenAI]] — authoring organization.
- [[Safety]] — the discipline.
- [[LlamaGuard]] — Meta's competitor with its own taxonomy.
- [[PerspectiveAPI]] / [[FacebookHateSpeech]] / [[SkolkovoToxicityClassifier]] — other safety classifiers.
- [[Guardrail]] — the broader defensive layer category.
