---
title: "RefCell"
type: concept
tags: [rust, language-feature, concurrency]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# `RefCell<T>`

Top layer of safe [[InteriorMutability|interior mutability]] in [[RustLanguage|Rust]] — *"uses a runtime check to ensure only one reference to a peripheral is given out at a time. This has more overhead than the plain [[CellRust|`Cell`]], but since we are giving out references rather than copies, we must be sure only one exists at a time"* ([[rust-embedded-book-concurrency-index]]).

`borrow()` returns `Ref<'_, T>` (a runtime-tracked shared borrow). `borrow_mut()` returns `RefMut<'_, T>` (runtime-tracked exclusive borrow). The borrow counter is checked at runtime — violating the *one mut XOR many shared* rule **panics** rather than miscompiling.

## Why `RefCell` is the embedded peripheral-sharing primitive

[[CellRust|`Cell`]]'s copy-in / copy-out API is **useless for non-`Copy` types** like a peripheral struct. To share an `stm32f405::GPIOA` or a `Timer<TIM2>` between `main` and an [[Interrupt|interrupt handler]], you need to hand out references — which is exactly what `RefCell` provides.

The canonical embedded pattern is **`Mutex<RefCell<Option<T>>>`** ([[rust-embedded-book-concurrency-index]]):

```rust,ignore
use core::cell::RefCell;
use cortex_m::interrupt::{self, Mutex};
use stm32f4::stm32f405;

static MY_GPIO: Mutex<RefCell<Option<stm32f405::GPIOA>>> =
    Mutex::new(RefCell::new(None));

// In main, after taking the singleton:
interrupt::free(|cs| MY_GPIO.borrow(cs).replace(Some(dp.GPIOA)));

// Later access (read):
interrupt::free(|cs| {
    let gpioa = MY_GPIO.borrow(cs).borrow();
    gpioa.as_ref().unwrap().idr.read().idr0().bit_is_set()
});

// Mutable access (e.g. on a timer):
interrupt::free(|cs| {
    if let Some(ref mut tim) = G_TIM.borrow(cs).borrow_mut().deref_mut() {
        tim.start(1.hz());
    }
});
```

Three layers, each load-bearing:
- **[[Mutex]]**: recovers [[Sync]] (so we can put it in a `static`); ensures access only inside a [[CriticalSection|critical section]].
- **`RefCell`**: gives reference-granting [[InteriorMutability|interior mutability]] (which plain [[CellRust|`Cell`]] does not).
- **`Option`**: allows `static` initialization to `None` and deferred move-in once the peripheral has been `Peripherals::take()`-d.

## Init-order trap

*"Be careful to enable the interrupt only after setting `MY_GPIO`: otherwise the interrupt might fire while it still contains `None`, and as-written (with `unwrap()`), it would panic"* ([[rust-embedded-book-concurrency-index]]).

## Connections

- [[InteriorMutability]] — `RefCell` is the safe reference-granting layer.
- [[UnsafeCell]] — what `RefCell` wraps internally.
- [[CellRust|`Cell`]] — sibling cheaper layer (copy-only); insufficient for non-`Copy` types.
- [[Mutex]] — the standard embedded composition: `Mutex<RefCell<Option<T>>>` for shared peripherals.
- [[Sync]] — `RefCell` is not `Sync`; embedding in a `Mutex` recovers `Sync`.
- [[Peripheral]] / [[Singleton]] / [[PeripheralsTake]] — the canonical cargo `RefCell` ferries from `main` into an interrupt-shared static.
- [[Interrupt]] — the "other thread" the `RefCell<Option<…>>` pattern is protecting against.
- [[RustLanguage]] — `core::cell::RefCell` is in the Rust core library.
