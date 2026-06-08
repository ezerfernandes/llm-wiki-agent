---
title: "Design by Contract"
type: concept
tags: [software-engineering, design-pattern, types, embedded]
sources: [rust-embedded-book-static-guarantees-design-contracts, fuzzingbook-02-intro-testing, fuzzingbook-03-fuzzer, fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
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

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] of *The Fuzzing Book* approaches DbC from the dynamic/testing side rather than the type-system side. It frames a function's [[Precondition|preconditions]] as caller obligations (`my_sqrt`'s implicit "`x` must be non-negative and finite," made explicit as `assert 0 <= x` in `my_sqrt_fixed`) and a function's [[Postcondition|postcondition]] as a property the result must satisfy (`root * root ≈ x`). Enforcing the postcondition on every call is its notion of [[RunTimeVerification|run-time verification]] — runtime DbC. Crucially for fuzzing, the chapter argues you can only safely *generate* calls into a function if you "*know* its precise preconditions"; at the *system* boundary, by contrast, robust code must accept and validate arbitrary input, which is what makes it fuzzable. This complements the wiki's existing compile-time (typestate) view of DbC: the Rust chapters push contracts into types, while *The Fuzzing Book* checks them dynamically via [[Assertion|assertions]].

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] extends the contract idea from single functions to **whole data structures** via the [[RepresentationInvariant|`repOK()`]] *class invariant* — the DbC clause asserting an object is internally consistent. Mutating methods assert `repOK()` both before and after every change (`add_new_airport_2`, `RedBlackTree.add_element`/`delete_element`), so a contract violation is caught at the moment of corruption. The chapter argues such assertions both *find errors* (especially under [[Fuzzing|fuzzing]]) and *document the design assumptions*, and contrasts them with [[StaticAnalysis|static type checking]] ([[MyPy]]), which enforces simple type contracts but cannot statically verify rich invariants — exactly the same runtime-vs-compile-time DbC tension the Rust chapters frame.

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] both *implements* and *mines* DbC contracts. It first builds a clean runtime-DbC mechanism: a `condition()` decorator factory yielding `@precondition(lambda x: x > 0)` and `@postcondition(lambda ret, x: ...)` decorators that `assert` the [[Precondition|pre-]]/[[Postcondition|postcondition]] around every call (a runtime form of [[DesignByContract|DbC]] / [[RunTimeVerification|run-time verification]]). It then closes the loop by *automatically inferring* the contract: the `InvariantAnnotator` observes a function's executions and emits the surviving [[DynamicInvariant|dynamic invariants]] as exactly these decorators (or, in Exercise 9, as inline `assert`s). This is the dynamic, learned counterpart to the Rust chapters' compile-time (typestate) DbC: where Rust encodes contracts into types, Ch 22 *discovers* the contract from runs and checks it at runtime — and the mined contract doubles as a regression [[TestOracle|oracle]] (it catches a `my_sqrt` that starts returning a negative root). See [[Daikon]] for the seminal tool that mines such contracts.

## Relation to adjacent patterns

- [[TypeStateProgramming]] — the **mechanism** by which compile-time DbC is implemented in Rust. The wiki's DbC page is the *named framing* of *why* one would reach for typestate; the typestate page is the *how*.
- [[FiniteStateMachine]] — DbC's *invariant* clause typically encodes "the object is in a valid state of its FSM"; typestate-DbC encodes the FSM into types so invariants become impossible to violate.
- [[BuilderPattern]] — a DbC pattern where the **construction precondition** ("all required fields must be set") is enforced at compile time via consuming-`self` transitions.
- [[Singleton]] — a DbC pattern enforcing the invariant *"at most one live handle to peripheral X exists"* via a one-shot gate.
- [[BorrowChecker]] — Rust's general-purpose DbC engine for the *"shared / exclusive access"* contract on every `&T` / `&mut T`.

## Connections

- [[Precondition]] / [[Postcondition]] — the caller/callee obligations DbC is built from; *The Fuzzing Book* treats them as dynamically-checked assertions.
- [[RunTimeVerification]] — runtime DbC: enforcing the postcondition on every invocation.
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2; the dynamic/testing view of DbC (preconditions + property postconditions via `assert`).
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3; the class-invariant form of DbC ([[RepresentationInvariant|`repOK()`]]) checked before/after mutations and under fuzzing.
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22; implements `@precondition`/`@postcondition` decorators and *mines* the contract automatically from executions ([[SpecificationMining]] / [[DynamicInvariant]]).
- [[Daikon]] — the seminal tool that mines DbC contracts (likely invariants) from runs.
- [[RepresentationInvariant]] — the data-structure invariant (`repOK()`) that is the class-level DbC clause.
- [[StaticGuarantee]] — the wiki's umbrella term for compile-time-enforced properties; DbC is the **classical software-engineering name** for the family of designs `StaticGuarantee` covers.
- [[rust-embedded-book-static-guarantees-design-contracts]] — the source chapter; provides the side-by-side GPIO runtime-vs-compile-time DbC worked example.
- [[rust-embedded-book-static-guarantees-state-machines]] — the prior chapter file that built the GPIO FSM the DbC contract operates over.
- [[rust-embedded-book-static-guarantees-typestate-programming]] — the prior chapter file that introduced the consuming-`self` typestate mechanism used to enforce DbC at compile time.
- [[rust-embedded-book-start-registers]] — the productionized DbC example (`into_af_push_pull::<AF1>()`, `Clock`-borrow-before-`Serial::new`).
- [[TheEmbeddedRustBook]] — chapter 25/44; the wiki's primary DbC source.
