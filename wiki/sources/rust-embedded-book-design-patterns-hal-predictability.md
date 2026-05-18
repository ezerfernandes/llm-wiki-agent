---
title: "The Embedded Rust Book — HAL Predictability"
type: source
tags: [rust, embedded, book-chapter, hal, predictability]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/design-patterns/hal/predictability.md
sources: [rust-embedded-book-design-patterns-hal-predictability]
---

## Summary

File 35/44 of *[[TheEmbeddedRustBook]]* — **third leaf-section** of the *HAL Design Patterns* sub-chapter ([[rust-embedded-book-design-patterns-hal-index]]) and the **Predictability** group of the [[rust-embedded-book-design-patterns-hal-checklist|HAL Checklist]] (groups Naming → Interoperability → **Predictability** → GPIO). Two named short-form patterns: **`C-CTOR`** — *"All [[Peripheral|peripherals]] to which the [[HALCrate|HAL]] adds functionality should be wrapped in a new type, even if no additional fields are required for that functionality. Extension traits implemented for the raw peripheral should be avoided."* — the wrapper-new-type-over-extension-trait discipline that makes [[BorrowChecker|borrow-checker]] reasoning, [[Singleton|singleton]] reclaim ([[rust-embedded-book-peripherals-singletons]]), and [[TypeStateProgramming|typestate]] parameterization ([[rust-embedded-book-static-guarantees-design-contracts]]) all attachable to the same surface; and **`C-INLINE`** — *"All 'small' functions should be marked `#[inline]`. […] Functions that are very likely to take constant values as parameters should be marked as `#[inline]`. This enables the compiler to compute even complicated initialization logic at compile time, provided the function inputs are known."* — the explicit cross-crate inlining hint that the Rust compiler does **not** apply by default, motivated by embedded's code-size sensitivity and necessary to realize the [[ZeroCostAbstraction|zero-cost-abstraction]] payoff established in [[rust-embedded-book-static-guarantees-zero-cost-abstractions]] across crate boundaries.

## Key Claims

- **`C-CTOR` — peripherals are wrapped in new types, not extended via traits**: *"All peripherals to which the HAL adds functionality should be wrapped in a new type, even if no additional fields are required for that functionality. Extension traits implemented for the raw peripheral should be avoided."*
- **Zero-field wrappers are still required**: the *"even if no additional fields are required"* clause makes the rule unconditional — a wrapper that is structurally just `pub struct Timer(TIMER0)` is still mandatory rather than `impl SomeTrait for TIMER0 { … }`. This is what makes [[rust-embedded-book-design-patterns-hal-interoperability|`C-FREE`]]'s `pub fn free(self) -> TIMER0` callable: extension traits could not consume the raw [[Peripheral|peripheral]] by value, but a new-type wrapper can.
- **`C-INLINE` — `#[inline]` is the explicit cross-crate inlining hint**: *"The Rust compiler does not by default perform full inlining across crate boundaries. As embedded applications are sensitive to unexpected code size increases, `#[inline]` should be used to guide the compiler."*
- **Default-off cross-crate inlining is named as the underlying mechanism**: the rule is **not** a Rust-language law but a [[Rustc|rustc]] policy — *generic* functions inline across crates because their bodies travel with the signature in crate metadata, but **non-generic** functions in a [[HALCrate|HAL]] crate that an application consumes will *not* inline unless `#[inline]` (or `#[inline(always)]`) is applied. `C-INLINE` is the authoring-side discipline that defeats this default.
- **"Small" functions should be `#[inline]`**: *"All 'small' functions should be marked `#[inline]`. What qualifies as 'small' is subjective, but generally all functions that are expected to compile down to single-digit instruction sequences qualify as small."* — single-digit instruction count is the operative cutoff for the author's judgment.
- **Constant-argument functions should be `#[inline]`**: *"Functions that are very likely to take constant values as parameters should be marked as `#[inline]`. This enables the compiler to compute even complicated initialization logic at compile time, provided the function inputs are known."* — this is the rule that turns hand-written `set_baud_rate(115200)` / `set_freq(MHz(168))` initializer calls into single-store instructions in the call site, recovering the [[ZeroCostAbstraction|zero-cost-abstraction]] property from [[rust-embedded-book-static-guarantees-zero-cost-abstractions]] across crate boundaries.

## Key Quotes

> "All peripherals to which the HAL adds functionality should be wrapped in a new type, even if no additional fields are required for that functionality. Extension traits implemented for the raw peripheral should be avoided." — the entire normative content of `C-CTOR`.

> "The Rust compiler does not by default perform full inlining across crate boundaries. As embedded applications are sensitive to unexpected code size increases, `#[inline]` should be used to guide the compiler as follows:" — the **why** sentence of `C-INLINE`; explicitly names the default-off cross-crate inlining policy as the motivating gap.

> "All 'small' functions should be marked `#[inline]`. What qualifies as 'small' is subjective, but generally all functions that are expected to compile down to single-digit instruction sequences qualify as small." — the **small-function** rule of `C-INLINE`.

> "Functions that are very likely to take constant values as parameters should be marked as `#[inline]`. This enables the compiler to compute even complicated initialization logic at compile time, provided the function inputs are known." — the **constant-argument** rule of `C-INLINE`, which operationalizes the [[ZeroCostAbstraction]] argument from file 26 (*"the ability to move certain behaviors to compile time execution or analysis"*) across the crate-boundary case.

The file is short-form (~25 lines, no code) — two named patterns, each two prose paragraphs, no worked code example. Like the [[rust-embedded-book-design-patterns-hal-naming|Naming]] and [[rust-embedded-book-design-patterns-hal-interoperability|Interoperability]] leaves, the patterns are designed to be **cite-able in code review** (*"this violates `C-CTOR`."* / *"this violates `C-INLINE`."*).

## Connections

- [[TheEmbeddedRustBook]] — file 35/44.
- [[rust-embedded-book-design-patterns-hal-index]] — parent sub-chapter (file 31/44).
- [[rust-embedded-book-design-patterns-hal-checklist]] — top-level checklist that lists `C-CTOR` under the **Predictability** group (file 32/44); `C-INLINE` is **not** in the checklist (the checklist enumerates only 8 patterns, and `C-INLINE` is the implicit ninth introduced by the leaf — the checklist is therefore **incomplete** relative to the leaf files, a minor inconsistency worth flagging).
- [[rust-embedded-book-design-patterns-hal-naming]] — first leaf-section (file 33/44, the **Naming** group).
- [[rust-embedded-book-design-patterns-hal-interoperability]] — prior leaf-section (file 34/44, the **Interoperability** group); `C-CTOR` is the **structural prerequisite** for `C-FREE` — only a new-type wrapper can have a consuming-`self` `free` method.
- [[HALCrate]] — the crate kind these two patterns govern.
- [[Peripheral]] — what `C-CTOR` mandates be wrapped (rather than extended via trait).
- [[BorrowChecker]] — extension traits can't consume the raw [[Peripheral|peripheral]] by value; new-type wrappers can, which is why `C-CTOR` is load-bearing for the [[Singleton|singleton]] reclaim discipline.
- [[Singleton]] — `C-CTOR` is the wrapper-type discipline the [[rust-embedded-book-peripherals-singletons|singleton]] pattern relies on.
- [[TypeStateProgramming]] — `C-CTOR` is also the structural prerequisite for the [[TypeStateProgramming|typestate]] parameterization in [[rust-embedded-book-static-guarantees-design-contracts]] — type parameters attach to a wrapper, not to the raw [[Peripheral|peripheral]].
- [[ZeroCostAbstraction]] — `C-INLINE` is the cross-crate-boundary mechanism for realizing the zero-cost-abstraction payoff from [[rust-embedded-book-static-guarantees-zero-cost-abstractions]]; without `#[inline]`, the file-26 example (`set_high()` compiling to a single store) would degrade to a non-inlined function call across the HAL/application boundary.
- [[rust-embedded-book-static-guarantees-zero-cost-abstractions]] — the chapter `C-INLINE` operationalizes across crate boundaries.
- [[rust-embedded-book-peripherals-singletons]] — the singleton discipline `C-CTOR` enables.

## Contradictions

- **Minor inconsistency with [[rust-embedded-book-design-patterns-hal-checklist|the HAL Checklist]]**: the file-32 checklist enumerates **eight** named patterns and lists only **`C-CTOR`** under *Predictability*; **`C-INLINE`** is introduced in this leaf file but is **not** in the checklist. Either the checklist is intentionally curated (skipping `C-INLINE` as a general Rust hygiene rule rather than a HAL-specific one) or it's an omission. **Flag for future check** if a downstream source cites a *"complete HAL pattern list"*.
- Otherwise **strictly additive** — `C-CTOR` is the wrapper-type discipline that makes both [[rust-embedded-book-design-patterns-hal-interoperability|`C-FREE`]] (consuming-`self` reclaim) and the [[TypeStateProgramming|typestate]] machinery from [[rust-embedded-book-static-guarantees-design-contracts]] structurally possible; `C-INLINE` is the cross-crate-boundary mechanism for the [[ZeroCostAbstraction|zero-cost-abstraction]] property from [[rust-embedded-book-static-guarantees-zero-cost-abstractions]].
