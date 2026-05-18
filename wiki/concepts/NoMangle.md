---
title: "#[no_mangle]"
type: concept
tags: [rust, embedded, ffi, linker, symbol-mangling, c-interop]
sources: [rust-embedded-book-interoperability-rust-with-c]
last_updated: 2026-05-16
---

# `#[no_mangle]`

Rust function attribute that **disables the compiler's symbol-name mangling** for the annotated item — the emitted symbol in the object file is exactly the source identifier (`rust_function`) instead of the mangled long form (`_ZN8my_crate13rust_function17h6c2e4a8b3d5f1e9aE` or similar).

## Why it exists

The Rust compiler **mangles symbol names** to encode namespace, generic parameters, and a stable hash that disambiguates separately-compiled crates. This is necessary for Rust ↔ Rust linkage but **incompatible with external linkers** that expect symbols to match C-style flat identifiers ([[rust-embedded-book-interoperability-rust-with-c]]):

> "The Rust compiler mangles symbol names differently than native code linkers expect. As such, any function that Rust exports to be used outside of Rust needs to be told not to be mangled by the compiler."

When a C source file calls `rust_function()`, the C compiler emits an unresolved symbol reference to the literal name `rust_function`; the linker then has to find a definition of exactly that symbol. Without `#[no_mangle]`, the Rust-emitted definition has a mangled name and the link fails.

## Canonical pairing — always with `pub extern "C"`

`#[no_mangle]` solves the **linker** half of the FFI export problem; [[ExternC|`extern "C"`]] solves the **calling-convention** half. Both are required on every Rust function exported to C ([[rust-embedded-book-interoperability-rust-with-c]]):

```rust,ignore
#[no_mangle]
pub extern "C" fn rust_function() {

}
```

The three attributes together — `pub` (visibility) + `#[no_mangle]` (symbol name) + `extern "C"` (ABI) — form the **canonical exported-function shape**. Omitting any one of them is a bug:

- Drop `pub` → the function isn't exported at all.
- Drop `#[no_mangle]` → the symbol is mangled; the C side can't find it.
- Drop `extern "C"` → the symbol exists but uses the Rust ABI; the C-side calling convention doesn't match → register/stack corruption at the call site.

## Position in FFI direction

`#[no_mangle]` is **specifically for exporting Rust to C** — i.e. the [[rust-embedded-book-interoperability-rust-with-c]] direction. The opposite direction ([[rust-embedded-book-interoperability-c-with-rust|importing C into Rust]]) doesn't need it, because the `extern "C" { fn cool_function(...); }` declaration block references symbols defined elsewhere — there's no Rust-emitted symbol to mangle in that case.

## Related — `#[link_name = "..."]`

The complementary attribute for **imported** symbols: when an `extern "C" { fn x(...); }` block needs to reference a C symbol whose name doesn't match the Rust identifier (e.g. a C symbol with leading underscore, or a name reserved in Rust), `#[link_name = "the_real_name"]` overrides the lookup symbol. `#[no_mangle]` and `#[link_name]` together cover all renaming needs at the FFI boundary.

## `#[export_name = "..."]` — an alternative

`#[export_name = "alt_name"]` lets you rename the exported symbol (vs. simply suppressing mangling). Less common than `#[no_mangle]`; mostly used when the C side expects a name that isn't a valid Rust identifier, or when shipping multiple ABI versions of the same function.

## Connections

- [[ExternC]] — the calling-convention companion; both attributes are needed on every exported Rust function.
- [[rust-embedded-book-interoperability-rust-with-c]] — the source that introduces `#[no_mangle]` and operationalizes it for Rust → C export.
- [[Cbindgen]] — when generating C headers from Rust source, `cbindgen` finds the `#[no_mangle] pub extern "C" fn`-shaped functions and emits matching `void rust_function();` declarations.
- [[ReprC]] — the data-layout companion; `#[no_mangle]` fixes the **function symbol**, `#[repr(C)]` fixes the **struct layout** of types passed through it.
- [[Rustc]] — implements the symbol-mangling scheme that `#[no_mangle]` overrides.
- [[CrateType]] — only the `cdylib` / `staticlib` crate types meaningfully use `#[no_mangle]` (since they're the forms a C consumer can link).
