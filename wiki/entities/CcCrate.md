---
title: "`cc` crate"
type: entity
tags: [rust, embedded, ffi, build, crate]
sources: [rust-embedded-book-interoperability-c-with-rust]
last_updated: 2026-05-16
---

# `cc` crate

Community crate (`github.com/alexcrichton/cc-rs`, originally **gcc-rs**) that wraps the **host's C/C++ compiler** in an idiomatic Rust builder API for use from a [[BuildRs|`build.rs`]] script ([[rust-embedded-book-interoperability-c-with-rust]]):

> "For projects with limited dependencies or complexity, or for projects where it is difficult to modify the build system to produce a static library (rather than a final binary or executable), it may be easier to instead utilize the `cc` crate, which provides an idiomatic Rust interface to the compiler provided by the host."

The simplest case — a single C file compiled into a static archive Cargo's final link step pulls in — is the four-line canonical recipe from the chapter:

```rust,ignore
fn main() {
    cc::Build::new()
        .file("src/foo.c")
        .compile("foo");
}
```

The `build.rs` lives at the **package root**. *"Then `cargo build` will compile and execute it before the build of the package. A static archive named `libfoo.a` is generated and placed in the `target` directory."* No `Cargo.toml` `[link]` stanza, no separate `Makefile`, no out-of-tree state.

## Position in the C-interop matrix

`cc` is the **simple-case branch** of the C-build decision tree in [[rust-embedded-book-interoperability-c-with-rust]]:

| C-side delivery | Build step |
|---|---|
| Already-distributed static archive | None — write the [[ExternC|`extern "C"`]] declarations and link it |
| Complex existing `make` / `CMake` project | Shell out via `std::process::Command` from `build.rs`, copy `lib*.a` into `target/` |
| **Small C source set** | **`cc` crate from `build.rs`** |

Pairs naturally with [[Bindgen]] (which auto-generates the Rust-side [[ExternC|`extern "C"`]] blocks) — a typical `build.rs` invokes both, with `cc` producing the static archive and `bindgen` producing the matching `bindings.rs`.

## Host/target sensitivity

`cc` invokes the **host-relevant** C compiler for the package's **target triple** — it dispatches by `$CC` / `$CC_<target>` env vars and `cargo`'s `TARGET` env, so cross-compiling a `thumbv7m-none-eabi` package on a Linux host correctly drives `arm-none-eabi-gcc`. The `build.rs` itself runs on the host (per [[BuildRs]]'s host/target split), but the C it produces is compiled **for the embedded target**.

## Connections

- [[BuildRs]] — the host-side script in which `cc::Build::new()` is invoked.
- [[rust-embedded-book-interoperability-c-with-rust]] — the source where `cc` is named.
- [[Bindgen]] — the matching auto-binder; `cc` builds the C side, `bindgen` builds the Rust side.
- [[ExternC]] — `cc` produces the static archive; `extern "C"` blocks declare the symbols against it.
- [[ReprC]] — the layout discipline on the structs shared between the C source `cc` compiles and the Rust side.
- [[Cargo]] — runs the `build.rs` that uses `cc`; the `target/` directory it shares with the package is where `lib*.a` lands.
- [[CrossCompilation]] — `cc`'s target-aware compiler dispatch is what makes it work for embedded targets, not just hosted.
