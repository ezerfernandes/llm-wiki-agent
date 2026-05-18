---
title: "Data Race"
type: concept
tags: [concurrency, embedded, undefined-behavior]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# Data Race

The failure mode of unsynchronized concurrent access to shared mutable state: two execution threads (in embedded: usually `main` and an [[Interrupt|interrupt handler]]) read/write the same memory location with at least one writer, and their accesses are *not* serialized, producing an undefined / observation-dependent result.

## The canonical embedded example

[[rust-embedded-book-concurrency-index]] gives the textbook walk-through — a 1 Hz frequency counter:

```rust,ignore
static mut COUNTER: u32 = 0;

#[entry]
fn main() -> ! {
    set_timer_1hz();
    loop {
        if rising_edge_detected() {
            unsafe { COUNTER += 1 };  // race!
        }
    }
}

#[interrupt]
fn timer() {
    unsafe { COUNTER = 0; }
}
```

*"The increment on `COUNTER` is **not** guaranteed to be atomic — in fact, on most embedded platforms, it will be split into a **load**, then the **increment**, then a **store**. If the interrupt fired after the load but before the store, the reset back to 0 would be ignored after the interrupt returns — and we would count twice as many transitions for that period."*

## Why `static mut` is *always* `unsafe` in Rust

*"Unlike non-embedded Rust, we will not usually have the luxury of creating heap allocations and passing references to that data into a newly-created thread. … In Rust, such `static mut` variables are always unsafe to read or write, because without taking special care, you might trigger a race condition, where your access to the variable is interrupted halfway through by an interrupt which also accesses that variable."*

The Rust language treats every `static mut` read/write as `unsafe` precisely because data races are undefined behavior — the programmer takes responsibility for proving the absence of a race.

## Four canonical fixes (in escalating sophistication)

[[rust-embedded-book-concurrency-index]] walks them in order:
1. **[[CriticalSection|Critical sections]]** ([[CortexMCrate|`cortex_m::interrupt::free`]]) — disable interrupts inside the racing region. Single-core only.
2. **[[Atomic|Atomic instructions]]** (`AtomicUsize::fetch_add`, `Ordering::Relaxed`) — hardware-indivisible read-modify-write. Multi-core safe.
3. **Type-state-encoded critical sections** — wrap [[UnsafeCell]] + require a `CriticalSection` token on every method (`unsafe impl Sync` once, no `unsafe` at call sites).
4. **[[Mutex|`Mutex<Cell<T>>` / `Mutex<RefCell<Option<T>>>`]]** — full safe abstraction for `Copy` / non-`Copy` shared state.

## Connections

- [[CriticalSection]] / [[Atomic]] / [[Mutex]] — the three primary mitigations.
- [[Interrupt]] — in embedded, the most common racing peer.
- [[Sync]] — the type-level invariant whose absence makes races a *type error*; `Sync`-violating placement is a compile error.
- [[Deadlock]] — sibling failure mode; *not* a data race, but a common false-cure for one.
- [[RustLanguage]] — the language whose type system criminalizes races (mostly) at compile time.
- [[ARMCortexM]] — the single-core-vs-multi-core distinction determines which mitigation is necessary.
