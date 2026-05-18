---
title: "Rust Macro"
type: concept
tags: [rust, language, macros, metaprogramming]
sources: [rust-embedded-book-c-tips-index]
last_updated: 2026-05-16
---

# Rust Macro

Rust's compile-time **metaprogramming facility** — the language-level replacement for the C preprocessor's function-style `#define`s. Unlike the C preprocessor, which operates **textually** before any parser sees the code, the Rust macro system operates on **token trees** at parse time and expands into **syntactically complete units** (expression / statement / item / pattern) ([[rust-embedded-book-c-tips-index]]).

## Two flavors

### 1. Macros by example — `macro_rules!`

The simpler, more common form. Defined with `macro_rules!`, invoked with a `name!(...)` call-like syntax. Pattern-matches on token trees with capture variables (`$x:expr`, `$ty:ty`, `$pat:pat`, `$($t:tt)*`, …) and substitutes into a template.

```rust,ignore
macro_rules! debug_pin_toggle {
    ($pin:expr) => {
        $pin.set_high().unwrap();
        $pin.set_low().unwrap();
    };
}
```

### 2. Procedural macros

More powerful and considerably more complex: *"can transform arbitrary Rust syntax into new Rust syntax."* Implemented as a separate crate (`proc-macro = true`) exposing a `fn(TokenStream) -> TokenStream`. Three sub-flavors: **function-like** (`my_macro!(...)`), **derive** (`#[derive(MyTrait)]`), and **attribute** (`#[my_attr] fn foo() { ... }`). The [[CortexMRTCrate|`cortex-m-rt`]] `#[entry]` / `#[exception]` / `#[interrupt]` attributes ([[ExceptionAttribute]] / [[InterruptAttribute]]) and `svd2rust`-style code generation are all procedural macros.

## Versus the C preprocessor

| | C `#define` | Rust macro |
|---|---|---|
| Operates on | Text | Token trees |
| Hygiene | None — captures identifiers | **Hygienic** — invented identifiers don't collide with the caller's |
| Output unit | Anything (even a fragment of a name or part of a list) | A complete expression, statement, item, or pattern |
| Type checking | After expansion | After expansion (same) |
| Recursive | Pre-C99 quirky, post-C99 limited | Yes, with `$($x:tt)*` repetition |
| Errors | Unhelpful (`error near "..."`) | Span-preserved, point at the macro **call site** |

C-preprocessor patterns that splice fragments of names (`#define MAKE_NAME(prefix) prefix##_handler`) or expand to **part** of a larger list of items **do not have a direct Rust macro analog** — the macro must always produce a syntactically complete unit. The chapter is explicit: *"some use cases of C preprocessor macros will not work, for example a macro that expands to part of a variable name or an incomplete set of items in a list."*

## When *not* to write a macro

The chapter pushes back against macros-by-default — *"in many cases a regular function is easier to understand and will be inlined to the same code as a macro"* ([[rust-embedded-book-c-tips-index]]). The `#[inline]` / `#[inline(always)]` attributes give explicit control over inlining; the compiler already auto-inlines small functions within a crate. The chapter cautions against forcing inlining: *"the compiler will automatically inline functions from the same crate where appropriate, so forcing it to do so inappropriately might actually lead to decreased performance."* Cross-crate inlining is **off by default** — see [[rust-embedded-book-design-patterns-hal-predictability|`C-INLINE`]] for the HAL-author-side discipline.

## Embedded Rust uses macros heavily

- **PAC register access**: [[Svd2Rust|`svd2rust`]]-generated [[PeripheralAccessCrate|PACs]] use the closure API `reg.write(|w| w.field().bits(0x42))` (file 13 [[rust-embedded-book-start-registers]]) — `w` is a writer proxy built by macro-generated `impl` blocks.
- **Concurrency frameworks**: [[RTIC]] is delivered as an attribute macro (`#[rtic::app(...)]`) that schedules tasks at compile time.
- **`cortex-m-rt`** entry / exception / interrupt attributes ([[ExceptionAttribute]] / [[InterruptAttribute]] / [[PanicHandlerAttribute]]) are procedural macros.
- **Tracing**: [[Defmt|`defmt`]]'s `info!` / `warn!` / `error!` are macros that interpolate format strings at compile time so device firmware ships only an integer index over RTT.
- **Hardware DSLs**: [[Embassy|`embassy`]]'s `#[embassy_executor::main]` and `#[task]` attributes; `register!` macros in some HAL crates.

## Connections

- [[CargoFeatures]] — the other mechanism the C-tips chapter names as a preprocessor replacement (compile-time code selection vs `#define`-style macros).
- [[rust-embedded-book-c-tips-index]] — file that introduces the macro system as the C-`#define` analog.
- [[ExceptionAttribute]] / [[InterruptAttribute]] / [[PanicHandlerAttribute]] — three concrete procedural attribute macros from [[CortexMRTCrate|`cortex-m-rt`]].
- [[Svd2Rust]] — code generator that emits a [[PeripheralAccessCrate|PAC]] whose ergonomic register-access API is built out of `macro_rules!` and procedural macros.
- [[Defmt]] — formatting-by-interning logging crate whose surface is entirely macros.
- [[RTIC]] / [[Embassy]] — concurrency frameworks delivered as attribute macros.
- [[ZeroCostAbstraction]] — macros are one of the mechanisms behind the zero-cost claim (compile-time expansion, no runtime dispatch).
- [[Rust2018Edition]] — the macro system has evolved across editions; `macro_rules!` semantics and `use` paths for macros were stabilized in 2018.
