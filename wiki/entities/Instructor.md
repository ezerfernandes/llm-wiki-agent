---
title: "Instructor"
type: entity
tags: [tool, library, structured-output, pydantic, llm, open-source]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Instructor

Open-source Python library for **structured-output generation** built on [[Pydantic]] schemas — primarily targeting chat-API providers (OpenAI, Anthropic). Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] alongside [[Guidance]] and [[Outlines]] as partial-workflow [[PromptEngineeringTools|prompt-engineering tools]].

> "Many tools aim to assist parts of prompt engineering. For example, Guidance, Outlines, and Instructor guide models toward structured outputs." — Ch 5

## Position

The [[Pydantic]]-native approach: define your output schema as a Pydantic model, and Instructor handles the prompt-templating and parsing (with retry-on-validation-failure). Distinct from [[Outlines]] (which constrains the model's *decoding*) and [[Guidance]] (which combines templating with constrained decoding) — Instructor works at the **API-message level** rather than the token-decoding level, which makes it portable across providers that don't expose decoding hooks.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptEngineeringTools]] — parent category.
- [[Outlines]] / [[Guidance]] — sibling structured-output libraries.
- [[Pydantic]] — the schema layer.
- [[StructuredOutputs]] — the capability.
