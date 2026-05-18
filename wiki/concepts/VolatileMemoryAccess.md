---
title: "Volatile Memory Access"
type: concept
tags: [rust, embedded, mmio, memory, compiler]
sources: [rust-embedded-book-peripherals-a-first-attempt]
last_updated: 2026-05-16
---

# Volatile Memory Access

A **memory access (load or store) that the compiler is forbidden to elide, reorder, fuse, or split**. Required whenever the underlying address is **not** "normal" memory — i.e. when the access has an observable side effect on hardware. Canonical case: [[MemoryMappedIO|memory-mapped peripheral]] registers, where every read may pop a value off a FIFO / clear a flag / arm a timer, and every write may trigger a transfer / change a clock / fire an interrupt.

## Why naive accesses are wrong

Compilers are aggressive about RAM. Given two consecutive writes to the same address `*p = 1; *p = 2;`, the optimizer is free to drop the first write — the second one "supersedes" it. For RAM that is correct; for an MMIO register, the first write may have **shifted a byte into a UART** while the second armed a different operation. Naive `(*systick).cvr` access **does not work** for hardware ([[rust-embedded-book-peripherals-a-first-attempt]]).

## C vs Rust expression

- **C**: the *variable* carries a `volatile` qualifier — `volatile uint32_t *csr = (volatile uint32_t *)0xE000_E010;`. The qualifier "infects" every access through that pointer.
- **Rust**: the **access** is the volatile primitive, not the type. The pointer / reference is ordinary; the *operation* is `core::ptr::read_volatile(ptr)` / `core::ptr::write_volatile(ptr, val)`. The data carries no qualifier — the function call expresses "this access must occur exactly once, in program order, as written" ([[rust-embedded-book-peripherals-a-first-attempt]]).

```rust,ignore
let systick = unsafe { &mut *(0xE000_E010 as *mut SysTick) };
let time = unsafe { core::ptr::read_volatile(&mut systick.cvr) };
```

Both `read_volatile` and `write_volatile` are `unsafe` (deref of [[RawPointer|raw pointer]]).

## Idiomatic wrapper: `volatile_register`

The viral-`unsafe` pain motivates [[VolatileRegisterCrate|`volatile_register`]], which provides `RW<T>` / `RO<T>` / `WO<T>` newtypes whose `.read()` and `.write()` methods perform the volatile access internally. Read-only-ness is encoded in the type (`RO<T>` has no `.write()`), and reads are no longer `unsafe`; writes remain `unsafe` because hardware safety is unprovable to the compiler ([[rust-embedded-book-peripherals-a-first-attempt]]).

## Connections

- [[MemoryMappedIO]] — the regime that *requires* volatile accesses; every MMIO load/store must be volatile.
- [[Peripheral]] — the hardware whose registers must not be elided.
- [[RawPointer]] — the underlying access primitive (`*mut T`); `read_volatile` / `write_volatile` take raw pointers.
- [[ReprC]] — used together with volatile accesses on register-block structs to lock both layout and access semantics.
- [[VolatileRegisterCrate]] — the typed-wrapper crate that hides volatile-access machinery behind `.read()` / `.write()`.
- [[CortexMCrate]] / [[PeripheralAccessCrate]] — production crate layers that use `volatile_register` (or equivalent) internally for every register access.
