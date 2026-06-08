---
title: "Time a function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, benchmarking, profiling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Time_a_function
---

## Summary
This task asks the programmer to write a program that uses a timer at the finest granularity available on the system to measure how long a given function takes to execute. The key insight is to prefer methods that measure only the CPU/processing time consumed by the current process, rather than naive wall-clock elapsed time, which can be inflated by other concurrent processes on the machine.

## Task Requirements
- Use a timer with the least (finest) granularity available on the system.
- Time how long a target function takes to execute.
- Where possible, measure only the processing time used by the current process, not wall-clock system time, to exclude time consumed by other processes.
- This task serves as a subtask for measuring the relative performance of sorting algorithm implementations.

## Language Coverage
121 languages implement this task, giving very broad coverage across compiled, interpreted, functional, and assembly languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, OCaml, and Ruby.

## Connections
- [[Benchmarking]] — the task is a minimal benchmarking harness.
- [[CPUTime]] — emphasizes process CPU time over wall-clock time.
- [[HighResolutionTimer]] — requires the finest available clock granularity.
- [[Profiling]] — closely related to measuring per-function execution cost.
- [[SortingAlgorithms]] — explicitly framed as a subtask for comparing sort implementations.

## Contradictions
- None — reference task page.
