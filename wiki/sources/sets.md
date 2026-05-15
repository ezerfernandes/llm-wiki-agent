---
title: "Sets"
type: source
tags: [math, set-theory, foundations]
date: 2026-05-10
source_file: raw/sets-and-numbers/sets.md
---

## Summary
Foundational treatment of sets: definitions (enumeration vs set-builder), cardinality, subsets, power sets, partitions, set operations (union, intersection, complement, difference, symmetric difference), De Morgan's laws, Cartesian products, and the set-theoretic definition of the ordered pair.

## Key Claims
- A set is a collection of distinguishable objects (elements); membership is unambiguous.
- Cardinality of a power set: \\(|\mathcal{P}(A)| = 2^n\\) for finite \\(A\\) with \\(n\\) elements.
- Inclusion-exclusion: \\(|A \cup B| = |A| + |B| - |A \cap B|\\).
- A partition of \\(A\\) is a family of non-empty, pairwise disjoint subsets covering \\(A\\); it corresponds bijectively to an equivalence relation.
- De Morgan's laws: \\((A \cup B)^c = A^c \cap B^c\\) and \\((A \cap B)^c = A^c \cup B^c\\); they generalise to arbitrary finite collections.
- Symmetric difference + intersection give the powerset of a set the structure of a Boolean ring.
- The Kuratowski definition of the ordered pair: \\((a, b) = \{\{a\}, \{a, b\}\}\\) — yields \\((a,b)=(c,d) \iff a=c \land b=d\\).

## Key Quotes
> "A set can be described by enumeration or by the set-builder notation."
> "Two sets are equal if and only if each is contained in the other."

## Connections
- [[integers|Integers]] — partition example: even / odd integers.
- [[real-numbers|RealNumbers]] — Cartesian plane as \\(\mathbb{R}\times\mathbb{R}\\).
- [[rings|Rings]] — symmetric difference + intersection give a Boolean ring structure.
- [[BooleanAlgebra]] — set operation identities are the foundation of Boolean algebra.
- [[PropositionalLogic]] — De Morgan's laws correspond to logical equivalences \\(\neg(P\lor Q) \equiv \neg P \land \neg Q\\).

## Contradictions
None.
