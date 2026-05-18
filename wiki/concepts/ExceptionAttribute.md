---
title: "#[exception] Attribute"
type: concept
tags: [rust, embedded, cortex-m, attribute, runtime]
sources: [rust-embedded-book-start-exceptions]
last_updated: 2026-05-16
---

# `#[exception]` Attribute

The **declarative surface for [[ARMCortexM|Cortex-M]] exception handlers in Rust** — an attribute macro from [`cortex-m-rt-macros`](https://docs.rs/cortex-m-rt-macros) (re-exported via [[CortexMRTCrate|`cortex-m-rt`]]) that marks an ordinary `fn` as the handler for a specific named architectural exception ([[SysTick]], [[HardFault]], `NMI`, `MemoryManagement`, `BusFault`, `UsageFault`, `SVCall`, `DebugMonitor`, `PendSV`) or as the catch-all [[DefaultHandler]] ([[rust-embedded-book-start-exceptions]]).

```rust,ignore
use cortex_m_rt::exception;

#[exception]
fn SysTick() {
    static mut COUNT: u32 = 0;
    *COUNT += 1;
}
```

## Two non-obvious guarantees

The attribute is more than a registration shim — it enforces two safety-relevant properties:

1. **Software-uncallable**. A function tagged `#[exception]` **cannot be called from regular Rust code** — `SysTick();` is a compile error. The handler is reachable only through the hardware's exception-dispatch path via the [[VectorTable|vector table]].
2. **`static mut` inside the body is *safe***. The attribute rewrites every `static mut X: T = …;` declared in the body into a `&mut T` binding of the same name, ergonomically as if wrapped in `unsafe`. Soundness rests on the prior guarantee: because the handler is hardware-only and the hardware will not concurrently re-enter the same handler **on a single core**, the `&mut` is unique by construction. (On multicore, this invariant breaks and explicit synchronization is required — [[rust-embedded-book-start-exceptions]].)

This is the same recipe the [[rust-embedded-book-start-panicking|Panicking chapter]] uses for [[PanicHandlerAttribute|`#[panic_handler]`]] — a `cortex-m-rt` attribute macro that wires a user function into a runtime-essential slot while encoding soundness obligations the user cannot violate.

## Two argument shapes

- Standard handlers: zero arguments — `fn SysTick() { … }`.
- [[DefaultHandler]]: takes `irqn: i16` — negative ⇒ Cortex-M architectural exception number, non-negative ⇒ device-specific [[Interrupt|IRQ]] number.
- [[HardFault]]: forced `fn(&ExceptionFrame) -> !` — must diverge; receives the register snapshot the runtime pushed in `HardFaultTrampoline`.

## Connections

- [[CortexMRTCrate]] — supplies the macro and populates `.vector_table` slots with user-tagged functions (or `DefaultHandler_` stubs otherwise).
- [[VectorTable]] — the data structure `#[exception]` ultimately writes into.
- [[DefaultHandler]] — the special name `#[exception]` recognizes for the catch-all.
- [[HardFault]] — the special name with the forced divergent `ExceptionFrame` signature.
- [[ExceptionFrame]] — the diagnostic struct passed to `HardFault`.
- [[SysTick]] — the canonical example exception handled by `#[exception]`.
- [[Interrupt]] — exceptions and interrupts share the dispatch path; `irqn: i16` discriminates which is being serviced.
- [[PanicHandlerAttribute]] — sibling attribute macro with an analogous "wire a user function into the runtime, encode a soundness invariant" design.
- [[ARMCortexM]] — defines the exception set the attribute's recognized names enumerate.
- [[TheEmbeddedRustBook]] — full chapter dedicated to this attribute at [[rust-embedded-book-start-exceptions]].
