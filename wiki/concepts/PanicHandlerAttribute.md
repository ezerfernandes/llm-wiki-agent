---
title: "#[panic_handler] Attribute"
type: concept
tags: [rust, embedded, panic, error-handling, no-std, language-feature]
sources: [rust-embedded-book-start-panicking]
last_updated: 2026-05-16
---

# `#[panic_handler]` Attribute

**Rust language attribute marking the single function that defines the program's panicking behavior in [[NoStd|`no_std`]] crates.** Required because, without [[RustStandardLibrary|`libstd`]]'s built-in unwind-or-abort runtime, the language has no default panic strategy — *"in programs without standard library [...] the panicking behavior is left undefined. A behavior can be chosen by declaring a `#[panic_handler]` function"* ([[rust-embedded-book-start-panicking]]).

## Contract

1. **Exactly one** `#[panic_handler]` function must appear in the entire dependency graph of a `no_std` binary. Two crates each declaring one → link error.
2. **Signature is fixed**: `fn(&PanicInfo) -> !` — takes a borrowed [[PanicInfo|`core::panic::PanicInfo`]] (location + payload), never returns.
3. The function is invoked by the compiler-generated panic dispatch (`rust_begin_unwind`) whenever any panic (`panic!()`, out-of-bounds index, integer overflow with overflow checks, unwrap-on-None, etc.) fires.

## How it's typically supplied

The dominant pattern in embedded Rust is **not** to write the handler by hand but to link a pre-packaged crate that ships one:

```rust
use panic_halt as _;   // or panic_abort / panic_itm / panic_semihosting / panic_probe
```

The `as _` rename is load-bearing: it suppresses the unused-import warning while still pulling the crate (and therefore its `#[panic_handler]` symbol) into the final binary ([[rust-embedded-book-start-panicking]]).

## Profile-conditional swap

The single-line declaration enables compiling different handlers per Cargo profile:

```rust
#[cfg(debug_assertions)]
use panic_halt as _;          // dev: keep `rust_begin_unwind` breakpointable
#[cfg(not(debug_assertions))]
use panic_abort as _;         // release: minimize binary size
```

— a pattern the chapter highlights as one of the practical payoffs of the attribute's design ([[rust-embedded-book-start-panicking]]).

## Connections

- [[NoStd]] — the regime that requires `#[panic_handler]`; on `libstd` builds the standard runtime supplies one.
- [[PanicInfo]] — the struct the attribute's function receives.
- [[PanicHaltCrate]] / [[PanicAbortCrate]] / [[PanicItmCrate]] / [[PanicSemihostingCrate]] / [[PanicProbeCrate]] — the canonical crates that supply a `#[panic_handler]` so the user doesn't have to.
- [[RustStandardLibrary]] — supplies the default panic runtime (unwind / abort) the `#[panic_handler]` mechanism replaces.
- [[TheEmbeddedRustBook]] — file 15/44 ([[rust-embedded-book-start-panicking]]) is the canonical introduction.
