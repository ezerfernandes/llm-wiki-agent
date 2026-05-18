---
title: "The Embedded Rust Book — HAL Interoperability"
type: source
tags: [rust, embedded, book-chapter, hal, interoperability]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/design-patterns/hal/interoperability.md
sources: [rust-embedded-book-design-patterns-hal-interoperability]
---

## Summary

File 34/44 of *[[TheEmbeddedRustBook]]* — **second leaf-section** of the *HAL Design Patterns* sub-chapter ([[rust-embedded-book-design-patterns-hal-index]]) and the **Interoperability** group of the [[rust-embedded-book-design-patterns-hal-checklist|HAL Checklist]]. Three named patterns, all short-form: **`C-FREE`** — wrapper types provide a `free` method that consumes the wrapper and returns back the raw [[Peripheral|peripheral]] (and any other non-`Copy` objects it was constructed from); **`C-REEXPORT-PAC`** — [[HALCrate|HAL]] crates **reexport** their [[PeripheralAccessCrate|register access (PAC)]] crate under the name **`pac`** (regardless of the actual crate name) at the HAL crate root; **`C-HAL-TRAITS`** — HAL types implement **all applicable** [[EmbeddedHalCrate|`embedded-hal`]] traits (multiple traits per type allowed). The three patterns operationalize the resource-flow contract the [[HALCrate|HAL]] layer owes upward (to applications) and downward (to the [[PeripheralAccessCrate|PAC]] / `embedded-hal` ecosystem) — `C-FREE` is the **destructor convention** that lets callers reclaim raw peripherals, `C-REEXPORT-PAC` is the **escape hatch** for callers who need lower-level register access without adding a second dependency, `C-HAL-TRAITS` is the **portability hook** that triggers the M·N → M+N complexity collapse from [[rust-embedded-book-portability-index]].

## Key Claims

- **`C-FREE` — wrapper types provide a destructor method**: *"Any non-`Copy` wrapper type provided by the [[HALCrate|HAL]] should provide a `free` method that consumes the wrapper and returns back the raw [[Peripheral|peripheral]] (and possibly other objects) it was created from."*
- **`free` is reset-on-release**: *"The method should shut down and reset the peripheral if necessary. Calling `new` with the raw peripheral returned by `free` should not fail due to an unexpected state of the peripheral."* — i.e. `new(peripheral)` after `free` returning that same peripheral must succeed (round-trip invariant).
- **`free` returns a tuple for multi-resource wrappers**: *"If the HAL type requires other non-`Copy` objects to be constructed (for example I/O pins), any such object should be released and returned by `free` as well. `free` should return a tuple in that case."*
- **`C-REEXPORT-PAC` — HALs reexport their register access crate**: *"HALs should always reexport the register access crate they are based on in their crate root."*
- **PAC reexport name is fixed to `pac`**: *"A PAC should be reexported under the name `pac`, regardless of the actual name of the crate, as the name of the HAL should already make it clear what PAC is being accessed."* — i.e. `stm32f4xx_hal::pac::*`, not `stm32f4xx_hal::stm32f4::*` (the underlying [[Svd2Rust|svd2rust]]-generated crate name is hidden behind a stable alias).
- **HALs can be built on `svd2rust` PACs or other register-access crates**: *"HALs can be written on top of [[Svd2Rust|svd2rust]]-generated PACs, or on top of other crates that provide raw register access."* — `C-REEXPORT-PAC` is agnostic about which.
- **`C-HAL-TRAITS` — types implement the `embedded-hal` traits**: *"Types provided by the [[HALCrate|HAL]] should implement all applicable traits provided by the [[EmbeddedHalCrate|`embedded-hal`]] crate."*
- **Multiple `embedded-hal` traits per type is allowed and expected**: *"Multiple traits may be implemented for the same type."* — e.g. a single `Serial` type implementing both `embedded-hal::serial::Read` and `embedded-hal::serial::Write`; a single GPIO pin type implementing both `InputPin` and `OutputPin` depending on typestate parameterization (cross-reference [[TypeStateProgramming]] from [[rust-embedded-book-static-guarantees-design-contracts]]).

## Key Quotes

> "Any non-`Copy` wrapper type provided by the HAL should provide a `free` method that consumes the wrapper and returns back the raw peripheral (and possibly other objects) it was created from." — the entire normative content of `C-FREE`.

> "The method should shut down and reset the peripheral if necessary. Calling `new` with the raw peripheral returned by `free` should not fail due to an unexpected state of the peripheral." — the round-trip invariant that distinguishes `free` from a plain field-access getter.

> "HALs should always reexport the register access crate they are based on in their crate root. […] A PAC should be reexported under the name `pac`, regardless of the actual name of the crate, as the name of the HAL should already make it clear what PAC is being accessed." — the entire normative content of `C-REEXPORT-PAC`.

> "Types provided by the HAL should implement all applicable traits provided by the `embedded-hal` crate. Multiple traits may be implemented for the same type." — the entire normative content of `C-HAL-TRAITS`.

The chapter's only worked code example (8 lines) — the canonical [[Peripheral|peripheral]] wrapper showing `new` / `free` symmetry:

```rust
pub struct Timer(TIMER0);

impl Timer {
    pub fn new(periph: TIMER0) -> Self {
        Self(periph)
    }

    pub fn free(self) -> TIMER0 {
        self.0
    }
}
```

The `self`-by-value parameter on `free` is load-bearing — it **consumes** the `Timer`, so the [[BorrowChecker|borrow checker]] guarantees no `Timer` reference outlives the reclaim. Combined with the [[Singleton|singleton]] / [[rust-embedded-book-peripherals-singletons|"exactly one peripheral handle"]] discipline from [[rust-embedded-book-peripherals-singletons]], `free` is the **only** legal way to get a `TIMER0` back from a `Timer` — so reusing the peripheral after `free` is a fresh `Timer::new(periph)` call, not an aliased mutation.

## Connections

- [[TheEmbeddedRustBook]] — file 34/44.
- [[rust-embedded-book-design-patterns-hal-index]] — parent sub-chapter (file 31/44).
- [[rust-embedded-book-design-patterns-hal-checklist]] — top-level checklist that lists `C-FREE` / `C-REEXPORT-PAC` / `C-HAL-TRAITS` under the **Interoperability** group (file 32/44).
- [[rust-embedded-book-design-patterns-hal-naming]] — prior leaf-section (file 33/44, the **Naming** group).
- [[HALCrate]] — the crate kind these three patterns govern.
- [[PeripheralAccessCrate]] — the underlying layer `C-REEXPORT-PAC` exposes (under the `pac` name).
- [[EmbeddedHalCrate]] — the trait crate `C-HAL-TRAITS` mandates implementations against.
- [[Svd2Rust]] — the canonical PAC generator named in `C-REEXPORT-PAC` (*"HALs can be written on top of svd2rust-generated PACs"*).
- [[Peripheral]] — the raw object `C-FREE` returns from the destructor.
- [[rust-embedded-book-portability-index]] — defines `embedded-hal` and the M·N → M+N complexity-collapse argument; `C-HAL-TRAITS` is the authoring-side discipline that enables the collapse.
- [[rust-embedded-book-peripherals-singletons]] — the singleton discipline `C-FREE` plugs into (the consumed `Timer` returns the unique `TIMER0` token).
- [[BorrowChecker]] — enforces the by-value `self` on `free` (no aliased peripheral after reclaim).
- [[TypeStateProgramming]] — relevant to `C-HAL-TRAITS` ("multiple traits per type" applies cleanly to typestate-parameterized GPIO pins implementing different trait sets in different states).

## Contradictions

- None. **Strictly additive** — operationalizes the [[HALCrate|HAL]] / [[PeripheralAccessCrate|PAC]] / [[EmbeddedHalCrate|`embedded-hal`]] stack from [[rust-embedded-book-start-registers]] and the M·N → M+N portability argument from [[rust-embedded-book-portability-index]] as three cite-able authoring conventions for [[HALCrate|HAL]] crates. The `C-FREE` round-trip invariant is consistent with — and reinforced by — the [[Singleton|singleton]] discipline established in [[rust-embedded-book-peripherals-singletons]].
