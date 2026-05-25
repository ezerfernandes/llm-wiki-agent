---
title: "PII Reverse Dictionary"
type: concept
tags: [privacy, guardrail, pii, masking, third-party-api]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# PII Reverse Dictionary

**A masking pattern for safely sending data through third-party model APIs: replace sensitive substrings with placeholders before egress, keep a reverse map, and restore the originals on the response side.** Named explicitly in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] (Figure 10-3) as the canonical [[InputGuardrail|input-guardrail]] technique for [[PII|PII]] protection when self-hosting isn't an option.

## The pattern

1. **Detect** — an AI- or rules-based detector scans the outgoing prompt for sensitive classes (personal info, faces, IP-marked phrases).
2. **Mask** — replace each detected value with a placeholder (e.g., a phone number `617-555-0123` becomes `[PHONE NUMBER]`).
3. **Store** — keep the mapping `[PHONE NUMBER]` → `617-555-0123` in a *reverse dictionary* keyed to this request.
4. **Send** — only the masked prompt leaves the organization.
5. **Restore** — when the model's response is returned, scan it for placeholders and substitute the original values from the reverse dictionary.

> *"You can mask a user's phone number with the placeholder [PHONE NUMBER]. If the generated response contains this placeholder, use a PII reverse dictionary that maps this placeholder to the original information so that you can unmask it."* — Ch 10

## Common sensitive classes

Ch 10 enumerates:

- **Personal information** — ID numbers, phone numbers, bank accounts.
- **Human faces** — for multimodal inputs.
- **Specific keywords / phrases** — company IP, codenames, privileged information.

## Why "reverse"

The dictionary direction is *placeholder → original*, applied on the response. If the model parrots `[PHONE NUMBER]` in its output, the reverse map restores the real value before the user sees it. The forward direction (original → placeholder) is the masking step.

## Limits

- **Detection isn't airtight.** *"There's no airtight way to eliminate potential leaks when using third-party APIs."* AI-based detectors miss novel phrasings; rule-based detectors miss obfuscated formats.
- **Block-the-whole-query fallback.** If detection fires on something the user *wants* the model to see, the alternative to masking is **rejection** — *"block the entire query or remove the sensitive information from it."*
- **Doesn't help against egress logging.** The third-party provider can still see the placeholder-laden prompt; the dictionary only stops *leakage of the original values*.

## The motivating incident

Ch 10's footnote: a Samsung employee pasted proprietary code into ChatGPT, *"accidentally leaking the company's secrets."* This is the canonical incident the pattern is designed to prevent at the application layer.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[Guardrail]] / [[InputGuardrail]] — parent category.
- [[PII]] — what is being detected and masked.
- [[OutputGuardrail]] — the response-side restoration is technically an output guardrail step.
- [[DataLeakage]] — the broader failure mode this defends against.
- [[ModelAPIProvider]] — third-party providers are the threat model.
