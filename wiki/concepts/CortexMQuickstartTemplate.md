---
title: "cortex-m-quickstart Template"
type: concept
tags: [rust, embedded, project-template, cortex-m]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# cortex-m-quickstart Template

The canonical **project template for new [[ARMCortexM|Cortex-M]] Rust applications**, maintained by the [[RustEmbeddedWorkingGroup]] at [`github.com/rust-embedded/cortex-m-quickstart`](https://github.com/rust-embedded/cortex-m-quickstart). *[[TheEmbeddedRustBook]]*'s first code chapter ([[rust-embedded-book-start-qemu]]) uses it as the starting point for every example.

## What the template ships

- A `Cargo.toml` pre-wired with [[CortexMRTCrate|`cortex-m-rt`]] + [[PanicHaltCrate|`panic-halt`]] + the `cortex-m` crate.
- A barebone `src/main.rs` with the [[NoStd|`#![no_std]`]] + `#![no_main]` skeleton (the five-line canonical structure of every embedded-Rust program).
- An `examples/` directory with several worked sub-programs (`hello`, panic demos, exceptions, etc.).
- A `memory.x` [[LinkerScript|linker script]] template with placeholders the user fills with target-specific Flash / RAM regions.
- A `.cargo/config.toml` listing the four common [[RustTarget|Cortex-M target triples]] (`thumbv6m-none-eabi`, `thumbv7m-none-eabi`, `thumbv7em-none-eabi`, `thumbv7em-none-eabihf`) — three commented out, one active — and a commented-out `[target.thumbv7m-none-eabi]` runner line invoking `qemu-system-arm`.

## Three instantiation paths

The chapter enumerates three ways to pull the template — operationally equivalent, ergonomically very different:

1. **[[CargoGenerate|`cargo-generate`]]** (modern, recommended): `cargo install cargo-generate` then `cargo generate --git https://github.com/knurling-rs/app-template`. Note: the book actually directs `cargo-generate` at the [[Knurling]] `app-template` (a downstream fork / modernization), not the bare `cortex-m-quickstart`.
2. **`git clone`** the upstream repo and **manually substitute** Cargo.toml placeholders (`{{authors}}`, `{{project-name}}`).
3. **Download a ZIP snapshot** from the GitHub UI ("Clone or download" → "Download ZIP"). Same placeholder substitution as #2.

All three converge on the same on-disk project structure.

## Connections

- [[CortexMRTCrate]] — the runtime crate the template pre-wires.
- [[PanicHaltCrate]] — the default panic handler the template pre-wires.
- [[LinkerScript]] — `memory.x` is part of the template.
- [[RustTarget]] — the four Cortex-M triples are catalogued in the template's `.cargo/config.toml`.
- [[CargoGenerate]] — the official tool for instantiating the template.
- [[NoStd]] — the regime the template's skeleton is designed for.
- [[Knurling]] — publishes `app-template`, the modernized fork the book actually recommends in the `cargo-generate` invocation.
- [[RustEmbeddedWorkingGroup]] — upstream maintainer of `cortex-m-quickstart` proper.
- [[TheEmbeddedRustBook]] — the template underlies every example from [[rust-embedded-book-start-qemu|Chapter 11]] onward.
