---
title: "Perspective API"
type: entity
tags: [google, jigsaw, toxicity, content-moderation, api]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Perspective API

**[[Google|Google]] / Jigsaw's toxicity-scoring API.** Cited in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as one of the named off-the-shelf [[Guardrail|guardrail]] solutions:

> *"Guardrail solutions that you can use out of the box include Meta's Purple Llama, NVIDIA's NeMo Guardrails, Azure's PyRIT, Azure's AI content filters, the Perspective API, and OpenAI's content moderation API."* — Ch 10

## What it does

Perspective scores a piece of text on multiple toxicity-related axes (toxicity, severe toxicity, identity attack, insult, profanity, threat) and returns probabilities suitable for moderation decisions. Originally built for **comment-section moderation** on news sites (Jigsaw was incubated at Alphabet for civic tech); has since become a generic toxicity classifier widely used as an [[OutputGuardrail|output guardrail]] in AI applications.

## Position

Perspective is the **toxicity-detection specialist** in the named-guardrail list — it is narrower than Llama Guard or NeMo Guardrails (which span multiple safety axes) but is a mature reference for the toxicity slice.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[OutputGuardrail]] — the typical integration point.
- [[Guardrail]] — broader category.
- [[PurpleLlama]] / [[NeMoGuardrails]] / [[GuardrailsAI]] / [[AzurePyRIT]] — peer guardrail solutions.
- [[safety]] / [[RealToxicityPrompts]] — adjacent toxicity-evaluation infrastructure.
