---
title: "The Embedded Rust Book — Installation (macOS)"
type: source
tags: [rust, embedded, book-chapter, installation, macos]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/install/macos.md
---

# The Embedded Rust Book — Installation (macOS)

## Summary

File 7 of 44 of *[[TheEmbeddedRustBook|The Embedded Rust Book]]* — the **macOS-specific** install sub-page, sibling to [[rust-embedded-book-intro-install-linux|Linux]] off the OS-agnostic [[rust-embedded-book-intro-install|install manifest]]. The shortest of the three OS branches: the three native binaries — [[GDB|`arm-none-eabi-gdb`]], [[OpenOCD]], and [[QEMU]] — are installed through either [[Homebrew|Homebrew]] (`brew install …`) or [[MacPorts]] (`sudo port install …`). No udev / driver / signing dance is required on macOS. A single side-note covers an [[OpenOCD]] crash workaround via `brew install --HEAD openocd`.

## Key Claims

- **Two package managers, identical tool list.** All three binaries — [[GDB|`arm-none-eabi-gdb`]], [[OpenOCD]], [[QEMU]] — are available through either [[Homebrew|Homebrew]] or [[MacPorts]]. The chapter is neutral on choice.
- **Homebrew formulae.** `brew install arm-none-eabi-gdb`, `brew install openocd`, `brew install qemu`.
- **MacPorts ports.** `sudo port install arm-none-eabi-gcc` (note: the *gcc* port, which carries the full ARM bare-metal toolchain including `gdb`), `sudo port install openocd`, `sudo port install qemu`.
- **OpenOCD crash workaround.** If the released [[OpenOCD]] formula crashes, install the development tip with `brew install --HEAD openocd`.
- **No probe-driver work on macOS.** Unlike [[rust-embedded-book-intro-install-linux|Linux]] (which requires a [[UdevRules|udev rule]] for [[STLink|ST-LINK]] ACLs), macOS exposes USB devices to the logged-in user by default — the chapter mentions nothing about driver setup or permissions.

## Key Quotes

> "All the tools can be installed using Homebrew or MacPorts."

> "If OpenOCD crashes you may need to install the latest version using: `brew install --HEAD openocd`."

## Connections

- [[TheEmbeddedRustBook]] — file 7/44; the macOS branch of the OS-specific install split.
- [[rust-embedded-book-intro-install]] — the OS-agnostic parent install chapter that branches here.
- [[rust-embedded-book-intro-install-linux]] — sibling OS branch; Linux is the only one needing per-distro tool naming + a udev rule.
- [[Homebrew]] — the primary macOS package manager used here; `brew install` covers all three tools.
- [[MacPorts]] — alternative macOS package manager; `sudo port install` covers all three (note `arm-none-eabi-gcc` port name).
- [[GDB]] — installed via `brew install arm-none-eabi-gdb` or the MacPorts `arm-none-eabi-gcc` port.
- [[OpenOCD]] — installed via `brew install openocd`; `--HEAD` variant for crash workaround.
- [[QEMU]] — installed via `brew install qemu`.

## Contradictions

- None. Strictly additive — macOS-side operationalization of the OS-agnostic [[rust-embedded-book-intro-install]] manifest. Tool list matches [[rust-embedded-book-intro-tooling]]. Quieter than the [[rust-embedded-book-intro-install-linux|Linux branch]]: no udev / ACL / group-membership step because macOS grants the seat user USB access by default.
