---
title: "Loops/Continue (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loops/Continue
---

## Summary
This task asks the programmer to print the numbers 1 through 10 using a single loop, formatted as five comma-separated values per line across two lines. The intended technique is to skip the rest of the current iteration's body (forcing the next iteration) on a specific condition rather than printing a newline directly — that is, demonstrating a language's `continue`-style construct to control output flow.

## Task Requirements
- Produce the exact output: `1, 2, 3, 4, 5` on the first line and `6, 7, 8, 9, 10` on the second.
- Use only one loop.
- Achieve the line break by forcing the next iteration upon a condition (e.g. every multiple of 5), using the language's continue/skip mechanism where available.

## Language Coverage
164 languages implement this task, reflecting that early-exit-of-iteration is a near-universal control-flow primitive. Representative implementations include C, C++, Java, Python, JavaScript, Go, Rust, Haskell, Ruby, and REXX, alongside assembly variants and many BASIC dialects.

## Connections
- [[ControlFlow]] — the task exercises mid-loop flow redirection
- [[Iteration]] — single-loop traversal over a numeric range
- [[ContinueStatement]] — the named construct the task is built around
- [[ConditionalBranching]] — the per-iteration condition that triggers the skip

## Contradictions
- None — reference task page.
