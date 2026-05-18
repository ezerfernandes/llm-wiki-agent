---
title: "cortex-m-semihosting"
type: entity
tags: [rust, embedded, crate, semihosting, debugging, cortex-m]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# cortex-m-semihosting

**Rust crate exposing the [[ARMSemihosting|ARM semihosting]] interface to [[ARMCortexM|Cortex-M]] firmware.** The user-facing macro is `hprintln!` (the `host print` analogue of `println!`); the canonical debug-exit call is `debug::exit(debug::EXIT_SUCCESS)` — both invoke the `BKPT 0xAB` semihosting trap routed by the debugger ([[GDB]]) or emulator ([[QEMU]] with `-semihosting-config enable=on`) to host stdout / a clean process exit.

Surfaces in *[[TheEmbeddedRustBook]]*'s first code example ([[rust-embedded-book-start-qemu]]) inside the GDB debug session: the `hello` example source reads

```rust
use cortex_m_semihosting::{debug, hprintln};

#[entry]
fn main() -> ! {
    hprintln!("Hello, world!").unwrap();
    // exit QEMU
    debug::exit(debug::EXIT_SUCCESS);
    loop {}
}
```

— and stepping past `hprintln!` causes "Hello, world!" to appear in the QEMU terminal; stepping past `debug::exit` ends the QEMU process with exit code 0.

## Caveat — overhead

[[ARMSemihosting|Semihosting]] traps the CPU on each character, making `hprintln!` **extremely slow** on real hardware. Production logging stacks (RTT-based, [[Defmt|`defmt`]], etc.) are several orders of magnitude faster. `cortex-m-semihosting` is best understood as a **debug-time-only** facility — perfect for QEMU-driven first contact, marginal on a physical board under timing constraints.

## Connections

- [[ARMSemihosting]] — the host-firmware bridge the crate wraps.
- [[CortexMRTCrate]] — provides the `#[entry]` runtime inside which semihosting calls live.
- [[QEMU]] — the emulator path where `cortex-m-semihosting` "just works" without a real debugger.
- [[GDB]] — on real hardware, semihosting routes through the GDB session over [[OnChipDebugging|on-chip debugging]].
- [[ARMCortexM]] — the ISA whose `BKPT 0xAB` instruction is the semihosting entry point.
- [[Defmt]] — the modern alternative; `cortex-m-semihosting` is the pre-`defmt` host-IO standard.
- [[TheEmbeddedRustBook]] — used in the `hello` example debugged via GDB+QEMU in [[rust-embedded-book-start-qemu]].
