---
title: "Design by Contract"
type: concept
tags: [software-engineering, design-pattern, types, embedded]
sources: [rust-embedded-book-static-guarantees-design-contracts]
last_updated: 2026-05-16
---

# Design by Contract

**Design by Contract (DbC)** is a software design approach (originating with Bertrand Meyer in Eiffel) in which an interface's *preconditions* (what the caller must guarantee), *postconditions* (what the callee then guarantees in return), and *invariants* (what holds throughout) are made **explicit obligations** of both parties to a function call. In embedded Rust, [[TheEmbeddedRustBook]] uses the term in [[rust-embedded-book-static-guarantees-design-contracts]] to frame a sharp design choice: contracts can be enforced **at runtime** (every call checks its preconditions and returns `Err` on a violation) or **at compile time** (the type system makes the violating call un-typeable). The chapter argues the second is strictly better for embedded peripherals because runtime checking *"wastes time and resources"* and pollutes return types with `Result<(), ()>` for caller-side concerns.

## The two enforcement modes — same contract, different cost

The chapter pins this down on one [[GPIO]] register block. The contract is the same in both designs:

> *"the pin must be enabled before its direction is set; the pin must be configured as input before its input mode is set; the pin must be configured as output before its output status is set."*

### Mode A — Runtime enforcement

Every method begins with a register-read + branch chain and returns `Result<(), ()>`:

```rust
pub fn set_input_mode(&mut self, variant: InputMode) -> Result<(), ()> {
    if self.periph.read().enable().bit_is_clear()   { return Err(()); }
    if self.periph.read().direction().bit_is_set()  { return Err(()); }
    self.periph.modify(|_r, w| w.input_mode().variant(variant));
    Ok(())
}
```

- **Cost.** 1–2 extra register reads + branches **per call**; `Result<(), ()>` return type that callers must `?` or `match` on.
- **Failure mode.** Contract violations are caught at runtime, *if they are caught*. A caller who `unwrap()`s an `Err(())` panics in production.
- **Caller pain.** *"This code will be much less pleasant for the developer to use."* The `Err(())` is uninformative (no payload distinguishes "not enabled" from "wrong direction").

### Mode B — Compile-time enforcement ([[TypeStateProgramming|typestate]])

The same contract, encoded as type parameters:

```rust
struct GpioConfig<ENABLED, DIRECTION, MODE> { periph: GPIO_CONFIG, ... }
impl GpioConfig<Enabled, Output, DontCare> { fn set_bit(&mut self, set_high: bool) { ... } }
impl<IN_MODE> GpioConfig<Enabled, Input, IN_MODE> { fn bit_is_set(&self) -> bool { ... } }
```

- **Cost.** Zero runtime overhead — the type markers (`Enabled` / `Output` / `DontCare`, …) are unit structs of size 0, and the precondition checks compile out entirely.
- **Failure mode.** Contract violations are **compile errors**: `input_pin.set_bit(true)` fails to type-check because `set_bit` is only `impl`d for `GpioConfig<Enabled, Output, DontCare>`. *"If they try to perform an illegal state transition, the code will not compile!"*
- **Caller ergonomics.** No `Result`s for caller-side preconditions; state transitions are consuming `self` methods (`into_enabled_input(self) -> GpioConfig<Enabled, Input, HighZ>`) that **rebuild** the wrapper at a new type.

## The four contract families on embedded peripherals

All four [[StaticGuarantee|static-guarantee]] families from the book's chapter framing are DbC contracts mechanized at compile time:

| Family | The contract | Enforced via |
|---|---|---|
| Data-race freedom | "this handle may not be sent across thread boundaries unless the type is `Send`" | `Send` / `Sync` marker traits ([[RustLanguage]]) |
| Initialization ordering | "the serial port may only be built after its pins are configured" | [[TypeStateProgramming]] |
| Configuration-dependent operations | "`set_low` may only be called on a pin currently configured as `Output`" | [[TypeStateProgramming]] |
| Access control | "exactly one Rust value per physical [[Peripheral]] exists at any time" | [[BorrowChecker]] + [[Singleton]] |

## Trade-offs

| | Runtime DbC | Compile-time DbC |
|---|---|---|
| Cost per call | 1+ extra reads + branches | 0 (compiles out) |
| Failure mode | `Err(())` / panic at runtime | Refuses to compile |
| Diagnostic | At violation site | At violation site, before flashing |
| Return type | `Result<(), ()>` everywhere | Plain `()` / `bool` / `T` |
| API design effort | Low (linear methods) | Higher (state-restricted `impl` blocks; transition methods) |
| Type signature complexity | Plain | Generic over state markers |
| Caller refactor cost on contract change | Low (`Result` already there) | Higher (signature changes) |

## Relation to adjacent patterns

- [[TypeStateProgramming]] — the **mechanism** by which compile-time DbC is implemented in Rust. The wiki's DbC page is the *named framing* of *why* one would reach for typestate; the typestate page is the *how*.
- [[FiniteStateMachine]] — DbC's *invariant* clause typically encodes "the object is in a valid state of its FSM"; typestate-DbC encodes the FSM into types so invariants become impossible to violate.
- [[BuilderPattern]] — a DbC pattern where the **construction precondition** ("all required fields must be set") is enforced at compile time via consuming-`self` transitions.
- [[Singleton]] — a DbC pattern enforcing the invariant *"at most one live handle to peripheral X exists"* via a one-shot gate.
- [[BorrowChecker]] — Rust's general-purpose DbC engine for the *"shared / exclusive access"* contract on every `&T` / `&mut T`.

## Connections

- [[StaticGuarantee]] — the wiki's umbrella term for compile-time-enforced properties; DbC is the **classical software-engineering name** for the family of designs `StaticGuarantee` covers.
- [[rust-embedded-book-static-guarantees-design-contracts]] — the source chapter; provides the side-by-side GPIO runtime-vs-compile-time DbC worked example.
- [[rust-embedded-book-static-guarantees-state-machines]] — the prior chapter file that built the GPIO FSM the DbC contract operates over.
- [[rust-embedded-book-static-guarantees-typestate-programming]] — the prior chapter file that introduced the consuming-`self` typestate mechanism used to enforce DbC at compile time.
- [[rust-embedded-book-start-registers]] — the productionized DbC example (`into_af_push_pull::<AF1>()`, `Clock`-borrow-before-`Serial::new`).
- [[TheEmbeddedRustBook]] — chapter 25/44; the wiki's primary DbC source.
