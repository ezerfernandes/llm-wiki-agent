---
title: "The Embedded Rust Book — Semihosting"
type: source
tags: [rust, embedded, book-chapter, semihosting, debugging]
date: 2026-05-16
source_file: raw/book/src/start/semihosting.md
last_updated: 2026-05-16
---

## Summary

File 14/44 of *[[TheEmbeddedRustBook]]* — the *Getting Started* chapter's **Semihosting** sub-section, immediately after Memory-mapped Registers ([[rust-embedded-book-start-registers]]). A compact operational chapter that introduces [[ARMSemihosting|semihosting]] as the book's first **debug-time host-IO mechanism**: `hprintln!` for logging, `debug::exit` for QEMU teardown, the OpenOCD `monitor arm semihosting enable` activation handshake, and the cross-cutting **"slow but zero-wire"** tradeoff. Closes with the `panic-semihosting` crate's `"exit"` feature as the recipe for `no_std` run-pass tests on QEMU.

## Key Claims

- **Semihosting requires only a debug session — no extra wires.** A firmware can do host stdout/stderr/stdin and file I/O purely by trapping into the attached debugger ([[GDB]] + [[OpenOCD]]) or emulator ([[QEMU]]). The user-facing convenience is enormous; the cost is per-call latency.
- **It is super slow on real hardware.** Each write op takes "several milliseconds depending on the hardware debugger (e.g. ST-Link) you use" — the book's first explicit caveat against using semihosting outside debug-time pedagogy.
- **The [[CortexMSemihostingCrate|`cortex-m-semihosting`]] crate is the Rust API.** Canonical "Hello, world!" uses `hprintln!("Hello, world!").unwrap()` inside a `#[entry]` function on the standard [[NoStd|`no_std`]] + `no_main` skeleton with [[PanicHaltCrate|`panic-halt`]].
- **Semihosting output appears in the OpenOCD console, not GDB.** On real hardware, `hprintln!` text shows up in the OpenOCD server window — semihosting is captured server-side, mirroring the observation from [[rust-embedded-book-start-hardware]].
- **OpenOCD requires an explicit enable from GDB**: `(gdb) monitor arm semihosting enable` → server replies `semihosting is enabled`. Without this, semihosting traps deadlock the CPU.
- **[[QEMU]] understands semihosting natively — no debug session needed.** Pass `-semihosting-config` flags (already wired into [[CortexMQuickstartTemplate|the template]]'s `.cargo/config.toml`) and `cargo run` blocks the terminal while QEMU runs the firmware; "Hello, world!" appears inline.
- **`debug::exit(EXIT_SUCCESS / EXIT_FAILURE)` is a semihosting operation that terminates the QEMU process** with the appropriate exit code. The book's worked example uses an `if roses == "red"` branch to demonstrate both exit codes (`echo $?` → `1` for the false branch).
- **CRITICAL: never call `debug::exit` on real hardware.** *"This function can corrupt your OpenOCD session and you will not be able to debug more programs until you restart it."* This re-states the warning from [[rust-embedded-book-start-hardware]]'s `examples/hello.rs` redaction.
- **`panic-semihosting` with the `"exit"` feature enables `no_std` run-pass tests on QEMU.** The crate logs the panic message to host stderr *then* invokes `exit(EXIT_FAILURE)` — turning a Rust `assert_eq!` failure on QEMU into a non-zero shell exit code consumable by `cargo test` / CI. Cargo dependency is `panic-semihosting = { version = "VERSION", features = ["exit"] }`.
- **The chapter does not name the underlying ISA trap.** Earlier pages ([[ARMSemihosting]] / [[CortexMSemihostingCrate]]) already document that the mechanism on Cortex-M is the `BKPT 0xAB` software breakpoint instruction; this chapter operates one layer above, at the `cortex-m-semihosting` crate API.

## Key Quotes

> "Semihosting is a mechanism that lets embedded devices do I/O on the host and is mainly used to log messages to the host console. Semihosting requires a debug session and pretty much nothing else (no extra wires!) so it's super convenient to use. The downside is that it's super slow: each write operation can take several milliseconds depending on the hardware debugger (e.g. ST-Link) you use." — the chapter's thesis paragraph.

> "You do need to enable semihosting in OpenOCD from GDB first: `(gdb) monitor arm semihosting enable` → `semihosting is enabled`" — the mandatory handshake on real hardware.

> "Important: do **not** use `debug::exit` on hardware; this function can corrupt your OpenOCD session and you will not be able to debug more programs until you restart it." — the chapter's most consequential operational warning.

> "One last tip: you can set the panicking behavior to `exit(EXIT_FAILURE)`. This will let you write `no_std` run-pass tests that you can run on QEMU." — the recipe for embedded-Rust CI via `panic-semihosting`.

## Connections

- [[TheEmbeddedRustBook]] — file 14/44; the Semihosting chapter.
- [[rust-embedded-book-start-registers]] — predecessor chapter (file 13); peripheral-access stack. This chapter is the operational pivot from "talking to hardware" to "talking to the host."
- [[rust-embedded-book-start-hardware]] — predecessor chapter (file 12); first introduced `monitor arm semihosting enable` and the `debug::exit` redaction. This chapter re-states and operationalizes both.
- [[rust-embedded-book-start-qemu]] — predecessor chapter (file 11); first introduced `hprintln!` and the QEMU `-semihosting-config` flag. This chapter is the canonical write-up.
- [[ARMSemihosting]] — the host-firmware bridge the chapter wraps in Rust; the underlying `BKPT 0xAB` trap is documented there.
- [[CortexMSemihostingCrate]] — the user-facing Rust API (`hprintln!` + `debug::exit`); already exists from chapter 11.
- [[PanicSemihostingCrate]] — the **new entity** introduced here; alternative panic handler that logs the panic via semihosting before optionally exiting QEMU.
- [[OpenOCD]] — the debug server; consumes `monitor arm semihosting enable` and prints semihosting output to its own console.
- [[GDB]] — the debugger driving OpenOCD; the source of the `monitor` command.
- [[QEMU]] — the emulator path where semihosting "just works" given `-semihosting-config enable=on`.
- [[CortexMRTCrate]] — provides the `#[entry]` runtime that hosts every code sample.
- [[PanicHaltCrate]] — the default panic handler in the first two code samples; swapped for `panic-semihosting` in the third.
- [[NoStd]] — every code sample is `#![no_std]` + `#![no_main]`.
- [[ARMCortexM]] — the target ISA; the `BKPT 0xAB` semihosting trap is Cortex-M-specific.
- [[Defmt]] / [[Knurling]] / [[FerrousSystems]] — the modern alternative ecosystem; the chapter implicitly motivates them by emphasizing semihosting's slowness.

## Contradictions

None. Strictly additive — consolidates the `hprintln!` / `debug::exit` / `monitor arm semihosting enable` fragments already scattered across [[rust-embedded-book-start-qemu]] and [[rust-embedded-book-start-hardware]] into a single canonical chapter, and adds the previously-unmentioned `panic-semihosting` crate ([[PanicSemihostingCrate]]) as the QEMU run-pass-test enabler. The "super slow on real hardware" caveat is consistent with the [[ARMSemihosting]] page's prior framing.
