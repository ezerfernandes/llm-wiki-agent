---
title: "Events (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, synchronization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Events
---

## Summary
This task asks the programmer to demonstrate how their language implements *events* — a low-level concurrency synchronization object with two states, *signaled* and *reset*. A task awaits an event entering a desired state and is *released* (notified) once that state is reached. The key insight is that a bare event carries no data about what caused it or who the subject is; events enriched with data or publisher-subscriber routing become messages or signals.

## Task Requirements
- Show how to create or represent an event synchronization object with signaled/reset states.
- Demonstrate one task awaiting (blocking on) the event and another task signaling it to release the waiter (event notification).
- Optionally illustrate event variants such as a manual-reset event and a pulse event.
- Contrast the event-driven approach with polling / busy waiting where appropriate.

## Language Coverage
43 languages implement this task, spanning systems and concurrent languages with native primitives as well as scripting and functional languages. Representative entries include Ada, C, C#, Go, Java, Haskell, Erlang, Elixir, Rust, Python, Tcl, and PowerShell.

## Connections
- [[Concurrency]] — events are a core concurrency synchronization mechanism.
- [[EventDrivenArchitecture]] — design pattern that deploys events to synchronize tasks with asynchronous activities.
- [[RaceCondition]] — a hazard event-driven systems must guard against, alongside deadlock and priority inversion.
- [[BusyWaiting]] — the polling alternative to events, trading resource use for predictability.
- [[PublisherSubscriber]] — scheme that augments raw events into routed messages or signals.

## Contradictions
- None — reference task page.
