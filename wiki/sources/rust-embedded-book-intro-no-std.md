---
title: "The Embedded Rust Book — `no_std`"
type: source
tags: [rust, embedded, book-chapter, no-std]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/no-std.md
---

# The Embedded Rust Book — `no_std`

## Summary

Chapter 3 (file 3/44) of *[[TheEmbeddedRustBook|The Embedded Rust Book]]* — the conceptual hinge of the introduction. Frames embedded programming as a spectrum from 8-bit MCUs (a few KB RAM/ROM) up to Linux-class SoCs (Raspberry Pi Cortex-A53 @ 1.4 GHz, 1 GB RAM) and splits it into two execution regimes: **[[HostedEnvironment|hosted environments]]** (POSIX-like; standard libraries on top of OS primitives) and **[[BareMetalProgramming|bare-metal environments]]** (no OS, no pre-loaded code, firmware owns the machine). Introduces the central language-level switch the rest of the book lives on — `#![no_std]` — which makes a [[RustLanguage|Rust]] crate link against [[RustCoreLibrary|libcore]] (the platform-agnostic subset) instead of [[RustStandardLibrary|libstd]] (which assumes an OS and ships its own [[RustRuntime|pre-main runtime]]). Spells out the consequences: no [[HeapAllocation|heap]] / no `Vec` / no stack-overflow protection / no init code before `main` — but you *can* now write [[Bootloader|bootloaders]], firmware, and kernels. Heap + collections can be re-enabled via the opt-in `alloc` / `collections` crates plus a user-supplied global allocator (e.g. [`alloc-cortex-m`](https://github.com/rust-embedded/alloc-cortex-m)).

## Key Claims

- **Embedded is a spectrum, not a point.** The book covers a wide range: from 8-bit MCUs (e.g. ST72325xx, a few KB RAM/ROM) to 4-core Cortex-A53 SoCs with 1 GB RAM (Raspberry Pi). Restrictions and idioms differ wildly across the range.
- **Two execution regimes:**
  - **[[HostedEnvironment|Hosted]]** — there is a system interface (e.g. POSIX) underneath you exposing file system / network / memory / threads. Standard libraries depend on these primitives. "Feels like coding on a special-purpose PC."
  - **[[BareMetalProgramming|Bare metal]]** — no code has been loaded before your program. No OS → no standard library available. Your crate plus its deps can only talk to the hardware directly.
- **The language-level switch is `#![no_std]`.** A *crate-level attribute* telling Rust **not** to link `std` (which would assume an OS). Instead the crate links against `core` — the platform-agnostic subset of `std`. This is the literal one-line contract that selects bare-metal mode.
- **[[RustCoreLibrary|libcore]] is what you keep.** Provides language primitives — floats, strings, slices — plus atomic operations and SIMD APIs. Makes **no assumptions about the system**. By construction, `no_std` + `libcore` is suitable for any *"bootstrapping (stage 0) code like bootloaders, firmware or kernels."*
- **[[RustStandardLibrary|libstd]] is what you lose** — and *why* matters. `std` is not just OS-abstraction wrappers; it also embeds a **runtime** that, before your `main()` runs, sets up stack-overflow protection, processes command-line arguments, and spawns the main thread. In `no_std` that runtime is absent — there is *no pre-main initialization* (see [[RustRuntime]]).
- **`libcore` deliberately omits things you wouldn't always want on embedded** — most notably, a **memory allocator for dynamic memory allocation**. No allocator means no heap, no `Vec`, no `Box`, no `String`. If a crate needs these, it must opt back in.
- **Opt-in heap path.** Use the `alloc` crate **plus a suitable global allocator** (e.g. `alloc-cortex-m` for Cortex-M). Then `Box` / `Vec` / `String` from `alloc` become available. Collections like `BTreeMap` come back via the `collections` crate + global default allocator. **`HashMap` / `HashSet` remain unavailable** even with an allocator — they require a *secure random number generator*, which `core` doesn't have.
- **The full feature delta (table) — the load-bearing summary of the chapter:**

  | Feature                                                   | `no_std` | `std` |
  |-----------------------------------------------------------|:--------:|:-----:|
  | heap (dynamic memory)                                     |   \*     |   ✓   |
  | collections (`Vec`, `BTreeMap`, …)                        |  \*\*    |   ✓   |
  | stack overflow protection                                 |    ✘     |   ✓   |
  | runs init code before main                                |    ✘     |   ✓   |
  | `libstd` available                                        |    ✘     |   ✓   |
  | `libcore` available                                       |    ✓     |   ✓   |
  | writing firmware, kernel, or bootloader code              |    ✓     |   ✘   |

  \* Only with the `alloc` crate + a suitable global allocator.
  \*\* Only with the `collections` crate + a configured global default allocator; `HashMap`/`HashSet` still excluded (no secure RNG in `core`).

- **The flip side** — `std` *cannot* write firmware / kernels / bootloaders. The two regimes are mutually exclusive at the bottom of the stack.
- **Spec authority**: [RFC-1184](https://github.com/rust-lang/rfcs/blob/master/text/1184-stabilize-no_std.md) stabilized the `no_std` attribute.

## Key Quotes

> "In a bare metal environment no code has been loaded before your program. Without the software provided by an OS we can not load the standard library. Instead the program, along with the crates it uses, can only use the hardware (bare metal) to run. To prevent rust from loading the standard library use `no_std`." — the operational definition of bare-metal Rust.

> "This runtime, among other things, takes care of setting up stack overflow protection, processing command line arguments, and spawning the main thread before a program's main function is invoked. This runtime also won't be available in a `no_std` environment." — explains what `libstd` actually does *beyond* the API surface, and why losing it is a real cost (not just an API restriction).

> "no_std and libcore code can be used for any kind of bootstrapping (stage 0) code like bootloaders, firmware or kernels." — the inverse contract: the floor-level systems code you can *only* write in `no_std`.

## Connections

- [[TheEmbeddedRustBook]] — chapter 3 of the book; the conceptual gate before any code chapter.
- [[RustLanguage]] — `no_std` is a Rust-language attribute; the gate to embedded use of the language.
- [[BareMetalProgramming]] — the execution regime that requires `no_std`; this chapter formalizes the link.
- [[EmbeddedSystems]] — the broader domain; this chapter draws its internal split.
- [[NoStd]] — the `#![no_std]` crate attribute itself (new concept this ingest).
- [[RustCoreLibrary]] — `libcore`, the platform-agnostic Rust standard library subset (new concept).
- [[RustStandardLibrary]] — `libstd`, the OS-assuming Rust standard library (new concept).
- [[RustRuntime]] — the pre-main initialization layer `libstd` ships and `libcore` does not (new concept).
- [[HostedEnvironment]] — the POSIX-class counterpart to bare-metal (new concept).
- [[HeapAllocation]] — dynamic memory allocation, the most prominent thing `no_std` removes by default (new concept).
- [[Bootloader]] — one of the "stage-0" use cases `no_std` enables (new concept).
- [[Microcontroller]] — the typical target where these constraints bite hardest.
- [[FlashMemory]] / [[SRAM]] — the on-chip memory tiers `no_std` firmware must live within, established in [[rust-embedded-book-intro-hardware]].

## Contradictions

- None. This chapter introduces a new conceptual layer (the `std` / `core` split + runtime model) with no overlap into existing wiki content. Strictly additive.

## Notes for the Embedded Rust corpus

- **File 3 of 44.** The conceptual pivot of the introduction. Everything from this chapter onward in *The Embedded Rust Book* assumes `#![no_std]`. The four `✘` rows in the table (no stack-overflow protection, no pre-main init, no `libstd`, no heap-by-default) are the recurring constraints the rest of the book teaches the reader to navigate.
- The chapter's "stage 0 / bootloader / firmware / kernel" framing implicitly forward-references concepts that later chapters (memory.md, semihosting.md, exceptions.md, interrupts.md) will operationalize — the reader is being primed that `no_std` is what lets Rust live at the bottom of the stack.
- The `alloc-cortex-m` pointer is the first concrete crate reference in the book and the first foreshadowing of the **opt-in heap pattern** that recurs across embedded Rust. The `HashMap`-needs-secure-RNG footnote is a small but real example of why `no_std` removes things for principled reasons, not arbitrary minimalism.
- Minor source-side observation: the table uses a `**` collision in the footnote markers (Markdown bold), so the third footnote re-uses `\**` instead of `\***`. Not a content bug — just renderer-fragile formatting, similar to the `**24**` collision flagged in [[rust-embedded-book-intro-hardware]].
