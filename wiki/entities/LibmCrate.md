---
title: "libm"
type: entity
tags: [rust, embedded, crate, math, no-std]
sources: [rust-embedded-book-unsorted-math]
last_updated: 2026-05-16
---

# libm

**Pure-Rust port of C's `libm` — the standard math library** ([`crates.io/crates/libm`](https://crates.io/crates/libm)). Re-exposes the C `<math.h>` operations (`sqrt`, `sin`, `cos`, `tan`, `exp`, `log`, `pow`, `floor`, `ceil`, `round`, `fma`, …) as Rust **free functions** callable from any [[NoStd|`#![no_std]`]] crate, with no [[GlobalAllocator|global allocator]] or [[RustRuntime|runtime]] dependency. The recommended drop-in fix in *[[TheEmbeddedRustBook]]* for the [[RustStandardLibrary|`std`]]-only methods on `f32` / `f64` that [[RustCoreLibrary|`core`]] does not provide ([[rust-embedded-book-unsorted-math]]):

```rust
// std side — inherent methods on the primitive type
let r = x.sqrt();

// no_std side — free functions
use libm::{exp, floorf, sin, sqrtf};
let r = sqrtf(x);
```

## Why it exists

Rust's float primitives (`f32`, `f64`) live in `core` and are always available, but their **transcendental and rounding methods** (`sqrt`, `sin`, `exp`, `floor`, `ln`, `pow`, `atan2`, etc.) live in `std`. The reason is historical: the canonical reference implementations are in C's `libm`, which `core` cannot depend on without a C runtime. `libm` (the Rust crate) is the gap-filler — a from-scratch Rust reimplementation maintained by the [[RustEmbeddedWorkingGroup|Rust Embedded WG]] (`rust-lang/libm`) that the entire [[NoStd|`no_std`]] ecosystem leans on.

## Precision-suffix convention

`libm` mirrors C's naming: `f`-suffixed functions take and return `f32`, no-suffix functions take and return `f64`. The chapter's example uses both forms:

| `libm` function | Input / output |
|---|---|
| `sqrtf(x: f32) -> f32` | single-precision |
| `floorf(x: f32) -> f32` | single-precision |
| `sin(x: f64) -> f64` | double-precision |
| `exp(x: f64) -> f64` | double-precision |

The chapter's example calls `.into()` on its `f32` arguments passed to `sin` / `exp` to widen them, e.g. `sin(floored_float.into())` — a giveaway that the `f` suffix is `libm`'s precision discriminator, not a Rust idiom.

## When `libm` isn't enough

The math chapter's further-reading list names five crates the wiki does not (yet) cover individually — `cmsis-dsp-sys` (CMSIS DSP bindings for SIMD-accelerated [[ARMCortexM|Cortex-M]] DSP), `constgebra` (`const fn` linear algebra), `micromath` (compact `no_std` math with accuracy-for-size tradeoffs), `microfft` (in-place FFT on stack), and `nalgebra` (general-purpose Rust linalg, optional `no_std` feature). `libm` is the scalar-transcendental floor of the stack; the rest layer on top for DSP / linalg / FFT.

## Connections

- [[NoStd]] — `libm` is the canonical math gap-filler for `#![no_std]` crates.
- [[RustCoreLibrary]] — exposes `f32` / `f64` but not their transcendental methods; `libm` covers the missing API surface.
- [[RustStandardLibrary]] — provides the same operations as **inherent methods** (`x.sqrt()`); `libm` provides them as **free functions** (`sqrtf(x)`).
- [[RustEmbeddedWorkingGroup]] — maintains the `rust-lang/libm` repo.
- [[TheEmbeddedRustBook]] — names `libm` in [[rust-embedded-book-unsorted-math]] as the standard `no_std` math recipe.
