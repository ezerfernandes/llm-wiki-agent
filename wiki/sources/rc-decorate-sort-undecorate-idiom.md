---
title: "Decorate-sort-undecorate idiom (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, functional-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Decorate-sort-undecorate_idiom
---

## Summary
The task asks the programmer to sort a list of words by length using the decorate-sort-undecorate idiom (also known as the Schwartzian transform). Instead of sorting with a custom comparator that recomputes an expensive key on every comparison, each element is first paired with its precomputed key (decorate), the pairs are sorted by that key (sort), and the keys are then stripped off (undecorate). The central insight is that the key is computed exactly once per element, so decoration acts as a form of memoization.

## Task Requirements
- Write a function/procedure/method that sorts a list of words by length using the decorate-sort-undecorate idiom.
- Bonus 1: accept the key function as a callback.
- Bonus 2: implement it as a true "Schwartzian transform" that uses no named temporary lists/arrays (a functional composition of map-sort-map).
- Optionally show two solutions: one with named intermediate lists (often clearer) and one without.

## Language Coverage
38 languages implement this task, spanning functional, imperative, array, and scripting paradigms. Representative implementations include Perl (the idiom's origin via Randal Schwartz), Python, Haskell, Ruby, Raku, JavaScript, Go, Rust, C++, and J.

## Connections
- [[SchwartzianTransform]] — the Perl-popularized name for this exact idiom
- [[Memoization]] — the key precomputation is a form of caching key values
- [[Sorting]] — the underlying operation, typically driven by a custom comparator
- [[HigherOrderFunctions]] — Bonus 1 passes the key function as a callback
- [[FunctionalComposition]] — the Schwartzian variant chains map-sort-map without named temporaries

## Contradictions
- None — reference task page.
