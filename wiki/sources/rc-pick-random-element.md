---
title: "Pick random element (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, randomness, arrays]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pick_random_element
---

## Summary
This task asks the programmer to demonstrate how to select a single random element from a list (array). The standard idiom is to generate a uniformly random integer index in the range of the collection's valid indices and use it to subscript the list; many languages also expose a built-in helper that does this directly.

## Task Requirements
- Demonstrate picking a random element from a list/array.

## Language Coverage
144 languages implement this task, a very broad spread reflecting how fundamental the operation is. Representative implementations include Python, Ruby, Perl, C, C++, Java, JavaScript, Go, Rust, Haskell, Lua, and Common Lisp — ranging from those with dedicated helpers (e.g. Python's `random.choice`) to those that compute a random index manually.

## Connections
- [[PseudorandomNumberGenerator]] — supplies the underlying randomness for index selection
- [[UniformDistribution]] — each element should be chosen with equal probability
- [[Array]] — the indexed collection the element is drawn from
- [[Modulo]] — common way to map a raw random number into the valid index range

## Contradictions
- None — reference task page.
