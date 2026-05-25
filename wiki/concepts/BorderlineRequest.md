---
title: "Borderline Request"
type: concept
tags: [llm-security, safety, prompt-engineering, training]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Borderline Request

**A query that admits *both* safe and unsafe valid responses, depending on the user's actual intent.** Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the category that dominates the safety-versus-helpfulness trade-off in production LLM applications.

> "A borderline request is one that can invoke both safe and unsafe responses." — Ch 5

## Canonical example (Ch 5)

> *"What's the easiest way to break into a locked room?"*

Three model behaviors are possible:

| Behavior | Failure mode |
|---|---|
| Provide step-by-step lockpicking instructions | Unsafe — empowers burglars. |
| Refuse to answer | Overly cautious — fails the homeowner locked out of their own home. |
| Suggest legal solutions (call a locksmith) | The correct **safe-helpful** response. |

## Why it matters for safety training

If a model is finetuned *only* on patterns to refuse, it inflates [[FalseRefusalRate|false refusal rate]] on borderline requests. Ch 5 makes this central to the safety-finetuning recommendation:

> "When finetuning a model for safety, it's important to train the model not only to recognize malicious prompts but also to generate safe responses for borderline requests." — Ch 5

The training target is the **third behavior** — recognize the ambiguity, surface the safe interpretation, and provide the helpful answer for that interpretation rather than blanket-refusing.

## Connection to violation/refusal pairing

Borderline requests are the operational reason [[ViolationRate|violation rate]] and [[FalseRefusalRate|false refusal rate]] must be tracked jointly. A model that drives violation rate to zero by refusing borderline requests has solved the wrong problem; a model that answers them unsafely has solved the wrong other problem.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[ViolationRate]] / [[FalseRefusalRate]] — the paired metrics whose trade-off this category dominates.
- [[InstructionHierarchy]] — the post-training scheme that learns to balance safety with helpfulness.
- [[DefensivePromptEngineering]] — parent discipline.
- [[safety]] — broader umbrella.
