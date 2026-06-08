---
title: "Rendezvous (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, synchronization, exception-handling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rendezvous
---

## Summary
The task demonstrates the "rendezvous" synchronization mechanism, in which one task calls an entry point exposed by another task and blocks synchronously until the callee accepts and services the call — much like a cross-task procedure call. Because rendezvous are synchronous, no parameter marshaling or message buffer is needed, and an implementation can avoid a context switch. The key illustration is building a printer monitor that guards a shared resource so that competing writer tasks print whole lines indivisibly.

## Task Requirements
- Show how the language supports rendezvous natively; if it doesn't, implement them from other concurrency primitives.
- Exceptions raised inside a rendezvous must propagate synchronously into both caller and callee tasks.
- Implement a printer monitor guarding a printer, with an entry point `Print` taking a text line.
- Print each character of a line separately to prove that whole lines are printed indivisibly (no interleaving).
- Provide two printers, *main* and *reserve*, each with its own monitor; each has ink for only 5 lines.
- When *main* runs out of ink, redirect its requests to *reserve*; when *reserve* is also exhausted, propagate an `Out_Of_Ink` exception back to the caller.
- Create two writer tasks printing plagiarisms: one *Humpty Dumpty*, the other *Mother Goose*.

## Language Coverage
24 languages implement this task, ranging from those with first-class rendezvous (Ada) to general-purpose languages that synthesize it from threads, channels, locks, or actors — including Ada, C, C++, Erlang, Go, Java, Python, Rust, Racket, Tcl, and Wren.

## Connections
- [[Concurrency]] — rendezvous is a concurrency model based on procedural decomposition
- [[Synchronization]] — the caller blocks until the callee accepts and services the call
- [[Monitor]] — the printer monitor guards a shared resource via accepted rendezvous
- [[MessagePassing]] — contrasted as the asynchronous, buffer-requiring alternative
- [[ExceptionHandling]] — exceptions must propagate into both tasks synchronously

## Contradictions
- None — reference task page.
