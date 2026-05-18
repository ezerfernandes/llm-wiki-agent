---
title: "The Embedded Rust Book — Installation"
type: source
tags: [rust, embedded, book-chapter, tooling, installation]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/install.md
---

# The Embedded Rust Book — Installation

## Summary

Chapter 5 (file 5/44) of *[[TheEmbeddedRustBook|The Embedded Rust Book]]* — a short pointer chapter laying down the **OS-agnostic** installation steps before branching into per-OS sub-pages (Linux / Windows / macOS, files 6–9). Three operational moves: (1) install [[Rustup|`rustup`]] from https://rustup.rs and ensure [[Rustc|`rustc`]] ≥ 1.31; (2) `rustup target add` the right [[ARMCortexM|ARM Cortex-M]] [[RustTarget|target triple]] for your hardware (the book's [[STM32F3DISCOVERY|F3 board]] needs `thumbv7em-none-eabihf`); (3) `cargo install` the host-side subcommands [[CargoBinutils|`cargo-binutils`]] (plus `rustup component add llvm-tools`) and [[CargoGenerate|`cargo-generate`]]. Caveats: Windows needs the Visual Studio 2019 C++ Build Tools; some Linuxes need `libssl-dev` + `pkg-config` for `cargo-generate`. This is the chapter that operationalizes the [[CrossCompilation|cross-compilation]] story from the prior tooling chapter into actual shell commands.

## Key Claims

- **Three OS-agnostic install moves.** (1) [[Rustup|`rustup`]] from https://rustup.rs; (2) `rustup target add <triple>` for the right [[ARMCortexM|Cortex-M]] [[RustTarget|target]]; (3) `cargo install cargo-binutils` + `rustup component add llvm-tools`, then `cargo install cargo-generate`. Everything else is OS-specific and lives in the next chapters.
- **[[Rustc|`rustc`]] ≥ 1.31 is the floor.** Verify via `rustc -V`. Consistent with the version floor stated in the tooling chapter ([[rust-embedded-book-intro-tooling]]).
- **Default install is host-native only.** [[CrossCompilation|Cross-compilation]] support is *opt-in* via `rustup target add`. The book justifies this on bandwidth / disk grounds — you only download the std-less core for the architectures you need.
- **Target triple is hardware-determined.** The book's [[STM32F3DISCOVERY|STM32F3DISCOVERY]] uses [[ARMCortexM|Cortex-M4F]] with hardware FP → `thumbv7em-none-eabihf`. Seven Cortex-M target triples are enumerated:
  - `thumbv6m-none-eabi` — Cortex-M0, M0+, M1 (ARMv6-M).
  - `thumbv7m-none-eabi` — Cortex-M3 (ARMv7-M).
  - `thumbv7em-none-eabi` — Cortex-M4, M7 *without* hardware FP (ARMv7E-M).
  - `thumbv7em-none-eabihf` — Cortex-M4F, M7F *with* hardware FP (ARMv7E-M). **F3 board uses this.**
  - `thumbv8m.base-none-eabi` — Cortex-M23 (ARMv8-M).
  - `thumbv8m.main-none-eabi` — Cortex-M33, M35P (ARMv8-M).
  - `thumbv8m.main-none-eabihf` — Cortex-M33F, M35PF with hardware FP (ARMv8-M).
- **[[CargoBinutils|`cargo-binutils`]] requires `llvm-tools` component.** Install via `cargo install cargo-binutils` + `rustup component add llvm-tools` — the LLVM tools are the actual binaries `cargo-binutils` wraps.
- **Windows prerequisite for `cargo-binutils`:** Visual Studio 2019 **C++ Build Tools**.
- **Linux prerequisite for `cargo-generate`:** on some distros (Ubuntu cited) install `libssl-dev` + `pkg-config` *before* `cargo install cargo-generate` — the build links against system OpenSSL.
- **OS-specific tail.** Linux / Windows / macOS each get a dedicated sub-page (files 6 / 7 / 8 of the 44-file corpus); files 9 is the verification chapter. This chapter is the manifest of what those pages share.

## Key Quotes

> "Install rustup by following the instructions at https://rustup.rs."

> "For bandwidth and disk usage concerns the default installation only supports native compilation. To add cross compilation support for the ARM Cortex-M architectures choose one of the following compilation targets. For the STM32F3DISCOVERY board used for the examples in this book, use the `thumbv7em-none-eabihf` target."

> "WINDOWS: prerequisite C++ Build Tools for Visual Studio 2019 is installed." — Windows-only caveat for `cargo-binutils`.

> "Note: on some Linux distros (e.g. Ubuntu) you may need to install the packages `libssl-dev` and `pkg-config` prior to installing cargo-generate."

## Connections

- [[TheEmbeddedRustBook]] — chapter 5 (file 5/44); the OS-agnostic install manifest before the per-OS sub-pages.
- [[rust-embedded-book-intro-tooling]] — the immediately prior chapter; this chapter operationalizes its tool inventory into shell commands.
- [[Rustup]] — the entry point; the chapter's first instruction.
- [[Rustc]] — version floor ≥ 1.31, verified via `rustc -V`.
- [[Cargo]] — carries `cargo install` and the subcommands `cargo-binutils` / `cargo-generate`.
- [[CargoBinutils]] — install line is `cargo install cargo-binutils` + `rustup component add llvm-tools`.
- [[CargoGenerate]] — install line is `cargo install cargo-generate`; on Linux may need `libssl-dev` + `pkg-config`.
- [[CrossCompilation]] — the *reason* this chapter exists: `rustup target add <triple>` is the operational switch.
- [[RustTarget]] — enumerates seven Cortex-M target triples and the mapping board → triple.
- [[ARMCortexM]] — the architecture family every triple in the list targets.
- [[STM32F3DISCOVERY]] — the book's reference board → `thumbv7em-none-eabihf`.
- [[STMicroelectronics]] — vendor of the F3 board.

## Contradictions

- None. Consistent with [[rust-embedded-book-intro-tooling]] on version floors (rustc 1.31), tool list, and the build-side / debug-side split. This chapter only adds the *how-to-install* layer.
