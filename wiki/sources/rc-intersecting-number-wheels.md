---
title: "Intersecting number wheels (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, state-machines, generators, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Intersecting_number_wheels
---

## Summary
The task models a system of "number wheels," each named by an uppercase letter and holding an ordered cycle of values that are either literal numbers or references to other wheels. Reading a wheel advances its own position and yields the next number; when a value is a reference, the program instead pulls the next value from the named wheel. The key insight is that each wheel has a single shared position, so multiple references to the same wheel cooperatively advance one cursor, producing intricate (and possibly non-terminating) intertwined sequences.

## Task Requirements
- Represent wheels as named cycles of values, where each value is either a number (yielded directly) or a name (delegating to that wheel's next value).
- Treat the first defined wheel in a group as the entry point for generation.
- Ensure a wheel referenced from multiple places shares one advancing position rather than independent cursors.
- Generate and print the first twenty terms for four given wheel groups (A:1 2 3; A:1 B 2 with B:3 4; A:1 D D with D:6 7 8; A:1 B C with B:3 4 and C:5 B).

## Language Coverage
33 languages implement this task, spanning systems, functional, scripting, and array families. Representative entries include C, C++, C#, Java, Go, Rust-adjacent Nim, Haskell, F#, Julia, Python, Perl, Raku, Ruby, JavaScript, J, and Factor.

## Connections
- [[StateMachine]] — each wheel is a small cyclic state machine with a persistent position
- [[Generators]] — terms are produced lazily one at a time, a natural fit for generator/iterator constructs
- [[Recursion]] — resolving a name reference recursively descends into another wheel until a number is yielded
- [[MutualRecursion]] — wheels can reference each other, forming mutually dependent cycles
- [[SharedState]] — a multiply-referenced wheel exposes one shared, mutable position

## Contradictions
- None — reference task page.
