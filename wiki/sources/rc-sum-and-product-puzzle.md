---
title: "Sum and product puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, logic-puzzle, constraint-solving]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sum_and_product_puzzle
---

## Summary
The task is to programmatically solve the classic "Impossible Puzzle" (Freudenthal's problem): two whole numbers X and Y satisfy 2 ≤ X < Y and X + Y ≤ 100, where mathematician S knows only the sum and P knows only the product. A three-line dialog encodes facts that, when applied as filters, leave a single solution. The key insight is that each statement is a meta-fact about how many decompositions remain consistent with prior statements, so the puzzle is solved by iterated elimination over all candidate pairs.

## Task Requirements
- Consider all candidate pairs (X, Y) with 2 ≤ X < Y ≤ 98 (sum ≤ 100).
- Fact 1 (S: "P does not know X and Y"): every sum decomposition of X+Y yields a product with more than one decomposition.
- Fact 2 (P: "Now I know X and Y"): the product X*Y has exactly one decomposition for which Fact 1 holds.
- Fact 3 (S: "Now I also know X and Y"): the sum X+Y has exactly one decomposition for which Fact 2 holds.
- Apply the three facts successively; exactly one solution remains.

## Language Coverage
40 languages implement this task, spanning systems and functional styles. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Julia, Racket, and Raku.

## Connections
- [[NumberTheory]] — relies on integer factorization and additive partitions.
- [[ConstraintSatisfaction]] — solved by iterative candidate elimination over a bounded search space.
- [[CommonKnowledge]] — the dialog encodes epistemic/common-knowledge reasoning between agents.
- [[BruteForceSearch]] — enumerates all valid (X, Y) pairs before filtering.

## Contradictions
- None — reference task page.
