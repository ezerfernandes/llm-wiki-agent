---
title: "Rust Target (Target Triple)"
type: concept
tags: [rust, toolchain, cross-compilation, embedded]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# Rust Target (Target Triple)

A *target triple* names the architecture / vendor / OS / ABI combination [[Rustc|`rustc`]] should emit code for — e.g. `thumbv7em-none-eabihf` (ARMv7E-M, no OS, hard-float EABI) for the [[STM32F303VCT6]]'s [[ARMCortexM|Cortex-M4F]], or `x86_64-unknown-linux-gnu` for a typical desktop. Installed via `rustup target add <triple>` ([[Rustup]]) and selected per build via `cargo build --target=<triple>` ([[Cargo]]).

In *[[TheEmbeddedRustBook]]* the target-triple system is the operational mechanism behind [[CrossCompilation|cross compilation]]: every Cortex-M example sets `--target=thumbv*-none-eabi*` and links against the pre-built target-specific [[RustCoreLibrary|`libcore`]] that `rustup target add` fetched ([[rust-embedded-book-intro-tooling]]).

## Connections

- [[Rustup]] — `rustup target add` installs target-specific artifacts.
- [[Cargo]] — `--target=<triple>` selects the target for a build.
- [[Rustc]] — consumes the triple to drive LLVM codegen.
- [[CrossCompilation]] — target triples are the operational unit of cross-compilation.
- [[ARMCortexM]] — the architecture family for which the embedded-Rust book picks triples like `thumbv7em-none-eabihf`.
- [[NoStd]] — `none` in the OS slot of the triple is what implies a bare-metal target with no OS.
