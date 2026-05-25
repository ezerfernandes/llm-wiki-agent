---
title: "Guardrails (Guardrails AI)"
type: entity
tags: [tool, library, structured-output, llm, open-source, validation]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Guardrails (Guardrails AI)

Open-source Python library — [Guardrails AI](https://www.guardrailsai.com/) — for **structured output + validation** with LLMs. Named in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]] alongside [[Guidance]] and [[LMQL]] as the canonical Python packages for **constrain-and-validate** LLM output:

> *"Packages have been rapidly developed to constrain and validate the output of generative models, like Guidance, Guardrails, and LMQL."* — Ch 6

## What it does

Two complementary operating modes covered in Ch 6:

1. **Use an LLM to validate the prior LLM's output** against a set of predefined rules. *"The generative models retrieve the output as new prompts and attempt to validate it based on a number of predefined guardrails."*
2. **Constrain the formatting / token-selection process** at generation time so the output adheres to a target schema (JSON, regex, etc.). The user supplies the parts of the format they know and the model only fills in the unknowns.

## Position in the prompt-engineering toolchain

Guardrails is a **partial-workflow [[PromptEngineeringTools|prompt-engineering tool]]** in [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]]'s taxonomy — focused on structured-output / validation rather than full prompt-search optimization. Sibling tools in the same niche:

- [[Guidance]] — templating + constrained decoding.
- [[Outlines]] — JSON / regex / context-free grammar / Pydantic schemas.
- [[LMQL]] — declarative query language for constraining LLM outputs.
- [[Instructor]] — Pydantic-based for chat APIs.

The wiki's [[ConstrainedSampling]] page is the runnable / mechanistic anchor; Ch 6 demonstrates the broader pattern via [[llamacpp|`llama-cpp-python`]]'s `response_format={"type": "json_object"}` rather than via Guardrails directly, but names Guardrails as one of the three canonical Python packages in the space.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source naming Guardrails.
- [[Guidance]] / [[LMQL]] — the two named siblings in Ch 6's triad.
- [[Outlines]] / [[Instructor]] — additional siblings named by [[ai-engineering-ch02-foundation-models|Huyen Ch 2]] / [[ai-engineering-ch05-prompt-engineering|Ch 5]] in the same niche.
- [[ConstrainedSampling]] — the mechanism.
- [[GrammarConstrainedDecoding]] — the chapter-level pattern.
- [[OutputVerification]] — the parent goal.
- [[StructuredOutputs]] — the broader capability family.
- [[PromptEngineeringTools]] — the taxonomy that catalogs partial-workflow tools.
