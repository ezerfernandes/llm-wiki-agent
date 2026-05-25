---
title: "Guidance"
type: entity
tags: [tool, library, structured-output, llm, open-source]
sources: [ai-engineering-ch05-prompt-engineering, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Guidance

Open-source library for **structured-output generation** with LLMs — templating + constrained decoding. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] alongside [[Outlines]] and [[Instructor]] as partial-workflow [[PromptEngineeringTools|prompt-engineering tools]] that guide models toward structured outputs.

> "Many tools aim to assist parts of prompt engineering. For example, Guidance, Outlines, and Instructor guide models toward structured outputs." — Ch 5

## Position

Guidance is a template-and-decoder approach: you write a prompt with placeholders and constraints; the library forces the model's output to match the constraint at decoding time. Sibling tools in the same niche:

- [[Outlines]] — JSON / regex / context-free grammar / Pydantic schemas.
- [[Instructor]] — Pydantic-based for chat APIs.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[hands-on-llm-ch06-prompt-engineering]] — second source naming Guidance.
- [[PromptEngineeringTools]] — parent category.
- [[Outlines]] / [[Instructor]] / [[Guardrails]] / [[LMQL]] — sibling structured-output libraries.
- [[StructuredOutputs]] — the capability.

## In *Hands-On LLMs* Ch 6

[[hands-on-llm-ch06-prompt-engineering|Ch 6]] names Guidance alongside [[Guardrails]] and [[LMQL]] as the canonical Python packages for **constrain-and-validate** LLM output:

> *"Packages have been rapidly developed to constrain and validate the output of generative models, like Guidance, Guardrails, and LMQL."* — Ch 6

Ch 6's framing emphasizes two operating modes both supported by Guidance:
1. **Post-hoc validation** — feed the LLM's output back to itself with a validation prompt.
2. **Token-level [[ConstrainedSampling|constrained sampling]]** — mask invalid tokens at each decoding step.

Ch 6's runnable worked example uses [[llamacpp|`llama-cpp-python`]]'s built-in JSON grammar (`response_format={"type": "json_object"}`) rather than Guidance directly, but Guidance is named as one of the three canonical Python packages in the space.
