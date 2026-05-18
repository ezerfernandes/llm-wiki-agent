---
title: "The Embedded Rust Book — Panicking"
type: source
tags: [rust, embedded, book-chapter, panic, error-handling]
date: 2026-05-16
source_file: raw/book/src/start/panicking.md
last_updated: 2026-05-16
---

## Summary

File 15/44 of *[[TheEmbeddedRustBook]]* — the *Getting Started* chapter's **Panicking** sub-section, immediately after [[rust-embedded-book-start-semihosting|Semihosting]]. Names panicking as a **core part of the Rust language** (runtime-checked operations like array indexing emit panics) and then makes the [[NoStd|`no_std`]]-specific point: unlike [[RustStandardLibrary|`libstd`]] (which has a defined unwind-or-abort behavior), a bare-metal program must **explicitly declare its panic behavior** via the [[PanicHandlerAttribute|`#[panic_handler]`]] attribute on a `fn(&PanicInfo) -> !`. Surveys the four commonly-used pre-packaged panic-handler crates ([[PanicAbortCrate|`panic-abort`]], [[PanicHaltCrate|`panic-halt`]], [[PanicItmCrate|`panic-itm`]], [[PanicSemihostingCrate|`panic-semihosting`]]) and the **profile-conditional panic-handler swap** pattern (`panic-halt` for `dev` to keep a breakpoint on `rust_begin_unwind`, `panic-abort` for `release` to minimize binary size).

## Key Claims

- **Panicking is a core Rust feature, not a library add-on.** Runtime-checked built-in ops (out-of-bounds indexing being the canonical example) emit a panic; this is part of the language's memory-safety contract, not the standard library's. The bare-metal regime cannot opt out.
- **In `libstd`, panicking has defined behavior — stack unwinding (default) or abort (user-opted).** This is the contrast against which the chapter motivates everything else.
- **In a `no_std` program, panicking behavior is undefined until the user declares it.** The mechanism is a single function annotated with [[PanicHandlerAttribute|`#[panic_handler]`]].
- **The `#[panic_handler]` function must appear exactly *once* in the entire dependency graph of a program.** This is a hard linker-level uniqueness invariant; multiple crates each declaring a `#[panic_handler]` is a link error.
- **The required signature is `fn(&PanicInfo) -> !`** — a diverging function taking a borrowed [[PanicInfo|`core::panic::PanicInfo`]] (which carries the panic location and payload).
- **The book's pedagogy is: pick a behavior by linking a crate.** Four commonly-used pre-packaged crates:
  - [[PanicAbortCrate|`panic-abort`]] — executes the **abort instruction** (Cortex-M `UDF` / similar).
  - [[PanicHaltCrate|`panic-halt`]] — enters an **infinite loop**, halting the current thread.
  - [[PanicItmCrate|`panic-itm`]] — logs the panic message via the **ITM** (ARM Cortex-M-specific Instrumentation Trace Macrocell peripheral).
  - [[PanicSemihostingCrate|`panic-semihosting`]] — logs the panic message to the host via [[ARMSemihosting|semihosting]] (already introduced in [[rust-embedded-book-start-semihosting]]).
- **"Panic-handler" is a crates.io keyword.** The chapter points readers at `crates.io/keywords/panic-handler` for the broader catalog (covers [[PanicProbeCrate|`panic-probe`]] and others not enumerated in the chapter's prose).
- **The `use panic_X as _;` idiom is load-bearing.** A bare `use panic_X;` would emit an unused-import warning; `as _` tells the compiler the crate is linked purely for its `#[panic_handler]` side effect with no name binding. The older `extern crate panic_X;` form (pre-2018-edition) survives only for sysroot crates (`proc_macro`, `alloc`, `std`, `test`).
- **The single-line panic-handler declaration enables profile-conditional swapping.** Canonical pattern in the chapter:
  ```rust
  #[cfg(debug_assertions)]
  use panic_halt as _;          // dev: keep `rust_begin_unwind` breakpointable
  #[cfg(not(debug_assertions))]
  use panic_abort as _;         // release: minimize binary size
  ```
  `cargo build` links `panic-halt`; `cargo build --release` links `panic-abort`.
- **Why `panic-halt` for dev: `rust_begin_unwind` is breakpointable.** The infinite-loop variant preserves a clean call stack at panic time and the symbol `rust_begin_unwind` (the panic dispatch entry) can carry a [[GDB]] breakpoint for post-mortem inspection.
- **Why `panic-abort` for release: minimize binary size.** The abort variant elides the unwinding/looping/formatting code path, trimming the final ELF.
- **Embedded systems span "user facing" to "safety critical" — no one-size-fits-all panic behavior exists.** This is the chapter's framing for *why* the panic handler is a swappable knob rather than a fixed runtime decision.
- **Worked example: out-of-bounds indexing.** A `#![no_main] #![no_std]` program with `use panic_semihosting as _;` and `xs[i]` where `i == xs.len()` produces the standard panic message on QEMU:
  ```
  panicked at 'index out of bounds: the len is 3 but the index is 4', src/main.rs:12:13
  ```
  Switching to `panic_halt` makes the same code panic silently (no host log).

## Key Quotes

> "Panicking is a core part of the Rust language. Built-in operations like indexing are runtime checked for memory safety. When out of bounds indexing is attempted this results in a panic." — the chapter's opening framing of panic as a language-level (not library-level) primitive.

> "In programs without standard library, however, the panicking behavior is left undefined. A behavior can be chosen by declaring a `#[panic_handler]` function. This function must appear exactly *once* in the dependency graph of a program, and must have the following signature: `fn(&PanicInfo) -> !`." — the bare-metal contract.

> "Given that embedded systems range from user facing to safety critical (cannot crash) there's no one size fits all panicking behavior but there are plenty of commonly used behaviors. These common behaviors have been packaged into crates that define the `#[panic_handler]` function." — why the panic handler is a per-program decision.

> "In this example the crate links to the `panic-halt` crate when built with the dev profile (`cargo build`), but links to the `panic-abort` crate when built with the release profile (`cargo build --release`)." — the profile-conditional swap idiom.

> "The `use panic_abort as _;` form of the `use` statement is used to ensure the `panic_abort` panic handler is included in our final executable while making it clear to the compiler that we won't explicitly use anything from the crate. Without the `as _` rename, the compiler would warn that we have an unused import." — the linker-level rationale for the `as _` idiom.

## Connections

- [[TheEmbeddedRustBook]] — file 15/44; the Panicking sub-section.
- [[rust-embedded-book-start-semihosting]] — predecessor chapter (file 14); first introduced [[PanicSemihostingCrate|`panic-semihosting`]] with the `"exit"` feature for QEMU run-pass tests.
- [[rust-embedded-book-start-registers]] — predecessor chapter (file 13).
- [[rust-embedded-book-start-hardware]] — predecessor chapter (file 12).
- [[rust-embedded-book-start-qemu]] — predecessor chapter (file 11); first introduced [[PanicHaltCrate|`panic-halt`]] in the canonical `no_std` skeleton.
- [[NoStd]] — the regime that demands an explicit `#[panic_handler]`; this chapter is the canonical write-up of *why*.
- [[PanicHandlerAttribute]] — **new concept**: the `#[panic_handler]` attribute itself, with its uniqueness invariant and `fn(&PanicInfo) -> !` signature.
- [[PanicInfo]] — **new concept**: the `core::panic::PanicInfo` struct carrying the panic location/payload, borrowed by every panic handler.
- [[PanicAbortCrate]] — **new entity**: minimal `#[panic_handler]` provider that executes the abort instruction.
- [[PanicItmCrate]] — **new entity**: `#[panic_handler]` provider that logs over the [[ARMCortexM|Cortex-M]]-specific ITM trace peripheral.
- [[PanicProbeCrate]] — **new entity**: the [[Knurling]] / `defmt` ecosystem's modern alternative panic provider (mentioned implicitly via the crates.io keyword pointer; explicit in the book's broader Rust-embedded canon).
- [[PanicHaltCrate]] — existing entity; the chapter's recommended **dev-profile** panic handler.
- [[PanicSemihostingCrate]] — existing entity; introduced in the predecessor chapter, re-listed here as one of the four canonical options.
- [[CortexMSemihostingCrate]] — the underlying API `panic-semihosting` writes through.
- [[RustStandardLibrary]] — the regime the bare-metal contract is contrasted against (where unwinding-or-abort is the default).
- [[ARMCortexM]] — the target ISA; the ITM peripheral that [[PanicItmCrate|`panic-itm`]] writes through is Cortex-M-specific.
- [[CortexMRTCrate]] — provides the `#[entry]` runtime that hosts the chapter's worked example.
- [[QEMU]] — the execution environment for the worked example (`panic-semihosting` text appears on the QEMU console).
- [[GDB]] — the dev-profile target for `panic-halt` (the `rust_begin_unwind` breakpoint).

## Contradictions

None. Strictly additive — formalizes the `#[panic_handler]` mechanism that was used opportunistically in [[rust-embedded-book-start-qemu]] ([[PanicHaltCrate|`panic-halt`]]) and [[rust-embedded-book-start-semihosting]] ([[PanicSemihostingCrate|`panic-semihosting`]]) into its canonical language-level write-up, and introduces the two remaining book-listed alternatives ([[PanicAbortCrate|`panic-abort`]], [[PanicItmCrate|`panic-itm`]]) plus the modern [[Knurling]] alternative ([[PanicProbeCrate|`panic-probe`]]).
