---
title: "Floyd's triangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, text-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Floyd's_triangle
---

## Summary
Floyd's triangle is a left-aligned right triangle that lists the natural numbers consecutively: row 1 holds 1, row 2 holds 2 and 3, row 3 holds 4, 5, 6, and so on, with each row containing one more number than the row above it. The task is to generate and print the first n rows. The key insight is that the largest value (in the bottom-right corner) determines the column width needed, so each column must be padded to align under the widest entry in that column for clean mono-space display.

## Task Requirements
- Generate and display the first n lines of a Floyd triangle, for n=5 and n=14.
- Row k starts with the next consecutive natural number and contains k numbers total.
- When rendered in a mono-space font, numbers must line up in vertical columns.
- Only a single space should separate the numbers in the final (widest) row.

## Language Coverage
112 languages implement this task, spanning systems, scripting, functional, and array languages as well as many BASIC dialects. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Ruby, Perl, and APL.

## Connections
- [[NaturalNumbers]] — the triangle is built from consecutive natural numbers.
- [[TriangularNumbers]] — the last value in row n equals the nth triangular number.
- [[TextFormatting]] — column alignment and field-width padding for mono-space output.
- [[Iteration]] — nested loops over rows and columns generate the values.

## Contradictions
- None — reference task page.
