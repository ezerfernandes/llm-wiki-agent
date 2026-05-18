---
title: "bindgen"
type: entity
tags: [rust, embedded, ffi, c-interop, codegen, tooling]
sources: [rust-embedded-book-interoperability-c-with-rust]
last_updated: 2026-05-16
---

# bindgen

`rust-lang/rust-bindgen` — the **automatic Rust-binding generator** for C and C++ headers. Replaces the error-prone manual translation of `cool.h` to `cool_bindings.rs` with a one-shot codegen pass over the C header set ([[rust-embedded-book-interoperability-c-with-rust]]):

> "Rather than manually generating these interfaces, which may be tedious and error prone, there is a tool called bindgen which will perform these conversions automatically."

Typical four-step recipe from the chapter:

1. **Gather** all C/C++ headers defining interfaces or datatypes you want to use from Rust.
2. **Write a `bindings.h`** that `#include`s each of those headers.
3. **Feed `bindings.h` to `bindgen`** along with the compilation flags the C build uses (include paths, defines, target triple). The output is Rust code.
4. **Pipe the output to `bindings.rs`** in your project (commonly from a [[BuildRs|`build.rs`]] script), then `include!()` it from your Rust source.

## The `no_std` flags

For [[NoStd|`no_std`]] embedded targets the chapter gives two specific tips:

- **`Builder.ctypes_prefix("cty")` / `--ctypes-prefix=cty`** — make the emitted code use the [`cty`](https://crates.io/crates/cty) crate's `c_int` / `c_char` / `c_void` aliases instead of `std::os::raw::*`, so the resulting bindings link in a `no_std` build.
- **`Builder.use_core()` / `--use-core`** — make the emitted code reference `core::` paths instead of `std::` paths, so the bindings compile under `#![no_std]`.

> "use `Builder.ctypes_prefix("cty")` / `--ctypes-prefix=cty` and `Builder.use_core()` / `--use-core` to make the generated code `#![no_std]` compatible."

The companion runtime dependency is the [`cty`](https://crates.io/crates/cty) crate — the [[rust-embedded-book-interoperability-index|interop-index chapter]] previously named it as the community equivalent of `core::ffi` for older toolchains.

## What it emits

For each C declaration, `bindgen` emits the Rust equivalent the chapter previously walked by hand:

- `typedef struct CoolStruct { int x; int y; }` → `#[repr(C)] pub struct CoolStruct { pub x: cty::c_int, pub y: cty::c_int }` ([[ReprC]]).
- `void cool_function(int i, char c, CoolStruct* cs);` → an `extern "C" { pub fn cool_function(i: cty::c_int, c: cty::c_char, cs: *mut CoolStruct); }` block ([[ExternC]], [[RawPointer]]).
- `enum`s, `#define` integer constants, function-like macros (sometimes), and (with C++ mode) opaque class types.

## Position in the C-interop matrix

`bindgen` is the **Rust-side codegen** half of the build decision tree in [[rust-embedded-book-interoperability-c-with-rust]]; pairs with the [[CcCrate|`cc` crate]] on the **C-side build** half. A canonical `build.rs` invokes both: `cc` to produce `libfoo.a` and `bindgen` to produce `bindings.rs`, both consumed by the final `cargo build`.

## Symmetric counterpart — [[Cbindgen|`cbindgen`]]

`bindgen` is the **C → Rust** direction; its mirror is [[Cbindgen|`cbindgen`]] (`eqrion/cbindgen`), introduced by [[rust-embedded-book-interoperability-rust-with-c]], which generates **C headers from Rust source** in the opposite direction. A project that embeds a Rust core in a C application uses `cbindgen`; a project that wraps a C library in Rust uses `bindgen`; a project doing both uses both.

## Connections

- [[BuildRs]] — the host-side script that typically invokes `bindgen` programmatically.
- [[rust-embedded-book-interoperability-c-with-rust]] — the source that names `bindgen` and gives the `no_std` flag recipe.
- [[rust-embedded-book-interoperability-index]] — its `cty` / `cstr_core` recommendation is the runtime companion to `bindgen --ctypes-prefix=cty`.
- [[CcCrate]] — the matching C-side build tool; `bindgen` writes the Rust side, `cc` builds the C side.
- [[ExternC]] — what `bindgen` emits for C function declarations.
- [[ReprC]] — what `bindgen` emits for C struct declarations.
- [[RawPointer]] — what `bindgen` emits in place of C `T*` parameters.
- [[NoStd]] — the regime for which `--use-core` / `--ctypes-prefix=cty` exist.
- [[RustCoreLibrary]] — the library `--use-core` redirects emitted code to.
- [[Cbindgen]] — the symmetric Rust → C header generator.
- [[rust-embedded-book-interoperability-rust-with-c]] — the chapter that introduces the symmetric `cbindgen` direction.
