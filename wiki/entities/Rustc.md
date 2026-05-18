---
title: "rustc"
type: entity
tags: [rust, compiler, llvm, toolchain]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# rustc

The [[RustLanguage|Rust]] compiler. LLVM-backed multi-target codegen — any architecture LLVM supports (ARM, x86_64, RISC-V, …) is in principle a `rustc` target. Distributed via [[Rustup]]; usually invoked indirectly through [[Cargo]] (`cargo build`) rather than directly.

*[[TheEmbeddedRustBook]]* requires `rustc` 1.31 / 1.31-beta or newer **plus** [[ARMCortexM|ARM Cortex-M]] target support installed via `rustup target add` ([[rust-embedded-book-intro-tooling]]). The shared LLVM backend is the reason [[CargoBinutils|`cargo-binutils`]]'s LLVM `objdump` / `nm` / `size` cover every architecture `rustc` cross-compiles to — *"because they both share the same LLVM backend."*

## Connections

- [[RustLanguage]] — the language `rustc` compiles.
- [[Cargo]] — the build front-end that drives `rustc`.
- [[Rustup]] — the installer that ships `rustc`.
- [[CargoBinutils]] — leans on `rustc`'s LLVM backend for universal architecture coverage.
- [[CrossCompilation]] — `rustc`'s multi-target LLVM codegen is what makes embedded cross-compilation trivial.
- [[ARMCortexM]] — the target ISA for every example in [[TheEmbeddedRustBook]].
