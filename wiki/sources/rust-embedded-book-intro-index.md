---
title: "The Embedded Rust Book — Introduction"
type: source
tags: [rust, embedded, book-chapter, embedded-systems, microcontroller]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/index.md
---

# The Embedded Rust Book — Introduction

## Summary

The opening chapter of *[[TheEmbeddedRustBook|The Embedded Rust Book]]*, an introductory text on using the [[RustLanguage|Rust]] programming language for **"[[BareMetalProgramming|bare-metal]]" [[EmbeddedSystems|embedded systems]]** such as [[Microcontroller|microcontrollers]]. The chapter scopes audience, prerequisites, and conventions: it targets developers who want embedded programming with Rust's higher-level safety guarantees, assumes Rust 2018 fluency *or* embedded experience in C/C++/Ada, standardizes examples on the [[ARMCortexM|ARM Cortex-M]] architecture using the [[STM32F3DISCOVERY]] dev board, and is coordinated by the [[RustEmbeddedWorkingGroup|Rust Embedded Working Group]]'s resources team. Dual MIT / Apache 2.0 (code) + CC-BY-SA 4.0 (prose) license. The chapter is administrative rather than technical — it sets the contract for the rest of the book.

## Key Claims

- **Scope**: the book has three goals — get developers onto embedded Rust quickly (env setup), share *current* best practices for using Rust's language features to write correct embedded software, and serve as a cookbook for tasks like mixing C and Rust in one project.
- **Architecture standardization**: all examples target the [[ARMCortexM|ARM Cortex-M]] architecture for tractability, but the book "doesn't assume that the reader is familiar with this particular architecture" and explains Cortex-M specifics where needed. This is a *pedagogical concession*, not a Rust-embedded constraint — Rust runs on many embedded ISAs.
- **Reader prerequisites** (either-or): (a) comfortable writing/debugging Rust on the desktop and familiar with the [[Rust2018Edition|Rust 2018 edition]] idioms; *or* (b) comfortable doing embedded development in C/C++/Ada, knowing **[[CrossCompilation|cross compilation]]**, **[[MemoryMappedIO|memory-mapped peripherals]]**, **[[Interrupt|interrupts]]**, and common interfaces like **[[I2C]]**, **[[SPI]]**, and **serial / UART**. The "Other Resources" section points readers to the [[RustBook|Rust Book]], the [[DiscoveryBook|Discovery Book]], the [[EmbeddedRustBookshelf|Embedded Rust Bookshelf]], the [[Embedonomicon]], the embedded FAQ, and Google's *Comprehensive Rust: Bare Metal* 4-day class.
- **Hardware target**: examples use the **[[STM32F3DISCOVERY]]** dev board from [[STMicroelectronics]]. The book recommends purchasing one for following along. The board is Cortex-M-based, but peripherals and implementation details vary between vendors and even between MCU families from the same vendor — a recurring source of portability friction in the embedded domain.
- **Reading order**: front-to-back. "Later chapters build on concepts in earlier chapters."
- **Governance**: the book is developed in `github.com/rust-embedded/book` by the [[RustEmbeddedWorkingGroup|Rust Embedded WG]]'s **resources team**; bug reports and PRs (typo fixes + new content) welcome.
- **Translations**: volunteer-maintained Japanese and Chinese translations.
- **License**: code under dual [[MITLicense|MIT]] / [[ApacheLicense2|Apache 2.0]]; prose / images under [[CCBYSA4|CC-BY-SA 4.0]] requiring attribution + license link + change indication + same-license redistribution.

## Key Quotes

> "Welcome to The Embedded Rust Book: An introductory book about using the Rust Programming Language on 'Bare Metal' embedded systems, such as Microcontrollers." — opening framing; defines the corpus

> "Embedded Rust is for everyone who wants to do embedded programming while taking advantage of the higher-level concepts and safety guarantees the Rust language provides." — Rust-in-embedded value proposition: safety + abstraction without giving up bare-metal control

> "This book tries to be as general as possible but to make things easier for both the readers and the writers it uses the ARM Cortex-M architecture in all its examples." — the standardization concession driving the rest of the corpus

## Connections

- [[RustLanguage]] — the language whose embedded use is the entire subject of the book.
- [[RustEmbeddedWorkingGroup]] — governing body; coordinates the book and the broader Embedded Rust Bookshelf.
- [[STMicroelectronics]] — vendor of the [[STM32F3DISCOVERY]] reference board used across all examples.
- [[EmbeddedSystems]] — the broader domain the book targets.
- [[Microcontroller]] — the specific class of embedded compute the book focuses on.
- [[BareMetalProgramming]] — the no-OS execution model assumed by every example.
- [[ARMCortexM]] — the standardized ISA / core profile family used in examples.
- [[CrossCompilation]] — assumed-known prerequisite (or to be learned); the host-vs-target toolchain split that defines embedded build flows.

## Contradictions

- None within the wiki. This ingest opens a **new domain** (embedded systems / systems programming) with no overlap to the existing ML/LLM/math corpora. No claims contradict prior content.

## Notes for the Embedded Rust corpus

- This is **file 1 of 44** of *The Embedded Rust Book*. The chapter is intentionally light — it bounds the scope rather than introducing technical concepts. Substantive content begins in the next chapter.
- Forward-pointers worth tracking as the corpus grows: every later chapter is expected to operationalize either *Rust language features used in embedded* (e.g. `no_std`, ownership at the [[MemoryMappedIO|MMIO]] boundary, type-state APIs for peripherals) or *toolchain mechanics* (cross-compilation, linker scripts, debug probes, RTT). These will need their own concept pages on first substantive mention.
