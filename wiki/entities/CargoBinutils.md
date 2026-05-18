---
title: "cargo-binutils"
type: entity
tags: [rust, cargo-subcommand, llvm, toolchain, embedded]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# cargo-binutils

A collection of [[Cargo]] subcommands wrapping the LLVM binary-inspection tools that ship with the [[RustLanguage|Rust]] toolchain — LLVM versions of `objdump`, `nm`, and `size`. Maintained at [github.com/rust-embedded/cargo-binutils](https://github.com/rust-embedded/cargo-binutils); the book targets version ≈ 0.1.4 ([[rust-embedded-book-intro-tooling]]).

Two stated advantages over GNU binutils:

1. **One-command cross-OS install** — `rustup component add llvm-tools` works the same on every host OS via [[Rustup]].
2. **Universal architecture coverage** — any architecture [[Rustc|`rustc`]] supports (ARM, x86_64, RISC-V, …) is also supported by `cargo-objdump` / `cargo-nm` / `cargo-size`, because they share the LLVM backend.

This is the canonical binary-inspection path on every platform supported by *[[TheEmbeddedRustBook]]*.

## Connections

- [[Cargo]] — the build system whose subcommand interface `cargo-binutils` extends.
- [[Rustc]] — shared LLVM backend is what enables universal architecture coverage.
- [[Rustup]] — `rustup component add llvm-tools` is the install path.
- [[RustEmbeddedWorkingGroup]] — maintainer (rust-embedded/cargo-binutils).
- [[TheEmbeddedRustBook]] — listed in the toolchain inventory ([[rust-embedded-book-intro-tooling]]).
