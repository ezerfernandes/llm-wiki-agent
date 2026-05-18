---
title: "Cilk"
type: concept
tags: [parallel-computing, programming-languages]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Cilk

A parallel-programming language extension of C (originally MIT, later Intel Cilk Plus and the open-source [OpenCilk](https://www.opencilk.org/)) whose **defining contribution is a work-stealing runtime**. Programmers express parallelism with the `cilk_spawn` / `cilk_sync` keywords; the runtime schedules the resulting task graph across cores by giving each worker a local deque and having idle workers **steal** tasks from busy peers.

## In the chapter

[[parproc-ch02-recurring-performance-issues]] §2.4.4 names Cilk by name as the canonical work-stealing implementation: *"This is the approach taken, for example, by the elegant Cilk language."* [[NormMatloff|Matloff]] is favorable on the language design (*"elegant"*) but skeptical of work-stealing as a default strategy — the cross-thread queue raids are an expensive form of [[CommunicationBottleneck|communication]] he would rather avoid.

## Connections

- [[WorkStealing]] — Cilk's core scheduling strategy.
- [[parproc-ch02-recurring-performance-issues]] — primary mention.
- [[DynamicTaskAssignment]] — the broader category.
