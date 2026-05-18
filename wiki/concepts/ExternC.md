---
title: "extern \"C\""
type: concept
tags: [rust, embedded, ffi, abi, c-interop]
sources: [rust-embedded-book-interoperability-c-with-rust, rust-embedded-book-interoperability-rust-with-c]
last_updated: 2026-05-16
---

# `extern "C"`

Rust's **calling-convention selector** for foreign-function-interface boundaries — declares that a function uses the **C ABI** (parameter passing, register usage, stack discipline as defined by the platform's C calling convention) rather than Rust's unstable internal ABI ([[rust-embedded-book-interoperability-c-with-rust]]).

Two syntactic forms:

```rust,ignore
// (1) Block of imported declarations — functions defined in C, called from Rust.
extern "C" {
    pub fn cool_function(i: cty::c_int, c: cty::c_char, cs: *mut CoolStruct);
}

// (2) Function definition exported to C — defined in Rust, called from C.
#[no_mangle]
pub extern "C" fn my_rust_callback(x: cty::c_int) -> cty::c_int { x + 1 }
```

Form (1) is what the [[rust-embedded-book-interoperability-c-with-rust|C-with-Rust chapter]] focuses on: *"This statement defines the signature of a function that uses the C ABI, called `cool_function`. By defining the signature without defining the body of the function, the definition of this function will need to be provided elsewhere, or linked into the final library or binary from a static library."*

## Why `"C"` is the lingua franca

C++ deliberately does **not** standardize an ABI (each compiler is free to mangle, lay out vtables, and pass classes differently — and they do). The Rust internal ABI is similarly **unstable** by design. The only ABI both languages can target predictably is the **platform C ABI**. Hence the chapter's rule: *"As C++ does not have a stable ABI for the Rust compiler to target, it is recommended to use the `C` ABI when combining Rust with C or C++."* Calling C++ from Rust typically goes through a thin **C wrapper layer** that re-exposes the C++ API as `extern "C"`.

## Pairs with `#[repr(C)]`

`extern "C"` is the **calling-convention half** of FFI; [[ReprC|`#[repr(C)]`]] is the **data-layout half**. Both are required on every type and signature that crosses the FFI boundary — fixing the calling convention without fixing struct layout (or vice versa) does not yield a correct interface. The [[Bindgen|`bindgen`]] tool emits both attributes from a single C header.

## Pointer types in `extern "C"` signatures

References (`&T` / `&mut T`) cannot cross an `extern "C"` boundary — C has no notion of borrow-checked references. The standard rewrite is to a [[RawPointer|raw pointer]] (`*const T` / `*mut T`): *"As C does not have a concept of Rust's references, which would look like this: `&mut CoolStruct`, we instead have a raw pointer. As dereferencing this pointer is `unsafe`, and the pointer may in fact be a `null` pointer, care must be taken to ensure the guarantees typical of Rust when interacting with C or C++ code."*

## Other ABI strings

Rust also accepts `extern "system"` (the platform-default — `"stdcall"` on 32-bit Windows, `"C"` elsewhere — for talking to Win32), `extern "Rust"` (the default, unstable), and arch-specific strings like `extern "aapcs"` / `extern "thiscall"`. For embedded C/C++ interop, `extern "C"` is the only string in scope.

## The two directions — imported vs exported

Form (1) above is the **imported** direction — C-from-Rust ([[rust-embedded-book-interoperability-c-with-rust]] coverage). Form (2) is the **exported** direction — Rust-to-C ([[rust-embedded-book-interoperability-rust-with-c]] coverage). The exported form must additionally carry [[NoMangle|`#[no_mangle]`]] to defeat Rust's symbol-mangling — otherwise the C linker can't find the symbol even though the calling convention is correct ([[rust-embedded-book-interoperability-rust-with-c]]):

> "By default, any function you write in Rust will use the Rust ABI (which is also not stabilized). Instead, when building outwards facing FFI APIs we need to tell the compiler to use the system ABI."

## Connections

- [[ReprC]] — the layout-half companion; both attributes are needed on the same boundary.
- [[NoMangle]] — the symbol-name companion required on the **exported** form (form 2 above).
- [[RawPointer]] — what replaces `&T` / `&mut T` in `extern "C"` signatures.
- [[rust-embedded-book-interoperability-c-with-rust]] — operationalizes `extern "C"` for the **imported** direction (C → Rust).
- [[rust-embedded-book-interoperability-rust-with-c]] — operationalizes `extern "C"` for the **exported** direction (Rust → C).
- [[Bindgen]] — auto-generates `extern "C"` blocks from C headers (imported direction).
- [[Cbindgen]] — auto-generates C `.h` declarations from `#[no_mangle] pub extern "C" fn` (exported direction).
- [[CcCrate]] — compiles the C side; `extern "C"` declarations name the symbols the resulting `lib*.a` provides.
- [[BuildRs]] — the host-side hook that builds the static archive `extern "C"` declarations resolve against.
- [[CrateType]] — the `cdylib` / `staticlib` selection determines what the exported `extern "C"` functions are packaged into.
- [[Rustc]] — implements the `C` ABI per target.
- [[NoStd]] — the regime in which `extern "C"` is the canonical RTOS / vendor-SDK glue.
