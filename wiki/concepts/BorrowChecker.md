---
title: "Borrow Checker"
type: concept
tags: [rust, embedded, safety, aliasing, compiler]
sources: [rust-embedded-book-peripherals-borrowck, rust-embedded-book-peripherals-singletons]
last_updated: 2026-05-16
---

# Borrow Checker

Rust's **compile-time aliasing-discipline checker**: enforces that at any given point in a program, a value has **either** any number of shared references (`&T`) **or** exactly one mutable reference (`&mut T`), never both. The mechanism Rust uses to prove the absence of data races and use-after-free at compile time, without a garbage collector.

## The peripheral-access mapping (this wiki's primary use case)

[[rust-embedded-book-peripherals-borrowck]]'s central insight: the three rules for safe [[Peripheral|peripheral]] access map directly onto the borrow checker.

| Safe-peripheral-access rule | Borrow checker analogue |
|---|---|
| (2) Any number of **read-only** holders may share a peripheral | `&T` — any number of shared references |
| (3) **Read-write** access requires the holder to be the **only** reference | `&mut T` — exactly one exclusive reference |

Rule (1) — [[VolatileMemoryAccess|volatile]] access — is **orthogonal** to the borrow checker; it concerns *how* a single access is compiled, not *how many* concurrent accesses are permitted. The borrow checker handles rules (2) and (3) for free, *provided* there is **exactly one** Rust value per physical peripheral.

## The exactly-one-instance precondition

The borrow checker reasons about aliasing of **Rust values**, not physical hardware. Two Rust values that *both* point at the same physical [[Peripheral|peripheral]] each satisfy the borrow checker independently — but the hardware experiences the union, which can violate rules (2) and (3). Hence the precondition: **there must be exactly one Rust value per peripheral**. Hardware naturally satisfies this (one [[SysTick]] / one [[NVIC]] / one [[GPIO]] block per chip), but the code must *expose* that uniqueness. The previous sub-section ([[rust-embedded-book-peripherals-a-first-attempt]]) hit precisely this gap: `SystemTimer::new()` was callable arbitrarily many times, so two threads could manufacture independent handles to the same `0xE000_E010` register block, and the borrow checker — operating on the two distinct `SystemTimer` values — could not detect it.

## Why this matters more in embedded than in app-level Rust

In application-level Rust, the value/address bijection is automatic — `Box`, `Vec`, etc. construct unique heap allocations. In embedded, hardware exists **before** any Rust value, so the bijection must be **manufactured**: each [[Peripheral|peripheral]] needs exactly one Rust value at startup, and the program must be unable to construct a second. This is the **[[Singleton|singleton]] pattern**, resolved in [[rust-embedded-book-peripherals-singletons]] (file 21/44) via the [[PeripheralsTake|`Peripherals::take()`]] / [[CortexMCrate|`singleton!()`]] gate.

## Connections

- [[Peripheral]] — the noun whose access discipline the borrow checker enforces (under the uniqueness precondition).
- [[VolatileMemoryAccess]] — the orthogonal rule (1) of safe peripheral access; concerns *how* the access compiles, not aliasing.
- [[RawPointer]] — **escapes** the borrow checker (raw pointers can alias freely; that's why dereferencing them is `unsafe`). The access primitive used *below* the borrow-checker layer.
- [[ARMCortexM]] / [[SysTick]] / [[NVIC]] — peripherals that exist in exactly one physical instance per chip; the uniqueness the next sub-section will mirror in code.
- [[RustLanguage]] — the language whose distinguishing safety feature this is.
- [[Singleton]] / [[PeripheralsTake]] — the runtime gate that satisfies the exactly-one-instance precondition above ([[rust-embedded-book-peripherals-singletons]]).
