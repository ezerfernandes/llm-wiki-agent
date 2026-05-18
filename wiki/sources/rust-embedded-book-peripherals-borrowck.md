---
title: "The Embedded Rust Book — The Borrow Checker"
type: source
tags: [rust, embedded, book-chapter, borrow-checker]
date: 2026-05-16
source_file: raw/book/src/peripherals/borrowck.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — The Borrow Checker

## Summary

File 20/44 of *[[TheEmbeddedRustBook]]* — the **Peripherals chapter's third sub-section**, immediately after [[rust-embedded-book-peripherals-a-first-attempt]] (file 19/44) which ended on the unresolved **singleton gap** ("`SystemTimer::new()` can be called arbitrarily many times"). Pivot chapter: states the **three rules** for safe peripheral access — (1) every access through [[VolatileMemoryAccess|`volatile`]] methods, (2) read-only access may be **shared** by any number of holders, (3) read-write access requires the holder to have the **only** reference to that [[Peripheral|peripheral]] — and observes that rules (2) and (3) are **exactly** Rust's [[BorrowChecker|borrow checker]] discipline (`&T` shared, `&mut T` exclusive). The bridge: if every [[Peripheral|peripheral]] is represented by **exactly one** Rust value, the [[BorrowChecker|borrow checker]] gives us safe hardware sharing *for free*. The chapter closes on the "exactly one instance" precondition — hardware is naturally unique (only one [[SysTick]] per [[ARMCortexM|Cortex-M]] core) — but how do we **expose that uniqueness in code**? That is the singleton problem, deferred to the next sub-section (file 21/44).

## Key Claims

- **Hardware is mutable global state.** "Hardware is basically nothing but mutable global state" — independent of the code's structure, modifiable at any time by the real world. The frightening framing motivates the three-rule discipline that follows.
- **Three rules for safe peripheral access**:
  1. **Always use [[VolatileMemoryAccess|volatile]] methods** to read or write peripheral memory (it can change at any time).
  2. **Any number of read-only accesses** to a peripheral may be **shared** in software.
  3. **Read-write access** requires the holder to be the **only reference** to that peripheral.
- **Rules 2 and 3 are exactly the [[BorrowChecker|borrow checker]]**: shared `&T` (any number) vs exclusive `&mut T` (exactly one). The chapter's central insight: Rust already enforces precisely the discipline peripheral access needs.
- **Ownership / borrowing as the API**: if we represent each [[Peripheral|peripheral]] as a Rust value, we can pass around **ownership**, hand out immutable references for read-only sharing, and hand out a mutable reference when read-write access is needed. The compiler enforces the rules at compile time.
- **The exactly-one-instance precondition**: for the [[BorrowChecker|borrow checker]] to do its job, there must be **exactly one** Rust value per physical peripheral. Hardware naturally satisfies this (one [[SysTick]] / one [[NVIC]] / one [[GPIO]] block per chip), but the code must **mirror** that uniqueness.
- **Open question (deferred to next sub-section)**: how do we **expose hardware uniqueness in the structure of our code**? Re-poses the singleton gap from [[rust-embedded-book-peripherals-a-first-attempt]] in [[BorrowChecker|borrow-checker]] terms — `SystemTimer::new()` callable twice violates the "exactly one instance" precondition.

## Key Quotes

> "Hardware is basically nothing but mutable global state, which can feel very frightening for a Rust developer." — opens the chapter with the **what makes hardware adversarial to Rust's safety model** framing.

> "The last two of these rules sound suspiciously similar to what the Borrow Checker does already!" — the chapter's punchline: the safe-peripheral-access discipline *is* the [[BorrowChecker|borrow checker]].

> "Imagine if we could pass around ownership of these peripherals, or offer immutable or mutable references to them?" — re-frames hardware access as the **ownership / borrowing** API, the standard Rust idiom.

> "For the Borrow Checker, we need to have exactly one instance of each peripheral, so Rust can handle this correctly." — the **uniqueness precondition** that motivates the singleton sub-section that follows.

> "In the hardware, there is only one instance of any given peripheral, but how can we expose that in the structure of our code?" — the chapter's closing question; the answer is the singleton pattern (next sub-section).

## Connections

- [[TheEmbeddedRustBook]] — file 20/44; third sub-section of the Peripherals chapter.
- [[rust-embedded-book-peripherals-a-first-attempt]] — preceding file (file 19/44); ended on the unresolved singleton gap. This file **diagnoses** the gap as a [[BorrowChecker|borrow-checker]] precondition violation.
- [[rust-embedded-book-peripherals-index]] — chapter opener (file 18/44); flagged ownership / aliasing as later sub-section topics — this is that sub-section.
- [[BorrowChecker]] — the central concept introduced in this chapter: Rust's compile-time aliasing-discipline checker. Mapped 1:1 onto rules (2) and (3) of safe peripheral access.
- [[Peripheral]] — the noun being managed; this chapter shows how the [[BorrowChecker|borrow checker]] gives peripherals safe sharing for free.
- [[VolatileMemoryAccess]] — rule (1) of safe peripheral access; the volatility primitive established in [[rust-embedded-book-peripherals-a-first-attempt]].
- [[RawPointer]] / [[VolatileRegisterCrate]] / [[ReprC]] — the access machinery from the prior sub-section; this chapter shifts focus from access primitives to the *aliasing-discipline* layer above.
- [[SysTick]] / [[NVIC]] / [[GPIO]] — examples of peripherals that exist in exactly one physical instance per chip; the uniqueness the next sub-section will mirror in code.
- [[ARMCortexM]] — defines the canonical peripherals whose uniqueness the chapter invokes.

## Contradictions

None. Strictly additive — bridges the access-primitives layer (volatile, raw pointers, `#[repr(C)]`) of [[rust-embedded-book-peripherals-a-first-attempt]] to the aliasing-discipline layer ([[BorrowChecker|borrow checker]] applied to peripherals) and re-poses the singleton gap in [[BorrowChecker|borrow-checker]] terms.
