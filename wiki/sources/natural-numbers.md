---
title: "Natural Numbers"
type: source
tags: [math, foundations, peano]
date: 2026-05-10
source_file: raw/sets-and-numbers/natural-numbers.md
---

## Summary
Builds \\(\mathbb{N}\\) from two angles: axiomatically via the Peano axioms (P1–P5 with successor function and induction), and concretely via von Neumann's set-theoretic construction \\(0 = \varnothing,\ S(n) = n \cup \{n\}\\). Defines addition and multiplication recursively, derives their algebraic properties, and discusses the well-ordering of \\(\mathbb{N}\\).

## Key Claims
- Peano axioms: \\(0 \in \mathbb{N}\\); successor stays in \\(\mathbb{N}\\); \\(0\\) is no successor; successor is injective; the induction axiom pins down \\(\mathbb{N}\\) as smallest model.
- Von Neumann construction: every \\(n\\) coincides with the set of its predecessors; \\(|n| = n\\).
- Addition/multiplication defined recursively from successor; both are associative, commutative; \\(0\\) is identity for \\(+\\), \\(1\\) for \\(\cdot\\); \\(\cdot\\) distributes over \\(+\\).
- \\(\mathbb{N}\\) has no zero divisors.
- Order \\(m \leq n \iff \exists k\, n = m+k\\) is a total well-ordering; well-ordering is equivalent to the induction principle.

## Key Quotes
> "Each natural number coincides with the set of all its predecessors, so that the number n has exactly n elements."
> "Well-ordering ... is logically equivalent to the principle of induction."

## Connections
- [[sets|Sets]] — von Neumann construction sits in set theory.
- [[PrincipleOfMathematicalInduction]] — the fifth Peano axiom.
- [[Functions]] — the successor function.
- [[types-of-numbers|TypesOfNumbers]] — \\(\mathbb{N}\\) as smallest layer.
- [[integers|Integers]] — extension resolving subtraction.

## Contradictions
None.
