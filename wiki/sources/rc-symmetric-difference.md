---
title: "Symmetric difference (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, set-theory, discrete-math]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Symmetric_difference
---

## Summary
Given two sets A and B, compute their symmetric difference: the items that belong to A or B but not to both. This equals (A \ B) ∪ (B \ A), equivalently (A ∪ B) \ (A ∩ B). The key implementation caveat is that when sets are modeled as lists, duplicate elements within a list must be collapsed so they don't distort the result.

## Task Requirements
- Compute the symmetric difference of two sets A and B.
- Optionally also report the individual relative complements A \ B and B \ A.
- Correctly deduplicate when lists are used to represent sets (e.g. ["John","Serena","Bob","Mary","Serena"] and ["Jim","Mary","John","Jim","Bob"] must yield just {"Serena","Jim"}).
- Test case: A = {John, Bob, Mary, Serena}, B = {Jim, Mary, John, Bob} → {Serena, Jim}.

## Language Coverage
113 languages implement this task, spanning functional, imperative, array, and database paradigms — many leverage native set types or set operators. Representative examples include Python, Haskell, Ruby, C++, Java, Clojure, J, APL, Raku, and SQL/PostgreSQL.

## Connections
- [[SetTheory]] — the task is a direct exercise in set operations
- [[SymmetricDifference]] — the named operation being computed
- [[SetUnion]] — used in the (A ∪ B) \ (A ∩ B) formulation
- [[SetIntersection]] — used to remove shared elements
- [[Deduplication]] — required when sets are backed by lists

## Contradictions
- None — reference task page.
