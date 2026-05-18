---
title: "ARM Semihosting"
type: concept
tags: [arm, embedded, debugging, host-io]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# ARM Semihosting

**Convention by which firmware running on an [[ARMCortexM|ARM]] target requests services — `printf`, `fopen`, `read`, `exit` — from the host machine** through a debugger or emulator. The firmware sets up arguments in registers, executes the magic instruction (`BKPT 0xAB` on Cortex-M, `SVC 0x123456` on classic A-profile), and the debug agent on the host intercepts the trap, performs the syscall against the host OS, and resumes the firmware.

*[[TheEmbeddedRustBook]]*'s first code chapter ([[rust-embedded-book-start-qemu]]) uses semihosting as the **no-debug-session host-IO path** for [[QEMU]]:

- `-semihosting-config enable=on,target=native` on the `qemu-system-arm` command line activates QEMU's semihosting handler — *"Semihosting lets the emulated device, among other things, use the host stdout, stderr and stdin and create files on the host."*
- The [[CortexMSemihostingCrate|`cortex-m-semihosting`]] crate exposes Rust-level `hprintln!` + `debug::exit(EXIT_SUCCESS)` macros over this mechanism.
- The chapter swaps [[Defmt|`defmt`]]'s default `defmt-rtt` transport for `defmt-semihosting` for the same reason: *"When using real hardware this requires a debug session but when using QEMU this Just Works."*

## Tradeoffs

- **Pro on emulators**: zero-extra-setup host stdout/stderr/stdin — QEMU is the only "debugger" needed.
- **Con on real hardware**: every semihosting call traps the CPU and round-trips through the [[OnChipDebugging|debug probe]], making host-IO **extremely slow**. Production firmware uses RTT (Real-Time Transfer) or memory-mapped log buffers instead.
- **Requires either a debug session ([[GDB]] + [[OpenOCD]] / [[ProbeRs]]) or an emulator** with semihosting enabled — semihosting calls on a target without a host attached deadlock the CPU.

## Connections

- [[CortexMSemihostingCrate]] — the Rust crate wrapping the mechanism.
- [[QEMU]] — provides built-in semihosting; the book's chapter-11 host-IO path.
- [[GDB]] — on real hardware, GDB sessions (via [[OpenOCD]] / [[ProbeRs]]) route semihosting calls to the developer's terminal.
- [[Defmt]] — `defmt-semihosting` rides this same mechanism.
- [[ARMCortexM]] — the ISA-level mechanism (`BKPT 0xAB`).
- [[OnChipDebugging]] — the debug-probe stack semihosting routes through on real hardware.
- [[TheEmbeddedRustBook]] — operationalized in [[rust-embedded-book-start-qemu]] for both `hprintln!` and `debug::exit`.
