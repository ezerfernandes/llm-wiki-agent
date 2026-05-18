---
title: "build.rs"
type: concept
tags: [rust, cargo, build, ffi]
sources: [rust-embedded-book-interoperability-c-with-rust, rust-embedded-book-c-tips-index]
last_updated: 2026-05-16
---

# `build.rs`

[[Cargo]]'s **pre-build hook** — a file written in Rust placed at the **package root** that Cargo compiles and **executes on the compilation host**, after the package's dependencies are built but **before** the package itself is built ([[rust-embedded-book-interoperability-c-with-rust]]):

> "A `build.rs` script is a file written in Rust syntax, that is executed on your compilation machine, AFTER dependencies of your project have been built, but BEFORE your project is built."

Three canonical embedded uses:

1. **Code generation** — most commonly running [[Bindgen]] over a C header to emit a `bindings.rs` the package then `include!()`s.
2. **Shelling out to external build systems** — using `std::process::Command` to invoke `make` / `CMake` / vendor SDK scripts and then copy the produced static archive into Cargo's `target` directory for the final link step.
3. **Direct C/C++ compilation** — via the [[CcCrate|`cc` crate]], whose `cc::Build::new().file("src/foo.c").compile("foo");` deposits a `libfoo.a` static archive that Cargo's link step picks up.

## Host vs target — the crucial subtlety

A `build.rs` is compiled and run **on the host that drives `cargo build`**, *not* the embedded target. Even when the package itself targets `thumbv7m-none-eabi` / [[NoStd|`no_std`]] / [[BareMetalProgramming|bare-metal]], the `build.rs` can freely depend on `std`, `tokio`, `reqwest`, anything that runs on the developer's machine ([[rust-embedded-book-interoperability-c-with-rust]]):

> "While your crate may be targeting a `no_std` embedded platform, your `build.rs` executes only on machines compiling your crate. This means you may use any Rust crates which will run on your compilation host."

This host/target split is what lets one Cargo package contain both **firmware code** (target-compiled, `no_std`) and a **C toolchain driver** (host-compiled, `std`-rich) without contradiction.

## Other embedded uses

The [[rust-embedded-book-c-tips-index|C-tips chapter]] named `build.rs` (in passing) as the Rust replacement for embedded-C custom-build steps such as **[[LinkerScript|linker-script]] generation** — and noted that Cargo has **no post-build hook**, so any post-link artifact mutation has to be done either as part of a runner command or as a separate script.

## Connections

- [[Cargo]] — owns the build-graph and is the entity that runs `build.rs`.
- [[rust-embedded-book-interoperability-c-with-rust]] — the source where `build.rs` is operationalized for C-interop.
- [[rust-embedded-book-c-tips-index]] — names `build.rs` as the C→Rust analog of custom build-system steps.
- [[CcCrate]] — the idiomatic-Rust C compiler wrapper invoked from inside `build.rs`.
- [[Bindgen]] — the auto-binding generator invoked from inside `build.rs`.
- [[LinkerScript]] — sometimes generated from `build.rs` (the `memory.x` pattern in the [[rust-embedded-book-start-qemu|`cortex-m-quickstart`]] template).
- [[CrossCompilation]] — `build.rs` runs on the host while the rest of the package cross-compiles.
- [[NoStd]] — the regime the **package** targets; the `build.rs` itself is `std`.
