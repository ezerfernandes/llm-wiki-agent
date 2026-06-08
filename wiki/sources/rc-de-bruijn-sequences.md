---
title: "De Bruijn sequences (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/De_Bruijn_sequences
---

## Summary
A de Bruijn sequence B(k, n) is a cyclic string over a size-k alphabet in which every possible length-n string appears exactly once as a contiguous (wrap-around) substring, giving it the minimal length of k^n. The task frames this through brute-forcing a keyless PIN lock that only inspects the last n digits entered: a single de Bruijn sequence of length k^n + (n-1) presses tries every code, instead of n * k^n presses for separate attempts. The concrete case is B(10, 4), a 10,000-digit sequence covering all 10,000 four-digit decimal PINs.

## Task Requirements
- Generate a de Bruijn sequence for a 4-digit decimal PIN code (B(10, 4)) and show its length (10,000).
- Show the first and last 130 digits of the sequence.
- Verify that all 1,000... actually all 10,000 four-digit PINs (0000 through 9999, with leading zeros) appear in the sequence.
- Reverse the sequence and run the verification again.
- Replace the 4,444th digit of the original sequence with a period (.) and verify once more — exactly four PIN codes should now be missing, and the verifier must list any and all missing codes.
- Show all output.

## Language Coverage
46 languages implement this task, spanning assembly through functional and array languages — representative examples include C++, Java, Python, Rust, Go, Haskell, Raku, J, Uiua, and 8080 Assembly.

## Connections
- [[DeBruijnSequence]] — the central combinatorial object being constructed.
- [[Combinatorics]] — the mathematical field that studies these optimally short cyclic sequences.
- [[EulerianPath]] — standard construction traverses an Eulerian/Hamiltonian path on a de Bruijn graph.
- [[BruteForceAttack]] — the practical motivation: shortening exhaustive PIN search on keyless locks.
- [[StringProcessing]] — verification relies on substring containment checks across the generated sequence.

## Contradictions
- None — reference task page.
