---
title: "Atomic (operation / instruction)"
type: concept
tags: [concurrency, embedded, hardware, rust, cortex-m]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# Atomic

Hardware-supported indivisible read-modify-write (or load-or-store) operation that **completes without being interruptible mid-flight**. The multi-core-safe alternative to disabling interrupts ([[CriticalSection|critical sections]]) for protecting shared state.

In [[RustLanguage|Rust]], exposed via the `core::sync::atomic` module: `AtomicUsize`, `AtomicBool`, `AtomicI32`, etc., with methods `load`, `store`, `fetch_add`, `compare_exchange`, all parameterized by an `Ordering` (memory ordering / barrier strength).

```rust,ignore
use core::sync::atomic::{AtomicUsize, Ordering};

static COUNTER: AtomicUsize = AtomicUsize::new(0);

// In main loop:
COUNTER.fetch_add(1, Ordering::Relaxed);

// In interrupt handler:
COUNTER.store(0, Ordering::Relaxed);
```

## Cortex-M architectural split (thumbv6 vs thumbv7)

[[rust-embedded-book-concurrency-index]] names the split:

- **`thumbv6`** ([[ARMCortexM|Cortex-M0, Cortex-M0+]]): only atomic **load** and **store** instructions. No CAS — no portable `fetch_add` etc.
- **`thumbv7`** (Cortex-M3 and above): full **Compare-and-Swap (CAS)** instructions (`LDREX` / `STREX`), enabling all `fetch_*` operations.

CAS-based atomic increment is the *"attempt the increment, it will succeed most of the time, but if it was interrupted it will automatically retry the entire increment operation"* pattern — a CAS loop, not a disable-interrupts loop.

## Multi-core safety

*"These atomic operations are safe even across multiple cores"* ([[rust-embedded-book-concurrency-index]]) — the processor's atomicity machinery extends to SMP. This is the main reason to prefer atomics over critical sections when both are available: critical sections only stop *interrupts on the current core*, atomics serialize *across all cores*.

## `Ordering::Relaxed` on single-core

*"Assuming that the target is a single core platform `Relaxed` is sufficient and the most efficient choice in this particular case. Stricter ordering will cause the compiler to emit memory barriers around the atomic operations; depending on what you're using atomics for you may or may not need this!"*

The full memory-ordering taxonomy is beyond the chapter's scope — see the Rust *Nomicon* on atomics.

## Connections

- [[CriticalSection]] — the alternative single-core mechanism; atomics replace it when available and are required for multi-core.
- [[ARMCortexM]] — the `thumbv6` vs `thumbv7` split that gates CAS availability.
- [[Mutex]] — built on critical sections in the embedded-Rust convention, but multi-core mutexes are typically built on atomic CAS primitives.
- [[Sync]] — `AtomicUsize` etc. are `Sync` by design; that's the entire point.
- [[Interrupt]] — atomics protect against interrupt-induced races without disabling interrupts.
- [[DataRace]] — what atomics prevent on the hardware level.
- [[RustLanguage]] — `core::sync::atomic` is the canonical surface.
