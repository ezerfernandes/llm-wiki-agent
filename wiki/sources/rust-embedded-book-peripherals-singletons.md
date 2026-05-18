---
title: "The Embedded Rust Book — Singletons"
type: source
tags: [rust, embedded, book-chapter, singletons]
date: 2026-05-16
source_file: raw/book/src/peripherals/singletons.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Singletons

## Summary

File 21/44 of *[[TheEmbeddedRustBook]]* — the **Peripherals chapter's fourth and final sub-section** (closes the chapter), immediately after [[rust-embedded-book-peripherals-borrowck]] (file 20/44) which restated the "exactly one Rust value per physical [[Peripheral|peripheral]]" precondition the [[BorrowChecker|borrow checker]] needs. This chapter **resolves** that precondition: the canonical Rust solution is the [[Singleton|singleton]] pattern — a runtime gate (`static mut PERIPHERALS = Some(...)` + a `take_serial()` method that `replace`s the inner with `None`) that hands out a peripheral handle **at most once** and panics on any subsequent call. The chapter closes the [[rust-embedded-book-peripherals-a-first-attempt]] `SystemTimer::new()`-callable-twice gap. Shows three implementation tiers: (1) the **hand-rolled** `Peripherals { serial: Option<SerialPort> }` struct, (2) the [[CortexMCrate|`cortex-m`]] crate's `singleton!()` macro that wraps the boilerplate, and (3) [[CortexMRTIC|`cortex-m-rtic`]] which abstracts the whole flow into `cx.core` / `cx.device` non-Option handles for `cortex_m::Peripherals` and the device PAC. Concludes with the **"treat your hardware like data"** payoff — once a peripheral is a borrow-checked Rust value, `&T` vs `&mut T` in function signatures tells the reader (and compiler) whether the function can modify hardware, enforced **at compile time**.

## Key Claims

- **Global `static mut` is insufficient** — `static mut THE_SERIAL_PORT: SerialPort = SerialPort;` is mutable global state, always `unsafe` to interact with, and program-wide visible — defeating the [[BorrowChecker|borrow checker]]'s reference / ownership tracking.
- **The singleton pattern in Rust** — wrap each peripheral in `Option<T>` inside a `static mut PERIPHERALS`. A `take_serial(&mut self)` method calls `replace(&mut self.serial, None)` and `unwrap()`s the `Option`; the second call panics. Once the caller has the unwrapped `SerialPort`, `unsafe` is no longer needed — borrow-checker discipline takes over.
- **One-time `unsafe` is the bargain** — interaction with `PERIPHERALS` is `unsafe` and has small runtime overhead (the `Option` wrapper, one `replace`), but this **up-front cost** buys the entire program's safety guarantees through the [[BorrowChecker]].
- **[[CortexMCrate|`cortex_m`]] ships `singleton!()`** — a macro that performs exactly this dance: `let x: &'static mut bool = singleton!(: bool = false).unwrap();`. The "OK if `main` is executed only once" caveat is the only safety obligation on the caller.
- **[[CortexMRTIC|`cortex-m-rtic`]] further abstracts it** — `#[rtic::app]` with `peripherals = true` hands `init` a `cx.core: cortex_m::Peripherals` and `cx.device: <pac>::Peripherals` with **non-`Option`** fields, eliminating the `.unwrap()` and the panic path entirely.
- **The methodological payoff: hardware-as-data + `&` / `&mut` signatures encode mutation intent**. `fn setup_spi_port(spi: &mut SpiPort, cs_pin: &mut GpioPin)` is allowed to mutate hardware; `fn read_button(gpio: &GpioPin) -> bool` is statically known not to. The compiler enforces this at **compile time**, "rather than at runtime" — generally only across one application, but bare-metal firmware compiles to exactly one application so this is not usually a restriction.
- **Why `&self` matters on register-access methods** — `SerialPort::read_speed(&self)` requires the caller to *have* a `SerialPort` value; combined with singleton uniqueness, this means accessing `SER_PORT_SPEED_REG` is only possible if you satisfied the borrow checker. **`SerialPort::read_speed()` (no `&self`) would not work.**

## Key Quotes

> "In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one object." — opening epigraph from *[[Wikipedia]]*; the chapter applies this classical GoF pattern to peripheral handles.

> "But this has a few problems. It is a mutable global variable, and in Rust, these are always unsafe to interact with. These variables are also visible across your whole program, which means the borrow checker is unable to help you track references and ownership of these variables." — the **diagnosis** of `static mut` as a non-solution.

> "If we try to call `take_serial()` more than once, our code will panic!" — the runtime-checked uniqueness guarantee at the heart of the singleton pattern.

> "Although interacting with this structure is `unsafe`, once we have the `SerialPort` it contained, we no longer need to use `unsafe`, or the `PERIPHERALS` structure at all." — the **one-time `unsafe` bargain** that buys the rest of the program's safety.

> "This small up-front cost allows us to leverage the borrow checker throughout the rest of our program." — the chapter's thesis: pay once at startup, get [[BorrowChecker|borrow-checker]] safety everywhere downstream.

> "It is only possible to access the hardware if we have appropriately satisfied the borrow checker, meaning that at no point do we have multiple mutable references to the same hardware!" — the **closure of the loop** between singleton uniqueness and `&mut T` exclusivity.

> "This allows us to enforce whether code should or should not make changes to hardware at **compile time**, rather than at runtime." — the **"treat your hardware like data"** payoff: function signatures encode mutation intent.

## Connections

- [[TheEmbeddedRustBook]] — file 21/44; closes the Peripherals chapter (sub-sections: index → a-first-attempt → borrowck → **singletons**).
- [[rust-embedded-book-peripherals-borrowck]] — preceding file (20/44); stated the "exactly one Rust value per peripheral" precondition this chapter resolves.
- [[rust-embedded-book-peripherals-a-first-attempt]] — file 19/44; ended on the `SystemTimer::new()`-callable-twice gap that this chapter closes.
- [[rust-embedded-book-peripherals-index]] — chapter opener (18/44); flagged singletons / ownership / RAII as later sub-sections — this is the singletons one.
- [[Singleton]] — the core concept introduced in this chapter (new page).
- [[PeripheralsTake]] — the canonical API pattern (`Peripherals::take()` / `singleton!()`) for obtaining the unique handle (new page).
- [[BorrowChecker]] — the discipline this chapter's singleton gate **feeds**: once peripherals are unique Rust values, `&T` / `&mut T` give safe hardware sharing for free.
- [[Peripheral]] — the noun being singleton-gated.
- [[VolatileMemoryAccess]] — rule (1) of safe peripheral access; orthogonal to singletons but co-required for any read/write through `SER_PORT_SPEED_REG`.
- [[CortexMCrate|`cortex-m`]] — ships the `singleton!()` macro and the `Peripherals::take()` gate; already documents the latter on its entity page.
- [[CortexMRTIC|`cortex-m-rtic`]] — further-abstracted layer; `#[rtic::app]` removes the `.unwrap()` boilerplate entirely (new entity).
- [[PeripheralAccessCrate|PAC]] — the chip-specific layer that, like `cortex-m`, generates a `Peripherals::take()` singleton for the chip's peripherals.
- [[RustLanguage]] / [[UnsafeRust]] — the singleton pattern is the canonical Rust idiom for confining `unsafe` to a single boundary.

## Contradictions

None. Strictly additive — closes the singleton gap that [[rust-embedded-book-peripherals-a-first-attempt]] opened and [[rust-embedded-book-peripherals-borrowck]] re-framed, and productionizes the pattern into the [[CortexMCrate|`cortex-m`]] / [[CortexMRTIC|`cortex-m-rtic`]] APIs the wiki has been referencing since [[rust-embedded-book-start-registers]].
