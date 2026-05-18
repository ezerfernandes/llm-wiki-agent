---
title: "MacPorts"
type: entity
tags: [package-manager, macos, tooling, open-source]
sources: [rust-embedded-book-intro-install-macos]
last_updated: 2026-05-16
---

# MacPorts

Open-source package manager for macOS, an alternative to [[Homebrew]]. Installs into `/opt/local` and uses `sudo port install <port>` to fetch + build + install packages. Hosted at <https://www.macports.org/>.

In *[[TheEmbeddedRustBook]]* ([[rust-embedded-book-intro-install-macos]]) MacPorts is the second of two macOS install paths for the embedded toolchain — `sudo port install arm-none-eabi-gcc` (the GCC port carries `gdb` for ARM bare-metal) + `sudo port install openocd` + `sudo port install qemu`.

## Connections

- [[Homebrew]] — alternative macOS package manager; sibling install path in [[rust-embedded-book-intro-install-macos]].
- [[GDB]] / [[OpenOCD]] / [[QEMU]] — the three Embedded-Rust toolchain binaries installable via `sudo port install`.
- [[TheEmbeddedRustBook]] — listed in the macOS install sub-chapter ([[rust-embedded-book-intro-install-macos]]).
