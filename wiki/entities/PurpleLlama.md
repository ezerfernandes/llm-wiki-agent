---
title: "Purple Llama"
type: entity
tags: [meta, safety, guardrail, llm-security, open-source]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Purple Llama

**[[meta|Meta]]'s umbrella project for open-source LLM trust-and-safety tooling.** Cited in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as one of the named off-the-shelf [[Guardrail|guardrail]] solutions:

> *"Guardrail solutions that you can use out of the box include Meta's Purple Llama, NVIDIA's NeMo Guardrails, Azure's PyRIT, Azure's AI content filters, the Perspective API, and OpenAI's content moderation API."* — Ch 10

## What it ships

Purple Llama is an umbrella over several Meta-released safety artifacts; the best-known components are:

- **[[LlamaGuard|Llama Guard]]** — a fine-tuned classifier for input/output safety scoring (already covered in this wiki under the [[Guardrail]] taxonomy).
- **CyberSecEval** — a cyber-risk evaluation benchmark for LLMs.
- **Code Shield** — an inference-time filter for insecure code suggestions.

The "purple" naming gestures at the red-team / blue-team color combination: offensive (red) + defensive (blue) = purple.

## Position in the guardrail ecosystem

Per the [[Guardrail]] wiki page, Llama Guard is the **trained-classifier** baseline in the guardrail taxonomy (alongside rule-based [[NeMoGuardrails|NeMo Guardrails]] and validator-style [[GuardrailsAI]]). Purple Llama as an umbrella thus represents Meta's official open-source position in the production-guardrail space.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[meta|Meta]] — author / publisher.
- [[LlamaGuard]] — flagship component.
- [[Guardrail]] — the broader product category.
- [[NeMoGuardrails]] / [[GuardrailsAI]] / [[AzurePyRIT]] / [[PerspectiveAPI]] — peer guardrail solutions named in Ch 10.
