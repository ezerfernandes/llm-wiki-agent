---
title: "The Embedded Rust Book — Optimizations: The speed size tradeoff"
type: source
tags: [rust, embedded, book-chapter, optimization]
date: 2026-05-16
source_file: raw/book/src/unsorted/speed-vs-size.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Optimizations: The speed size tradeoff

## Summary

File 42/44 of *[[TheEmbeddedRustBook]]* — **first substantive leaf** of the *Unsorted topics* chapter, immediately after the trivial placeholder opener at file 41 ([[rust-embedded-book-unsorted-index]]). Operational walkthrough of [[Rustc|`rustc`]]'s **five [[OptLevel|optimization levels]]** (`0` / `1` / `2` / `3` / `"s"` / `"z"`) and how to wire them through [[Cargo]]'s `[profile.*]` tables in `Cargo.toml`. **Three regimes** — *No optimizations* (`opt-level = 0`, the `dev` profile default — debugger-friendly but huge/slow binaries that may not fit in [[FlashMemory|Flash]]), *Optimize for speed* (`1` / `2` / `3`, the `release` profile default at `3` — `2` and `3` enable loop unrolling and aggressive inlining, vectorization), and *Optimize for size* (`"s"` / `"z"`, inherited from clang/LLVM — `"z"` is the smaller of the two). The chapter's signature trick: the **[`profile-overrides`] Cargo feature** that decouples the top-crate's optimization level from its dependencies — `[profile.dev.package."*"] opt-level = "z"` keeps the application debugger-friendly while shrinking dependency code (worked example shows `.text` going 9060 → 3490 bytes, **6 KiB Flash saved**). Closes with **inline-threshold tuning** — `"s"` / `"z"` slash LLVM's inline threshold (75 / 25) far below `2` / `3` (225 / 275), which can hurt Rust's many small zero-cost-abstraction functions; the recommended workaround is `rustflags = ["-C", "inline-threshold=225"]` in `.cargo/config.toml`.

## Key Claims

- **Five `opt-level` values**: `0` (no optimization — `dev` default), `1` / `2` / `3` (speed — `release` default is `3`), `"s"` / `"z"` (size — `"z"` is smaller). Inherited from clang/LLVM. Names "are not too descriptive but `"z"` is meant to give the idea that it produces smaller binaries than `"s"`."
- **`dev` profile is dangerous for embedded**: unoptimized binaries can occupy *"dozens of KiB of Flash, which your target device may not have — the result: your unoptimized binary doesn't fit in your device!"*
- **Debuginfo is zero-cost in embedded**: *"for bare metal development, debuginfo is zero cost in the sense that it won't occupy space in Flash / ROM"* — the chapter recommends `[profile.release] debug = true` so release builds remain breakpoint-friendly.
- **`opt-level = 0` is the debugger-friendliest**: *"stepping through the code feels like you are executing the program statement by statement"*, `print` works on stack variables. Higher optimization levels produce `$0 = <value optimized out>` in GDB.
- **The `profile-overrides` recipe** — `[profile.dev.package."*"] opt-level = "z"` optimizes **all dependencies for size** while keeping the top crate at `opt-level = 0`. Worked example: `.text` 9060 → 3490 bytes, `.rodata` 1708 → 1100 bytes, **6 KiB Flash reduction** with no loss of top-crate debuggability.
- **Granular per-dependency overrides**: `[profile.dev.package.cortex-m-rt] opt-level = 0` plus `[profile.dev.package."*"] opt-level = "z"` keeps a specific dependency debuggable while the rest are size-optimized.
- **Generic-code caveat**: *"generic code can sometimes be optimized alongside the crate where it is instantiated, rather than the crate where it is defined"* — `profile-overrides` may have no effect on monomorphized code instantiated in the top crate.
- **`opt-level = 2` / `3` unconditionally unroll loops**: *"loop unrolling has a rather high cost in terms of Flash / ROM (e.g. from 26 bytes to 194 for a zero this array loop) but can also halve the execution time"*. There is **no way to disable loop unrolling** at `2` / `3` — if Flash is tight, drop to `"s"` / `"z"`.
- **`opt-level = 3` adds vectorization and more inlining** over `opt-level = 2`.
- **`"s"` / `"z"` slash the inline threshold** — the metric LLVM uses to decide whether to inline a function. Low thresholds clash with Rust's *"zero cost abstractions"* style which uses many small functions (`deref`, `as_ref`, newtype wrappers).
- **Inline-threshold table** (as of `rustc` 1.29.0): `opt-level = 3` → 275, `2` → 225, `"s"` → 75, `"z"` → 25.
- **Tuning recommendation**: when optimizing for size, *"You should try `225` and `275`"* via `rustflags = ["-C", "inline-threshold=123"]` in `.cargo/config.toml`.
- **Compose with `codegen-units = 1`**: the example shows `[profile.dev.package."*"] codegen-units = 1` alongside `opt-level = "z"` for *"better optimizations"* on dependencies.

## Key Quotes

> "Everyone wants their program to be super fast and super small but it's usually not possible to have both characteristics."

> "for bare metal development, debuginfo is zero cost in the sense that it won't occupy space in Flash / ROM so we actually recommend that you enable debuginfo in the release profile"

> "Loop unrolling has a rather high cost in terms of Flash / ROM (e.g. from 26 bytes to 194 for a zero this array loop) but can also halve the execution time given the right conditions"

> "These two optimization levels [`"s"` / `"z"`] greatly reduce LLVM's inline threshold, a metric used to decide whether to inline a function or not. One of Rust principles are zero cost abstractions; these abstractions tend to use a lot of newtypes and small functions to hold invariants … so a low inline threshold can make LLVM miss optimization opportunities."

## Connections

- [[TheEmbeddedRustBook]] — file 42/44; first substantive leaf of the *Unsorted topics* chapter.
- [[rust-embedded-book-unsorted-index]] — predecessor (file 41/44, the chapter's placeholder opener).
- [[OptLevel]] — the chapter's central concept (the five `rustc` optimization levels and their Cargo profile bindings).
- [[Rustc]] — the compiler whose `-C opt-level` flag is exposed by [[Cargo]]'s `[profile.*]` tables.
- [[Cargo]] — owns the `[profile.dev]` / `[profile.release]` tables and the `profile-overrides` feature.
- [[CargoFeatures]] — *not the same* as the `profile-overrides` Cargo feature, but adjacent vocabulary; both are crate-manifest mechanisms.
- [[FlashMemory]] — the resource budget the chapter exists to optimize against; already cites `opt-level = "z"` in the embedded-Rust toolchain.
- [[GDB]] — the debugger whose `<value optimized out>` message motivates the `opt-level = 0` regime and the `debug = true` on `release` recommendation.
- [[BareMetalProgramming]] — the regime in which *"debuginfo is zero cost"* because it never reaches the device.
- [[ZeroCostAbstraction]] — Rust's *"zero cost abstractions"* principle is the chapter's stated reason `"s"` / `"z"` need an inline-threshold bump to keep paying off.
- [[CortexMRTCrate|`cortex-m-rt`]] — named in the per-dependency override example as the canonical *"don't optimize this one"* case.

## Contradictions

None — the chapter is a tactical Cargo/`rustc` reference compatible with prior files. The `opt-level = "z"` recommendation it operationalizes was already cited by [[FlashMemory]] (which referenced `cargo size`, `--release`, and `opt-level = "z"` as standard embedded-Rust tooling) — this file is the **canonical source** that earlier reference was implicitly pointing at.
