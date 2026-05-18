---
title: "cortex-m"
type: entity
tags: [rust, embedded, crate, arm, micro-architecture-crate]
sources: [rust-embedded-book-start-registers, rust-embedded-book-peripherals-singletons]
last_updated: 2026-05-16
---

# cortex-m

The canonical [[MicroArchitectureCrate|micro-architecture crate]] for the [[ARMCortexM|ARM Cortex-M]] family — `crates.io/crates/cortex-m`. Maintained by the [[RustEmbeddedWorkingGroup]]. Provides:

- Interrupt enable / disable primitives (the same instruction sequence on every Cortex-M).
- Access to **core-standardized peripherals** — most importantly [[SysTick]] (the 24-bit system-tick countdown timer baked into the Cortex-M core itself), plus NVIC / SCB / DWT / FPB / DCB / MPU control structs.
- The [[PeripheralsTake|`Peripherals::take()`]] [[Singleton|singleton]] gate that hands out the single `cortex_m::Peripherals` struct in the program; backed by the public `singleton!()` macro also usable for ad-hoc singletons ([[rust-embedded-book-peripherals-singletons]]).

Distinct from (and **below**) the chip-specific [[PeripheralAccessCrate|PAC]] in the four-layer crate stack ([[rust-embedded-book-start-registers]]).

Companion to [[CortexMRTCrate|`cortex-m-rt`]] (runtime / `#[entry]` macro / vector table) and [[CortexMSemihostingCrate|`cortex-m-semihosting`]] (host IO via [[ARMSemihosting]]) — the three `cortex-m-*` crates that anchor the embedded-Rust stack.

## Connections

- [[MicroArchitectureCrate]] — `cortex-m` is the canonical example of this stack layer.
- [[ARMCortexM]] — the processor-core family.
- [[SysTick]] — the headline peripheral exposed.
- [[RustEmbeddedWorkingGroup]] — maintains this crate.
- [[CortexMRTCrate]] — sibling crate (runtime).
- [[CortexMSemihostingCrate]] — sibling crate (host IO).
