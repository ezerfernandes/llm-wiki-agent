---
title: "Llama Guard"
type: concept
tags: [guardrail, safety, meta, classifier]
sources: [dspy-guardrails]
last_updated: 2026-05-22
---

# Llama Guard

**Llama Guard** is an **LLM-based input/output safeguard** for human-AI conversations introduced by [[InanEtAl2023|Inan, Upasani, Chi, Rungta, Iyer, Mao, Tontchev, Hu, Fuller, Testuggine et al. 2023]] ([[meta|Meta]], arXiv:2312.06674). It is a fine-tuned [[meta|Llama]]-family model that classifies prompts and responses against a predefined **safety taxonomy** (violence, sexual content, criminal planning, regulated content, etc.) and emits safe / unsafe judgments plus violated-category labels.

## Position

[[BoxiYu]] & [[PinjiaHe]]'s [[dspy-guardrails|DSPy Guardrails paper]] lists Llama Guard as one of three **manual-configuration baselines** the proposed [[DSPyGuardrails]] method positions itself against:

> *"Existing Guardrails like NeMo Guardrails necessitate manual configuration and prompting, which may not be universally adaptable to counter the evolving jailbreak methodologies."*

The taxonomy is the manual layer — adapting Llama Guard to a new attack family requires curating new training data and re-fine-tuning.

## Comparison

| Guardrail | Manual layer | Adaptation cost |
|---|---|---|
| **Llama Guard** | Safety taxonomy + labeled training data | Retraining |
| [[NeMoGuardrails]] | [[Colang]] dialog flows | Edit flow code |
| [[GuardrailsAI]] | Output validators | Edit validator definitions |
| [[DSPyGuardrails]] | (Auto-optimized) | Re-run [[BootstrapFewShot]] on new examples |

## See also

- [[Guardrail]] — general abstraction
- [[Jailbreak]] / [[CodeAttack]] — attacks Llama Guard would be evaluated against
- [[meta]] — Llama Guard's authoring organization
