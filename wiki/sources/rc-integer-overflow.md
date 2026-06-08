---
title: "Integer overflow (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, integer-arithmetic, fixed-width-types]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Integer_overflow
---

## Summary
The task asks the programmer to demonstrate what happens when arithmetic on a language's fixed-size integer types produces a result too large or too small to fit in that type. The key insight is that languages differ sharply in behavior: some silently wrap (modular arithmetic), some throw exceptions or trap, and some have no fixed-size integers at all (arbitrary precision), so the demonstration must surface whichever behavior the language exhibits.

## Task Requirements
- For 32-bit signed, 64-bit signed, 32-bit unsigned, and 64-bit unsigned integers, evaluate the listed expressions whose true results exceed the type's range (e.g. `-(-2147483647-1)`, `2000000000 + 2000000000`, `46341 * 46341`, `(-2147483647-1) / -1`).
- When overflow triggers an exception, show how it is caught.
- When overflow produces a (wrapped) value, print it.
- Explicitly note when overflow is unrecognized and the program continues with wrong results.
- Note when the language has no fixed-size integer type or when overflow cannot occur; arbitrary-precision support may be mentioned but is not to be demonstrated here.

## Language Coverage
81 languages implement this task, spanning low-level assembly, systems languages, and high-level scripting environments. Representative examples include C, C++, Rust, Go, Java, C#, Swift, Ada, Fortran, Python, and 360 Assembly.

## Connections
- [[IntegerOverflow]] — the core phenomenon being demonstrated
- [[ModularArithmetic]] — wraparound semantics for many fixed-width types
- [[TwosComplement]] — signed integer representation underlying the overflow boundaries
- [[FixedWidthIntegers]] — 8/16/32/64-bit signed and unsigned machine types
- [[UndefinedBehavior]] — signed overflow in languages like C

## Contradictions
- None — reference task page.
