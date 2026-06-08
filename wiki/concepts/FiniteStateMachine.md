---
title: "Finite State Machine"
type: concept
tags: [computation, modeling, embedded, design-pattern]
sources: [rust-embedded-book-static-guarantees-state-machines, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# Finite State Machine

A **finite state machine** (FSM) is a computational model with a finite set of *states*, a finite set of *transitions* between those states, and rules for which transitions are allowed from which states. At any moment the machine is in exactly one state; transitions are triggered by events or method calls and move the machine to a new (or the same) state. The *valid-state set* is typically a strict subset of the representable underlying state — most bit-patterns of an FSM's storage do **not** correspond to a valid state.

In [[TheEmbeddedRustBook]] ([[rust-embedded-book-static-guarantees-state-machines]]), the FSM is the underlying computational model the book uses to talk about MCU peripherals: *"the peripherals of a microcontroller can be thought of as set of state machines."* The chapter's worked example is a hierarchical FSM for a [[GPIO]] pin:

```
Disabled
Enabled
├─ Configured as Output
│  ├─ Output: High
│  └─ Output: Low
└─ Configured as Input
   ├─ Input: High Resistance
   ├─ Input: Pulled Low
   └─ Input: Pulled High
```

Three intermediate states (Disabled, Configured as Output, Configured as Input — plus the Enabled super-state) and seven configurations the pin can be in. Transitions are explicit walks through the tree: *Input: Pulled Low → Output: High* requires four steps (Input: Pulled Low → Configured as Input → Configured as Output → Output: High); diagonal jumps are not allowed.

## Valid states vs representable states

A core FSM property — and the reason FSM thinking matters for embedded — is that the **valid-state set is smaller than the representable-state set**. In [[rust-embedded-book-static-guarantees-state-machines]]'s GPIO example, a packed configuration register has fields `enable` (1 bit), `direction` (1 bit), `input_mode` (2 bits), `output_mode` (1 bit). The bit-pattern Cartesian product has 32 combinations, but:

- `input_mode = 11` is explicitly **invalid** ("n/a — Invalid state. Do not set").
- `output_mode` is meaningless when `direction = input`.
- `input_mode` is meaningless when `direction = output`.

So the valid-state set is **seven** leaf states, not 32. An API that exposes the register bits independently (as the chapter's naive `GpioConfig` does) lets callers reach the 25 invalid bit-patterns; an FSM-aware API exposes only the seven valid states.

## Relation to [[TypeStateProgramming|typestate programming]]

[[TypeStateProgramming|Typestate programming]] is the **Rust mechanism for encoding an FSM into the type system**: each state of the FSM becomes a distinct Rust type, each transition becomes a method that consumes a value of one state-type and returns a value of another. *"By creating a `FooBuilder`, and exchanging it for a `Foo` object, we have walked through the steps of a basic state machine"* ([[rust-embedded-book-static-guarantees-typestate-programming]]). The compiler's strong type system + move semantics then **statically reject** every transition the FSM disallows — invalid bit-patterns become **compile errors** rather than runtime hardware faults.

The FSM is the *what* (the abstract model of valid states + valid transitions); typestate is the *how* (the Rust idiom that mechanizes that model in the type system at zero runtime cost).

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] uses an FSM as the model of a *user interface* for [[GUIFuzzing|GUI fuzzing]]: each *state* is a page (identified by its set of interactive elements, **not** its URL) and each *transition* is a user action (`click`/`submit`). The chapter's central trick is to **embed the FSM into a [[Grammar|grammar]]** — every state becomes a grammar symbol and every transition becomes a grammar alternative `actions <target-state>` — so one structure encodes both states and form values ([[ModelBasedTesting|model-based testing]] / a [[UINavigationModel|UI navigation model]]). A consequence is that covering all FSM transitions reduces to covering all [[GrammarCoverage|grammar expansions]], which an off-the-shelf [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] does for free. `fsm_diagram()` renders such a state grammar back as a Graphviz state machine. This is a different use of FSMs than the embedded-systems framing below — here the FSM is *mined by exploration* rather than designed up front.

## Applications in this wiki

- **Embedded peripherals** ([[rust-embedded-book-static-guarantees-state-machines]]): GPIO pins, USART configuration, clock-tree configuration, DMA channel state.
- **The [[BuilderPattern|builder pattern]]** ([[rust-embedded-book-static-guarantees-typestate-programming]]): the smallest non-trivial FSM — two states (`FooBuilder`, `Foo`) and one transition (`into_foo`).
- **GPIO pin modes** ([[rust-embedded-book-start-registers]]): each Input / Output / AlternateFunction*N* mode is a state; `into_af_push_pull::<AF1>()` is a transition.

## Connections

- [[TypeStateProgramming]] — the Rust design pattern that encodes an FSM into the type system; the mechanism by which an FSM becomes a [[StaticGuarantee|static guarantee]].
- [[BuilderPattern]] — the smallest worked FSM in Rust (two states, one transition); the pedagogical anchor of [[rust-embedded-book-static-guarantees-typestate-programming]].
- [[StaticGuarantee]] — the chapter-level framing; an FSM mechanized as types is a static guarantee that illegal transitions cannot happen.
- [[GPIO]] — the canonical embedded FSM the book uses as its worked example.
- [[Peripheral]] — the noun the book recasts as an FSM: each peripheral has a finite state machine of valid configurations.
- [[HALCrate]] — the crate-stack layer where peripheral FSMs are concretely encoded as typestate APIs.
- [[UINavigationModel]] — an FSM of UI pages and actions, mined by exploration in [[fuzzingbook-28-gui-fuzzer|Ch 28]].
- [[ModelBasedTesting]] — testing by traversing an FSM (or other model) of expected behavior.
- [[GUIFuzzing]] / [[GUIFuzzer]] — embed a UI FSM into a grammar and cover its transitions.
- [[Grammar]] / [[GrammarCoverageFuzzer]] — Ch 28 embeds the FSM in a grammar so transition coverage = grammar coverage.

## Sources
- [[rust-embedded-book-static-guarantees-state-machines]] — *The Embedded Rust Book* (FSMs as the model for MCU peripherals + typestate).
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (FSM-of-pages embedded in a grammar for GUI fuzzing).
