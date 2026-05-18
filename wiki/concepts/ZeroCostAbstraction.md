---
title: "Zero Cost Abstraction"
type: concept
tags: [rust, embedded, type-system, compile-time, design-philosophy, zero-cost]
sources: [rust-embedded-book-static-guarantees-zero-cost-abstractions, rust-embedded-book-static-guarantees-design-contracts, rust-embedded-book-start-registers]
last_updated: 2026-05-16
---

# Zero Cost Abstraction

A program abstraction whose **runtime cost (CPU cycles, RAM, code space) is zero** relative to the equivalent hand-written low-level code — *"the ability to move certain behaviors to compile time execution or analysis"* ([[rust-embedded-book-static-guarantees-zero-cost-abstractions]]). The compile-time machinery (types, generics, marker structs) is **stripped by the optimizer** so the resulting machine code is indistinguishable from a direct, untyped implementation.

The named concept of the closing sub-section of the [[StaticGuarantee|*Static Guarantees*]] chapter of [[TheEmbeddedRustBook]] ([[rust-embedded-book-static-guarantees-zero-cost-abstractions]], file 26/44). The phrase had appeared earlier in the book (*"All with no run-time cost!"* in [[rust-embedded-book-start-registers]]) and across [[TypeStateProgramming]] / [[StaticGuarantee]] / [[BuilderPattern]] / [[DesignByContract]] — this chapter **names it and substantiates it mechanically**.

## The canonical worked example: a typestate GPIO handle

The book's worked example is the `GpioConfig<ENABLED, DIRECTION, MODE>` typestate API from [[rust-embedded-book-static-guarantees-design-contracts]]:

```rust,ignore
use core::mem::size_of;

let _ = size_of::<Enabled>();      // == 0
let _ = size_of::<Input>();        // == 0
let _ = size_of::<PulledHigh>();   // == 0
let _ = size_of::<GpioConfig<Enabled, Input, PulledHigh>>(); // == 0
```

Three independent state-axis markers ([[ZeroSizedType|ZSTs]]) and the fully parameterized configured-pin handle are **all zero bytes wide**. A transition method:

```rust,ignore
pub fn into_input_high_z(self) -> GpioConfig<Enabled, Input, HighZ> {
    self.periph.modify(|_r, w| w.input_mode().high_z());
    GpioConfig { periph: self.periph, enabled: Enabled, direction: Input, mode: HighZ }
}
```

*"Will generally boil down to a single assembly instruction — storing a constant register value to a register location."* The four ZST-marker field initializations compile out; only the register store remains. *"Renders to the same machine code as a direct register access."*

## The cost model in one sentence

> *"It uses no more CPU, RAM, or code space tracking the state of `GpioConfig`, and renders to the same machine code as a direct register access."* — [[rust-embedded-book-static-guarantees-zero-cost-abstractions]]

Three resources, three zeros: **zero extra cycles**, **zero extra bytes of RAM**, **zero extra bytes of code**.

## Compositional property

> *"In general, these abstractions may be nested as deeply as you would like. As long as all components used are zero sized types, the whole structure will not exist at runtime."*

ZST-of-ZST is a ZST. Nesting typestate handles arbitrarily deep preserves the zero-cost property — provided every type parameter and every field is itself a ZST. This is what justifies the macro-generated state-tuple `impl` blocks of production HAL crates.

## The compile-time cost

A zero-cost abstraction trades **runtime cost** for **compile-time cost**:

- More types (one per state).
- More generic parameters (one per state axis).
- More `into_*` transition methods (one per legal transition).
- Combinatorially many `impl` blocks for state-restricted operations — *"it may be tedious to define all possible combinations of state. In these cases, macros may be used to generate all implementations."*
- Intimidating type signatures and compile errors.

The macro-escape hatch is the standard production response (see `embedded-hal` GPIO + clock implementations).

## Position in the [[StaticGuarantee|static-guarantee]] taxonomy

| Property of the abstraction | Where it comes from |
|---|---|
| **Correctness** — illegal states are uncallable | [[TypeStateProgramming]] / [[DesignByContract]] (compile-time) |
| **Zero runtime cost** — no `if`, no flag, no branch | **this concept** (ZST + monomorphization) |
| **Self-documenting** — function signatures carry state | [[TypeStateProgramming]] / [[BuilderPattern]] |

The first two are the *raison d'être* of the [[StaticGuarantee|*Static Guarantees*]] chapter: types make violations un-typeable **and** the bookkeeping is free. This concept supplies the second.

## Connections

- [[ZeroSizedType]] — the **mechanism** under zero-cost typestate; unit-struct markers compile to zero bytes and the optimizer strips them.
- [[TypeStateProgramming]] — the **canonical example** of a zero-cost abstraction in embedded Rust; *"type states are also an excellent example of Zero Cost Abstractions."*
- [[StaticGuarantee]] — the **chapter-level framing**; the *"buys: zero runtime cost"* row of that page's trade-off table is mechanized here.
- [[BuilderPattern]] — the simplest zero-cost typestate; `FooBuilder` → `Foo` via consuming `self` produces no extra code beyond an in-place mutation.
- [[DesignByContract]] — the **chapter-naming pattern** the prior file proved compile-time-enforceable; this concept proves compile-time enforcement is **free**.
- [[HALCrate]] — the crate-stack layer where zero-cost typestate is the standard idiom; the macro-escape hatch generalizes builder-pattern boilerplate to N-axis state typestate.
- [[RustLanguage]] — `size_of::<T>()`, unit structs, and **monomorphization** (one specialized codegen per `GpioConfig<A, B, C>` instantiation, each one inlinable down to the raw register access) are the language features that make zero-cost abstractions work.
- [[Svd2Rust]] / [[PeripheralAccessCrate]] — the PAC layer whose own typed register-block proxies are themselves ZSTs; this is what lets the composite `GpioConfig<...>` handle be zero bytes (the `periph` field disappears too).
