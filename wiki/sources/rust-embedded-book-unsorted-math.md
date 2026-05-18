---
title: "The Embedded Rust Book — Performing Math Functionality"
type: source
tags: [rust, embedded, book-chapter, math]
date: 2026-05-16
source_file: raw/book/src/unsorted/math.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Performing Math Functionality

## Summary

File 43/44 of *[[TheEmbeddedRustBook]]* — **second substantive leaf** of the *Unsorted topics* chapter, immediately after [[rust-embedded-book-unsorted-speed-vs-size]] (file 42). Short, single-recipe chapter: with [[RustStandardLibrary|`std`]] the math methods `f32::floor` / `f32::sqrt` / `f32::sin` / `f32::exp` come for free as inherent methods on the primitive float types, but under [[NoStd|`#![no_std]`]] **these methods are not available** — [[RustCoreLibrary|`core`]] exposes the float primitives but not their transcendental / rounding operations, because their reference implementations live in C's `libm` and `core` cannot depend on a C runtime. The chapter's drop-in fix is the **[[LibmCrate|`libm`]] crate** — a pure-Rust port of the C `libm` that re-exposes the same operations as **free functions** (`libm::floorf` / `libm::sqrtf` / `libm::sin` / `libm::exp`) callable from any `no_std` crate without a global allocator or runtime. The worked example rewrites the same four-operation `hello`-style program twice — once for hosted `std`, once for [[ARMCortexM|Cortex-M]] `no_std` ([[CortexMRTCrate|`cortex-m-rt`]] + [[CortexMSemihostingCrate|`cortex-m-semihosting`]] + [[PanicHaltCrate|`panic-halt`]] + [[ARMSemihosting|`hprintln!`]]) — showing the syntactic delta is only **method-call vs free-function** (`x.sqrt()` → `sqrtf(x)`). Closes with a five-crate **further-reading list** for when scalar `libm` is not enough — `cmsis-dsp-sys` bindings (ARM's SIMD DSP library, hardware-accelerated on Cortex-M4F+), `constgebra` (`const fn` linear algebra), `micromath` (compact `no_std` math, accuracy-for-size tradeoffs), `microfft` (in-place FFT on `no_std`), and `nalgebra` (general-purpose Rust linalg, has a `no_std` feature). **`f32` vs `f64`** appears implicitly in the API split — `libm::sqrtf` (single-precision) vs `libm::sin` / `libm::exp` (double-precision); the chapter calls `.into()` on the `f32` arguments to widen them, signaling that the `*f` suffix is `libm`'s precision-naming convention (a port of C's `sqrtf` / `sqrt`).

## Key Claims

- **`std` math methods rely on the standard library.** With `std` available, `f32::floor` / `f32::sqrt` / `f32::sin` / `f32::exp` are callable as inherent methods on the primitive type. *"If you want to perform math related functionality like calculating the squareroot or the exponential of a number and you have the full standard library available, your code might look like this …"*
- **Under `no_std`, these methods are not available.** *"Without standard library support, these functions are not available."* The float primitive types themselves still exist in `core` — only the transcendental / rounding operations are missing.
- **The drop-in fix is the [`libm`](https://crates.io/crates/libm) crate.** *"An external crate like `libm` can be used instead."* Pure-Rust port of C's `libm`; no [[GlobalAllocator|global allocator]] required; works on every `no_std` target.
- **API shape: free functions, not methods.** `libm` exposes `floorf` / `sqrtf` / `sin` / `exp` as plain `pub fn`s — `x.sqrt()` becomes `sqrtf(x)` and is imported via `use libm::{exp, floorf, sin, sqrtf};`.
- **Precision suffix follows C convention.** Single-precision (`f32`) operations get the `f` suffix (`sqrtf`, `floorf`); double-precision (`f64`) operations have no suffix (`sin`, `exp`). The chapter's example calls `.into()` on `f32` arguments passed to `sin` / `exp` to widen them to `f64`.
- **The chapter's `no_std` skeleton is the canonical book template** — `#![no_main]` + `#![no_std]` + `use panic_halt as _;` ([[PanicHaltCrate|`panic-halt`]]) + `use cortex_m_rt::entry;` ([[CortexMRTCrate|`cortex-m-rt`]]) + `use cortex_m_semihosting::{debug, hprintln};` ([[CortexMSemihostingCrate|`cortex-m-semihosting`]] for [[ARMSemihosting|host I/O]]) + a `#[entry] fn main() -> !` divergent `main` ending in `loop {}`. Same shape as every prior code chapter from [[rust-embedded-book-start-qemu]] onward.
- **Five named crates for heavier math.** *"If you need to perform more complex operations like DSP signal processing or advanced linear algebra on your MCU, the following crates might help you"* — [`cmsis-dsp-sys`](https://github.com/jacobrosenthal/cmsis-dsp-sys) (CMSIS DSP library bindings), [`constgebra`](https://crates.io/crates/constgebra) (`const fn` linear algebra), [`micromath`](https://github.com/tarcieri/micromath) (compact `no_std` math), [`microfft`](https://crates.io/crates/microfft) (in-place FFT on stack), [`nalgebra`](https://github.com/dimforge/nalgebra) (general-purpose Rust linalg, optional `no_std`).
- **The hosted vs `no_std` halves of the example differ only in host-I/O macro.** `println!` (`std`) vs `hprintln!` ([[ARMSemihosting]] via [[CortexMSemihostingCrate|`cortex-m-semihosting`]]) — the math computation is otherwise the same modulo the method-vs-free-function change.
- **`debug::exit(debug::EXIT_SUCCESS)` is hardware-unsafe.** The closing comment — *"NOTE do not run this on hardware; it can corrupt OpenOCD state"* — re-iterates the warning from [[rust-embedded-book-start-semihosting]]: `debug::exit` is a [[QEMU]]-only escape hatch.

## Key Quotes

> "If you want to perform math related functionality like calculating the squareroot or the exponential of a number and you have the full standard library available, your code might look like this …"

> "Without standard library support, these functions are not available. An external crate like `libm` can be used instead."

> "If you need to perform more complex operations like DSP signal processing or advanced linear algebra on your MCU, the following crates might help you"

## Connections

- [[TheEmbeddedRustBook]] — file 43/44; second substantive leaf of the *Unsorted topics* chapter.
- [[rust-embedded-book-unsorted-speed-vs-size]] — predecessor (file 42/44).
- [[rust-embedded-book-unsorted-index]] — chapter opener (file 41/44).
- [[LibmCrate]] — the chapter's protagonist; the `no_std` math-functions crate.
- [[NoStd]] — the regime that motivates `libm`; the chapter is a worked example of *"what you lose when you drop `std`"* (the float method set) and how to recover it.
- [[RustCoreLibrary]] — exposes the `f32` / `f64` types but not their transcendental / rounding methods; `libm` is the gap-filler.
- [[RustStandardLibrary]] — provides `f32::sqrt` / `f32::sin` / `f32::exp` / `f32::floor` as inherent methods on the hosted side of the chapter's two examples.
- [[Rustc]] — the compiler whose `f32` / `f64` types are exposed in `core` but whose transcendental methods live in `std`.
- [[ARMCortexM]] — the target of the `no_std` half of the example.
- [[CortexMRTCrate]] — provides `#[entry]` for the `no_std` example's `fn main() -> !`.
- [[CortexMSemihostingCrate]] — provides `hprintln!` / `debug::exit` for host-side I/O on the `no_std` half.
- [[PanicHaltCrate]] — the example's panic handler (`use panic_halt as _;`).
- [[ARMSemihosting]] — the host-I/O transport `hprintln!` uses to print the math results to the debugger.

## Contradictions

None — the chapter is a tactical `no_std` recipe compatible with prior files. The `libm` recommendation is **net-new** to the wiki (no prior chapter named it); the `no_std` skeleton, `panic_halt` / `cortex-m-rt` / `cortex-m-semihosting` / `hprintln!` shape, and the *"don't `debug::exit` on hardware"* warning all match prior files exactly.
