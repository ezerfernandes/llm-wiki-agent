---
title: "#[repr(C)]"
type: concept
tags: [rust, embedded, abi, struct-layout]
sources: [rust-embedded-book-peripherals-a-first-attempt, rust-embedded-book-interoperability-c-with-rust]
last_updated: 2026-05-16
---

# `#[repr(C)]`

Rust struct-layout attribute that tells the compiler to **lay out the struct's fields as a C compiler would**: fields in source order, each at the natural alignment of its type, padding inserted between fields to maintain alignment, total size rounded up to a multiple of the largest field's alignment.

## Why it matters for embedded

By default, Rust **may reorder struct fields** to minimize padding — a valid optimization for pure-Rust code, but **catastrophic** for any struct whose layout must match an external ABI: C interop, on-the-wire protocol headers, and — most relevant here — **memory-mapped peripheral register blocks**.

A register block is a contiguous sequence of registers at fixed offsets defined by the chip's datasheet ([[rust-embedded-book-peripherals-a-first-attempt]]):

```rust,ignore
#[repr(C)]
struct SysTick {
    pub csr:   u32,  // offset 0x00
    pub rvr:   u32,  // offset 0x04
    pub cvr:   u32,  // offset 0x08
    pub calib: u32,  // offset 0x0C
}
```

Without `#[repr(C)]`, the Rust compiler is free to silently shuffle `csr`/`rvr`/`cvr`/`calib` — and `register.cvr` would suddenly read from a different hardware register. *"You can imagine the debugging we'd have to do if these fields were silently re-arranged by the compiler!"* ([[rust-embedded-book-peripherals-a-first-attempt]]).

## Companion attributes

- `#[repr(transparent)]` — single-field newtype with identical ABI to the inner type (used by the [[VolatileRegisterCrate|`volatile_register`]] crate's `RW<T>` / `RO<T>` wrappers so they layout-coincide with a bare `T`).
- `#[repr(packed)]` — drop alignment padding entirely (rare in embedded; mostly for protocol parsers).
- `#[repr(u32)]` etc. — pin the discriminant size of an enum, typically used for register-bitfield enums.

## Connections

- [[MemoryMappedIO]] — `#[repr(C)]` is mandatory on every register-block struct exposed to MMIO.
- [[RawPointer]] — the layout of the pointee struct must match hardware; `#[repr(C)]` is what guarantees that.
- [[Peripheral]] — register-block-as-struct is the standard Rust modeling primitive.
- [[VolatileMemoryAccess]] — register-block structs combine `#[repr(C)]` (layout) with volatile-access wrappers (semantics).
- [[VolatileRegisterCrate]] — `volatile_register::{RW, RO}` are `#[repr(transparent)]` newtypes designed to slot into `#[repr(C)]` register-block structs without layout disturbance.
- [[PeripheralAccessCrate]] — [[Svd2Rust|`svd2rust`]]-generated PACs emit `#[repr(C)]` register-block structs automatically from the chip's [[SVDFile|SVD]].
- [[ExternC]] — the calling-convention companion; `#[repr(C)]` fixes data layout, `extern "C"` fixes function ABI; both are required on every FFI boundary ([[rust-embedded-book-interoperability-c-with-rust]]).
- [[Bindgen]] — emits `#[repr(C)]` automatically for every C `typedef struct` it sees in the input header.
