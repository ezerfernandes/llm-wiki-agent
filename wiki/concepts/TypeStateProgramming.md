---
title: "Type-State Programming"
type: concept
tags: [rust, embedded, type-system, design-pattern, zero-cost]
sources: [rust-embedded-book-start-registers, rust-embedded-book-static-guarantees-typestate-programming]
last_updated: 2026-05-16
---

# Type-State Programming

Design pattern in which a value's **runtime state machine** is encoded directly in the **compile-time type system** — each state is a distinct type, and state transitions are functions that consume a value of one type and produce a value of another. Illegal state transitions become **compile errors**. Formal definition ([Wikipedia: typestate analysis](https://en.wikipedia.org/wiki/Typestate_analysis), per [[rust-embedded-book-static-guarantees-typestate-programming]]): *"the encoding of information about the current state of an object into the type of that object."*

Idiomatic in Rust because of two language features that, together, make typestate **enforceable rather than merely suggestive** ([[rust-embedded-book-static-guarantees-typestate-programming]]):

1. **Strong type system** — no implicit conversions between distinct types; the compiler refuses to turn a `FooBuilder` into a `Foo` (or any state-A type into a state-B type) without an explicit transition method call. No "magic instantiation path" exists for the configured-state type.
2. **Move semantics by default** — transition methods take `self` by value (not `&self` or `&mut self`), so the source-state value is **consumed** by the transition. The original `FooBuilder` cannot be reused after `.into_foo()`; the compiler enforces "this state value is gone" at compile time. This is what prevents double-transitions / use-after-transition.

The pattern is also **zero-cost**: phantom-type parameters carry no runtime data, and consuming-`self` methods produce no extra code beyond what an in-place mutation would. *"All with no run-time cost!"* ([[rust-embedded-book-start-registers]]).

## The canonical illustration: the [[BuilderPattern|builder pattern]]

The [[BuilderPattern|builder pattern]] is the typestate pattern the average Rust programmer has already met — *"if you have used the Builder Pattern in Rust, you have already started using Typestate Programming!"* ([[rust-embedded-book-static-guarantees-typestate-programming]]). The minimum reproducible example ([[rust-embedded-book-static-guarantees-typestate-programming]]):

```rust
pub struct Foo { inner: u32 }                       // state B: "configured / ready"
pub struct FooBuilder { a: u32, b: u32 }            // state A: "unconfigured"

impl FooBuilder {
    pub fn new(starter: u32) -> Self { ... }        // entry into state A
    pub fn double_a(self) -> Self { ... }           // state A -> state A (rebuild)
    pub fn into_foo(self) -> Foo { ... }            // transition: state A -> state B
}
// usage: FooBuilder::new(10).double_a().into_foo()
```

Two states, one transition (`into_foo`), one self-loop (`double_a`). Note every method takes `self` by value — the original is consumed and rebuilt. Equivalently, *"this allows us to represent the states of our system as types, and to include the necessary actions for state transitions into the methods that exchange one type for another. By creating a `FooBuilder`, and exchanging it for a `Foo` object, we have walked through the steps of a basic state machine."* ([[rust-embedded-book-static-guarantees-typestate-programming]])

## Embedded applications

[[rust-embedded-book-start-registers]] is where the pattern shows up *operationally* on real embedded hardware, before the conceptual write-up at [[rust-embedded-book-static-guarantees-typestate-programming]]. The [[Registers chapter|rust-embedded-book-start-registers]] introduces typestate as the core design pattern of [[HALCrate|HAL crates]]:

- **GPIO pin modes**: each Input / Output / AlternateFunction*N* mode is a distinct type. The pin starts in some default mode; `pin.into_af_push_pull::<AF1>()` consumes it and returns a pin of a different type. Passing a pin in the wrong mode to a peripheral constructor (e.g. a `Serial` UART transmit pin that hasn't been put into AF mode) is a **compile error**.
- **Clock configuration**: a `Serial::new` constructor takes a borrow on a `Clock` struct, which can only be produced by *configuring the PLLs and freezing the clock setup*. It is **statically impossible** to construct a Serial port without first having configured clock rates, or for the Serial port to miscompute the baud-rate divisor.

Both are direct generalizations of the `FooBuilder` → `Foo` recipe: each pin mode / clock-state is a distinct Rust type, each `into_*` / `.freeze()` / `Serial::new` is a consuming transition.

## Position in the [[StaticGuarantee|static-guarantee]] taxonomy

Per [[rust-embedded-book-static-guarantees-index]]'s four-family taxonomy, typestate is the mechanism behind **two** of the four families:

| Family | Mechanism |
|---|---|
| Initialization ordering — `Serial::new` only after pins are configured | typestate (phantom-typed state machine) |
| Configuration-dependent operations — `set_low` on a floating-input pin is a compile error | typestate (per-state methods) |

The remaining two families — data-race freedom (`Send` / `Sync`) and access control ([[BorrowChecker]] + [[Singleton]]) — use other mechanisms, but **all four** share the typestate-pattern shape of encoding the property in **types** so violations are rejected by the compiler.

## Connections

- [[BuilderPattern]] — the canonical Rust idiom that *is* a typestate pattern; the pedagogical hook of [[rust-embedded-book-static-guarantees-typestate-programming]].
- [[StaticGuarantee]] — the chapter-level framing umbrella; typestate mechanizes two of its four embedded-Rust families.
- [[HALCrate]] — the crate-stack layer that uses typestate pervasively for GPIO pin modes + clock-configuration ordering.
- [[RustLanguage]] — the language whose **strong type system + move semantics** make typestate cheap and enforceable.
- [[EmbeddedHalCrate]] — typestate APIs are typically defined as `embedded-hal` traits with phantom-typed pin states, so typestate composes with `embedded-hal` portability.
- [[BorrowChecker]] / [[Singleton]] — the sibling [[StaticGuarantee|static-guarantee]] mechanisms; together with typestate they cover all four embedded-Rust static-guarantee families.
