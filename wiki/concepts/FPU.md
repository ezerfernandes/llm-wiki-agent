---
title: "FPU (Floating-Point Unit)"
type: concept
tags: [embedded, hardware, cpu, floating-point, acronym]
sources: [rust-embedded-book-appendix-glossary, rust-embedded-book-start-hardware]
last_updated: 2026-05-16
---

# FPU — Floating-Point Unit

**FPU** = *Floating-Point Unit*. A dedicated hardware block on (some) CPUs / [[Microcontroller|microcontrollers]] that executes **floating-point arithmetic** (IEEE 754 add / mul / sub / div / sqrt / fused-multiply-add) in hardware rather than via software emulation in [[RustCoreLibrary|`core`]] / `libgcc` / `compiler-builtins`. *[[TheEmbeddedRustBook]]*'s glossary describes it as **"a 'math processor' running only operations on floating-point numbers"** ([[rust-embedded-book-appendix-glossary]]).

## Why it matters in embedded Rust

The presence or absence of an FPU is encoded in the [[RustTarget|target triple]] used to cross-compile firmware:

| Target triple | Core | FPU |
|---|---|---|
| `thumbv6m-none-eabi` | [[ARMCortexM|Cortex-M0 / M0+ / M1]] | none |
| `thumbv7m-none-eabi` | [[ARMCortexM|Cortex-M3]] | none |
| `thumbv7em-none-eabi` | [[ARMCortexM|Cortex-M4 / M7]] (soft-float) | optional, **disabled** |
| `thumbv7em-none-eabihf` | [[ARMCortexM|Cortex-M4F / M7F]] | **hardware** (`hf` suffix) |
| `thumbv8m.main-none-eabihf` | [[ARMCortexM|Cortex-M33F / M35PF / M55]] | hardware |

The **`hf` suffix** means the calling convention uses the FPU registers (`s0`–`s31`) to pass `f32` arguments rather than the integer registers — **ABI-incompatible** with soft-float code, so the suffix must match the chip. The book's first hardware chapter ([[rust-embedded-book-start-hardware]]) switches to `thumbv7em-none-eabihf` precisely because the [[STM32F303VCT6]] is a [[ARMCortexM|Cortex-M4F]] with FPU.

## Software-float fallback

Without an FPU (and for `f64` on a single-precision FPU like the M4F's), the [[Rustc|rustc]] / LLVM backend lowers float operations to **soft-float** calls into `compiler-builtins` (`__aeabi_fadd`, `__aeabi_fmul`, etc.). Same arithmetic, dramatically slower — see [[rust-embedded-book-unsorted-math]] for the [[NoStd|`no_std`]] math-function corollary (transcendentals need the [[LibmCrate|`libm`]] crate even with an FPU).

## Connections

- [[ARMCortexM]] — the ISA family whose M4F / M7F / M33F / M35PF / M55 variants carry an FPU; M0 / M0+ / M3 do not.
- [[STM32F303VCT6]] — the [[STM32F3DISCOVERY]]'s MCU; Cortex-M4F **with FPU** — drives the book's `thumbv7em-none-eabihf` target choice.
- [[RustTarget]] — target triples carry the FPU presence in the `hf` suffix.
- [[rust-embedded-book-start-hardware]] — sets `target = "thumbv7em-none-eabihf"` for the real-hardware F3 board.
- [[rust-embedded-book-unsorted-math]] — transcendental ops are not in [[RustCoreLibrary|`core`]] even with an FPU; the [[LibmCrate|`libm`]] crate fills the gap.
- [[LibmCrate]] — pure-Rust libm port for `no_std`.
- [[rust-embedded-book-appendix-glossary]] — source for this acronym entry.
- [[TheEmbeddedRustBook]] — parent book.
