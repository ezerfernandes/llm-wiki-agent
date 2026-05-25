---
title: "Colang"
type: concept
tags: [dsl, dialog-flow, nvidia, guardrail]
sources: [dspy-guardrails]
last_updated: 2026-05-22
---

# Colang

**Colang** is the domain-specific language [[NVIDIA]] designed for [[NeMoGuardrails]] — a dialog-flow DSL that lets developers specify conversational rails (allowed user intents, response templates, safety checks, retrieval policies) in a Python-adjacent syntax. Introduced with [[RebedeaEtAl2023|Rebedea et al. 2023]] (*NeMo Guardrails*).

## Position in the guardrail debate

Colang represents the **"safety as hand-authored dialog flows"** design point. The [[dspy-guardrails|DSPy Guardrails paper]] critiques this whole class — *"users need to write specific rules and some prompts manually, which is not universal"* — and replaces it with [[DSPyOptimizers|automatic optimization]] over a [[DSPy]] program.

## See also

- [[NeMoGuardrails]] — the runtime Colang programs target
- [[Guardrail]] — general abstraction
- [[DSPyGuardrails]] — auto-optimized alternative
