---
title: "Rate counter (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, benchmarking, timing, performance]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rate_counter
---

## Summary
This task asks the programmer to build a rate counter: code that measures how quickly a repeated job is being executed. The key idea is to time many runs of some operation and report the throughput (jobs per unit time), while being mindful of the resolution and accuracy of the platform's timing mechanism.

## Task Requirements
- Implement code that measures the rate at which a repeatedly-performed job runs.
- Either run a fixed number of seconds (N) worth of jobs, and/or run a fixed number of jobs (Y).
- Report at least three distinct timings.
- Be aware of and, where possible, document the precision and accuracy limitations of the timing mechanism used.

## Language Coverage
58 languages implement this task, spanning systems and scripting languages as well as many BASIC dialects. Representative implementations include C, C++, Go, Java, Python, Perl, Ruby, Haskell, Common Lisp, and Tcl.

## Connections
- [[Benchmarking]] — measuring execution throughput is the core purpose
- [[SystemTime]] — relies on reading the system clock to compute elapsed durations
- [[ClockResolution]] — timing precision and accuracy bound the measurement quality
- [[Throughput]] — the reported metric is jobs completed per unit time

## Contradictions
- None — reference task page.
