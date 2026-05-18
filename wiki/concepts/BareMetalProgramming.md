---
title: "Bare-Metal Programming"
type: concept
tags: [embedded, systems-programming, no-os]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# Bare-Metal Programming

Programming model in which code runs **directly on hardware with no operating system** underneath — the firmware owns the CPU, memory, interrupt vectors, and peripherals. The execution model assumed by [[TheEmbeddedRustBook]] (the book's title literally describes it as "an introductory book about using the Rust Programming Language on 'Bare Metal' embedded systems"). Typical of small [[Microcontroller|microcontroller]] firmware. [[rust-embedded-book-intro-no-std]] formalizes the dichotomy with [[HostedEnvironment]] — bare metal means *"no code has been loaded before your program"*, so the [[RustStandardLibrary|standard library]] cannot be loaded.

Implications surfaced (some directly stated in [[rust-embedded-book-intro-no-std]], others in [[rust-embedded-book-intro-index]]'s prerequisites list):
- No standard library facilities that assume an OS — [[NoStd|`#![no_std]`]] is mandatory in [[RustLanguage|Rust]]; only [[RustCoreLibrary|`libcore`]] is available.
- No pre-`main` [[RustRuntime|runtime]] — stack-overflow protection, arg processing, main-thread spawn must be supplied manually (typically by a runtime crate like `cortex-m-rt`) or omitted.
- [[HeapAllocation|Heap]] is off by default; opt back in via the `alloc` crate + a global allocator.
- Direct [[MemoryMappedIO|memory-mapped I/O]] for peripheral access.
- Manual [[Interrupt|interrupt]] handler registration.
- Linker scripts and [[CrossCompilation|cross-compilation]] are part of the build flow.
- Enables *stage-0* code that **only** bare metal can run: [[Bootloader|bootloaders]], firmware, kernels ([[rust-embedded-book-intro-no-std]]).

## Connections

- [[EmbeddedSystems]] — the broader domain.
- [[HostedEnvironment]] — the complementary regime; mutually exclusive with bare metal.
- [[Microcontroller]] — typical hardware target.
- [[RustLanguage]] — Rust's `no_std` mode + ownership/borrow checker enables bare-metal work with safety guarantees.
- [[NoStd]] — the Rust language switch that selects this regime.
- [[RustCoreLibrary]] — the standard-library subset available on bare metal.
- [[RustRuntime]] — the pre-`main` init layer absent on bare metal.
- [[Bootloader]] — canonical bare-metal-only use case.
