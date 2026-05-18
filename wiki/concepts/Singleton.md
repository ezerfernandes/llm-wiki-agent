---
title: "Singleton"
type: concept
tags: [rust, embedded, design-pattern, peripherals, safety]
sources: [rust-embedded-book-peripherals-singletons]
last_updated: 2026-05-16
---

# Singleton

A **design pattern that restricts a type to at most one live instance** for the lifetime of the program. Wikipedia's gloss (quoted as the opening epigraph of [[rust-embedded-book-peripherals-singletons]]): *"In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one object."*

In embedded Rust, the singleton is **the bridge** between the [[BorrowChecker|borrow checker]]'s aliasing discipline and the physical uniqueness of hardware: the [[BorrowChecker]] needs **exactly one Rust value per physical [[Peripheral|peripheral]]** to make `&T` / `&mut T` enforce safe hardware sharing, but Rust's type system alone cannot prevent two `SystemTimer::new()` calls from manufacturing independent handles to the same `0xE000_E010` register block ([[rust-embedded-book-peripherals-a-first-attempt]]). The singleton **manufactures** that uniqueness at runtime via a one-shot gate.

## The canonical implementation

Wrap each peripheral in `Option<T>` inside a `static mut`, expose a `take_*` method that calls `replace(&mut self.foo, None)` and `unwrap`s — second call panics:

```rust
struct Peripherals { serial: Option<SerialPort> }
impl Peripherals {
    fn take_serial(&mut self) -> SerialPort {
        let p = replace(&mut self.serial, None);
        p.unwrap()  // panics on second call
    }
}
static mut PERIPHERALS: Peripherals = Peripherals { serial: Some(SerialPort) };
```

Interaction with `PERIPHERALS` is `unsafe` (it's `static mut`), but **once the inner `SerialPort` is unwrapped, `unsafe` is no longer needed** — the [[BorrowChecker]] takes over for the rest of the program's lifetime.

## The one-time `unsafe` bargain

The singleton is the embedded-Rust expression of a deeper Rust idiom: **confine `unsafe` to a single, audited boundary; expose a safe API above it**. The runtime cost is one `Option` wrapper + one `replace` per peripheral at startup; the payoff is whole-program [[BorrowChecker]] safety on every subsequent register access ([[rust-embedded-book-peripherals-singletons]]).

## Library layers

- **Hand-rolled** — the `Peripherals { serial: Option<SerialPort> }` pattern above. Pedagogically clear; production code rarely writes this.
- **[[CortexMCrate|`cortex-m`]]'s `singleton!()` macro** — wraps the boilerplate: `let x: &'static mut bool = singleton!(: bool = false).unwrap();`. Returns `Option<&'static mut T>`; second call returns `None`.
- **`Peripherals::take()` on [[CortexMCrate|`cortex-m`]] and on [[PeripheralAccessCrate|PACs]]** — the standardized API: hands out a single `cortex_m::Peripherals` / `<chip>::Peripherals` struct containing all the core / chip peripherals at once (see [[PeripheralsTake]]).
- **[[CortexMRTIC|`cortex-m-rtic`]]** — eliminates the `.unwrap()` entirely: `#[rtic::app(peripherals = true)]` hands `init` a `cx.core: cortex_m::Peripherals` and `cx.device: <pac>::Peripherals` with **non-`Option`** fields. No panic path; the framework guarantees `init` runs at most once.

## Caveats

- **`static mut` is unsound when concurrently mutated** — the singleton works because the `take` operation is called at most once (typically in `main` / `init`, before interrupts are enabled). Concurrent calls would race on the `Option`.
- **`main` must run at most once** — `singleton!()`'s safety doc says "OK if `main` is executed only once"; on bare-metal this is always true (no `fork`, no re-entry into `main`).
- **Compile-time vs runtime check** — singleton uniqueness is **runtime-enforced** (panic on second `take`); only the downstream `&T` / `&mut T` discipline is compile-time. This contrasts with [[TypeStateProgramming]], which encodes some uniqueness facts directly in the type system.

## Connections

- [[rust-embedded-book-peripherals-singletons]] — the chapter that introduces this pattern (file 21/44).
- [[BorrowChecker]] — the discipline the singleton **feeds**: makes `&T` / `&mut T` reasoning sound by guaranteeing one Rust value per peripheral.
- [[Peripheral]] — the noun being singleton-gated.
- [[PeripheralsTake]] — the canonical API embodiment (`Peripherals::take()` / `singleton!()`).
- [[CortexMCrate]] — ships the `singleton!()` macro and `Peripherals::take()` for [[ARMCortexM|Cortex-M]] architectural peripherals.
- [[PeripheralAccessCrate]] — chip-specific layer; also generates a `Peripherals::take()` singleton for the chip's device peripherals.
- [[CortexMRTIC|`cortex-m-rtic`]] — the further-abstracted layer that eliminates the unwrap.
- [[UnsafeRust]] / [[RustLanguage]] — the singleton is the canonical Rust idiom for confining `unsafe` to one boundary.
- [[TypeStateProgramming]] — a complementary pattern; encodes peripheral *configuration state* in the type system once the singleton has manufactured a unique value.
- [[rust-embedded-book-peripherals-a-first-attempt]] — exhibited the singleton **gap** (`SystemTimer::new()` callable twice) this pattern closes.
- [[rust-embedded-book-peripherals-borrowck]] — restated the gap as a [[BorrowChecker]] precondition.
