---
title: "NeMo Guardrails"
type: concept
tags: [guardrail, safety, nvidia, dialog-flow]
sources: [dspy-guardrails]
last_updated: 2026-05-22
---

# NeMo Guardrails

**NeMo Guardrails** is [[NVIDIA]]'s toolkit for adding programmable safety rails to LLM applications, introduced by [[RebedeaEtAl2023|Rebedea, Dinu, Sreedhar, Parisien & Cohen 2023]] (arXiv:2310.10501, *"NeMo Guardrails: A toolkit for controllable and safe LLM applications with programmable rails"*). Safety policies are expressed in **[[Colang]]**, a domain-specific dialog-flow language, which the runtime executes around each LM call (input rails, output rails, dialog rails, retrieval rails, execution rails).

## Position

[[BoxiYu]] & [[PinjiaHe]]'s [[dspy-guardrails|DSPy Guardrails paper]] lists NeMo Guardrails as the canonical example of the **manual-configuration baseline** they critique:

> *"To use these Guardrails, users need to write specific rules and some prompts manually, which is not universal. In addition, jailbreak techniques are constantly evolving every day."*

NeMo's [[Colang]] flows must be hand-written and maintained as attack distributions shift. The [[DSPyGuardrails]] argument: replace the [[Colang]]-author with an auto-optimizer.

## See also

- [[Guardrail]] — general abstraction
- [[Colang]] — NeMo's dialog DSL
- [[NVIDIA]] — authoring organization
- [[LlamaGuard]] / [[GuardrailsAI]] — sibling baselines
- [[DSPyGuardrails]] — auto-optimized alternative
