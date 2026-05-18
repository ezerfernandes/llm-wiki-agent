---
title: "The Embedded Rust Book — HAL Checklist"
type: source
tags: [rust, embedded, book-chapter, hal, checklist]
date: 2026-05-16
source_file: raw/book/src/design-patterns/hal/checklist.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — HAL Checklist

## Summary

File 32/44 of *[[TheEmbeddedRustBook]]* — the **top-level Checklist** of the *HAL Design Patterns* sub-chapter ([[rust-embedded-book-design-patterns-hal-index]], file 31/44). Pure aggregator page (~25 lines, no prose, no code): a single **GitHub-flavored Markdown checkbox list** consolidating every named pattern across the sub-chapter's four leaf files (`naming.md`, `interoperability.md`, `predictability.md`, `gpio.md`) into one printable / reviewable form. Eight checkboxes grouped under four headings, each labeled by a short-code (`C-CRATE-NAME`, `C-FREE`, `C-REEXPORT-PAC`, `C-HAL-TRAITS`, `C-CTOR`, `C-ZST-PIN`, `C-ERASED-PIN`, `C-PIN-STATE`) with hyperlink references to the leaf file anchors. Mirrors the [Rust API Guidelines Checklist](https://rust-lang.github.io/api-guidelines/checklist.html) convention — author parenthesis-glosses each pattern group with its **one-line intent**: *Naming* (*"crate aligns with Rust naming conventions"*), *Interoperability* (*"crate interacts nicely with other library functionality"*), *Predictability* (*"crate enables legible code that acts how it looks"*), *GPIO Interfaces* (*"GPIO Interfaces follow a common pattern"*). No new vocabulary; the patterns themselves are defined in the leaf files.

## Key Claims

- **The eight named [[HALCrate|HAL]] patterns** (short-code → group → intent):
  - `C-CRATE-NAME` — *Naming* — crate is named appropriately.
  - `C-FREE` — *Interoperability* — wrapper types provide a destructor method (give back the inner resource).
  - `C-REEXPORT-PAC` — *Interoperability* — HALs reexport their [[PeripheralAccessCrate|register access crate (PAC)]] so downstream code doesn't have to add a separate dependency.
  - `C-HAL-TRAITS` — *Interoperability* — types implement the [[EmbeddedHalCrate|`embedded-hal`]] traits — the M·N → M+N complexity-collapse mechanism from [[rust-embedded-book-portability-index]].
  - `C-CTOR` — *Predictability* — constructors are used instead of extension traits (favor explicit `::new()`-style construction over importing a trait that adds methods to a foreign type).
  - `C-ZST-PIN` — *GPIO Interfaces* — pin types are zero-sized by default — operationalizes [[ZeroSizedType|ZSTs]] / [[ZeroCostAbstraction]] from [[rust-embedded-book-static-guarantees-zero-cost-abstractions]] specifically for [[GPIO]] pins.
  - `C-ERASED-PIN` — *GPIO Interfaces* — pin types provide methods to erase pin and port (convert a strongly-typed `PA5`-style handle to a runtime-typed handle for heterogeneous collections / runtime dispatch).
  - `C-PIN-STATE` — *GPIO Interfaces* — pin state should be encoded as type parameters — the [[TypeStateProgramming|typestate]] pattern from [[rust-embedded-book-static-guarantees-design-contracts]] applied specifically to pin configuration (enabled/disabled, input/output, pull-up/pull-down/high-impedance).
- **Three-axis structure** of every checklist item: short-code + group + intent gloss + hyperlink to leaf-file anchor. The short-codes are designed to be **cite-able** in code review (*"this violates C-ZST-PIN"*) — a Rust-ecosystem convention inherited from the upstream API Guidelines.
- **Four named pattern groups** (matching [[rust-embedded-book-design-patterns-hal-index]]'s sub-chapter structure): Naming (1 item), Interoperability (3 items), Predictability (1 item), GPIO Interfaces (3 items).
- **GPIO is the dominant axis**: 3 of 8 checklist items (37.5%) are GPIO-specific (`C-ZST-PIN`, `C-ERASED-PIN`, `C-PIN-STATE`) — operationalizing the [[rust-embedded-book-static-guarantees-design-contracts|Design Contracts]] and [[rust-embedded-book-static-guarantees-zero-cost-abstractions|Zero Cost Abstractions]] worked examples (which used GPIO as the worked example) as **mandatory authoring conventions** for any embedded-Rust [[HALCrate|HAL]].
- **Position in corpus**: file 32/44 — the top-level catalog of the HAL Design Patterns sub-chapter; the entry-point for a HAL author who wants a quick gap-list to audit their crate against.

## Key Quotes

> "**Naming** *(crate aligns with Rust naming conventions)* — The crate is named appropriately ([C-CRATE-NAME])"

> "**Interoperability** *(crate interacts nicely with other library functionality)* — Wrapper types provide a destructor method ([C-FREE]) — HALs reexport their register access crate ([C-REEXPORT-PAC]) — Types implement the `embedded-hal` traits ([C-HAL-TRAITS])"

> "**Predictability** *(crate enables legible code that acts how it looks)* — Constructors are used instead of extension traits ([C-CTOR])"

> "**GPIO Interfaces** *(GPIO Interfaces follow a common pattern)* — Pin types are zero-sized by default ([C-ZST-PIN]) — Pin types provide methods to erase pin and port ([C-ERASED-PIN]) — Pin state should be encoded as type parameters ([C-PIN-STATE])"

## Connections

- [[TheEmbeddedRustBook]] — file 32/44; top-level Checklist of the *HAL Design Patterns* sub-chapter.
- [[rust-embedded-book-design-patterns-hal-index]] — parent sub-chapter opener (file 31/44); enumerated the four pattern groups this checklist collates.
- [[rust-embedded-book-design-patterns-index]] — grandparent chapter opener (file 30/44).
- [[rust-embedded-book-portability-index]] — file 27/44; introduced [[EmbeddedHalCrate]] and the M·N → M+N complexity-collapse argument that `C-HAL-TRAITS` operationalizes.
- [[rust-embedded-book-static-guarantees-design-contracts]] — file 25/44; the worked multi-axis typestate GPIO example that `C-PIN-STATE` codifies as authoring convention.
- [[rust-embedded-book-static-guarantees-zero-cost-abstractions]] — file 26/44; the [[ZeroSizedType|ZST]] / [[ZeroCostAbstraction]] mechanism that `C-ZST-PIN` mandates for pin types.
- [[HALCrate]] — pre-existing concept; the artifact this checklist audits.
- [[EmbeddedHalCrate]] — pre-existing entity; the trait set `C-HAL-TRAITS` requires implementing.
- [[PeripheralAccessCrate]] — pre-existing concept; the dependency `C-REEXPORT-PAC` requires re-exporting.
- [[GPIO]] — pre-existing concept; the worked example for 3 of 8 checklist items.
- [[TypeStateProgramming]] — pre-existing concept; the mechanism behind `C-PIN-STATE`.
- [[ZeroSizedType]] — pre-existing concept; the mechanism behind `C-ZST-PIN`.
- [[ZeroCostAbstraction]] — pre-existing concept; the framing behind `C-ZST-PIN`.
- Upstream [Rust API Guidelines Checklist](https://rust-lang.github.io/api-guidelines/checklist.html) — the convention this page mirrors (short-codes + checkbox aggregator).

## Contradictions

None — the file is a pure aggregator of the leaf-file patterns. No standalone substantive claims to contradict.
