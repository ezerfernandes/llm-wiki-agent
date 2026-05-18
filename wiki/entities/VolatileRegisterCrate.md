---
title: "volatile_register"
type: entity
tags: [rust, embedded, crate, mmio]
sources: [rust-embedded-book-peripherals-a-first-attempt]
last_updated: 2026-05-16
---

# volatile_register

Third-party crate — `crates.io/crates/volatile_register` — providing **typed wrapper structs** that encode register access permissions and perform [[VolatileMemoryAccess|volatile reads/writes]] internally. The standard primitive used in hand-written and [[Svd2Rust|`svd2rust`]]-generated [[PeripheralAccessCrate|PACs]] alike for representing individual MMIO registers within a [[ReprC|`#[repr(C)]`]] register-block struct.

## Wrapper types

- `RW<T>` — read-write register. `.read() -> T` and `.write(val: T)`; `.modify(|t| …)` for read-modify-write.
- `RO<T>` — read-only register. `.read() -> T` only (write attempts are compile errors).
- `WO<T>` — write-only register. `.write(val: T)` only.

All wrappers are `#[repr(transparent)]` over `T`, so they slot into a `#[repr(C)]` register-block struct at exactly the size and alignment of `T` — no layout disturbance.

## Idiom

```rust,ignore
use volatile_register::{RW, RO};

#[repr(C)]
struct SysTick {
    pub csr:   RW<u32>,
    pub rvr:   RW<u32>,
    pub cvr:   RW<u32>,
    pub calib: RO<u32>,   // calibration is read-only
}
```

This single change vs. the naive `pub csr: u32` form ([[rust-embedded-book-peripherals-a-first-attempt]]):

1. Encodes read-only-ness in the type (`calib.write(…)` is a compile error).
2. Performs volatile access in every `.read()` / `.write()` (compiler cannot elide).
3. Makes reads safe (no `unsafe` block needed); writes remain `unsafe` because hardware-write safety is unprovable.

## Connections

- [[VolatileMemoryAccess]] — the access semantics this crate encapsulates.
- [[ReprC]] — the layout attribute that makes the register-block-of-`RW`/`RO`-fields idiom work.
- [[Peripheral]] — the noun whose registers are wrapped.
- [[MemoryMappedIO]] — the regime.
- [[PeripheralAccessCrate]] — production PACs use `volatile_register` (or an equivalent typed-volatile wrapper) for every register field.
- [[CortexMCrate]] — uses the same wrapper pattern internally for the core-standardized peripherals it exposes.
