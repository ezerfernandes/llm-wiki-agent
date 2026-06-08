---
title: "Sorting algorithms/Sleep sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, concurrency]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Sleep_sort
---

## Summary
Implement "sleep sort," a novelty sorting technique that spawns a separate concurrent task for each input value. Each task sleeps for a duration proportional to its item's sort key and then emits that item, so values are naturally collected in ascending order as their timers fire. The key insight is that the ordering work is offloaded to the scheduler's timing rather than any comparison logic, which makes it impractical (its running time depends on the magnitude of the values) but a striking demonstration of concurrency.

## Task Requirements
- Write a program that implements sleep sort.
- Accept non-negative integers as input (idiomatically from the command line).
- Print the integers in sorted order.
- Alternative input/output is allowed if the command-line convention is not idiomatic for the language.
- Optimization, generalization, robustness, etc. are explicitly not required.

## Language Coverage
71 languages implement this task, spanning systems languages, scripting languages, functional languages, and even esoteric ones, since almost any environment with threads, timers, or async support can express it. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Erlang, Bash, and Brainf***.

## Connections
- [[SortingAlgorithm]] — sleep sort is a (non-comparison, non-practical) member of this family
- [[Concurrency]] — relies on independent tasks running in parallel
- [[Threading]] — each item typically runs in its own thread or async task
- [[SchedulerTiming]] — correctness depends on the OS/runtime timer ordering

## Contradictions
- None — reference task page.
