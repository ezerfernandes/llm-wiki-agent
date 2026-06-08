---
title: "Categorical Logic"
type: concept
tags: [logic, deductive-reasoning, syllogism, venn-diagram]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Categorical Logic

**Categorical logic** is the logic of relationships between **categorical statements** — statements about a category or type of thing ("All humans are mortal"). Its logical terms are **"all"** and **"some"**, and its capital letters stand for **categories of things in the world** (noun phrases), *not* for atomic propositions as in [[PropositionalLogic|propositional logic]].

## Why propositional logic is not enough
[[logic-text-v2|Van Cleave]] §2.14 motivates categorical logic by a valid argument propositional logic **cannot** capture:
```
1. All humans are mortal
2. All mortal things die
3. ∴ All humans die
```
Each premise is atomic in propositional logic (`H`, `M`, `D`), giving the obviously invalid form `H, M ∴ D`. Yet the argument is plainly valid. This exposes a **real limitation of propositional logic** and is the reason other formal logics exist.

## The four categorical forms (A / E / I / O)
With **S** = subject term, **P** = predicate term:

| | Form | Name | Quantity/Quality |
|---|---|---|---|
| **A** | All S are P | universal affirmative | universal, affirmative |
| **E** | No S are P | universal negative | universal, negative |
| **I** | Some S are P | particular affirmative | particular, affirmative |
| **O** | Some S are not P | particular negative | particular, negative |

## Venn diagrams
A **Venn diagram** graphically represents a categorical statement with overlapping circles. **Shading** an area means "nothing exists here"; an **×** means "something exists here." "All S are P" shades the part of S outside P. Van Cleave uses Venn diagrams as the **test of validity** for both **immediate inferences** (one premise) and **categorical syllogisms** (two premises, three terms): diagram the premises, then check whether the conclusion is *already* drawn.

A subtlety the book flags (§2.16): **universal statements and existential commitment** — whether "All S are P" implies that any S actually exists affects which syllogisms come out valid.

## Connections
- [[PropositionalLogic]] — the system categorical logic supplements; its expressive gap motivates this one.
- [[Validity]] — Venn diagrams are categorical logic's validity test.
- [[RulesOfInference]] — propositional logic's proof method, the complementary formal tool.
- [[DeductiveReasoning]] — categorical syllogisms are deductive.
- [[logic-text-v2]] — canonical source (§2.14–2.17).
