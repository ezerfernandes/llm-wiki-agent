---
title: "9 billion names of God the integer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics, dynamic-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/9_billion_names_of_God_the_integer
---

## Summary
A "name" of integer n is one of its additive compositions into non-increasing parts (i.e. an integer partition), so the count of names of n equals the number of partitions of n. The task asks the programmer to build a number triangle where the cell in row m, column C counts partitions of m whose largest part is exactly C, then sum each row. The key insight is that each row sum G(n) equals the integer partition function P(n), and both can be computed efficiently with a recurrence rather than enumeration, since the values grow enormous (the title alludes to Clarke's story).

## Task Requirements
- Display the first 25 rows of the partition triangle, where cell (row m, column C) is the number of partitions of m with largest part C.
- Implement a function G(n) returning the sum of the n-th row.
- Demonstrate G(n) for n = 23, 123, 1234, and 12345.
- Note that the row sum equals the integer partition function P(n); demonstrate equivalence by also printing P(23), P(123), P(1234), and P(12345).
- Extra credit: plot P(n) against n for n = 1..999.

## Language Coverage
75 languages implement this task, a broad cross-section spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Julia, Raku, J, and Wren.

## Connections
- [[IntegerPartition]] — names of n are exactly the partitions of n
- [[PartitionFunction]] — the row sum G(n) equals P(n)
- [[DynamicProgramming]] — the triangle/recurrence avoids enumerating each partition
- [[Combinatorics]] — counting decompositions into summands
- [[BigIntegerArithmetic]] — P(12345) far exceeds native integer ranges

## Solved in (Rosetta Code languages)
Solved in **68** of the wiki's catalogued languages (Rosetta Code shows 75 language sections for this task). (7 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Ada]], [[ALGOL 68]], [[ARM Assembly]], [[AutoHotkey]], [[C]], [[C++]], [[Clojure]], [[Common Lisp]], [[Crystal]], [[D]], [[Dart]], [[Delphi]], [[Dyalect]], [[EasyLang]], [[Elixir]], [[Erlang]], [[Factor]], [[Forth]], [[FreeBASIC]], [[Frink]], [[FutureBasic]], [[GAP]], [[Go]], [[Groovy]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Kotlin]], [[Lasso]], [[Lua]], [[Maple]], [[Maxima]], [[Nim]], [[OCaml]], [[Ol]], [[PARI-GP]], [[Perl]], [[Phix]], [[Phixmonti]], [[Picat]], [[PicoLisp]], [[Pike]], [[Pluto]], [[PureBasic]], [[Python]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[Red]], [[REXX]], [[Ruby]], [[Rust]], [[Scala]], [[Sidef]], [[SPL]], [[Stata]], [[Swift]], [[Tcl]], [[V (Vlang)]], [[VBA]], [[Wren]], [[Yabasic]], [[Zig]]

## Contradictions
- None — reference task page.
