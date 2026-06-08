---
title: "Atomic updates (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, synchronization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Atomic_updates
---

## Summary
This task asks the programmer to build a data type of fixed-size "buckets" holding nonnegative integers, with operations to read any bucket and to transfer an amount from one bucket to another while preserving the total and clamping so values stay nonnegative. The key insight is concurrency safety: the task spawns competing threads (one equalizing pairs, one randomly redistributing) and the transfer must be atomic so the invariant total is never corrupted by simultaneous transfers.

## Task Requirements
- Define a data type of a fixed number of buckets, each holding a nonnegative integer.
- Support getting the current value of any bucket.
- Support transferring an amount from one bucket to another, preserving the overall total and clamping the transferred amount so no value goes negative.
- Run three concurrent tasks: one making pairs of buckets closer to equal, one arbitrarily redistributing values between pairs, and one displaying the total (and optionally individual values).
- Ensure the sum of bucket values is preserved even under simultaneous transfers — i.e., transfers must be atomic (a simple solution allows only one transfer at a time).

## Language Coverage
47 languages implement this task, spanning systems languages, functional languages, and scripting languages. Representative examples include C, C++, C#, Rust, Go, Java, Haskell, Clojure, Erlang, Python, and Ada.

## Connections
- [[Concurrency]] — the central theme of the task
- [[AtomicOperations]] — transfers must be indivisible
- [[Mutex]] — common mechanism to serialize transfers
- [[RaceCondition]] — the hazard the atomicity requirement prevents
- [[InvariantPreservation]] — the conserved total across all buckets

## Contradictions
- None — reference task page.
