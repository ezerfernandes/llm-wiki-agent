---
title: "The Embedded Rust Book — Memory-mapped Registers"
type: source
tags: [rust, embedded, book-chapter, registers, peripherals]
date: 2026-05-16
source_file: raw/book/src/start/registers.md
last_updated: 2026-05-16
---

## Summary

File 13/44 of *[[TheEmbeddedRustBook]]* — the **Memory-mapped Registers** chapter of *Getting Started*, immediately after the hardware sub-section ([[rust-embedded-book-start-hardware]]). The pedagogical hinge from the toolchain / runtime / linker plumbing of the prior chapters into actual **peripheral access**. Builds the **four-layer crate stack** that the embedded-Rust ecosystem uses to wrap [[MemoryMappedIO|memory-mapped I/O]] in safe, zero-cost Rust abstractions, walks each layer with a worked example, and demonstrates the [[Svd2Rust|`svd2rust`]]-generated `read()` / `write()` / `modify()` closure idiom that replaces C's read-modify-write footgun.

## Key Claims

- **Four-layer crate stack** for peripheral access ([[ARMCortexM|Cortex-M]] ecosystem convention):
  1. **[[MicroArchitectureCrate|Micro-architecture crate]]** — common to every chip with this core. Example: [[CortexMCrate|`cortex-m`]] (interrupt enable/disable; [[SysTick]] peripheral; `Peripherals::take()`).
  2. **[[PeripheralAccessCrate|Peripheral Access Crate (PAC)]]** — thin wrapper over the part-number-specific [[MemoryMappedIO|MMIO]] register map. Examples: [[Tm4c123xCrate|`tm4c123x`]] (TI Tiva-C), `stm32f30x` (ST [[STM32F303VCT6|F30x]]). Auto-generated from the chip's [[SVDFile|SVD file]] by [[Svd2Rust|`svd2rust`]].
  3. **HAL crate** — implements [[EmbeddedHalCrate|`embedded-hal`]] traits (the portability layer); offers ergonomic abstractions (a `Serial` struct that takes pins + baud rate). Example: `tm4c123x-hal`.
  4. **Board crate** — pre-configures peripherals + GPIO for a specific dev board. Example: `stm32f3-discovery` for the [[STM32F3DISCOVERY]].
- **Recommended entry point depends on level**: board crate (beginner) → HAL (portable apps) → PAC (chip-specific bit-twiddling) → micro-arch (core-level routines). The book deliberately skips board crates to stay hardware-agnostic.
- **`Peripherals::take()` is the singleton gate**: a one-shot routine that guarantees only one `SYST` (or chip `Peripherals`) struct exists in the program — the type-system enforcement of single ownership over memory-mapped peripherals.
- **The `svd2rust` API is closure-based**, not numeric-argument-based. Three primitives on every register:
  - `reg.read()` returns an `R` struct with **read-only** typed sub-field accessors (e.g. `pwm.ctl.read().globalsync0().is_set()`).
  - `reg.write(|w| …)` takes a closure on a `W` struct; **all unset sub-fields revert to their default values** — the existing register contents are lost.
  - `reg.modify(|r, w| …)` takes a two-argument closure (read + write) that does atomic-from-source-perspective read-modify-write, eliminating the C wrong-variable footgun (`uint32_t temp = pwm0.ctl.read(); ... pwm0.enable.write(temp);`).
- **Sub-fields are `unsafe` when the SVD lacks value semantics**: if the SVD declares a register field as 32-bit without enumerating valid values, the generated `bits()` accessor is marked `unsafe`. Example: `pwm._2_load.write(|w| unsafe { w.load().bits(263) })`.
- **HAL crates use `constrain()` / `split()` to consume the PAC peripheral** and return a higher-level wrapper. The wrapper can require a borrowed `Clock` struct (constructible only by configuring the PLLs) — making it **statically impossible** to create a Serial port without first setting clock rates, or for the Serial port to miscompute the baud-rate divisor. **All with zero runtime cost.**
- **[[TypeStateProgramming|Type-state]] for GPIO pin states**: HAL crates can define distinct types per pin mode (Input / Output / Alternate Function), requiring the user to call `.into_af_push_pull::<AF1>()` *before* the pin can be passed into a peripheral constructor — compile-time enforcement of correct configuration order.
- **The compiler-checked closure API generates machine code "pretty close to hand-written assembler"** — zero-cost abstraction in the Rust sense.

## Key Quotes

> "While this looks like a lot of code, the Rust compiler can use it to perform a bunch of checks for us, but then generate machine-code which is pretty close to hand-written assembler!" — on the [[Svd2Rust|`svd2rust`]] closure idiom.

> "The `modify` function really shows the power of closures here. In C, we'd have to read into some temporary value, modify the correct bits and then write the value back. This means there's considerable scope for error" — chapter's framing of the C footgun (followed by a worked example of writing the wrong `temp` variable to the wrong register).

> "In this way, it is statically impossible to create a Serial port object without first having configured the clock rates, or for the Serial port object to misconvert the baud rate into clock ticks. […] All with no run-time cost!" — the [[TypeStateProgramming|type-state]] / [[HALCrate]] core thesis.

> "Note that we can't access our `SYST` struct until we have called `Peripherals::take()` - this is a special routine that guarantees that there is only one `SYST` structure in our entire program." — the singleton invariant.

## Connections

- [[TheEmbeddedRustBook]] — file 13/44; the chapter that finally introduces *peripheral access*.
- [[rust-embedded-book-start-hardware]] — predecessor chapter (file 12); set up [[OpenOCD]] + [[GDB]] + flashing. This chapter assumes a working hardware-debug loop.
- [[rust-embedded-book-start-qemu]] — predecessor chapter (file 11); introduced the `no_std` + `#[entry]` + `panic-halt` skeleton this chapter's code samples build on.
- [[MemoryMappedIO]] — the underlying hardware contract every example wraps.
- [[ARMCortexM]] — every example targets a Cortex-M core; the [[MicroArchitectureCrate|`cortex-m` crate]] is the chapter's entry layer.
- [[MicroArchitectureCrate]] — **layer 1** of the crate stack. New concept introduced here.
- [[PeripheralAccessCrate]] — **layer 2** of the crate stack. New concept introduced here.
- [[HALCrate]] — **layer 3** of the crate stack. New concept introduced here.
- [[BoardCrate]] — **layer 4** of the crate stack. New concept introduced here.
- [[SVDFile]] — CMSIS-SVD XML description of a chip's register map; the input to [[Svd2Rust|`svd2rust`]]. New concept introduced here.
- [[TypeStateProgramming]] — encoding state-machine transitions in the type system; the design pattern HAL crates use for GPIO pin modes. New concept introduced here.
- [[CortexMCrate]] — the [[MicroArchitectureCrate|micro-arch crate]] used in the chapter's first code sample. New entity introduced here.
- [[Svd2Rust]] — the auto-generator producing all [[PeripheralAccessCrate|PAC]] crates from [[SVDFile|SVD files]]. New entity introduced here.
- [[EmbeddedHalCrate]] — the portability trait crate that all [[HALCrate|HAL crates]] implement. New entity introduced here.
- [[Tm4c123xCrate]] — the chapter's worked [[PeripheralAccessCrate|PAC]] example for the TI Tiva-C TM4C123. New entity introduced here.
- [[SysTick]] — the Cortex-M-standardized system tick timer; the chapter's first peripheral example. New concept introduced here.
- [[CortexMRTCrate]] — reused from prior chapters; provides `#[entry]`.
- [[PanicHaltCrate]] — reused from prior chapters; the panic handler in all code samples.
- [[NoStd]] — reused; every code sample is `#![no_std]` + `#![no_main]`.
- [[STM32F303VCT6]] — the F3 board's MCU; the [`stm32f30x`] PAC family targets it.
- [[STM32F3DISCOVERY]] — the dev board; the `stm32f3-discovery` board-crate targets it.
- [[RustEmbeddedWorkingGroup]] — maintains the [[CortexMCrate|`cortex-m`]] / [[EmbeddedHalCrate|`embedded-hal`]] / [[Svd2Rust|`svd2rust`]] crates.

## Contradictions

None. Strictly additive — operationalizes the [[MemoryMappedIO]] page's claim that *"In Rust this is typically wrapped behind type-state peripheral access crates (`svd2rust`-generated PAC + HAL layers)"* into the concrete four-layer stack with worked examples. The Portability chapter (forward reference, not yet ingested) will expand on [[EmbeddedHalCrate|`embedded-hal`]].
