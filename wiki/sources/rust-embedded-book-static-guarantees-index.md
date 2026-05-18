---
title: "The Embedded Rust Book — Static Guarantees"
type: source
tags: [rust, embedded, book-chapter, static-guarantees, type-system]
date: 2026-05-16
source_file: raw/book/src/static-guarantees/index.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Static Guarantees

## Summary

File 22/44 of *[[TheEmbeddedRustBook]]* — the **chapter opener** for the *Static Guarantees* part of the book, immediately after the Peripherals chapter closed at file 21 ([[rust-embedded-book-peripherals-singletons]]). Very compact (~20 lines, no code) — generalizes the prior chapter's specific singleton/[[BorrowChecker]] result into a **named framing concept**: Rust's type system can be used to **check properties at compile time, reducing the need for runtime checks**. Anchors the generalization with three concrete embedded examples (all foreshadowing later sub-sections): (1) data-race prevention via the standard `Send` / `Sync` marker traits, (2) **initialization ordering** — an API where a serial interface can only be initialized *after* the pins it uses have been configured, (3) **configuration-dependent operations** — calling "set this pin low" on a pin configured as floating input is a **compile error**. Closes by re-summarizing the prior chapter's [[Singleton|singleton]] / [[BorrowChecker|ownership]] result as the *access-control* instance of the same framing — peripherals as ownership-controlled values vs. global mutable state.

## Key Claims

- **Rust's type system prevents data races at compile time** via the marker traits [`Send`](https://doc.rust-lang.org/core/marker/trait.Send.html) (safe to transfer across thread boundaries) and [`Sync`](https://doc.rust-lang.org/core/marker/trait.Sync.html) (safe to share via `&T` across threads). This is the canonical, language-built-in instance of the framing.
- **The type system can be used to check other properties at compile time**, reducing the need for runtime checks — the chapter's headline generalization. The remaining bullets are instances of this framing.
- **Initialization-ordering enforcement (example 1)**: an API can be designed so that a serial interface can only be initialized *after* the pins it uses have been configured. Out-of-order initialization is not a runtime error but a **type error**.
- **Configuration-dependent operation enforcement (example 2)**: an API can be designed so that operations like "set this pin low" can only be performed on a correctly-configured peripheral. Trying to change the output state of a pin configured as floating input would **raise a compile error**, not a runtime fault.
- **Ownership as access control (example 3, callback to the previous chapter)**: the concept of ownership applied to peripherals — as resolved in [[rust-embedded-book-peripherals-singletons|the previous chapter]] — ensures only certain parts of a program can modify a peripheral. This *access control* makes software **easier to reason about** compared to treating peripherals as global mutable state.

## Key Quotes

> "Rust's type system prevents data races at compile time (see `Send` and `Sync` traits). The type system can also be used to check other properties at compile time; reducing the need for runtime checks in some cases." — the chapter's headline framing.

> "Trying to change the output state of a pin configured in floating input mode would raise a compile error." — the most concrete embedded illustration of the framing; the two-line preview of what the [[TypeStateProgramming|type-state]] sub-section (later in the chapter) will mechanize.

> "This *access control* makes software easier to reason about compared to the alternative of treating peripherals as global mutable state." — re-summarizes the previous chapter ([[rust-embedded-book-peripherals-singletons]]) as the *access-control* instance of the same framing.

## Connections

- [[TheEmbeddedRustBook]] — file 22/44; **opens the Static Guarantees chapter** after the Peripherals chapter closed at file 21 ([[rust-embedded-book-peripherals-singletons]]).
- [[rust-embedded-book-peripherals-singletons]] — directly preceding file; closed the Peripherals chapter on the singleton resolution. This chapter intro reframes that resolution as one instance of the *access-control* family of static guarantees and previews two more families (initialization ordering, configuration-dependent operations).
- [[rust-embedded-book-peripherals-borrowck]] — earlier sub-section that introduced [[BorrowChecker|borrow-checker]] discipline; the conceptual ancestor of the *access-control* example here.
- [[StaticGuarantee]] — the framing concept this file defines (a compile-time-checked property that obviates a runtime check).
- [[TypeStateProgramming]] — the design pattern that mechanizes examples (1) and (2). Already introduced operationally in [[rust-embedded-book-start-registers]] (GPIO pin modes, clock configuration); this chapter is the *conceptual umbrella* that names what type-state APIs accomplish.
- [[BorrowChecker]] — the compile-time aliasing-discipline checker; the engine behind example (3) (access control / ownership applied to peripherals).
- [[Singleton]] / [[PeripheralsTake]] — the previous chapter's runtime gate; the *exactly-one-instance* precondition that makes the [[BorrowChecker|borrow checker]]'s access-control guarantee load-bearing in embedded.
- [[Peripheral]] — the noun the chapter's examples (serial interface, pin) all instantiate.
- [[GPIO]] — example (2)'s subject; floating-input vs. output mode is a [[GPIO]] configuration.
- [[USART]] — example (1)'s subject (the "serial interface" whose initialization order is constrained by pin configuration).
- [[RustLanguage]] — the language whose type system carries the guarantees. The `Send` / `Sync` marker traits are part of the language's core safety story.

## Contradictions

None with existing wiki content. Strictly additive — names and generalizes the framing the wiki has already been operating under since [[rust-embedded-book-start-registers]] introduced [[TypeStateProgramming]] and [[rust-embedded-book-peripherals-borrowck]] introduced [[BorrowChecker]]. This chapter intro is the **conceptual umbrella** — the unifying noun ([[StaticGuarantee|static guarantee]]) that ties type-state APIs, the borrow checker, and the [[Send]]/[[Sync|`Send`/`Sync`]] marker traits into one design family.
