---
title: "Cross Compilation"
type: concept
tags: [embedded, toolchain, build]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# Cross Compilation

Building a binary on one machine (the *host*, typically a desktop x86_64 or arm64 workstation) for execution on a different target architecture (e.g. an [[ARMCortexM|ARM Cortex-M]] [[Microcontroller|microcontroller]]). Standard in [[EmbeddedSystems|embedded development]] because the target MCU usually cannot host a compiler itself. [[TheEmbeddedRustBook]] lists cross-compilation as a prerequisite concept the embedded-experienced reader should already know ([[rust-embedded-book-intro-index]]).

In the Rust ecosystem this is handled by `rustup target add` + Cargo's `--target=<triple>` flag (e.g. `thumbv7em-none-eabihf` for Cortex-M4 with hardware float), backed by LLVM's multi-target codegen. The target-triple system is itself a separate concept ([[RustTarget]]); the toolchain inventory that operationalizes cross-compilation in the book is *[[rust-embedded-book-intro-tooling]]*: [[Cargo]] + [[Rustc]] + [[Rustup]] + [[CargoBinutils]] + [[QEMU]].

## Connections

- [[EmbeddedSystems]] — cross-compilation is part of the embedded build flow.
- [[BareMetalProgramming]] — the target side typically has no OS to host a native compiler.
- [[RustLanguage]] — Rust's `rustup` + LLVM backend makes cross-compilation a first-class workflow.
- [[Cargo]] / [[Rustc]] / [[Rustup]] — the concrete toolchain implementing it ([[rust-embedded-book-intro-tooling]]).
- [[RustTarget]] — the target-triple system that names what "cross" means in any given build.
- [[CargoBinutils]] — the LLVM `objdump` / `nm` / `size` cross-architecture binary-inspection layer.
