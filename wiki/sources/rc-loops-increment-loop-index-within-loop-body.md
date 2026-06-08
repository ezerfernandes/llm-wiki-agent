---
title: "Loops/Increment loop index within loop body (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loops/Increment_loop_index_within_loop_body
---

## Summary
This task demonstrates how to mutate a loop's iterator from inside the loop body, on top of the normal per-iteration increment supplied by the loop construct. The concrete exercise starts the index at 42, advances it by one each iteration, and whenever the index is prime, prints the running count and that prime, then jumps the index forward by the prime's own value. The key insight is that many languages forbid modifying a counted-`for` index, so the idiomatic workaround is usually a `while` loop with an explicit counter variable.

## Task Requirements
- Start the index variable at 42.
- Increment the index by one at each iteration (the loop's normal step).
- When the index is prime: display the count of primes found so far together with the prime, then add that prime to the index (so the next index becomes old index + prime).
- Terminate the loop once 42 primes have been displayed.
- Extra credit: format the (large) primes with thousands separators (commas) for readability.
- Note where a language's loop index cannot be modified and describe the idiomatic alternative used.

## Language Coverage
78 languages implement this task, spanning assembly (360 Assembly, ARM, AArch64), systems languages (C, C++, Rust-adjacent Zig), functional languages (Haskell, F#, Standard ML, Common Lisp), scripting languages (Python, Perl, Raku, Ruby, AWK, Tcl), and many BASIC dialects (FreeBASIC, Yabasic, S-BASIC). The breadth highlights how differently each language treats whether and how a loop counter may be reassigned inside the body.

## Connections
- [[PrimalityTesting]] — each candidate index must be checked for primeness
- [[ControlFlow]] — the task is fundamentally about loop iterator mutation
- [[WhileLoop]] — the common idiom when counted-for indices are immutable
- [[NumberFormatting]] — the extra-credit comma grouping of large integers

## Contradictions
- None — reference task page.
