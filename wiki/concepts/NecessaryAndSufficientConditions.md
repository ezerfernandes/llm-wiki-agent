---
title: "Necessary and Sufficient Conditions"
type: concept
tags: [logic, critical-thinking, causal-reasoning, inductive-reasoning]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Necessary and Sufficient Conditions

A **necessary condition** for an effect is one that **must be present** for the effect to occur (oxygen for a flame; gas in the tank for a running car). A **sufficient condition** is one that, **if present, always brings about** the effect (being fed through a wood chipper is sufficient for death). [[logic-text-v2|Van Cleave]] §3.4 uses these to analyze **causal reasoning** as a kind of [[InductiveReasoning|inductive]] argument.

## Causes and background conditions
No event causes an effect alone; every cause operates against a web of **background conditions** (striking a match lights it *only given* oxygen, dry match, etc.). Which condition we *call* "the cause" is partly contextual — in outer space, spraying oxygen is "the cause" of the flame. A **causal generalization** has the form:

> For any *x*, if *x* has feature(s) **F**, then *x* has feature **G**.

## The two elimination tests
Given a presence/absence table of candidate features (A, B, C, D) against a target effect (S) across observed cases, two tests narrow down the cause (a Mill-style eliminative method, drawn from Sinnott-Armstrong & Fogelin):

- **Necessary-condition test** — *any candidate that is **absent when the target is present** is eliminated* as a necessary condition. (If S happened without A, then A isn't required for S.)
- **Sufficient-condition test** — *any candidate that is **present when the target is absent** is eliminated* as a sufficient condition. (If A happened without S, then A alone doesn't force S.)

When no single feature is sufficient, two features may be **jointly sufficient** (no case where both are present yet the target is absent). The same logic supports **diagnosis**: check each necessary condition in turn to find what failed (the match didn't light → are the matches wet?).

## Connection to conditionals
These conditions are the semantic content behind the **conditional** (`⊃`) of [[PropositionalLogic|propositional logic]] (§2.7): "A only if B" makes B necessary for A; "if A then B" makes A sufficient for B.

## Connections
- [[InductiveReasoning]] — causal arguments are inductive.
- [[PropositionalLogic]] — necessary/sufficient is the meaning of the conditional.
- [[InferenceToBestExplanation]] — sibling Ch 3 tool; causal claims are often the best explanation.
- [[CriticalThinking]] — assessing causal generalizations is a core skill.
- [[logic-text-v2]] — canonical source (§3.4).
