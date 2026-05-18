---
title: "The Embedded Rust Book — Tooling"
type: source
tags: [rust, embedded, book-chapter, tooling]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/tooling.md
---

# The Embedded Rust Book — Tooling

## Summary

Chapter 4 (file 4/44) of *[[TheEmbeddedRustBook|The Embedded Rust Book]]* — the toolchain inventory. Two halves stitched together: a *build-side* list ([[RustLanguage|Rust]] 1.31+ with [[ARMCortexM|ARM Cortex-M]] target support, [[CargoBinutils|`cargo-binutils`]] for LLVM `objdump` / `nm` / `size`, [[QEMU|`qemu-system-arm`]] for full-system ARM emulation on the host, [[OpenOCD]] ≥ 0.8 for [[OnChipDebugging|on-chip debugging]], [[GDB]] ≥ 7.12 with ARM support, [[CargoGenerate|`cargo-generate`]] *or* `git` for template instantiation) and a *debug-side* survey of the embedded-Rust debugging ecosystem ([[ProbeRs|Probe-rs]] as the modern Rust-native alternative to [[OpenOCD]]; debuggers [[GDB]] / [[ProbeRsVSCodeExtension|Probe-rs VS Code extension]] / [[TRACE32]]; hardware probes [[RustyProbe|Rusty-probe]] / [[STLink|ST-Link]] / [[JLink|J-Link]] / [[MCULink|MCU-Link]] over [[JTAG]] / [[SWD]]). Establishes the operational stack every later chapter assumes — host runs Cargo + GDB + OpenOCD/Probe-rs, target hardware is reached through an [[STLink|ST-LINK]]-class probe over [[SWD]] / [[JTAG]].

## Key Claims

- **Two-layer toolchain.** Build-side = `rustc` + `cargo` + LLVM (via [[Rustup|`rustup`]] target install + [[CargoBinutils|`cargo-binutils`]]). Debug-side = a debugger ([[GDB]] / [[ProbeRsVSCodeExtension|Probe-rs VSC ext]] / [[TRACE32]]) talking *through* a server ([[OpenOCD]] / [[ProbeRs|Probe-rs]]) to a hardware probe ([[STLink|ST-Link]] / [[JLink|J-Link]] / [[MCULink|MCU-Link]] / [[RustyProbe|Rusty-probe]]) over [[SWD]] or [[JTAG]]. Every later chapter sits on this exact stack.
- **Minimum versions:** Rust 1.31 / 1.31-beta or newer **plus** ARM Cortex-M target support; [[CargoBinutils|`cargo-binutils`]] ≈ 0.1.4; [[QEMU|`qemu-system-arm`]] tested 3.0.0; [[OpenOCD]] ≥ 0.8 (tested 0.9.0 / 0.10.0); [[GDB]] ≥ 7.10 (≥ 7.12 highly recommended; tested through 8.1). Cargo and rustc come bundled with [[Rustup]] so are not separately versioned in the list.
- **[[CargoBinutils|`cargo-binutils`]] wraps LLVM tools shipped with the Rust toolchain** — LLVM `objdump`, `nm`, `size`. Two advantages over GNU binutils: (a) one-command cross-OS install via `rustup component add llvm-tools`; (b) every tool supports every architecture [[Rustc|`rustc`]] supports — ARM, x86_64, RISC-V, … — because they share the LLVM backend. This is the *binary-inspection* path on every platform [[TheEmbeddedRustBook]] supports.
- **[[CargoGenerate|`cargo-generate`]] OR `git`** (and `curl` / `wget` / browser as fallbacks). [[BareMetalProgramming|Bare-metal]] [[NoStd|`no_std`]] programs need extra plumbing — linker scripts, linker flags, memory layout — so the book packages it in a template. `cargo-generate` is a Cargo subcommand that instantiates Cargo projects from such templates; `git clone` of the template repo is the manual equivalent.
- **[[QEMU|`qemu-system-arm`]] = full-system ARM emulator on the host.** Enables following parts of the book without owning the [[STM32F3DISCOVERY|F3 hardware]]. Distinct from QEMU's user-mode emulation; this is the full-machine variant.
- **[[OnChipDebugging|On-chip debugging]] requires three software layers + hardware:**
  1. Probe driver / server — [[ProbeRs|Probe-rs]] or [[OpenOCD]] — speaks to the probe over USB and exposes a remote-debug protocol (e.g. GDB Remote Serial Protocol) to a higher-level debugger.
  2. Debugger — [[GDB]] / [[ProbeRsVSCodeExtension|Probe-rs VS Code extension]] / [[TRACE32]] — drives breakpoints, watchpoints, register reads, single-stepping.
  3. Hardware probe — [[STLink|ST-Link]] / [[JLink|J-Link]] / [[MCULink|MCU-Link]] / [[RustyProbe|Rusty-probe]] — bridges USB ↔ [[JTAG]] / [[SWD]] on the target MCU.
- **What a debugger does — book's own canonical list:** interact with [[MemoryMappedIO|memory-mapped registers]]; set breakpoints / watchpoints; read & write memory; detect MCU halt-on-debug-event; resume execution; erase + write target [[FlashMemory|FLASH]]. This is the *operational contract* every embedded debugger must implement.
- **[[ProbeRs|Probe-rs]] vs [[OpenOCD]].** Both are server-side; [[OpenOCD]] is the established open-source standard ([[JTAG]] + [[SWD]], integrates with [[GDB]], huge community, complex config); [[ProbeRs|Probe-rs]] is the modern Rust-native alternative — simpler config, integrates with Rust tooling, ships its own VS Code extension. Trade-off: maturity / target coverage (OpenOCD) vs Rust-ergonomics (Probe-rs).
- **Probe survey:**
  - **[[STLink|ST-Link]]** — STMicro's probe; default for STM32 / STM8 boards; the [[STM32F3DISCOVERY|F3 board]] ships one on-board ([[rust-embedded-book-intro-hardware]]).
  - **[[JLink|J-Link]]** — SEGGER's probe; supports ARM + RISC-V + more; advanced features like unlimited flash breakpoints.
  - **[[MCULink|MCU-Link]]** — NXP's probe; ARM Cortex coverage; pairs with MCUXpresso IDE; budget-friendly.
  - **[[RustyProbe|Rusty-probe]]** — open-source USB probe designed for [[ProbeRs|probe-rs]].
- **[[TRACE32]]** — Lauterbach's professional debugger; ARM + RISC-V; uses standard ELF/DWARF debug info so it works with Rust binaries from conventional toolchains without custom support.

## Key Quotes

> "Dealing with microcontrollers involves using several different tools as we'll be dealing with an architecture different than your laptop's and we'll have to run and debug programs on a *remote* device." — the book's framing of why the toolchain inventory exists: the target is *not* the host.

> "The advantage of using these tools over GNU binutils is that (a) installing the LLVM tools is the same one-command installation (`rustup component add llvm-tools`) regardless of your OS and (b) tools like `objdump` support all the architectures that `rustc` supports — from ARM to x86_64 — because they both share the same LLVM backend." — the operational pitch for [[CargoBinutils|`cargo-binutils`]] over the GNU tradition.

> "We use QEMU to run embedded programs on the host. Thanks to this you can follow some parts of this book even if you don't have any hardware with you!" — the no-hardware escape hatch the book gives the reader.

> Debuggers know how to: "Interact with the memory mapped registers. Set Breakpoints/Watchpoints. Read and write to the memory mapped registers. Detect when the MCU has been halted for a debug event. Continue MCU execution after a debug event has been encountered. Erase and write to the microcontroller's FLASH." — the canonical capability list for an embedded debugger.

## Connections

- [[TheEmbeddedRustBook]] — chapter 4 (file 4/44) — the toolchain inventory.
- [[RustLanguage]] — version 1.31+ with ARM Cortex-M target is the build-side floor.
- [[Cargo]] — Rust's build system; carries the subcommands [[CargoBinutils|`cargo-binutils`]] and [[CargoGenerate|`cargo-generate`]] plug into (new entity).
- [[Rustc]] — Rust compiler; LLVM-backed multi-target codegen is why [[CargoBinutils|`cargo-binutils`]] tools cover every architecture (new entity).
- [[Rustup]] — Rust toolchain installer / multiplexer; provides `rustup target add` and `rustup component add llvm-tools` (new entity).
- [[CargoBinutils]] — Cargo wrapper around LLVM `objdump` / `nm` / `size` (new entity).
- [[CargoGenerate]] — Cargo subcommand for instantiating projects from templates (new entity).
- [[QEMU]] — full-system ARM emulator the book uses to run firmware on the host (new entity).
- [[OpenOCD]] — open-source on-chip debug server bridging probes ↔ [[GDB]] (new entity).
- [[GDB]] — GNU Debugger; the canonical front-end for embedded-Rust debugging via OpenOCD or Probe-rs (new entity).
- [[ProbeRs]] — modern Rust-native alternative to [[OpenOCD]] (new entity).
- [[ProbeRsVSCodeExtension]] — VS Code debugger UI on top of [[ProbeRs]] (new entity).
- [[TRACE32]] — Lauterbach's professional multi-arch debugger (new entity).
- [[Lauterbach]] — vendor behind [[TRACE32]] (new entity).
- [[RustyProbe]] — open-source USB probe for [[ProbeRs]] (new entity).
- [[STLink]] — STMicro probe; already on the [[STM32F3DISCOVERY]] board.
- [[JLink]] — SEGGER probe (new entity).
- [[Segger]] — vendor behind [[JLink]] (new entity).
- [[MCULink]] — NXP probe (new entity).
- [[NXP]] — vendor behind [[MCULink]] (new entity).
- [[OnChipDebugging]] — the umbrella concept the debug-side stack implements (new concept).
- [[JTAG]] — wireline debug protocol (new concept).
- [[SWD]] — STMicro's two-wire debug protocol (new concept).
- [[RustTarget]] — `rustup target add` target triple model (new concept).
- [[CrossCompilation]] — the build-side regime this toolchain implements.
- [[BareMetalProgramming]] / [[NoStd]] — the linker-script + memory-layout reason templates ([[CargoGenerate]]) exist.
- [[FlashMemory]] / [[SRAM]] — what the debugger erases / inspects on the target.
- [[STM32F3DISCOVERY]] — the reference target board; ships an on-board [[STLink|ST-LINK]] used by this stack.

## Contradictions

- None. Chapter is a toolchain inventory — strictly additive to the corpus; introduces no claims that overlap with existing wiki content. Re-anchors the [[STLink|ST-LINK]] page (already present from chapter 2) into a wider probe-vendor / debug-server context.

## Notes for the Embedded Rust corpus

- **File 4 of 44.** Last *administrative* chapter of the introduction — the next file (installation.md) operationalizes everything listed here. The chapter has a noticeable seam: the first half ("Rust 1.31 / `cargo-binutils` / `qemu-system-arm` / OpenOCD / GDB / `cargo-generate`") is the *build-and-run* inventory from the original book; the second half ("Tooling for Embedded Rust Debugging") is a later append covering [[ProbeRs|Probe-rs]] / [[TRACE32]] / probe-vendor survey — the heading promotes back to H1 and the prose style shifts. Worth keeping in mind when re-reading.
- **Probe-rs vs OpenOCD framing** is the live debate of the embedded-Rust ecosystem. The book covers OpenOCD in the body but flags Probe-rs as the modern alternative — track which one later chapters actually use in code paths (`memory.md`, `flashing.md` likely).
- **Semihosting** is *not* introduced here despite being toolchain-adjacent; it's deferred to later chapters (`semihosting.md`). Flagging so the next ingest can promote it cleanly.
- **`rustup target add` mechanism** — already mentioned in [[CrossCompilation]] from [[rust-embedded-book-intro-index]] — is the operational bridge between [[Rustup]] and [[RustTarget]]. The latter is the new concept added here that names the *target triple* abstraction itself (e.g. `thumbv7em-none-eabihf`).
- Versions listed are 2018-era (GDB 8.1 max-tested, QEMU 3.0.0, OpenOCD 0.10.0) — consistent with the [[Rust2018Edition]] anchor; modern versions (GDB 14+, QEMU 9+, OpenOCD 0.12+) are not addressed. Could matter if the user follows along on a current toolchain.
