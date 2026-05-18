---
title: "Homebrew"
type: entity
tags: [package-manager, macos, tooling, open-source]
sources: [rust-embedded-book-intro-install-macos]
last_updated: 2026-05-16
---

# Homebrew

The de-facto community package manager for macOS (also supported on Linux as Linuxbrew). Provides `brew install <formula>` to fetch + build + symlink user-space binaries into `/opt/homebrew` (Apple Silicon) or `/usr/local` (Intel) without `sudo`. Hosted at <https://brew.sh>.

In *[[TheEmbeddedRustBook]]* ([[rust-embedded-book-intro-install-macos]]) Homebrew is one of two macOS install paths for the embedded toolchain — `brew install arm-none-eabi-gdb` + `brew install openocd` + `brew install qemu` — alongside the [[MacPorts]] alternative. A `brew install --HEAD openocd` variant is documented as a workaround for crashes in the released [[OpenOCD]] formula.

## Connections

- [[MacPorts]] — alternative macOS package manager; sibling install path in [[rust-embedded-book-intro-install-macos]].
- [[GDB]] / [[OpenOCD]] / [[QEMU]] — the three Embedded-Rust toolchain binaries installable via `brew install`.
- [[TheEmbeddedRustBook]] — listed in the macOS install sub-chapter ([[rust-embedded-book-intro-install-macos]]).
