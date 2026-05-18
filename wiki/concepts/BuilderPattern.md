---
title: "Builder Pattern"
type: concept
tags: [rust, design-pattern, type-system, idiom]
sources: [rust-embedded-book-static-guarantees-typestate-programming]
last_updated: 2026-05-16
---

# Builder Pattern

Design pattern in which a complex object is constructed step-by-step through an intermediate **builder** value, rather than via a single multi-argument constructor. The builder accumulates configuration; a final terminal method converts the builder into the configured target object. Documented as a canonical Rust idiom in the official [Rust style guide](https://doc.rust-lang.org/1.0.0/style/ownership/builders.html) (cited by [[rust-embedded-book-static-guarantees-typestate-programming]]).

In Rust, the builder pattern is **a special case of [[TypeStateProgramming|typestate programming]]** — the "configuring" state (the builder type) and the "configured" state (the target type) are *distinct types*, and the terminal conversion method **consumes** the builder by value (`fn into_foo(self) -> Foo`). *"If you have used the Builder Pattern in Rust, you have already started using Typestate Programming!"* ([[rust-embedded-book-static-guarantees-typestate-programming]])

## Canonical shape

```rust
pub struct Foo { inner: u32 }                       // target: "configured"
pub struct FooBuilder { a: u32, b: u32 }            // builder: "configuring"

impl FooBuilder {
    pub fn new(starter: u32) -> Self { ... }        // entry
    pub fn double_a(self) -> Self { ... }           // configuration step (consuming-self)
    pub fn into_foo(self) -> Foo { ... }            // terminal: builder -> target
}
// usage: FooBuilder::new(10).double_a().into_foo()
```

Three properties make this a typestate pattern rather than a mere convenience wrapper:

1. **No direct construction path** for `Foo` — Rust's strong type system refuses any conversion from `FooBuilder` to `Foo` that does not go through `into_foo`.
2. **Consuming `self` on every step** — `double_a(self) -> Self` (not `&mut self`) means the builder is **rebuilt** at each step; the original builder value is gone after the call.
3. **One-shot terminal transition** — `into_foo(self) -> Foo` consumes the builder. The compiler enforces "this builder is done" at compile time; double-calling `.into_foo()` is a compile error (use-of-moved-value).

## Variants

The two-state `FooBuilder` → `Foo` is the simplest form. More elaborate builder chains have **N intermediate states**, each its own type, with transitions like `BuilderWithA -> BuilderWithAB -> BuilderWithABC -> Built`. The compiler then statically guarantees that `Built` can only be obtained after all required configuration steps have been performed in some valid order — a typestate state machine encoded directly in the conversion-method type signatures.

## Connections

- [[TypeStateProgramming]] — the design-pattern family the builder pattern belongs to; the builder's distinct-types + consuming-`self` shape is exactly the typestate recipe.
- [[StaticGuarantee]] — the framing concept; a builder pattern delivers a static guarantee that the target object cannot be constructed without going through the configuration steps.
- [[RustLanguage]] — the language whose move semantics + strong typing make the builder pattern's consuming-`self` mechanic enforce one-shot construction.
- [[HALCrate]] — embedded-Rust HALs use builder-like typestate patterns extensively for peripheral / clock / pin configuration (per [[rust-embedded-book-start-registers]]).
