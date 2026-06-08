---
title: "Averages/Simple moving average (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, closures, streaming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Averages/Simple_moving_average
---

## Summary
The task is to implement a stateful simple moving average (SMA) over a stream of numbers. The programmer writes an initializer that takes a period P and returns a routine which, on each call with a new number, returns the mean of (up to) the last P values seen so far. The key insight is statefulness via closures or objects: each initializer call must produce an independent routine with its own retained buffer, so two streams never share state.

## Task Requirements
- Provide an initializer I(P) that, given a period P, returns a callable SMA routine.
- SMA(N) appends N to an ordered container, drops the oldest element once the container exceeds P, and returns the mean of the retained elements.
- The routine must remember the period and at least the last P numbers between calls.
- Successive calls to I() must return separate routines that do not share saved state (independent streams).

## Language Coverage
102 languages implement this task, giving very broad coverage across functional, object-oriented, and procedural paradigms. Representative implementations include C, C++, Java, Python, Haskell, Ruby, Go, Rust, JavaScript, and Common Lisp.

## Connections
- [[MovingAverage]] — the broader family of moving-average techniques this is a member of
- [[Closures]] — the idiomatic way to capture the period and buffer as per-instance state
- [[StatefulFunctions]] — the task hinges on retaining data between calls
- [[ArithmeticMean]] — SMA reduces to the mean of the windowed elements
- [[SlidingWindow]] — the fixed-size last-P buffer is a sliding window over the stream

## Contradictions
- None — reference task page.
