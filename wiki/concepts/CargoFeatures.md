---
title: "Cargo Features"
type: concept
tags: [rust, cargo, build, conditional-compilation]
sources: [rust-embedded-book-c-tips-index]
last_updated: 2026-05-16
---

# Cargo Features

[[Cargo]]'s named-boolean toggles for **opt-in/opt-out compilation** within a crate — the Rust idiomatic replacement for the embedded-C habit of using preprocessor `#ifdef` macros for compile-time code selection ([[rust-embedded-book-c-tips-index]]).

## Mechanism

- Declared per crate under a `[features]` table in `Cargo.toml` — *"all possible features are explicitly listed per crate, and can only be either on or off."*
- Activated by a consumer either by listing them when adding the dependency (`crate = { version = "1", features = ["FIR"] }`) or by enabling them from a downstream crate's own `[features]` table.
- **Additive**: *"if any crate in your dependency tree enables a feature for another crate, that feature will be enabled for all users of that crate"* — there is no way for one consumer to *disable* a feature another consumer has enabled. A feature must never break the API or behavior of a crate that doesn't ask for it.
- Gated in source with `#[cfg(feature = "FIR")]` (and `#[cfg(not(feature = "FIR"))]`, `#[cfg(any(...))]`, `#[cfg(all(...))]`) — the attribute applies to **the next item or block only**, so a multi-block selection needs the attribute multiple times.

```toml
# Cargo.toml
[features]
FIR = []
IIR = []
```

```rust,ignore
// lib.rs
#[cfg(feature = "FIR")]
pub mod fir;

#[cfg(feature = "IIR")]
pub mod iir;
```

## Versus the C preprocessor

| | C `#ifdef` | Cargo feature |
|---|---|---|
| Declaration site | Anywhere a `#define` reaches | Crate manifest (closed enumeration) |
| Scope | Translation unit + included headers | Crate + transitive consumers |
| Polarity | Either direction, freely toggled | **Monotonic on** (additive across deps) |
| Granularity | Per file or per line via `#if` | Per item or per block via `#[cfg]` |
| Discovery | grep for `#ifdef NAME` | `cargo metadata` / `[features]` table |

## When *not* to use a feature

The chapter is explicit that **most embedded code should *not* reach for `#[cfg]`**: *"most of the time it is better to simply include all the code and allow the compiler to remove dead code when optimising: it's simpler for you and your users, and in general the compiler will do a good job of removing unused code"* ([[rust-embedded-book-c-tips-index]]). A feature is the right tool when (a) the code wouldn't compile on a target without the feature (missing platform support, missing dep), (b) the code would link a heavy table of constants that the consumer demonstrably doesn't need, or (c) the cost is a measurable binary-size / compile-time win — *not* for everyday code variants.

## Compiler-supplied cfg

Cargo features are only one source of `#[cfg(...)]` predicates; the compiler also exposes [[RustTarget|target]]-driven conditions like `target_arch = "arm"`, `target_os = "none"`, `target_pointer_width = "32"`, `target_endian = "little"`. These are how arch-specific assembly stubs, [[NoStd|`no_std`]] vs hosted shims, and bit-width-dependent integer paths are gated in [[RustCoreLibrary|`libcore`]] and [[CortexMCrate|`cortex-m`]]-class crates without needing a custom feature.

## Composes with `const fn`

A common embedded pattern combines a feature with [[Cargo]]'s evaluation-at-compile-time `const fn` to vary array sizes:

```rust,ignore
const fn array_size() -> usize {
    #[cfg(feature = "use_more_ram")] { 1024 }
    #[cfg(not(feature = "use_more_ram"))] { 128 }
}
static BUF: [u32; array_size()] = [0u32; array_size()];
```

This is the canonical replacement for the C pattern `#define BUF_SIZE 1024` / `int buf[BUF_SIZE];`.

## Connections

- [[Cargo]] — the build tool that owns the feature graph; resolves the union across all transitive enablers.
- [[rust-embedded-book-c-tips-index]] — the file that introduces features explicitly as the `#ifdef` analog for C-experienced learners.
- [[RustMacro]] — the *other* mechanism the chapter introduces in place of the C preprocessor (`#define`-style function-like macros).
- [[CrossCompilation]] — features compose with `--target` for arch-conditional code paths.
- [[RustTarget]] — the source of compiler-supplied `target_arch` / `target_os` / `target_pointer_width` cfg predicates.
- [[NoStd]] — `default-features = false` + opt-in `std` feature is the **canonical pattern** for crates that want to support both `no_std` and hosted use.
- [[VolatileRegisterCrate]] / [[PeripheralAccessCrate]] — chip-family crates commonly use features to gate per-chip support so one PAC family crate covers many SKUs without exploding compile time.
- [[PanicSemihostingCrate]] — uses the `"exit"` Cargo feature to gate `debug::exit(EXIT_FAILURE)` after panic logging ([[rust-embedded-book-start-semihosting]]) — a textbook example of a behavior-toggle feature.
