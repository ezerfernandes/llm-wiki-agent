---
title: "Static Guarantee"
type: concept
tags: [rust, embedded, type-system, safety, compile-time, design-philosophy]
sources: [rust-embedded-book-static-guarantees-index]
last_updated: 2026-05-16
---

# Static Guarantee

A **property of a program that is checked at compile time** rather than at run time — so that a class of errors becomes a **type error** instead of a runtime fault, and the corresponding runtime check can be **omitted entirely**. The chapter-opening framing concept of the *Static Guarantees* chapter of [[TheEmbeddedRustBook]] ([[rust-embedded-book-static-guarantees-index]], file 22/44).

> "The type system can also be used to check other properties at compile time; reducing the need for runtime checks in some cases." ([[rust-embedded-book-static-guarantees-index]])

## Examples in the wiki's embedded-Rust corpus

| Family | Mechanism | Wiki page |
|---|---|---|
| **Data-race freedom** | `Send` / `Sync` marker traits (built into the language) | [[RustLanguage]] |
| **Initialization ordering** — a serial interface can only be constructed *after* its pins are configured | [[TypeStateProgramming]] (phantom-typed state machine) | [[TypeStateProgramming]] |
| **Configuration-dependent operations** — `set_low` on a floating-input pin is a compile error | [[TypeStateProgramming]] (per-state methods) | [[TypeStateProgramming]] |
| **Access control** — only one part of the program can modify a [[Peripheral|peripheral]] at a time | [[BorrowChecker]] + [[Singleton]] | [[BorrowChecker]] / [[Singleton]] |

All four families share the same shape: encode the property in **types**, so that violations are rejected by the compiler and the runtime never has to check.

## The trade

A static guarantee buys:

- **Zero runtime cost** — no branch, no flag, no panic-on-misuse. The check has already happened at compile time. (See the [[TypeStateProgramming]] "All with no run-time cost!" claim.)
- **Earlier failure** — bugs surface at `cargo build` instead of in the field.
- **Self-documenting APIs** — a function signature that takes `Pin<Output>` rather than `Pin<Floating>` carries the precondition in its type.

It costs:

- **API design effort** — the precondition must be encoded as a type, which often means more types, more generic parameters, and more `into_*` transition methods.
- **Compile-time complexity** — type-state machines can produce intimidating type signatures and error messages.

## Why this matters in embedded

In embedded Rust the runtime "check" that a static guarantee replaces is often a **hardware fault** — a misconfigured peripheral does not produce a Rust `Result::Err`, it produces a malfunctioning device. The static-guarantee design philosophy therefore covers ground that on a hosted system would be covered by runtime assertions, exception handlers, or operating-system primitives. The [[rust-embedded-book-peripherals-singletons|previous chapter]] established the **access-control** family operationally; this chapter intro generalizes that result and previews the **type-state** family that the rest of the chapter mechanizes.

## Connections

- [[TypeStateProgramming]] — the design pattern that mechanizes the *initialization-ordering* and *configuration-dependent-operation* families.
- [[BorrowChecker]] — the compile-time aliasing checker that mechanizes the *access-control* family.
- [[Singleton]] / [[PeripheralsTake]] — the runtime gate that supplies the **exactly-one-instance** precondition the [[BorrowChecker]] needs to give an access-control static guarantee.
- [[Peripheral]] — the noun whose configuration / access / ownership the embedded-Rust static guarantees constrain.
- [[GPIO]] / [[USART]] — the concrete peripheral families the chapter intro uses as examples.
- [[RustLanguage]] — the language whose type system carries the guarantees; the `Send` / `Sync` marker traits are the language-built-in instance.
- [[HALCrate]] / [[EmbeddedHalCrate]] — the crate-stack layer where embedded-Rust static guarantees are concretely encoded as type-state APIs.
