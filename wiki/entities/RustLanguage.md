---
title: "Rust (Programming Language)"
type: entity
tags: [rust, language, systems-programming]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# Rust (Programming Language)

Systems programming language emphasizing memory safety, zero-cost abstractions, and concurrency-safety without a runtime garbage collector. The official *Rust Book* at `doc.rust-lang.org/book` is the canonical introduction. Editions are reference snapshots of language idioms; [[TheEmbeddedRustBook]] targets the [[Rust2018Edition|2018 edition]].

The language ships **two standard libraries**:
- [[RustStandardLibrary|`std`]] — the default; OS-abstraction layer + a pre-`main` [[RustRuntime|runtime]]. Used by every desktop Rust binary.
- [[RustCoreLibrary|`core`]] — platform-agnostic subset; no OS assumptions. Selected via the [[NoStd|`#![no_std]`]] crate attribute ([[rust-embedded-book-intro-no-std]]).

In embedded contexts, Rust's value is providing higher-level concepts (ownership, type-state APIs, trait-based abstraction) and compile-time safety guarantees *without* sacrificing the bare-metal control needed on [[Microcontroller|microcontrollers]] — see [[rust-embedded-book-intro-index]]. The `no_std` mode is what makes Rust usable for *stage-0* code — [[Bootloader|bootloaders]], firmware, kernels — that [[RustStandardLibrary|`std`]] structurally cannot target.

## Connections

- [[TheEmbeddedRustBook]] — the embedded-systems story for Rust.
- [[RustEmbeddedWorkingGroup]] — community working group that owns the embedded ecosystem.
- [[Rust2018Edition]] — the edition targeted by [[TheEmbeddedRustBook]].
- [[NoStd]] — the crate attribute that selects bare-metal mode.
- [[RustStandardLibrary]] / [[RustCoreLibrary]] — the two standard libraries.
- [[RustRuntime]] — the pre-`main` init layer that ships with `std`.
