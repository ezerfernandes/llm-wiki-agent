---
title: "The Embedded Rust Book — Interoperability"
type: source
tags: [rust, embedded, book-chapter, ffi, interoperability]
date: 2026-05-16
source_file: raw/book/src/interoperability/index.md
sources: []
last_updated: 2026-05-16
---

## Summary

File 38/44 of *[[TheEmbeddedRustBook]]* — **opens Part 6's *Interoperability* chapter**, the natural successor to file 37 ([[rust-embedded-book-c-tips-index]]) which the prior chapter forward-referenced (*"see also: A little C with your Rust / A little Rust with your C"*). Short three-section framing page (≈30 lines): (1) the **`std::ffi` family** — `stdlib` module providing C primitive type aliases (`c_uint` ≡ `unsigned int`, etc.) and string-conversion utilities (`CString` / `CStr`), mirrored in `core::ffi` (no-alloc) and `alloc::ffi` (alloc-required) since Rust 1.30, with [`cty`] and [`cstr_core`] as community-crate equivalents for older toolchains; (2) **Build-system interop** — combining [[Cargo]] with Make / CMake is open work (tracked in [rust-embedded/book#61](https://github.com/rust-embedded/book/issues/61)); (3) **RTOS interop** — calling FreeRTOS / ChibiOS from Rust is "work in progress," with the [Zephyr Project](https://docs.zephyrproject.org/latest/develop/languages/rust/index.html) named as the lone publicly-supported integration (tracked in [#62](https://github.com/rust-embedded/book/issues/62)). The chapter establishes that **interop = bidirectional data-type marshaling** and previews the Rust↔C type table the leaf chapters will operationalize.

## Key Claims

- **Interop is a marshaling problem, not a calling-convention problem** — *"Interoperability between Rust and C code is always dependent on transforming data between the two languages."* The calling convention is handled by [[ReprC|`#[repr(C)]`]] and `extern "C"` (covered in prior / later chapters); this chapter scopes itself to the **value-shape translation table**.
- **`std::ffi` is the canonical bridge module** — provides type aliases for C primitives (`c_int`, `c_uint`, `c_long`, `c_void`, `c_char`, …) and conversion utilities for compound types. *"A value of a C primitive type can be used as one of the corresponding Rust type and vice versa, since the former is simply a type alias of the latter."* Example: on platforms where `unsigned int` is 32-bit, `let c_num: c_uint = num;` compiles for a `u32`.
- **`no_std` split since Rust 1.30** — *"functionalities of `std::ffi` are available in either `core::ffi` or `alloc::ffi` depending on whether or not memory allocation is involved."* `core::ffi` is usable in [[NoStd|`no_std`]] firmware without an allocator; `alloc::ffi` is gated on the `alloc` crate (heap required). Pre-1.30 / vendor-stuck builds reach for the [`cty`] crate (primitive aliases) and [`cstr_core`] crate (string types) as drop-in replacements.
- **The Rust ↔ C type table** — reproduced in the chapter:

  | Rust type      | Intermediate | C type         |
  |----------------|--------------|----------------|
  | `String`       | `CString`    | `char *`       |
  | `&str`         | `CStr`       | `const char *` |
  | `()`           | `c_void`     | `void`         |
  | `u32` or `u64` | `c_uint`     | `unsigned int` |
  | etc            | …            | …              |

  Heap-owning string maps to `CString` (alloc); borrowed string slice maps to `CStr` (no-alloc); unit type maps to `c_void` (for opaque-pointer / void-return positions). The `u32`-or-`u64` ambiguity on the `unsigned int` row reflects that **the C width is platform-dependent** — the chapter punts to `c_uint` precisely so user code stays portable.
- **Other-build-system interop is unresolved** — *"A common requirement for including Rust in your embedded project is combining Cargo with your existing build system, such as make or cmake. We are collecting examples and use cases for this on our issue tracker in issue #61."* No prescribed recipe; the chapter is an open call for case studies as of writing.
- **RTOS interop is unresolved (modulo Zephyr)** — *"Integrating Rust with an RTOS such as FreeRTOS or ChibiOS is still a work in progress; especially calling RTOS functions from Rust can be tricky."* Only the **[Zephyr Project](https://docs.zephyrproject.org/latest/develop/languages/rust/index.html)** is listed as publicly supporting Rust↔RTOS interop. Tracked in [issue #62].
- **No new vocabulary** — the chapter is a **pointer-and-promise page**: it names the `std::ffi` / `core::ffi` / `alloc::ffi` modules, the [`cty`] / [`cstr_core`] community crates, and the marshaling table, then defers all depth to leaf chapters. Reuses [[ReprC]], [[RawPointer]], [[Cargo]], [[Rustc]], [[NoStd]], [[RustCoreLibrary|`libcore`]], [[RustStandardLibrary|`libstd`]], [[AllocCrate|`alloc`]] from prior files.

## Key Quotes

> "Interoperability between Rust and C code is always dependent on transforming data between the two languages." — opening, framing the chapter as a marshaling problem

> "For this purpose, there is a dedicated module in the `stdlib` called `std::ffi`." — naming the canonical bridge module

> "As of Rust 1.30, functionalities of `std::ffi` are available in either `core::ffi` or `alloc::ffi` depending on whether or not memory allocation is involved." — the `no_std` split that matters for embedded

> "A value of a C primitive type can be used as one of the corresponding Rust type and vice versa, since the former is simply a type alias of the latter." — why FFI-bridge code rarely needs runtime conversion

> "Integrating Rust with an RTOS such as FreeRTOS or ChibiOS is still a work in progress; especially calling RTOS functions from Rust can be tricky." — RTOS-interop honesty disclaimer

## Connections

- [[TheEmbeddedRustBook]] — file 38/44; opens the *Interoperability* chapter.
- [[rust-embedded-book-c-tips-index]] — preceding file (37/44); its *Other Resources* section forward-referenced *"A little C with your Rust / A little Rust with your C"* — this chapter is the framing page for those leaves.
- [[ReprC]] — `#[repr(C)]`, the **layout** half of FFI (this chapter is the **type-marshaling** half).
- [[RawPointer]] — `*const T` / `*mut T`, the underlying handle the `CStr` / `CString` types wrap.
- [[Cargo]] — named as the build system whose Make / CMake interop is still open work.
- [[Rustc]] — the compiler that implements the `extern "C"` calling convention the leaves will use.
- [[NoStd|`no_std`]] — the regime that forces the `std::ffi` → `core::ffi` / `alloc::ffi` split.
- [[RustCoreLibrary|`libcore`]] — host of `core::ffi` (no allocator required).
- [[RustStandardLibrary|`libstd`]] — host of `std::ffi` (hosted environment).

## Contradictions

None. The chapter is a short framing page that names modules and surfaces two open-issue trackers (#61 build-system interop, #62 RTOS interop); it neither restates nor revises anything in prior files.
