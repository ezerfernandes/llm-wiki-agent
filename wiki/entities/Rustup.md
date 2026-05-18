---
title: "rustup"
type: entity
tags: [rust, toolchain, installer]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# rustup

[[RustLanguage|Rust]]'s official toolchain installer and multiplexer. Manages multiple parallel Rust toolchains (stable / beta / nightly / pinned versions), installs cross-compilation targets (`rustup target add <triple>`), and installs optional components (`rustup component add <component>`). Ships [[Cargo]] and [[Rustc]].

In *[[TheEmbeddedRustBook]]* `rustup` is the gateway tool for the embedded build flow: `rustup target add thumbv7em-none-eabihf` (and friends) installs the [[ARMCortexM|Cortex-M]] target's pre-built core library; `rustup component add llvm-tools` installs the LLVM binaries that [[CargoBinutils|`cargo-binutils`]] wraps — *"the same one-command installation regardless of your OS"* ([[rust-embedded-book-intro-tooling]]).

## Connections

- [[RustLanguage]] — the language whose toolchain `rustup` manages.
- [[Cargo]] — shipped with `rustup`.
- [[Rustc]] — shipped with `rustup`.
- [[CargoBinutils]] — depends on `rustup component add llvm-tools`.
- [[RustTarget]] — `rustup target add` installs target-triple-specific artifacts.
- [[CrossCompilation]] — `rustup target add` is the operational bridge for cross-builds.
