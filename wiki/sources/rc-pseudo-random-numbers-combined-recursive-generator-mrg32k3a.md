---
title: "Pseudo-random numbers/Combined recursive generator MRG32k3a (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, prng, number-theory, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pseudo-random_numbers/Combined_recursive_generator_MRG32k3a
---

## Summary
The task asks the programmer to implement L'Ecuyer's MRG32k3a combined multiple recursive pseudo-random number generator. The generator runs two independent third-order linear recurrences modulo two distinct primes (m1 = 2^32 - 209 and m2 = 2^32 - 22853), then combines their latest outputs by subtraction modulo m1 to produce each value. The key insight is that combining two well-chosen recursive generators yields a far longer period and better statistical quality than either alone.

## Task Requirements
- Build a class or set of functions implementing MRG32k3a with `seed`, `next_int`, and `next_float` methods, using the given constants a1=[0,1403580,-810728], a2=[527612,0,-1370589], and d = m1 + 1.
- Seed each generator's three-element state with the seed value, advance via the modular recurrences, keep the last three values, and compute `z = (x1i - x2i) mod m1`, returning `z + 1`.
- Show the first five integers from seed `1234567` match: 1459213977, 2827710106, 4245671317, 3877608661, 2595287583.
- For seed `987654321`, tally 100,000 results of `floor(next_float() * 5)` and confirm counts: 0:20002, 1:20060, 2:19948, 3:20059, 4:19931.
- Display the output on the page.

## Language Coverage
26 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and Forth.

## Connections
- [[PseudorandomNumberGenerator]] — MRG32k3a is one specific PRNG design.
- [[ModularArithmetic]] — the recurrences and combination step are computed modulo large primes.
- [[LinearRecurrence]] — each sub-generator is a third-order linear recurrence.
- [[LEcuyerCombinedGenerator]] — the named technique this task implements.

## Contradictions
- None — reference task page.
