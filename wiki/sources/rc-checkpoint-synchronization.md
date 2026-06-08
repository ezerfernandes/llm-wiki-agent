---
title: "Checkpoint synchronization (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, synchronization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Checkpoint_synchronization
---

## Summary
This classic concurrency task asks the programmer to coordinate multiple concurrent workers so they all meet at a shared checkpoint before any of them proceeds — the equivalent of assembly-line workers who must finish their individual parts before the pieces are combined. The key insight is that the solution must be race-condition free: the naive event-based approach (each task signals its own event, then waits on the AND of all events and resets) can lose a slow task and let the fastest worker run two cycles while the slowest lags, so a proper barrier primitive is required.

## Task Requirements
- Implement checkpoint synchronization so multiple tasks rendezvous at a barrier before continuing.
- Guarantee the implementation is free of race conditions; avoid the event-signaling pitfall described in the task.
- Prevent a worker from being counted twice within one working cycle (no premature completion of the fastest worker while the slowest is behind).
- If possible, support workers dynamically joining and leaving the group.

## Language Coverage
34 languages implement this task, spanning concurrency models from OS threads to actors and message passing. Representative implementations include Ada, C, C++, C#, Go, Haskell, Erlang, Java, Python, Rust, Clojure, and Scala.

## Connections
- [[BarrierSynchronization]] — the core primitive the task implements
- [[RaceCondition]] — the failure mode the solution must avoid
- [[Concurrency]] — the problem domain
- [[ProducerConsumer]] — a related coordination pattern
- [[MessagePassing]] — used by actor-based language solutions

## Contradictions
- None — reference task page.
