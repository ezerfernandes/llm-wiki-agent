---
title: "RTIC"
type: entity
tags: [rust, embedded, framework, concurrency, async]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# RTIC

**Real-Time Interrupt-driven Concurrency** — a [[RustLanguage|Rust]] framework for embedded concurrency that **statically tracks accesses to `static mut` "resources"** to enforce shared-state safety at compile time, without the runtime cost of the manual [[CriticalSection|critical-section]]-and-[[RefCell|`RefCell`]]-borrow-counting machinery the *Concurrency* chapter develops by hand.

[[rust-embedded-book-concurrency-index]] introduces it as the **first named higher-level alternative** to the `Mutex<RefCell<Option<T>>>` pattern:

> *"One alternative is the RTIC framework, short for Real Time Interrupt-driven Concurrency. It enforces static priorities and tracks accesses to `static mut` variables ("resources") to statically ensure that shared resources are always accessed safely, without requiring the overhead of always entering critical sections and using reference counting (as in `RefCell`). This has a number of advantages such as guaranteeing no deadlocks and giving extremely low time and memory overhead."*

## Distinguishing features (per the chapter)

- **Static priorities**: each task is pinned to a fixed [[InterruptPriority|interrupt priority]] at compile time.
- **Compile-time resource tracking**: the framework analyzes which tasks access which `static mut` resources and inserts the *minimum-priority-ceiling* critical sections needed — instead of every access taking the same heavy-handed *disable-all-interrupts* hammer.
- **No [[Deadlock|deadlocks]] by construction**: priority-ceiling protocol is provably deadlock-free.
- **Extremely low time + memory overhead**: no reference-counted `RefCell` borrows at runtime.
- **`async` executor included**: *"RTIC comes with as[sic] asynchronous executor, so your software tasks are `async` functions where you can use `async` APIs in addition to regular synchronous APIs."*
- **Message passing + task scheduling**: *"the framework also includes other features like message passing, which reduces the need for explicit shared state, and the ability to schedule tasks to run at a given time, which can be used to implement periodic tasks."*

## Reference

Documentation: <https://rtic.rs> (the chapter links specifically to <https://rtic.rs/2/book/en>).

## Connections

- [[TheEmbeddedRustBook]] — introduces RTIC as the headline higher-level alternative in [[rust-embedded-book-concurrency-index|the Concurrency chapter]].
- [[Embassy]] — sibling higher-level alternative; complementary `async`/`await`-first ecosystem.
- [[CriticalSection]] / [[Mutex]] — the *lower-level* mechanisms RTIC replaces with priority-ceiling resource tracking.
- [[RefCell]] — the runtime-borrow-counted layer RTIC eliminates.
- [[Deadlock]] — the failure mode RTIC eliminates by construction.
- [[Interrupt]] / [[InterruptAttribute]] / [[InterruptPriority]] — the mechanism RTIC builds its scheduling on.
- [[ARMCortexM]] — the primary target architecture; uses the [[NVIC]] priority-ceiling features.
- [[RustEmbeddedWorkingGroup]] — community context (not directly maintained by the WG, but adjacent).
