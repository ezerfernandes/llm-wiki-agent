---
title: "Validity"
type: concept
tags: [logic, critical-thinking, deductive-reasoning, foundational]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Validity

An [[Argument|argument]] is **valid** iff it is **impossible for all the premises to be true while the conclusion is false** — equivalently, *if* the premises were true, the conclusion *would have to be* true. Validity is a property of **deductive** arguments ([[DeductiveReasoning]]).

## Validity is about form, not truth
The single most-repeated lesson of [[logic-text-v2|Van Cleave]] Ch 1: **validity does not depend on whether the premises (or conclusion) are actually true.** It depends only on the **logical relationship** between them.

```
1. A person can be President of the U.S. only if they were born in Kenya   (false!)
2. Obama is President of the U.S.
3. Therefore, Obama was born in Kenya
```
This argument is **valid** — *if* the premises held, the conclusion would follow — even though premise 1 is false. (To also get a true conclusion you need [[Soundness|soundness]].)

## The informal test of validity
Van Cleave's Chapter-1 method, applicable before any formal apparatus:

> Try to **imagine a scenario** in which all the premises are true and yet the conclusion is false.
> - If you **can** construct such a scenario, that scenario is a **counterexample** and the argument is **invalid**.
> - If you **cannot** (it is genuinely impossible), the argument is **valid**.

A single counterexample is decisive proof of invalidity. The formal methods of Chapter 2 mechanize this same idea: the [[TruthTable|truth-table test of validity]] checks every row for a "premises-true / conclusion-false" line; [[RulesOfInference|proofs]] derive the conclusion by valid steps; [[CategoricalLogic|Venn diagrams]] test categorical syllogisms.

## Validity vs. strength
Validity is **all-or-nothing** and belongs to deductive arguments. The inductive analogue is **strength** — an [[InductiveReasoning|inductive argument]] can make its conclusion highly probable without guaranteeing it, and is **defeasible** (further premises can defeat it), whereas a valid deductive argument is not.

## Connections
- [[Soundness]] — validity *plus* true premises.
- [[Argument]] — what validity is a property of.
- [[DeductiveReasoning]] — the argument class validity applies to.
- [[TruthTable]] / [[RulesOfInference]] / [[CategoricalLogic]] — the formal tests of validity.
- [[LogicalFallacy]] — invalid forms (denying the antecedent, affirming the consequent).
- [[logic-text-v2]] — canonical source (§1.6).
