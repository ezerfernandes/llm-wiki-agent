---
title: "The Embedded Rust Book — Tips for embedded C developers"
type: source
tags: [rust, embedded, book-chapter, c-tips]
date: 2026-05-16
source_file: raw/book/src/c-tips/index.md
sources: []
last_updated: 2026-05-16
---

## Summary

File 37/44 of *[[TheEmbeddedRustBook]]* — **opens Part 6, the *Tips for embedded C developers* chapter**, immediately after the *Design Patterns* chapter closed at file 36 ([[rust-embedded-book-design-patterns-hal-gpio]]). The chapter's audience flips: prior chapters assumed Rust fluency or generic embedded background; this one assumes **embedded C fluency** and walks the reader through the C→Rust idiom translation table the book deferred until now. Six top-level sections — *Preprocessor*, *Build System*, *Iterators vs Array Access*, *References vs Pointers*, *Volatile Access*, *Packed and Aligned Types* — each pairing a familiar embedded-C pattern with its Rust counterpart and explaining where the mapping is **non-identical** (the points that bite C-experienced learners). Pure cross-walk chapter: no new embedded-Rust mechanisms, just an alternate access path into the vocabulary the wiki already accumulated across files 1–36. Closes with a short *Other Resources* list cross-referencing the still-deferred *Interoperability* chapter ([[rust-embedded-book-c-tips-index|file 37]] → forward to *A little C with your Rust* / *A little Rust with your C*).

## Key Claims

- **No preprocessor in Rust** — *"In Rust there is no preprocessor, and so many of these use cases are addressed differently."* The three canonical C preprocessor use cases — `#ifdef` conditional compilation, `#define` compile-time constants/sizes, function-style macros — are addressed by **three separate Rust mechanisms**, not one.
- **`#ifdef` → [[CargoFeatures|Cargo features]] + `#[cfg(...)]`** — *"The closest match to `#ifdef ... #endif` in Rust are Cargo features. These are a little more formal than the C preprocessor: all possible features are explicitly listed per crate, and can only be either on or off."* Features are **additive** across the dependency tree (any enabling consumer turns the feature on for everyone). Pattern: declare under `[features]` in `Cargo.toml`, gate with `#[cfg(feature="FIR")]` on the next item or block. Compiler-supplied conditions like `target_arch` are also available — see the [conditional compilation] reference chapter. *"Most of the time it is better to simply include all the code and allow the compiler to remove dead code when optimising"* — `cfg` is a sharper tool than its C ergonomics suggest.
- **`#define SIZE 1024` → `const fn`** — *"Rust supports `const fn`, functions which are guaranteed to be evaluable at compile-time and can therefore be used where constants are required, such as in the size of arrays."* Composes with `#[cfg]`: `const fn array_size() -> usize { #[cfg(feature="use_more_ram")] { 1024 } #[cfg(not(...))] { 128 } }` then `static BUF: [u32; array_size()] = [0u32; array_size()];`. Stable since 1.31; the set of allowed operations is still expanding.
- **Function-style `#define` → declarative or procedural macros** — Rust's [[RustMacro|macro system]] operates *"at a higher level"* than the C preprocessor (token-tree, not text). Two flavors: **macros-by-example** (`macro_rules!`, function-call syntax, expand to expressions/statements/items/patterns) and **procedural macros** (*"can transform arbitrary Rust syntax into new Rust syntax"*). C-preprocessor patterns that expand to **fragments** of names or list items **do not translate** — Rust macros must expand to a syntactically complete unit. Often a `#[inline]`-annotated regular function is enough and clearer — *"the compiler will automatically inline functions from the same crate where appropriate, so forcing it to do so inappropriately might actually lead to decreased performance."*
- **Build system: [[Cargo]] + `build.rs`** — Custom build steps live in a `build.rs` script (itself Rust code), not in a separate Make/CMake fragment. Documented use cases: embed build date or Git commit hash, **generate linker scripts at build time** (the same mechanism the [[CortexMRTCrate|`cortex-m-rt`]] family uses), tweak Cargo build config, link extra static libraries. **No post-build hooks** at the time of writing — pre-build only.
- **[[CrossCompilation|Cross-compiling]] is one flag** — *"Using Cargo for your build system also simplifies cross-compiling. In most cases it suffices to tell Cargo `--target thumbv6m-none-eabi` and find a suitable executable in `target/thumbv6m-none-eabi/debug/myapp`."* Targets not natively supported by Rust require building [[RustCoreLibrary|`libcore`]] yourself; the chapter names **[[Xargo]]** as the historical workaround (modern equivalent is `cargo build -Z build-std=core`).
- **Array indexing is an anti-pattern; use iterators** — *"In Rust this is an anti-pattern: indexed access can be slower (as it needs to be bounds checked) and may prevent various compiler optimisations. … Rust will check for out-of-bounds access on manual array indexing to guarantee memory safety, while C will happily index outside the array."* Iterators are the idiomatic loop: `for element in arr.iter() { process(*element); }`. Iterators chain (`.zip()`, `.enumerate()`, `.chain()`, `.min()`, `.max()`, `.sum()`) — patterns that require manual loop bookkeeping in C.
- **Raw pointers exist but are `unsafe` to deref; default is references** — *"In Rust, pointers (called raw pointers) exist but are only used in specific circumstances, as dereferencing them is always considered `unsafe`."* The everyday handle is `&T` / `&mut T`, governed by the [[BorrowChecker|borrow checker]]: *"only one mutable reference or multiple non-mutable references to the same value at any given time."* **Mutability is opt-in**: *"where in C the default is mutable and you must be explicit about `const`, in Rust the opposite is true."* [[RawPointer|Raw pointers]] are reserved for hardware-pointer work (DMA buffer addresses, [[MemoryMappedIO|MMIO]] register blocks behind every [[PeripheralAccessCrate|PAC]]).
- **`volatile` is an operation, not a qualifier** — *"In Rust, instead of marking a variable as `volatile`, we use specific methods to perform volatile access: [`core::ptr::read_volatile`] and [`core::ptr::write_volatile`]."* These take `*const T` / `*mut T` — references auto-coerce to raw pointers but the read/write itself is `unsafe`. Worked example: a `static mut SIGNALLED: bool` flag flipped from an `#[interrupt]` ISR and polled in a `loop`, with the caveat *"in real code, you should consider a higher level primitive, such as an atomic type"* (forward reference to [[Atomic]] / the [[rust-embedded-book-concurrency-index|Concurrency chapter]]). Routine code rarely calls these directly — they are wrapped by [[PeripheralAccessCrate|PACs]] and [[VolatileRegisterCrate|`volatile_register`]]. See [[VolatileMemoryAccess]].
- **Struct layout: `repr` attribute, not compiler-specific pragmas** — Rust's default repr makes **no layout guarantees** — *"The compiler may re-order struct members or insert padding and the behaviour may change with future versions of Rust."* Three explicit reprs: **`#[repr(C)]`** for C-ABI / hardware register-block layouts (see [[ReprC]]); **`#[repr(packed)]`** for protocol-header parsing (sets alignment to `1`, can produce unaligned fields — must use `addr_of!` to take addresses rather than naked `&v.x`); **`#[repr(align(n))]`** for explicit over-alignment (`n` a power of two; useful for cache-line / page alignment). Combinations: **`repr(C)` + `repr(align(n))`** is legal; **`repr(packed)` + `repr(align(n))`** is **not** legal (contradictory), and a `repr(packed)` struct **cannot contain** a `repr(align(n))` field.
- **No new vocabulary in this chapter** — the chapter is a **cross-walk index** into mechanisms already introduced: [[CargoFeatures]] (new concept), [[RustMacro]] (new concept), [[BorrowChecker]], [[RawPointer]], [[VolatileMemoryAccess]], [[ReprC]], [[CrossCompilation]], [[Cargo]]. Two new concept pages (the two **language-level** mechanisms the prior 36 files referenced but never made standalone); everything else reuses.

## Key Quotes

> "In Rust there is no preprocessor, and so many of these use cases are addressed differently." — opening of the *Preprocessor* section, framing the chapter

> "Most of the time it is better to simply include all the code and allow the compiler to remove dead code when optimising: it's simpler for you and your users, and in general the compiler will do a good job of removing unused code." — when `#[cfg]` is the wrong tool

> "In Rust this is an anti-pattern: indexed access can be slower (as it needs to be bounds checked) and may prevent various compiler optimisations." — on `for(i=0; i<n; i++) arr[i]`-style loops

> "Rust will check for out-of-bounds access on manual array indexing to guarantee memory safety, while C will happily index outside the array." — the safety-vs-performance reframing

> "Where in C the default is mutable and you must be explicit about `const`, in Rust the opposite is true." — the mutability-default inversion C developers most often miss

> "In Rust, instead of marking a variable as `volatile`, we use specific methods to perform volatile access." — the qualifier-to-operation reframing for MMIO

> "The default representation provides no guarantees of layout, so should not be used for code that interoperates with hardware or C." — why `#[repr(C)]` is mandatory at FFI boundaries

## Connections

- [[TheEmbeddedRustBook]] — file 37/44; opens Part 6, the *Tips for embedded C developers* chapter.
- [[rust-embedded-book-design-patterns-hal-gpio]] — preceding file (36/44); closed the *Design Patterns* chapter.
- [[CargoFeatures]] — new concept; Rust's `#ifdef` analog, introduced explicitly here.
- [[RustMacro]] — new concept; the two-flavor macro system that subsumes function-style `#define`.
- [[Cargo]] — the build system the chapter recommends as the C-make replacement.
- [[CrossCompilation]] — the `--target` workflow the chapter names as the standard cross-compile flow.
- [[Xargo]] — historical workaround for non-Tier-1 targets (needed to build `libcore`); now superseded by `-Z build-std=core`.
- [[RustCoreLibrary|`libcore`]] — the `no_std` runtime library that Xargo rebuilds for unsupported targets.
- [[BorrowChecker]] — the mechanism that makes `&T` / `&mut T` safe by default (multiple `&` xor one `&mut`).
- [[RawPointer]] — Rust's `*const T` / `*mut T`; the `unsafe`-to-deref C-pointer analog used in [[MemoryMappedIO|MMIO]] and DMA work.
- [[VolatileMemoryAccess]] — the operation-not-qualifier reframing of C's `volatile`; `core::ptr::read_volatile` / `write_volatile`.
- [[ReprC]] — `#[repr(C)]` for hardware/FFI layout; this chapter introduces `#[repr(packed)]` and `#[repr(align(n))]` alongside it.
- [[Atomic]] — forward-referenced as the higher-level primitive that should replace the chapter's `static mut SIGNALLED: bool` toy ISR-flag pattern.
- [[rust-embedded-book-concurrency-index]] — the chapter the volatile-ISR example explicitly defers to for concurrency primitives.
- [[PeripheralAccessCrate]] — the layer that hides the volatile-access machinery for hardware registers.
- [[VolatileRegisterCrate]] — `RW<T>` / `RO<T>` wrappers that hide raw-pointer-plus-`read_volatile` boilerplate.

## Contradictions

None. The chapter is a cross-walk from C idioms into Rust mechanisms the wiki has accumulated across files 1–36; every section either names an already-recorded concept ([[BorrowChecker]] / [[RawPointer]] / [[VolatileMemoryAccess]] / [[ReprC]] / [[CrossCompilation]]) or introduces one of the two new language-level concepts ([[CargoFeatures]] / [[RustMacro]]) at the depth the prior files only referenced obliquely.
