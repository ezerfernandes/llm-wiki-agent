---
title: "Probe-rs Visual Studio Code Extension"
type: entity
tags: [vscode, debugger, rust, embedded, tooling]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# Probe-rs Visual Studio Code Extension

A Visual Studio Code extension layering an IDE-grade debugger UI on top of [[ProbeRs|Probe-rs]]. Provides breakpoints / variable inspection / step-through inside VS Code, with Rust-specific features like pretty printing and detailed error messages — *"a seamless debugging experience without extensive setup"* ([[rust-embedded-book-intro-tooling]]).

Effectively fills the same UX slot as [[GDB]] on the embedded-Rust debug stack, but with VS Code as the front-end instead of `gdb` on the command line.

## Connections

- [[ProbeRs]] — the underlying debug-server software the extension drives.
- [[GDB]] — the CLI alternative front-end.
- [[OnChipDebugging]] — the operating regime.
- [[TheEmbeddedRustBook]] — listed in the toolchain inventory ([[rust-embedded-book-intro-tooling]]).
