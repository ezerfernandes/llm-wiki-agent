---
title: "Mutex"
type: concept
tags: [concurrency, synchronization, rust, embedded]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# Mutex

Short for **mut**ual **ex**clusion. A *"synchronisation primitive"* that grants exclusive access to a wrapped variable. *"A thread can attempt to **lock** (or **acquire**) the mutex, and either succeeds immediately, or blocks waiting for the lock to be acquired, or returns an error that the mutex could not be locked. While that thread holds the lock, it is granted access to the protected data. When the thread is done, it **unlocks** (or **releases**) the mutex, allowing another thread to lock it"* ([[rust-embedded-book-concurrency-index]]).

In [[RustLanguage|Rust]], unlock is conventionally implemented via the `Drop` trait so the mutex is *always* released when the lock guard goes out of scope.

## Why blocking mutexes are dangerous in interrupt handlers

*"It is not normally acceptable for the interrupt handler to block, and it would be especially disastrous for it to block waiting for the main thread to release a lock, since we would then **[[Deadlock|deadlock]]** (the main thread will never release the lock because execution stays in the interrupt handler). Deadlocking is not considered unsafe: it is possible even in safe Rust"* ([[rust-embedded-book-concurrency-index]]).

This rules out `std::sync::Mutex` (or anything that *blocks*) for `main` ↔ [[Interrupt|interrupt]] sharing.

## `cortex_m::interrupt::Mutex`: the critical-section-gated alternative

The embedded-Rust convention (per the [[CortexMCrate|`cortex-m`]] crate, named in this chapter as the canonical example):

- **Lock = [[CriticalSection|critical section]]**. The only way to get at the inner `T` is `mutex.borrow(cs)`, which takes a `&CriticalSection` token. *"So long as the critical section must last as long as the lock, we can be sure we have exclusive access to the wrapped variable without even needing to track the lock/unlock state of the mutex."*
- **No deadlock possible**. No separate lock-state to wait on; the critical section itself is the exclusion.
- **`Mutex<T>: Sync` for any `T: Send`** — *"it can do this safely because it only gives access to its contents during a critical section."* Result: you can put it in a `static`.

```rust,ignore
use core::cell::Cell;
use cortex_m::interrupt::{self, Mutex};

static COUNTER: Mutex<Cell<u32>> = Mutex::new(Cell::new(0));

// Access:
interrupt::free(|cs| COUNTER.borrow(cs).set(COUNTER.borrow(cs).get() + 1));
```

## The `Mutex<RefCell<Option<T>>>` peripheral-sharing pattern

For non-`Copy` shared state (e.g. a [[Peripheral|peripheral]] [[Singleton|singleton]] like `stm32f405::GPIOA`), the chapter promotes:

```rust,ignore
static MY_GPIO: Mutex<RefCell<Option<stm32f405::GPIOA>>> =
    Mutex::new(RefCell::new(None));
```

- **`Mutex`**: makes it [[Sync]]; only accessible inside a critical section.
- **[[RefCell]]**: gives **safe interior mutability via references** (which plain [[CellRust|`Cell`]] does not).
- **`Option`**: allows `static` initialization to `None`, with a deferred `borrow(cs).replace(Some(periph))` move-in once the peripheral has been `Peripherals::take()`-d at runtime.

For mutable access, use `borrow_mut().deref_mut()`:

```rust,ignore
interrupt::free(|cs| {
    if let Some(ref mut tim) = G_TIM.borrow(cs).borrow_mut().deref_mut() {
        tim.start(1.hz());
    }
});
```

**Init-order trap**: *"Be careful to enable the interrupt only after setting `MY_GPIO`: otherwise the interrupt might fire while it still contains `None`, and as-written (with `unwrap()`), it would panic."*

## Connections

- [[CriticalSection]] — the lock mechanism for `cortex_m::interrupt::Mutex`.
- [[CortexMCrate|`cortex-m`]] — the crate providing `cortex_m::interrupt::Mutex`.
- [[Deadlock]] — the failure mode standard blocking mutexes have inside interrupt handlers; critical-section-gated mutexes sidestep it entirely.
- [[InteriorMutability]] — `Mutex` is *part of* the embedded interior-mutability stack alongside [[CellRust|`Cell`]] / [[RefCell]] / [[UnsafeCell]].
- [[CellRust|`Cell`]] — typical inner for `Copy` shared state.
- [[RefCell]] — typical inner for non-`Copy` shared state (peripherals).
- [[Sync]] / [[Send]] — `Mutex<T>: Sync` for any `T: Send`; the rule that makes `static MUTEX: …` placement legal.
- [[Interrupt]] — the "other thread" the mutex is protecting against.
- [[Peripheral]] / [[Singleton]] — the canonical non-`Copy` cargo for `Mutex<RefCell<Option<T>>>`.
- [[Atomic]] — the lighter-weight alternative for `Copy` numeric state on platforms with CAS.
- [[RTIC]] — higher-level framework that eliminates the need for explicit `Mutex<RefCell<…>>` boilerplate via static priority + compile-time resource tracking.
