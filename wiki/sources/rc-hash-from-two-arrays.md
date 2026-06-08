---
title: "Hash from two arrays (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hash_from_two_arrays
---

## Summary
The task asks the programmer to take two arrays of equal length and combine them into a single hash (associative array / map), treating one array as the keys and the parallel array as the corresponding values. The key insight is the element-wise pairing of two sequences by shared index position, an operation often expressed via a "zip" primitive or a parallel iteration.

## Task Requirements
- Start with two arrays of equal length.
- Use one array as the keys and the other as the values.
- Produce a single hash/map object linking each key to the value at the same index.

## Language Coverage
137 languages implement this task, reflecting very broad coverage across functional, scripting, object-oriented, and assembly languages. Representative implementations include Python, Perl, Ruby, JavaScript, Haskell, Java, C++, Go, Rust, Clojure, and Lua.

## Connections
- [[AssociativeArray]] — the resulting hash is an associative array (key-value map).
- [[Zip]] — pairing two equal-length sequences element-wise is the canonical zip operation.
- [[HashTable]] — common underlying implementation of the resulting map.
- [[ParallelIteration]] — iterating two arrays together by index drives the construction.

## Contradictions
- None — reference task page.
