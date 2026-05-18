---
title: "The Embedded Rust Book — Typestate Programming"
type: source
tags: [rust, embedded, book-chapter, typestate, type-system]
date: 2026-05-16
source_file: raw/book/src/static-guarantees/typestate-programming.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Typestate Programming

## Summary

File 23/44 of *[[TheEmbeddedRustBook]]* — the **first named sub-section** of the *Static Guarantees* chapter, immediately after the chapter opener at file 22 ([[rust-embedded-book-static-guarantees-index]]). Defines [[TypeStateProgramming|typestate programming]] explicitly (Wikipedia link to *typestate analysis*) as "the encoding of information about the current state of an object into the type of that object." Names the [[BuilderPattern|builder pattern]] as the canonical Rust illustration — *"if you have used the Builder Pattern in Rust, you have already started using Typestate Programming!"* Walks one minimal worked example: a `FooBuilder` struct (un-configured state) whose `into_foo(self) -> Foo` method **consumes** the builder by value (`self`, not `&self`) and returns a `Foo` struct (configured state). Anchors the design pattern on two specific Rust features — the **strong type system** (no implicit conversions between `FooBuilder` and `Foo`) and **move semantics by default** (`into_foo` takes `self` by value, so the original `FooBuilder` is gone after the call and cannot be reused). Closes by framing the example as a basic **state machine** — two states encoded as types, one transition encoded as the `into_foo` method. The chapter intro that *names* what was already operationally introduced for [[GPIO]] pin modes / clock configuration in [[rust-embedded-book-start-registers]].

## Key Claims

- **Typestate = encoding state-machine state in the type system.** "The concept of typestates describes the encoding of information about the current state of an object into the type of that object." The runtime state-machine state is **lifted to compile time** as a Rust type.
- **The [[BuilderPattern|builder pattern]] is a typestate pattern.** *"If you have used the Builder Pattern in Rust, you have already started using Typestate Programming!"* — the chapter's pedagogical hook: the reader already knows the pattern under a different name.
- **The canonical worked example.** A `FooBuilder` struct ("unconfigured / configuration-in-process" state) and a `Foo` struct ("configured / ready-to-use" state); the only way to obtain a `Foo` is to call `FooBuilder::new(starter)` and then `.into_foo()`. Configuration methods like `.double_a()` take `self` by value and return `Self` — the builder is **rebuilt** on each step, not mutated in place.
- **No magic instantiation path.** Rust's [strong type system](https://en.wikipedia.org/wiki/Strong_and_weak_typing) makes it impossible to obtain a `Foo` without going through a `FooBuilder` — there is no implicit conversion. *"There is no easy way to magically create an instance of `Foo`, or to turn a `FooBuilder` into a `Foo` without calling the `into_foo()` method."*
- **Move semantics enforce the transition's one-shot nature.** `into_foo(self)` (and `double_a(self)`) take `self` by value, **consuming** the original — so the same `FooBuilder` value cannot be reused after the transition. *"Calling the `into_foo()` method consumes the original `FooBuilder` structure, meaning it can not be reused without the creation of a new instance."* This is the type-state property that compile-time-prevents double-transitions / use-after-transition.
- **States = types, transitions = consuming methods.** The general recipe: *"This allows us to represent the states of our system as types, and to include the necessary actions for state transitions into the methods that exchange one type for another."*
- **The result is a state machine in the type system.** *"By creating a `FooBuilder`, and exchanging it for a `Foo` object, we have walked through the steps of a basic state machine."* The state machine's transition graph is encoded in the type signatures of the conversion methods.

## Key Quotes

> "The concept of typestates describes the encoding of information about the current state of an object into the type of that object. Although this can sound a little arcane, if you have used the Builder Pattern in Rust, you have already started using Typestate Programming!" — the chapter's headline definition and pedagogical hook.

> "Because Rust has a Strong Type System, there is no easy way to magically create an instance of `Foo`, or to turn a `FooBuilder` into a `Foo` without calling the `into_foo()` method. Additionally, calling the `into_foo()` method consumes the original `FooBuilder` structure, meaning it can not be reused without the creation of a new instance." — the **two language features** (strong typing + move semantics) that together make typestate enforceable rather than merely suggestive.

> "This allows us to represent the states of our system as types, and to include the necessary actions for state transitions into the methods that exchange one type for another. By creating a `FooBuilder`, and exchanging it for a `Foo` object, we have walked through the steps of a basic state machine." — the chapter's closing generalization: typestate **is** state-machine programming with the state machine living in the type system.

## Connections

- [[TheEmbeddedRustBook]] — file 23/44; **first named sub-section of the Static Guarantees chapter** (after the chapter opener at file 22, [[rust-embedded-book-static-guarantees-index]]).
- [[rust-embedded-book-static-guarantees-index]] — directly preceding file; the chapter opener that previewed [[TypeStateProgramming|typestate]] as the mechanism behind two of the four [[StaticGuarantee|static-guarantee]] families (initialization ordering, configuration-dependent operations). This sub-section defines and demonstrates the mechanism.
- [[rust-embedded-book-start-registers]] — earlier file (13/44) that **already used** typestate operationally on real embedded examples ([[GPIO]] pin modes, `Serial::new` borrowing a `Clock`, *"all with no run-time cost"*). This chapter is the **conceptual write-up** of what that chapter showed in practice.
- [[TypeStateProgramming]] — the concept page; this file extends it with the canonical Rust [[BuilderPattern|builder-pattern]] illustration, the explicit Wikipedia *typestate analysis* link, and the **strong-typing + move-semantics** mechanism story.
- [[StaticGuarantee]] — the chapter-level framing concept; typestate is the mechanism that mechanizes two of its four embedded-Rust families.
- [[BuilderPattern]] — the canonical Rust idiom the chapter uses as the pedagogical anchor — the chapter explicitly identifies the builder pattern as a typestate pattern.
- [[RustLanguage]] — the language whose **strong type system** and **move-by-default semantics** together make typestate enforceable.
- [[HALCrate]] / [[EmbeddedHalCrate]] — the crate-stack layer that uses typestate pervasively (GPIO pin modes, clock configuration); the productionized embedded application of the pattern this chapter abstracts.

## Contradictions

None with existing wiki content. Strictly additive — names and demonstrates the design pattern the wiki has been operating under since [[rust-embedded-book-start-registers]] introduced it operationally and [[rust-embedded-book-static-guarantees-index]] previewed it conceptually. This file supplies the **minimum reproducible example** (the `FooBuilder` / `Foo` pair) and the **mechanism explanation** (strong typing + move semantics) for the concept page.
