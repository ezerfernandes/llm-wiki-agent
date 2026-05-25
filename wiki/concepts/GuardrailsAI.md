---
title: "Guardrails AI"
type: concept
tags: [guardrail, safety, validator]
sources: [dspy-guardrails]
last_updated: 2026-05-22
---

# Guardrails AI

**Guardrails AI** is an open-source library and platform for adding **validators** and **output specifications** around LLM calls — schemas, regexes, semantic checks, PII filters, profanity filters, etc. — introduced by [[Rajpal2023|Shreya Rajpal (2023)]] ([guardrailsai.com](https://www.guardrailsai.com/)). Validators run on the LM output and either pass, fix (auto-repair), or fail.

## Position

[[BoxiYu]] & [[PinjiaHe]]'s [[dspy-guardrails|DSPy Guardrails paper]] lists Guardrails AI alongside [[LlamaGuard]] and [[NeMoGuardrails]] as a **manually-configured** baseline. The validators must be written by hand and maintained as new attack surfaces emerge — the same critique applies as to [[NeMoGuardrails]]'s [[Colang]] flows.

## See also

- [[Guardrail]] — general abstraction
- [[LlamaGuard]] / [[NeMoGuardrails]] — sibling baselines
- [[DSPyGuardrails]] — auto-optimized alternative
