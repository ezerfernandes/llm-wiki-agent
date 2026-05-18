---
title: "cbindgen"
type: entity
tags: [rust, embedded, ffi, c-interop, codegen, tooling]
sources: [rust-embedded-book-interoperability-rust-with-c]
last_updated: 2026-05-16
---

# cbindgen

`eqrion/cbindgen` (`github.com/eqrion/cbindgen`) — the **automatic C/C++ header generator** that analyzes Rust source code and emits `.h` / `.hpp` declarations for each `#[no_mangle] pub extern "C" fn` and every `#[repr(C)]` type the Rust crate exports ([[rust-embedded-book-interoperability-rust-with-c]]):

> "There is a tool to automate this process, called cbindgen which analyses your Rust code and then generates headers for your C and C++ projects from it."

## Position — the inverse of [[Bindgen]]

`cbindgen` is the **mirror** of [[Bindgen|`bindgen`]]:

| Tool | Direction | Input | Output |
|---|---|---|---|
| [[Bindgen]] | C → Rust | `.h` / `.hpp` C headers | Rust `extern "C" { ... }` blocks + `#[repr(C)]` structs |
| **`cbindgen`** | **Rust → C** | **Rust source** | **C `.h` / `.hpp` headers with `void rust_function();` etc.** |

A project that exposes Rust to C uses `cbindgen`; a project that consumes C from Rust uses `bindgen`. A project doing **both directions** (a Rust core wrapped in a thin C shim around an existing C codebase) uses **both**.

## What it emits

For each Rust function exported with the canonical pair ([[NoMangle|`#[no_mangle]`]] + [[ExternC|`pub extern "C"`]]):

```rust,ignore
#[no_mangle]
pub extern "C" fn rust_function() {}
```

`cbindgen` produces the matching C declaration:

```C
void rust_function();
```

For each `#[repr(C)]` struct ([[ReprC]]), `cbindgen` emits the equivalent C `typedef struct` declaration. Same scope as the manual translations the chapter walks through; just automated.

## Consumption from C

Once `cbindgen` has generated `my-rust-project.h`, the C consumer's responsibility is trivial ([[rust-embedded-book-interoperability-rust-with-c]]):

```C
#include "my-rust-project.h"
rust_function();
```

The C compiler now has a function declaration; the linker resolves it at link time against whatever Cargo's `[lib] crate-type` produced — `lib<name>.so` ([[CrateType|`cdylib`]]) or `lib<name>.a` ([[CrateType|`staticlib`]]).

## Position in the Rust → C export pipeline

| Stage | Tool |
|---|---|
| Mark exported functions | `#[no_mangle] pub extern "C" fn` |
| Compile to systems library | `cargo build` with `crate-type = ["cdylib"]` / `["staticlib"]` |
| Generate the matching C header | **`cbindgen`** |
| Consume from C | `#include "my-rust-project.h"` + link |

## Connections

- [[rust-embedded-book-interoperability-rust-with-c]] — the source that names `cbindgen`.
- [[Bindgen]] — the **opposite-direction** tool (C → Rust). The two together cover the full bidirectional FFI codegen story.
- [[NoMangle]] — `cbindgen` keys off `#[no_mangle] pub extern "C" fn`-shaped functions when scanning the Rust source.
- [[ExternC]] — `cbindgen` only emits declarations for functions whose signature already specifies `extern "C"`.
- [[ReprC]] — `cbindgen` emits `typedef struct` declarations for `#[repr(C)]` structs that appear in exported signatures.
- [[CrateType]] — the C header `cbindgen` generates is only useful when the crate is built as `cdylib` or `staticlib`.
- [[BuildRs]] — `cbindgen` is typically invoked from a `build.rs` (programmatically, via its library API) so the C header is regenerated whenever the Rust source changes.
- [[Cargo]] — owns the `build.rs` execution that drives `cbindgen`; emits the `.so` / `.a` the generated header points at.
