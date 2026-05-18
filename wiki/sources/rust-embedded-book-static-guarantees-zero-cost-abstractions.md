---
title: "The Embedded Rust Book — Zero Cost Abstractions"
type: source
tags: [rust, embedded, book-chapter, zero-cost-abstractions]
date: 2026-05-16
source_file: raw/book/src/static-guarantees/zero-cost-abstractions.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Zero Cost Abstractions

## Summary

File 26/44 of *[[TheEmbeddedRustBook]]* — the **fourth and final named sub-section** of the *Static Guarantees* chapter, immediately after [[rust-embedded-book-static-guarantees-design-contracts]] (which presented the runtime-vs-compile-time GPIO trade-off and the worked `GpioConfig<ENABLED, DIRECTION, MODE>` typestate API). This file **names the mechanism** that makes the prior file's "no runtime cost" claim concrete: [[ZeroCostAbstraction|Zero Cost Abstractions]] — *"the ability to move certain behaviors to compile time execution or analysis."* Five lines of `core::mem::size_of` evidence: `size_of::<Enabled>() == 0`, `size_of::<Input>() == 0`, `size_of::<PulledHigh>() == 0`, and (most importantly) `size_of::<GpioConfig<Enabled, Input, PulledHigh>>() == 0`. The fully parameterized configured-pin handle is **zero bytes wide**. Names [[ZeroSizedType|Zero Sized Types (ZSTs)]] — *"structures defined like this … contain no actual data. Although these types act 'real' at compile time — you can copy them, move them, take references to them, etc., however the optimizer will completely strip them away."* Closes with the *Nesting* paragraph: typestate wrappers may be nested arbitrarily deeply and *"as long as all components used are zero sized types, the whole structure will not exist at runtime"* — and a forward-pointer to **macros** for combinatorially-large state taxonomies. Worked example: `into_input_high_z(self) -> GpioConfig<Enabled, Input, HighZ>` compiles down to **a single store of a constant register value** — *"renders to the same machine code as a direct register access."* The chapter that **closes the** [[StaticGuarantee|*static-guarantee*]] **chapter** by stating, mechanically, why the type-system bookkeeping the chapter has built up over four files costs zero bytes and zero cycles at runtime.

## Key Claims

- **Typestate is the canonical example of a Zero Cost Abstraction.** *"Type states are also an excellent example of Zero Cost Abstractions — the ability to move certain behaviors to compile time execution or analysis."* The prior three sub-sections built up the typestate machinery; this one **names the cost model**.
- **State-marker structs are Zero Sized Types.** A unit struct like `struct Enabled;` has *"no actual data"* and *"no actual representation in memory at runtime."* `size_of::<Enabled>() == 0` (and same for `Input`, `PulledHigh`, etc.).
- **The composite typestate handle is also zero-sized.** `size_of::<GpioConfig<Enabled, Input, PulledHigh>>() == 0` — the entire three-parameter, four-field configured-pin handle (with `enabled: Enabled, direction: Input, mode: PulledHigh, periph: ...`) takes zero bytes (modulo the bare `periph` handle, which by the file-25 setup is itself a ZST [[Svd2Rust|svd2rust]] register-block proxy). The Cartesian-product type explosion costs nothing at runtime.
- **ZSTs behave "real" at compile time.** *"You can copy them, move them, take references to them, etc."* — the Rust value-semantics rules apply normally; only the **optimizer** is responsible for stripping them away. The type checker treats `Enabled` exactly as it would any other unit struct.
- **Transitions compile to single store instructions.** *"The GpioConfig we return never exists at runtime. Calling this function will generally boil down to a single assembly instruction — storing a constant register value to a register location."* The `into_input_high_z(self) -> GpioConfig<Enabled, Input, HighZ>` example body is one `self.periph.modify(|_r, w| w.input_mode().high_z())` + four field initializations of ZST markers — the four ZST writes vanish, leaving the bare register store.
- **Zero cost across all three resources.** *"It uses no more CPU, RAM, or code space tracking the state of `GpioConfig`, and renders to the same machine code as a direct register access."* The trade-off table from [[StaticGuarantee]] (zero runtime cost / earlier failure / self-documenting APIs vs. API-design and compile-time-complexity costs) is settled on the runtime side **mechanically** here.
- **Arbitrary nesting preserves zero-cost.** *"In general, these abstractions may be nested as deeply as you would like. As long as all components used are zero sized types, the whole structure will not exist at runtime."* Compositional property: ZST-of-ZST is a ZST.
- **Macros are the escape hatch for combinatorial state explosion.** *"For complex or deeply nested structures, it may be tedious to define all possible combinations of state. In these cases, macros may be used to generate all implementations."* Names the **macro escape** for the manual-`impl`-per-state-tuple cost that motivates production HAL crates' macro-heavy code (e.g. `embedded-hal` GPIO + clock implementations).

## Key Quotes

> "Type states are also an excellent example of Zero Cost Abstractions — the ability to move certain behaviors to compile time execution or analysis." — the chapter's definition of [[ZeroCostAbstraction|Zero Cost Abstraction]] in one sentence.

> "These type states contain no actual data, and are instead used as markers. Since they contain no data, they have no actual representation in memory at runtime." — the ZST claim, stated mechanically.

> "Structures defined like this are called Zero Sized Types, as they contain no actual data. Although these types act 'real' at compile time — you can copy them, move them, take references to them, etc., however the optimizer will completely strip them away." — the canonical Rust [[ZeroSizedType|ZST]] definition the wiki now records.

> "The GpioConfig we return never exists at runtime. Calling this function will generally boil down to a single assembly instruction — storing a constant register value to a register location. This means that the type state interface we've developed is a zero cost abstraction — it uses no more CPU, RAM, or code space tracking the state of GpioConfig, and renders to the same machine code as a direct register access." — the chapter's mechanical-cost statement on the file-25 worked example.

> "In general, these abstractions may be nested as deeply as you would like. As long as all components used are zero sized types, the whole structure will not exist at runtime." — the compositional zero-cost property.

> "For complex or deeply nested structures, it may be tedious to define all possible combinations of state. In these cases, macros may be used to generate all implementations." — the **macro escape hatch**, forward-pointer to production HAL idiom.

## Connections

- [[TheEmbeddedRustBook]] — file 26/44; **fourth and final** named sub-section of the *Static Guarantees* chapter — **closes the chapter**.
- [[rust-embedded-book-static-guarantees-design-contracts]] — directly preceding file (25/44); built the `GpioConfig<ENABLED, DIRECTION, MODE>` typestate API and claimed *"this incurs no runtime cost."* **This file mechanically supplies that claim** via `size_of::<...>() == 0` evidence and the single-store-instruction lowering.
- [[rust-embedded-book-static-guarantees-state-machines]] — file 24/44; the `GpioConfig` whose runtime cost this file pins down (zero bytes for the configured handle, one store for transitions).
- [[rust-embedded-book-static-guarantees-typestate-programming]] — file 23/44; the abstract `FooBuilder` → `Foo` recipe whose **runtime cost** this file finally states explicitly (the `FooBuilder` struct holds real `a: u32, b: u32` data so is not itself a ZST, but pure-marker typestate handles like `GpioConfig<Enabled, ...>` are).
- [[rust-embedded-book-static-guarantees-index]] — chapter opener (22/44); the *"reducing the need for runtime checks"* framing whose **literal zero-cost lowering** this file demonstrates.
- [[rust-embedded-book-start-registers]] — file 13/44; the *"All with no run-time cost!"* one-liner that this file finally **mechanizes** with `size_of` evidence.
- [[ZeroCostAbstraction]] — the chapter's titular concept; this file is the wiki's **primary worked example** for the term.
- [[ZeroSizedType]] — the *mechanism* under the chapter's zero-cost claim; unit-struct typestate markers are ZSTs and the optimizer strips them.
- [[TypeStateProgramming]] — the design pattern whose zero-cost property the chapter substantiates; the file's *"All with no run-time cost!"* invariant is now mechanically grounded.
- [[StaticGuarantee]] — the chapter-level framing; this file resolves the *"buys: zero runtime cost"* row of the trade-off table by stating the lowering.
- [[GPIO]] — the peripheral; the `GpioConfig<Enabled, Input, PulledHigh>` example is the file-25 GPIO API at run time, evidence-checked at zero bytes.
- [[BuilderPattern]] — file 23's named special case of typestate; the chapter's macro-escape-hatch paragraph generalizes builder-pattern boilerplate to N-axis state typestate.
- [[Svd2Rust]] — the PAC-layer register-block proxy whose own ZST-ness is what lets the composite `GpioConfig<...>` be a ZST (the `periph: GPIO_CONFIG` field disappears too).
- [[PeripheralAccessCrate]] — the layer the zero-cost typestate wrapper sits on top of; the *"renders to the same machine code as a direct register access"* claim is what makes a HAL-typestate layer free relative to a raw PAC layer.
- [[HALCrate]] — the crate-stack layer where these zero-cost typestate APIs are the standard idiom; the macro-escape paragraph forward-references `embedded-hal` GPIO/clock implementations.
- [[RustLanguage]] — `size_of::<T>()`, unit structs, and monomorphization (the compile-time mechanism that lets `GpioConfig<Enabled, Input, PulledHigh>` exist as its own type with its own optimized lowering) are language features the chapter assumes.

## Contradictions

None with existing wiki content. **Strictly additive — this file *names* the cost model behind every prior typestate / static-guarantee claim in the corpus.** The *"zero runtime cost"* claim already on [[StaticGuarantee]], [[TypeStateProgramming]], [[BuilderPattern]], and [[DesignByContract]] is here mechanically grounded with `size_of::<...>() == 0` evidence and the single-store-instruction lowering — strengthening, not contradicting, those pages.
