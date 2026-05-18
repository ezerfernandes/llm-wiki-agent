---
title: "The Embedded Rust Book — A first attempt in Rust"
type: source
tags: [rust, embedded, book-chapter, peripherals]
date: 2026-05-16
source_file: raw/book/src/peripherals/a-first-attempt.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — A first attempt in Rust

## Summary

File 19/44 of *[[TheEmbeddedRustBook]]* — the **Peripherals chapter's first code sub-section**, immediately after the chapter opener at file 18 ([[rust-embedded-book-peripherals-index]]). Walks the naive translation of the C "MMIO struct + pointer-cast" idiom into Rust, then iteratively patches its four defects (`unsafe` viral, no R/W discrimination, unrestricted access, **and most importantly, the compiler silently elides reads/writes without `volatile`**) by introducing (1) `core::ptr::read_volatile` / `write_volatile`, (2) the [[VolatileRegisterCrate|`volatile_register`]] crate's `RW<T>` / `RO<T>` typed register wrappers, and (3) a [[RustyWrapper|"Rusty wrapper"]] struct that owns an `&'static mut RegisterBlock`. Ends by exhibiting the remaining defect — `SystemTimer::new()` is callable arbitrarily many times, so two threads can manufacture independent handles to the same hardware register block — which **motivates the next sub-section on singletons / `Peripherals::take()`**. Anchor example: the [[ARMCortexM|Cortex-M]] [[SysTick]] register block at `0xE000_E010` (four 32-bit registers: `SYST_CSR`, `SYST_RVR`, `SYST_CVR`, `SYST_CALIB`).

## Key Claims

- **Registers as a `#[repr(C)]` struct**: a peripheral's register block is naturally modeled as a Rust struct with one field per register, marked `#[repr(C)]` so the Rust compiler uses C layout (field order preserved, no reordering). Without `#[repr(C)]`, Rust is free to re-order struct fields and the addresses would silently drift.
- **The C-style pointer cast**: `let systick = 0xE000_E010 as *mut SysTick; let time = unsafe { (*systick).cvr };` — works syntactically in Rust but inherits **four** problems from the C version.
- **The four defects of the naive struct-pointer approach**:
  1. `unsafe` is required at every access (viral `unsafe`).
  2. No way to declare which registers are read-only vs. read-write at the type level.
  3. Any code anywhere in the program can manufacture a pointer and access the hardware (no aliasing control).
  4. **It doesn't actually work** — compilers will elide repeated stores to the same RAM-typed address.
- **The volatility problem**: optimizers can drop a write that is immediately followed by another write to the same address (the first appears "dead"). For hardware registers, every read and write has a **side effect on the peripheral** and must not be elided.
- **C vs Rust volatility**: in C, the *variable* is marked `volatile`; in Rust, the **accesses** are marked volatile via `core::ptr::read_volatile` / `core::ptr::write_volatile`. The data carries no qualifier — the operation does.
- **`volatile_register` crate**: third-party crate providing `RW<T>` / `RO<T>` (and `WO<T>`) wrapper types with `read()` / `write()` methods that perform the volatile access internally. Encodes read-only-ness in the type (defect #2) and removes per-access `unsafe` for reads (defect #1 partially). Writes remain `unsafe` because "hardware is a bunch of mutable state and there's no way for the compiler to know whether these writes are actually safe."
- **The "Rusty wrapper" pattern**: hide the raw `RegisterBlock` behind a higher-level type (`SystemTimer`) holding an `&'static mut RegisterBlock`; expose safe methods (`get_time(&self)`, `set_reload(&mut self, …)`). The driver author hand-verifies the `unsafe` once and presents a safe API.
- **The remaining defect (singleton gap)**: `SystemTimer::new()` can be called arbitrarily many times. `&mut self` only prevents aliasing of *that specific `SystemTimer` value* — it does **not** prevent constructing a second `SystemTimer` pointing at the same physical register block. Two threads each calling `SystemTimer::new()` produce a race the borrow checker cannot detect — motivating the singleton pattern in the next sub-section.

## Key Quotes

> "The qualifier `#[repr(C)]` tells the Rust compiler to lay this structure out like a C compiler would. That's very important, as Rust allows structure fields to be re-ordered, while C does not." — the structural rationale for [[ReprC|`#[repr(C)]`]] on register-block structs.

> "Most importantly, it doesn't actually work…" — the punchline that makes [[VolatileMemoryAccess|volatility]] the chapter's central correctness concern (not a performance footnote).

> "In C, we can mark variables as `volatile` to ensure that every read or write occurs as intended. In Rust, we instead mark the *accesses* as volatile, not the variable." — the contrastive design choice that explains why Rust has `read_volatile` / `write_volatile` functions instead of a `volatile` type qualifier.

> "Hardware is a bunch of mutable state and there's no way for the compiler to know whether these writes are actually safe, so this is a good default position." — the chapter's rationale for keeping writes `unsafe` even after `volatile_register`.

> "Our `&mut self` argument to the `set_reload` function checks that there are no other references to *that* particular `SystemTimer` struct, but they don't stop the user creating a second `SystemTimer` which points to the exact same peripheral!" — the **singleton gap** that justifies the *next* sub-section.

## Connections

- [[TheEmbeddedRustBook]] — file 19/44; first code sub-section of the Peripherals chapter.
- [[rust-embedded-book-peripherals-index]] — preceding file (chapter opener); this file is the concrete-code follow-on that builds on the address-space mental model.
- [[Peripheral]] — the noun being accessed; this chapter shows the canonical Rust pattern for wrapping a [[MemoryMappedIO|memory-mapped]] register block.
- [[MemoryMappedIO]] — the access regime; this chapter is where MMIO meets the Rust **`volatile` access** primitives.
- [[SysTick]] — the worked example (four registers at `0xE000_E010`); same peripheral [[rust-embedded-book-start-registers]] accessed via the [[CortexMCrate|`cortex-m` crate]]. This chapter shows what would be required to *roll your own* SysTick driver from raw addresses up.
- [[ARMCortexM]] — defines the SysTick register block and address used as the running example.
- [[VolatileMemoryAccess]] (new) — the central correctness concept this chapter introduces.
- [[RawPointer]] (new) — the `*mut T` / `as` cast machinery Rust uses to express "the integer 0xE000_E010 is a pointer to a `SysTick`."
- [[ReprC]] (new) — the struct-layout attribute that makes the register-block-as-struct trick safe in Rust.
- [[VolatileRegisterCrate]] (new) — the `volatile_register` crate's `RW<T>` / `RO<T>` typed register wrappers.
- [[CortexMCrate]] — the production-grade equivalent of the "Rusty wrapper" pattern this chapter ends at (one layer above + with the singleton fix).
- [[PeripheralAccessCrate]] — the auto-generated chip-specific stack that productionizes the pattern at scale via [[Svd2Rust|`svd2rust`]] + [[SVDFile|SVD]].
- [[TypeStateProgramming]] — the broader Rust-on-hardware idiom this chapter participates in (encode read-only-ness, configuration state, etc. in the type system).
- [[NoStd]] — the regime this entire chapter assumes.

## Contradictions

None with existing wiki content. Strictly additive — concretizes the four-layer-crate-stack abstractions that [[rust-embedded-book-start-registers]] introduced operationally into the **manual-from-raw-addresses** version. Faintly clarifies an unstated assumption in [[SysTick]]'s page (which uses the polished `cortex_m::Peripherals::take()` interface): the [[CortexMCrate|`cortex-m`]] crate is the productionized form of exactly the wrapper-with-singleton pattern this chapter is building up to.
