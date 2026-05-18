---
title: "Cargo"
type: entity
tags: [rust, build-system, package-manager, toolchain]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# Cargo

[[RustLanguage|Rust]]'s official build system and package manager. Distributed with the toolchain via [[Rustup]]; invoked as `cargo build` / `cargo run` / `cargo test`. Subcommands are extensible — any `cargo-<name>` binary on `$PATH` becomes `cargo <name>`. In *[[TheEmbeddedRustBook]]* the build-side toolchain is anchored on Cargo plus two of its subcommand extensions: [[CargoBinutils|`cargo-binutils`]] (LLVM `objdump` / `nm` / `size`) and [[CargoGenerate|`cargo-generate`]] (project-from-template instantiation) ([[rust-embedded-book-intro-tooling]]).

Cross-compilation is a first-class Cargo workflow: `cargo build --target=<triple>` (e.g. `thumbv7em-none-eabihf`) combined with `rustup target add` installs and uses the per-target standard library ([[CrossCompilation]]).

## Connections

- [[RustLanguage]] — the language Cargo builds.
- [[Rustc]] — the compiler Cargo drives.
- [[Rustup]] — the toolchain installer that ships Cargo.
- [[CargoBinutils]] — Cargo subcommand wrapping LLVM binutils.
- [[CargoGenerate]] — Cargo subcommand for project templates.
- [[CrossCompilation]] — Cargo's `--target` flag drives the embedded build flow.
- [[TheEmbeddedRustBook]] — uses Cargo as the build-side anchor.
