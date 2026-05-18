---
title: "DefaultHandler (cortex-m-rt)"
type: concept
tags: [rust, embedded, cortex-m, exceptions, runtime, debugging]
sources: [rust-embedded-book-start-exceptions]
last_updated: 2026-05-16
---

# DefaultHandler

The **catch-all exception handler in [[CortexMRTCrate|`cortex-m-rt`]]** — the function that ends up in every [[VectorTable|vector-table]] slot the user did not explicitly override with [[ExceptionAttribute|`#[exception]`]]. Default body is an infinite loop; symbol is `#[no_mangle]` so a debugger can place a breakpoint on `"DefaultHandler"` and trap *any* unhandled exception ([[rust-embedded-book-start-exceptions]]):

```rust,ignore
fn DefaultHandler() {
    loop {}
}
```

## User override (with the IRQ discriminant)

Unlike a standard `#[exception]` handler (zero arguments, one specific exception), the `DefaultHandler` slot takes an extra `irqn: i16` parameter telling the user **which** exception is being serviced:

```rust,ignore
#[exception]
fn DefaultHandler(irqn: i16) {
    // custom catch-all
}
```

`irqn` semantics ([[rust-embedded-book-start-exceptions]]):

- **`irqn < 0`** — a [[ARMCortexM|Cortex-M]] **architectural exception** (negative numbering: e.g. `-14` = `NMI`, `-13` = `HardFault`, `-1` = `SysTick`).
- **`irqn >= 0`** — a **device-specific [[Interrupt|interrupt]]** (the IRQ number from the chip's NVIC).

This makes `DefaultHandler` the single point where a firmware can centralize logging / reset / `HardFault`-style post-mortem for everything it did not explicitly catch.

## Why the `#[no_mangle]` matters

The default body is `loop {}` precisely so that a debugger sees the program halted at a known symbol. Without `#[no_mangle]`, mangled Rust names would make breakpoint-by-name fragile across rebuilds; the runtime's choice ensures `b DefaultHandler` always works in [[GDB]] / [[OpenOCD]] / [[ProbeRs|probe-rs]] sessions.

## Connections

- [[CortexMRTCrate]] — supplier of the default function and the `#[exception]` macro that overrides it; ships `DefaultHandler_` stubs in every unfilled `.vector_table` slot.
- [[ExceptionAttribute]] — the attribute used to override the default.
- [[VectorTable]] — the data structure populated with `DefaultHandler_` references in unused slots.
- [[Interrupt]] — the device-specific exceptions selected by `irqn >= 0`.
- [[HardFault]] — a sibling exception that is **also** ultimately handled here unless explicitly overridden.
- [[ARMCortexM]] — defines the negative-numbering convention for architectural exceptions.
- [[TheEmbeddedRustBook]] — documents the override pattern at [[rust-embedded-book-start-exceptions]].
