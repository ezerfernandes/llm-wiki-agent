---
title: "Raw Pointer"
type: concept
tags: [rust, embedded, memory, unsafe]
sources: [rust-embedded-book-peripherals-a-first-attempt, rust-embedded-book-interoperability-c-with-rust]
last_updated: 2026-05-16
---

# Raw Pointer

Rust's **unchecked pointer type** — `*const T` (immutable) and `*mut T` (mutable). Unlike Rust's safe references `&T` / `&mut T`, raw pointers:

- Are **not** subject to borrow-checker rules (multiple `*mut T` to the same address are legal).
- May be null, dangling, or unaligned.
- Are **not** automatically dereferenced — `*ptr` is an `unsafe` operation.
- Can be **freely cast from integers** via `addr as *mut T`.

## Embedded use case

The Rust idiom for typing a [[MemoryMappedIO|memory-mapped]] register block is exactly an integer-to-raw-pointer cast ([[rust-embedded-book-peripherals-a-first-attempt]]):

```rust,ignore
let systick = 0xE000_E010 as *mut SysTick;
let time = unsafe { (*systick).cvr };
```

The cast asserts "treat the integer `0xE000_E010` as a pointer to a [[SysTick]] register block." The compiler trusts the cast; the **programmer owns correctness**: address must be valid, lifetime must be `'static` (peripheral registers are), alignment must match, and the layout of the pointee must match the hardware — which is why register-block structs are also marked [[ReprC|`#[repr(C)]`]].

## Volatile access takes raw pointers

`core::ptr::read_volatile::<T>(*const T) -> T` and `core::ptr::write_volatile::<T>(*mut T, T)` take raw pointers, not references — because [[VolatileMemoryAccess|volatile access]] semantically violates the "no spooky side effects" contract of `&T` / `&mut T` and must therefore live below the reference layer.

## Connections

- [[VolatileMemoryAccess]] — operates on raw pointers; `read_volatile` / `write_volatile` are the primitive volatile-access operators in Rust.
- [[MemoryMappedIO]] — the regime where raw-pointer-from-integer casts are the standard entry point.
- [[ReprC]] — used together with raw pointers so the in-memory layout of the pointee struct matches the hardware register block.
- [[Peripheral]] — the typed target of the cast; one register block ↔ one `#[repr(C)]` struct ↔ one raw pointer.
- [[NoStd]] — the regime in which this pattern is ubiquitous (no OS abstractions over hardware).
- [[ExternC]] — `extern "C"` function signatures use `*const T` / `*mut T` in place of Rust references, since C has no notion of borrow-checked references ([[rust-embedded-book-interoperability-c-with-rust]]).
- [[Bindgen]] — emits `*mut T` / `*const T` automatically for every C `T*` / `const T*` parameter it sees in the input header.
