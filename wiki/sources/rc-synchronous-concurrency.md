---
title: "Synchronous concurrency (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, message-passing, threads]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Synchronous_concurrency
---

## Summary
This task asks the programmer to create two concurrent units (threads or tasks, not separate OS processes) that share data synchronously. One unit reads "input.txt" line by line and passes each line to a second unit, which prints the lines and counts them; after the last line, the reader requests the count and prints it. The key insight is that this requires bidirectional communication between in-process concurrent units and a clean coordinated shutdown — not fork/spawn or pipes.

## Task Requirements
- Spawn two concurrent activities within one process (threads, tasks, or co-processes) — no fork, spawn, or OS pipes.
- The reader unit reads "input.txt" and sends its contents one line at a time to the printer unit.
- The printer unit prints each received line to standard output and counts the lines it prints.
- After sending the last line, the reader requests the line count from the printer (two-way communication).
- The reader prints the count it receives back.
- All concurrent units must terminate cleanly at program end.

## Language Coverage
58 languages implement this task, spanning thread-based, actor/message-passing, and channel-based concurrency models. Representative implementations include Ada, C, C++, Go, Erlang, Haskell, Java, Python, Rust, Clojure, OCaml, and Tcl.

## Connections
- [[Concurrency]] — the core paradigm the task exercises.
- [[MessagePassing]] — synchronous channels/messages carry lines and the count between units.
- [[Threads]] — common implementation vehicle for the two concurrent units.
- [[ProducerConsumer]] — the reader-as-producer, printer-as-consumer pattern with a synchronization handshake.
- [[Synchronization]] — coordinating handoff and clean termination across units.

## Contradictions
- None — reference task page.
