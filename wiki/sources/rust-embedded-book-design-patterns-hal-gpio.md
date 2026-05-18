---
title: "The Embedded Rust Book — HAL GPIO"
type: source
tags: [rust, embedded, book-chapter, hal, gpio, typestate]
date: 2026-05-16
source_file: raw/book/src/design-patterns/hal/gpio.md
sources: []
last_updated: 2026-05-16
---

## Summary

File 36/44 of *[[TheEmbeddedRustBook]]* — the **fourth and final leaf-section** of the *HAL Design Patterns* sub-chapter ([[rust-embedded-book-design-patterns-hal-index]]) and the **GPIO Interfaces** group of the [[rust-embedded-book-design-patterns-hal-checklist|HAL Checklist]]. By far the **most substantive** of the four leaves (Naming / Interoperability / Predictability / GPIO): ~200 lines, four code blocks, three named patterns — **`C-ZST-PIN`**, **`C-ERASED-PIN`**, **`C-PIN-STATE`** — covering 3 of the 8 checklist items (37.5% of the entire HAL Checklist is GPIO-specific). Operationalizes the three abstractions the wiki has accumulated across the *Static Guarantees* chapter ([[ZeroSizedType|ZSTs]], [[TypeStateProgramming|typestate]], [[ZeroCostAbstraction|zero-cost abstractions]]) into one concrete pattern stack for [[GPIO]] pin APIs — the canonical [[HALCrate|HAL]] surface every embedded-Rust learner first touches.

## Key Claims

- **`C-ZST-PIN`** — *"GPIO Interfaces exposed by the HAL should provide dedicated zero-sized types for each pin on every interface or port, resulting in a zero-cost GPIO abstraction when all pin assignments are statically known."* Each [[GPIO]] port / interface implements a **`split` method** returning a struct whose fields are one [[ZeroSizedType|ZST]] per physical pin — `pub struct PA0; pub struct PA1; ... impl PortA { pub fn split(self) -> PortAPins { PortAPins { pa0: PA0, pa1: PA1, ... } } }`. Each pin is its own distinct type (`PA0` ≠ `PA1`), so pin-to-peripheral connections are checked at compile time — passing `PA1` to a function that expects `PA0` is a type error. Operationalizes the [[ZeroSizedType]] / [[ZeroCostAbstraction]] property from [[rust-embedded-book-static-guarantees-zero-cost-abstractions]] for pins specifically.
- **`C-ERASED-PIN`** — *"Pins should provide type erasure methods that move their properties from compile time to runtime, and allow more flexibility in applications."* Two-stage erasure: (1) `PA0::erase_pin(self) -> PA { pin: 0 }` collapses 16 distinct types (`PA0` … `PA15`) into a single `PA` carrying a `u8` pin number — pin identity moves from compile time to runtime; (2) `PA::erase_port(self) -> Pin { port: Port::A, pin: self.pin }` collapses 4 ports (`PA` / `PB` / `PC` / `PD`) into a single `Pin { port: Port, pin: u8 }` — port identity also moves to runtime. The trade-off is **compile-time-pin-distinctness for heterogeneous-collection-ability**: only a fully erased `Pin` can be stored in `[Pin; N]` / `Vec<Pin>` / `&dyn` trait objects. The signed runtime cost is *"these fields can be packed to reduce the memory footprint"* (a port enum + 4-bit pin index fits in one byte).
- **`C-PIN-STATE`** — *"Pin state should be encoded as type parameters … to prevent use of pins in incorrect states. Additional, chip-specific state (eg. drive strength) may also be encoded in this way, using additional type parameters."* The [[TypeStateProgramming|typestate]] pattern from [[rust-embedded-book-static-guarantees-design-contracts]] applied to pin configuration. Four required methods per pin type — `into_input<N: InputState>(self, input: N) -> Pin<Input<N>>`, `into_output<N: OutputState>(self, output: N) -> Pin<Output<N>>`, plus **`with_input_state` / `with_output_state`** scoped-reconfiguration variants (`&mut self` + `FnOnce(&mut Pin<N>) -> R`) for *"temporarily reconfigur[ing] a pin in a different state without moving it."*
- **The same API on erased and non-erased pins** — *"both erased and non-erased pin types should provide the same API."* Pin-state methods are required on `PA1<S>`, `PA<S>`, **and** `Pin<S>` — type erasure must not lose typestate guarantees. This is the [[ZeroCostAbstraction|zero-cost]] / runtime-flexibility trade-off without sacrificing the typestate invariant.
- **Sealed-trait state bound** — *"Pin state should be bounded by sealed traits. Users of the HAL should have no need to add their own state. The traits can provide HAL-specific methods required to implement the pin state API."* The **sealed-trait pattern** (private supertrait `mod sealed { pub trait Sealed {} }`, public `trait PinState: sealed::Sealed`) — downstream crates cannot implement the trait, so the HAL author controls the full set of states. Enables internal HAL-specific helper methods on the trait without exposing implementation details.
- **Three-layer trait stack** — `PinState: sealed::Sealed` (the **top**), with `OutputState: sealed::Sealed` and `InputState: sealed::Sealed` as **leaf** trait bounds. Concrete state markers — **`Output<S: OutputState>` / `Input<S: InputState>`** (parameterized wrappers) plus **`PushPull` / `OpenDrain`** (`OutputState` markers) and **`Floating` / `PullUp` / `PullDown`** (`InputState` markers) — give a **two-axis typestate**: `Input<PullUp>`, `Output<PushPull>`, etc., all bounded by `PinState`.
- **`PhantomData` carries the parameter** — `pub struct Output<S: OutputState> { _p: PhantomData<S> }` and `pub struct PA1<S: PinState> { _p: PhantomData<S> }` — the standard Rust idiom for *"this type is parameterized by `S` even though no field of type `S` exists."* Required because `PA1<Input<Floating>>` and `PA1<Output<PushPull>>` must be **distinct types** to the compiler, but they should both have zero size at runtime — see [[ZeroSizedType]].
- **Composes with `C-ZST-PIN` and `C-ERASED-PIN`** — the three patterns are designed to **stack**: a fully-statically-known `PA1<Output<PushPull>>` is a zero-sized handle whose state is compile-time-verified; calling `.erase_pin()` produces a `PA<Output<PushPull>>` (now `u8` wide) that's still in the same typestate; calling `.erase_port()` further reduces to `Pin<Output<PushPull>>` (two-byte) — none of the three steps loses the typestate parameter.

## Key Quotes

> "GPIO Interfaces exposed by the HAL should provide dedicated zero-sized types for each pin on every interface or port, resulting in a zero-cost GPIO abstraction when all pin assignments are statically known." — `C-ZST-PIN`

> "Pins should provide type erasure methods that move their properties from compile time to runtime, and allow more flexibility in applications." — `C-ERASED-PIN`

> "Pin state should be encoded as type parameters … to prevent use of pins in incorrect states." — `C-PIN-STATE`

> "Both erased and non-erased pin types should provide the same API." — the discipline that prevents type-erasure from costing typestate guarantees

> "Pin state should be bounded by sealed traits. Users of the HAL should have no need to add their own state." — the sealed-trait pattern, controlling the closed set of states

## Connections

- [[TheEmbeddedRustBook]] — file 36/44; closes the **GPIO Interfaces** group, the largest group of the HAL Checklist.
- [[rust-embedded-book-design-patterns-hal-index]] — parent sub-chapter; this file is the fourth (and final) leaf.
- [[rust-embedded-book-design-patterns-hal-checklist]] — the HAL Checklist file that aggregates `C-ZST-PIN` / `C-ERASED-PIN` / `C-PIN-STATE`.
- [[rust-embedded-book-design-patterns-hal-naming]] / [[rust-embedded-book-design-patterns-hal-interoperability]] / [[rust-embedded-book-design-patterns-hal-predictability]] — the three sibling leaves.
- [[GPIO]] — the peripheral being patterned; this file is the canonical HAL surface for GPIO.
- [[ZeroSizedType]] — the mechanism `C-ZST-PIN` operationalizes for pins (and the basis for `PhantomData<S>` state markers).
- [[ZeroCostAbstraction]] — the property `C-ZST-PIN` delivers when all pin assignments are statically known.
- [[TypeStateProgramming]] — the pattern `C-PIN-STATE` operationalizes for pin configuration.
- [[ErasedPin]] — new concept; the **type-erased pin** abstraction introduced by `C-ERASED-PIN`.
- [[PinTypeState]] — new concept; the **two-axis pin typestate** (Input/Output × per-direction modes) introduced by `C-PIN-STATE`.
- [[HALCrate]] — the crate layer this pattern stack lives in.
- [[rust-embedded-book-static-guarantees-design-contracts]] — the earlier file that introduced the multi-axis typestate pattern on an imaginary GPIO API; this file mechanizes that pattern as the canonical HAL surface.
- [[rust-embedded-book-static-guarantees-zero-cost-abstractions]] — the earlier file that named the [[ZeroSizedType|ZST]]-based zero-cost mechanism; `C-ZST-PIN` is its applied corollary for pins.
- [[BuilderPattern]] — distant cousin; both use consuming-`self` transitions, but `C-PIN-STATE` adds the *scoped-reconfiguration* `with_*_state` variant (`&mut self` + closure) that the builder pattern doesn't have.

## Contradictions

None. The three patterns extend and operationalize the *Static Guarantees* chapter's [[ZeroSizedType|ZST]] / [[TypeStateProgramming|typestate]] / [[ZeroCostAbstraction|zero-cost-abstraction]] vocabulary onto the [[GPIO]] surface without contradicting any prior file.
