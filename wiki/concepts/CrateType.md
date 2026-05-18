---
title: "Crate Type (cdylib / staticlib)"
type: concept
tags: [rust, embedded, cargo, ffi, linker, c-interop]
sources: [rust-embedded-book-interoperability-rust-with-c]
last_updated: 2026-05-16
---

# Crate Type — `cdylib` / `staticlib` / `rlib`

[[Cargo]]'s `[lib] crate-type` declaration in `Cargo.toml` selects the **systems-library output format** the Rust compiler emits for a library crate. The two forms relevant to **exporting Rust to C/C++** are `cdylib` (dynamic library) and `staticlib` (static archive) ([[rust-embedded-book-interoperability-rust-with-c]]):

```toml
[lib]
name = "your_crate"
crate-type = ["cdylib"]      # Creates dynamic lib
# crate-type = ["staticlib"] # Creates static lib
```

The `name = "..."` line decouples the library output name from the crate name — useful when the consuming C project expects a specific `lib<name>.{so,a,dylib,dll}` filename.

## `cdylib` — dynamic library for C consumers

Emits a **dynamic library with a C-compatible export table**:
- Linux → `lib<name>.so`
- macOS → `lib<name>.dylib`
- Windows → `<name>.dll`

Only `#[no_mangle] pub extern "C" fn` symbols ([[NoMangle]] + [[ExternC]]) are exposed in the export table. Rust-internal symbols stay hidden. Suitable for hosted-OS consumers that have a dynamic loader.

## `staticlib` — static archive for any consumer

Emits a **static archive** (a bundle of `.o` files):
- Unix-like → `lib<name>.a`
- Windows MSVC → `<name>.lib`

The C consumer links this at compile time; no runtime dependency on the produced file. **This is the form file 39 named as the embedded delivery format** for [[BareMetalProgramming|bare-metal]] firmware — there's no dynamic loader in bare-metal, so `cdylib` is not an option.

## `rlib` — the Rust-internal form

The default form for a library crate when no `crate-type` is specified — the "Rust library" archive used for Rust → Rust linkage (preserves Rust generics / metadata that `cdylib` / `staticlib` strip away). Cannot be consumed from C; included here only to clarify why the chapter explicitly opts into `cdylib` / `staticlib`.

Other less-common forms: `dylib` (Rust dynamic library — for Rust ↔ Rust), `bin` (executable), `proc-macro` (compiler plugin crate).

## Position in the FFI export pipeline

| Stage | What it does | Mechanism |
|---|---|---|
| Source | Mark each exported function | `#[no_mangle] pub extern "C" fn` ([[NoMangle]] + [[ExternC]]) |
| Compile | Select output format | `crate-type = ["cdylib"]` or `["staticlib"]` |
| Header | Generate C `.h` for the C consumer | [[Cbindgen|`cbindgen`]] |
| Link | C build system links the artifact | `make` / `CMake` / IDE |

## Connections

- [[rust-embedded-book-interoperability-rust-with-c]] — the source that introduces the `crate-type = ["cdylib"]` / `["staticlib"]` declaration.
- [[NoMangle]] — only `cdylib` / `staticlib` consumers care about symbol-name preservation.
- [[ExternC]] — only `cdylib` / `staticlib` exports go through the C ABI.
- [[Cbindgen]] — generates the matching C header for `cdylib` / `staticlib` exports.
- [[Cargo]] — owns the `Cargo.toml` parser and the build pipeline that honors `crate-type`.
- [[Rustc]] — implements each crate-type's emission backend.
- [[BareMetalProgramming]] — the regime that forces `staticlib` (no dynamic loader → `cdylib` unusable).
- [[rust-embedded-book-interoperability-c-with-rust]] — the inverse direction; recall that the C side delivered to Rust is also typically a `lib*.a` static archive.
