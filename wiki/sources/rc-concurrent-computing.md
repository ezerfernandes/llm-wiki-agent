---
title: "Concurrent computing (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, threads]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Concurrent_computing
---

## Summary
This task asks the programmer to print the three strings "Enjoy", "Rosetta", and "Code" — one per line — in a non-deterministic order. The order must arise from running the print operations concurrently rather than shuffling a list, so the exercise is really a minimal demonstration of a language's native concurrency primitives. The key insight is that the random ordering is an emergent property of independent threads racing rather than an explicit randomization step.

## Task Requirements
- Display the strings "Enjoy", "Rosetta", "Code", one string per line.
- Emit them in random (non-deterministic) order across runs.
- Use the language's concurrency mechanism — threads, tasks, co-routines, async, actors, or equivalent — rather than a sequential shuffle.
- May rely on native concurrency syntax or freely available concurrency libraries.

## Language Coverage
87 languages implement this task, spanning systems languages, functional languages, scripting languages, and shells, illustrating how varied concurrency models are across ecosystems. Representative examples include Ada (tasks), Go (goroutines), Erlang and Elixir (actor processes), Rust (std::thread), Java and C# (threads), Haskell (forkIO), Clojure, Python, and even UnixPipes (process-level concurrency).

## Connections
- [[Concurrency]] — the central paradigm the task exercises
- [[Threads]] — the most common mechanism used to achieve concurrent output
- [[Coroutines]] — an alternative concurrency model cited by the task
- [[ActorModel]] — used by Erlang/Elixir-style message-passing implementations
- [[RaceCondition]] — the non-deterministic ordering is itself a benign race

## Contradictions
- None — reference task page.
