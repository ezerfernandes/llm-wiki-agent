---
title: "panic-itm"
type: entity
tags: [rust, embedded, crate, panic-handler, itm, debugging, no-std, cortex-m]
sources: [rust-embedded-book-start-panicking]
last_updated: 2026-05-16
---

# panic-itm

**Rust crate providing a [[PanicHandlerAttribute|`#[panic_handler]`]] that logs the panic message via the ITM** (Instrumentation Trace Macrocell) — an [[ARMCortexM|ARM Cortex-M]]-specific debug peripheral that streams trace data out the SWO pin (single-wire output) or the on-chip ETM. One of the four pre-packaged panic-handler crates surveyed by [[rust-embedded-book-start-panicking|chapter 15 of *The Embedded Rust Book*]].

```rust
use panic_itm as _;
```

## When to pick it

`panic-itm` is the **right choice on real hardware when [[ARMSemihosting|semihosting]] is too slow** (semihosting writes cost several milliseconds each — [[rust-embedded-book-start-semihosting]]). ITM trace output is hardware-formatted and DMA-streamed; an attached debug probe ([[STLink]], [[JLink]]) decodes the SWO line and forwards the panic text to the host without trapping the CPU.

The cost is platform-specificity: ITM exists on most Cortex-M3/M4/M7 cores but is **absent** on Cortex-M0/M0+, and the SWO pin requires correct probe wiring and pin-mux configuration. Where ITM is not available, [[PanicSemihostingCrate|`panic-semihosting`]] (slow but universal under a debug session) or [[PanicProbeCrate|`panic-probe`]] (RTT-based, no SWO required) are the alternatives.

## Connections

- [[PanicHandlerAttribute]] — the attribute the crate implements.
- [[PanicInfo]] — the struct the crate formats onto the ITM channel.
- [[ARMCortexM]] — the ITM peripheral is Cortex-M-specific.
- [[NoStd]] — the regime that requires an explicit panic handler.
- [[PanicHaltCrate]] / [[PanicAbortCrate]] — the silent siblings (no logging).
- [[PanicSemihostingCrate]] — the alternative logging sibling using [[ARMSemihosting|semihosting]] instead of ITM; slower but does not require an SWO pin.
- [[PanicProbeCrate]] — the modern alternative using `defmt` over RTT (no SWO required).
- [[STLink]] / [[JLink]] — debug probes that decode the SWO trace channel.
- [[TheEmbeddedRustBook]] — surveyed in [[rust-embedded-book-start-panicking]].
