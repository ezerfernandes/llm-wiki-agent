---
title: "Associative array/Merging (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, hash-map]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Associative_array/Merging
---

## Summary
The task asks the programmer to merge two associative arrays (maps/dictionaries) — a "base" map and an "update" map — into a new map containing every key from either source. When a key exists in both, the value from the update map wins; otherwise the base value is kept. The key insight is to perform this as a non-destructive ("immutable") operation that leaves the two original maps unmodified, which many languages express with a single built-in operation.

## Task Requirements
- Define a "base" associative array (name/price/color) and an "update" associative array (price/color/year).
- Produce a new associative array holding the union of all keys from both.
- For shared keys, the update map's value takes precedence over the base map's value.
- If possible, do not mutate either of the two original associative arrays.
- The approach must be general, working for arbitrary data, not just the sample values.

## Language Coverage
69 languages implement this task, reflecting that key-value merging is a near-universal data-structure operation. Representative implementations include Python, JavaScript, Ruby, Rust, Go, Haskell, Clojure, C#, Java, Perl, and Raku — many of which expose this via a single spread/union/update primitive (e.g. dict unpacking, `Object.assign`, or `merge`).

## Connections
- [[AssociativeArray]] — the core data structure being merged
- [[HashMap]] — the typical implementation backing these maps
- [[ImmutableDataStructures]] — the non-mutating "produce a new map" requirement
- [[KeyValueStore]] — the abstract model of the data being combined

## Contradictions
- None — reference task page.
