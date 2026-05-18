---
title: "PanicInfo (core::panic::PanicInfo)"
type: concept
tags: [rust, embedded, panic, error-handling, no-std, language-feature]
sources: [rust-embedded-book-start-panicking]
last_updated: 2026-05-16
---

# `core::panic::PanicInfo`

**Struct passed by reference to every Rust `#[panic_handler]` function**, carrying the panic's **location** (file / line / column) and **payload** (the formatted message). Lives in `core::panic`, so it is available in [[NoStd|`no_std`]] crates — the standard-library `std::panic::PanicInfo` is a re-export.

> *"`PanicInfo` is a struct containing information about the location of the panic."* — [[rust-embedded-book-start-panicking]]

## Signature contract

Any function bearing the [[PanicHandlerAttribute|`#[panic_handler]`]] attribute must have type `fn(&PanicInfo) -> !`. The handler receives a `&PanicInfo` (not by value — `PanicInfo` is opaque and not `Copy`) and never returns.

## Typical use

The pre-packaged panic-handler crates extract the location and payload to either log them or discard them:

- [[PanicHaltCrate|`panic-halt`]] **ignores** the `PanicInfo` and enters `loop {}`.
- [[PanicAbortCrate|`panic-abort`]] ignores it and executes the abort instruction.
- [[PanicItmCrate|`panic-itm`]] formats it onto the [[ARMCortexM|Cortex-M]] ITM trace channel.
- [[PanicSemihostingCrate|`panic-semihosting`]] formats it through `cortex-m-semihosting`'s `hstderr` → host stderr.
- [[PanicProbeCrate|`panic-probe`]] formats it via `defmt` over the probe-rs RTT channel.

## What the chapter's worked example shows

A program panicking via out-of-bounds indexing (`xs[i]` with `i == xs.len()`) under `panic-semihosting` produces:

```
panicked at 'index out of bounds: the len is 3 but the index is 4', src/main.rs:12:13
```

The location (`src/main.rs:12:13`) and message (`'index out of bounds: ...'`) are exactly the fields the handler extracted from its `&PanicInfo` argument ([[rust-embedded-book-start-panicking]]).

## Connections

- [[PanicHandlerAttribute]] — the attribute that requires a `fn(&PanicInfo) -> !` signature.
- [[PanicHaltCrate]] / [[PanicAbortCrate]] / [[PanicItmCrate]] / [[PanicSemihostingCrate]] / [[PanicProbeCrate]] — the canonical consumers.
- [[RustCoreLibrary]] — the crate that hosts `core::panic::PanicInfo` and therefore makes it available under `no_std`.
- [[NoStd]] — the regime in which `core::panic::PanicInfo` (rather than `std::panic::PanicInfo`) is the relevant type.
- [[TheEmbeddedRustBook]] — file 15/44 ([[rust-embedded-book-start-panicking]]).
