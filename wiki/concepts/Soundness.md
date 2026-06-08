---
title: "Soundness"
type: concept
tags: [logic, critical-thinking, deductive-reasoning, foundational]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Soundness

A **sound** argument is **a [[Validity|valid]] argument that has all true premises**. Because validity transmits truth from premises to conclusion, **the conclusion of a sound argument is guaranteed true**.

## Relationship to validity
[[logic-text-v2|Van Cleave]] (§1.7) states the asymmetry crisply:

> **All sound arguments are valid arguments, but not all valid arguments are sound arguments.**

Soundness adds exactly one requirement to validity — that the premises actually be true:

| | valid? | all premises true? | conclusion guaranteed true? |
|---|---|---|---|
| Valid but unsound | ✓ | ✗ | ✗ |
| **Sound** | ✓ | ✓ | ✓ |
| Invalid | ✗ | — | ✗ |

## Why logic mostly ignores soundness
Verifying whether the premises are *actually* true "has nothing to do with logic, per se" — you consult biology, history, Google, or experts, not logic. So the book (and formal logic generally) concentrates on **[[Validity|validity]]**, which *is* a logical property, and treats soundness as "outside the purview of logic." Soundness is nonetheless what any good [[Argument|argument]] should ultimately aim for: a valid argument with false premises "doesn't provide any reason for accepting the conclusion."

## Connections
- [[Validity]] — the property soundness is defined on top of.
- [[Argument]] — what soundness evaluates.
- [[DeductiveReasoning]] — soundness applies to deductive arguments.
- [[CriticalThinking]] — assessing premise truth is the empirical half of evaluation.
- [[logic-text-v2]] — canonical source (§1.7).
