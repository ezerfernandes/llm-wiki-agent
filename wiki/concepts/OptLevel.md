---
title: "opt-level"
type: concept
tags: [rust, rustc, cargo, optimization, embedded]
sources: [rust-embedded-book-unsorted-speed-vs-size]
last_updated: 2026-05-16
---

# opt-level

[[Rustc|`rustc`]]'s **optimization-level dial** — the `-C opt-level=<N>` flag, surfaced through [[Cargo]]'s `[profile.*]` tables in `Cargo.toml` ([[rust-embedded-book-unsorted-speed-vs-size]]). Inherited from clang/LLVM. **Five values across three regimes**:

| Value | Regime | Profile default | Notes |
|---|---|---|---|
| `0` | No optimization | `dev` (`cargo build`) | Statement-by-statement debugging; huge/slow binary; `print` works in GDB on stack vars |
| `1` | Speed (mild) | — | Some optimizations, no aggressive inlining |
| `2` | Speed | — | Loop unrolling, inline-threshold 225 |
| `3` | Speed (aggressive) | `release` (`cargo build --release`) | Adds vectorization + more inlining, inline-threshold 275 |
| `"s"` | Size | — | Inline-threshold 75 |
| `"z"` | Size (smallest) | — | Inline-threshold 25 |

## Embedded relevance

The chapter's central tension: *"Everyone wants their program to be super fast and super small but it's usually not possible to have both characteristics."* The `dev` profile (`opt-level = 0`) is debugger-friendly but routinely produces binaries that *"don't fit in your device"* — embedded targets like the [[STM32F303VCT6]] have **256 KiB of [[FlashMemory|Flash]]** as a hard ceiling. Rust's [[ZeroCostAbstraction|zero-cost-abstraction]] style — many small newtype wrappers and `deref` / `as_ref` functions — makes unoptimized binaries especially heavy, and makes `"s"` / `"z"`'s aggressive inline-threshold cuts (75 / 25) especially harmful: a low threshold leaves zero-cost abstractions un-inlined and *"can make LLVM miss optimization opportunities."* Recommended tuning: when forced to `"s"` or `"z"`, bump the threshold back up via `rustflags = ["-C", "inline-threshold=225"]` in `.cargo/config.toml`.

## Loop unrolling

`opt-level = 2` and `3` unconditionally enable loop unrolling — high Flash cost (*"from 26 bytes to 194 for a zero this array loop"*) but *"can also halve the execution time."* **There is no way to disable loop unrolling at `2` / `3`** — if Flash is tight, the only escape is to drop down to `"s"` / `"z"`.

## Debuginfo coexists with optimization

In embedded *"debuginfo is zero cost in the sense that it won't occupy space in Flash / ROM"* — symbols stay host-side in the ELF, never reaching the device. The chapter therefore recommends `[profile.release] debug = true` so release builds remain breakpoint-friendly. (Variables themselves still print as `$0 = <value optimized out>` in [[GDB]] once optimized.)

## `profile-overrides` — different levels per crate

[[Cargo]]'s [`profile-overrides`](https://doc.rust-lang.org/cargo/reference/profiles.html#overrides) feature decouples the top crate's optimization level from its dependencies:

```toml
# Cargo.toml
[profile.dev.package."*"]   # all deps
opt-level = "z"
codegen-units = 1           # better optimizations

[profile.dev.package.cortex-m-rt]   # but not this one
opt-level = 0
```

Worked example in the chapter — applying `[profile.dev.package."*"] opt-level = "z"` to an app shrinks `.text` 9060 → 3490 bytes and `.rodata` 1708 → 1100 bytes, **a 6 KiB Flash reduction with no loss of top-crate debuggability** (the top crate is the only thing the developer typically wants to step through anyway).

**Caveat**: *"generic code can sometimes be optimized alongside the crate where it is instantiated, rather than the crate where it is defined."* If a heavy generic struct is instantiated in the top crate, raising the *dependency's* optimization level may have no effect — the monomorphized code is being emitted in the application, not the library.

## Connections

- [[Rustc]] — owns the `-C opt-level` flag; the LLVM backend translates it to the codegen pipeline.
- [[Cargo]] — surfaces `opt-level` via `[profile.dev]` / `[profile.release]` / `[profile.<name>.package.<crate>]` tables in `Cargo.toml`.
- [[FlashMemory]] — the resource budget that forces the speed-vs-size choice on embedded targets; already named `opt-level = "z"` as part of the standard embedded-Rust toolchain.
- [[ZeroCostAbstraction]] — the Rust style whose payoff depends on the LLVM inline threshold; `"s"` / `"z"` may need an explicit `inline-threshold=225` bump to preserve it.
- [[GDB]] — the debugger affected by `opt-level`; `$0 = <value optimized out>` is the canonical symptom.
- [[BareMetalProgramming]] — the regime where *"debuginfo is zero cost"* and `[profile.release] debug = true` is a free win.
- [[CortexMRTCrate]] — named in the chapter's per-dependency override example as the canonical *"keep this one at `opt-level = 0`"* case.
- [[rust-embedded-book-unsorted-speed-vs-size]] — the canonical chapter.
