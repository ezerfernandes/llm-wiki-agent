---
title: "SysTick"
type: concept
tags: [embedded, arm, cortex-m, peripheral, timer]
sources: [rust-embedded-book-start-registers, rust-embedded-book-start-exceptions]
last_updated: 2026-05-16
---

# SysTick

The **System Tick Timer** — a 24-bit countdown timer **standardized into the [[ARMCortexM|ARM Cortex-M]] core itself**, so it is present and identical on every Cortex-M MCU regardless of vendor. Defined by the ARM Cortex-M Technical Reference Manual; canonically used as the OS tick / scheduler interrupt source / coarse delay primitive.

Because SysTick is core-standardized, it is exposed by the **[[MicroArchitectureCrate|micro-arch crate]]** ([[CortexMCrate|`cortex-m`]]) rather than by any chip-specific [[PeripheralAccessCrate|PAC]]. Access pattern in the [[rust-embedded-book-start-registers|Registers chapter]]:

```rust
let peripherals = cortex_m::Peripherals::take().unwrap();
let mut systick = peripherals.SYST;
systick.set_clock_source(syst::SystClkSource::Core);
systick.set_reload(1_000);
systick.clear_current();
systick.enable_counter();
while !systick.has_wrapped() { /* spin */ }
```

The `Peripherals::take()` call is the **singleton gate**: it guarantees only one `SYST` struct exists in the entire program ([[rust-embedded-book-start-registers]]).

## Connections

- [[ARMCortexM]] — the processor-core family that standardizes SysTick.
- [[CortexMCrate]] — the micro-arch crate that exposes SysTick.
- [[MicroArchitectureCrate]] — the stack layer SysTick lives at (because it is core-not-chip).
- [[ExceptionAttribute]] — the [[CortexMRTCrate|`cortex-m-rt`]] attribute for installing a SysTick handler; the [[rust-embedded-book-start-exceptions|Exceptions chapter]]'s long worked example raises SysTick every second and counts ticks in a `static mut`.
