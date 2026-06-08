---
title: "Rust Standard Library (`libstd`)"
type: concept
tags: [rust, standard-library, hosted-environment]
sources: [rust-embedded-book-intro-no-std, zig-why-zig-vs-rust-d-cpp]
last_updated: 2026-06-07
---

# Rust Standard Library (`libstd`)

The full default [[RustLanguage|Rust]] standard library, exposed at [`doc.rust-lang.org/std`](https://doc.rust-lang.org/std/). `std` is what desktop Rust crates link against by default. In *embedded* terms, `std` is two things bundled into one:

1. A **common API surface over OS abstractions** — file system, networking, threads, processes, environment variables, memory management.
2. A **[[RustRuntime|runtime]]** that runs *before* `main()` — sets up stack-overflow protection, processes command-line arguments, and spawns the main thread ([[rust-embedded-book-intro-no-std]]).

Both halves assume there is an OS underneath providing system primitives (e.g. POSIX); `std` cannot work in a [[BareMetalProgramming|bare-metal]] environment ([[HostedEnvironment]] only). Opting out with [[NoStd|`#![no_std]`]] drops `std` and links only [[RustCoreLibrary|`core`]] instead.

## Why `std` is the wrong choice for firmware / kernels / bootloaders

The chapter is explicit: *"`#![no_std]` … makes no assumptions about the system. As such, no_std and libcore code can be used for any kind of bootstrapping (stage 0) code like bootloaders, firmware or kernels"* ([[rust-embedded-book-intro-no-std]]). The corollary — `std` *cannot* be used for those — is the inverse contract: the runtime + OS-coupling that makes `std` convenient on a hosted target makes it structurally unsuitable on bare metal.

## What you gain on the `std` side of the trade

The feature-delta table from [[rust-embedded-book-intro-no-std]] enumerates what `std` provides over `core` / `no_std`:

- Default heap + dynamic memory.
- Collections (`Vec`, `BTreeMap`, `HashMap` — the last requires `std`'s secure RNG).
- Stack-overflow protection.
- Pre-main init code ([[RustRuntime]]).
- The OS-abstraction layer (file system, threads, networking, …).

## Outside critique: OOM behavior

The [[Zig]] rationale essay [[zig-why-zig-vs-rust-d-cpp]] cites `std` as an example of *hidden allocation* policy it wants to avoid: "The main Rust standard library APIs panic on out of memory conditions, and the alternate APIs that accept allocator parameters are an afterthought," referencing [rust-lang/rust#29802](https://github.com/rust-lang/rust/issues/29802). The contrast is with [[ZigAllocator|Zig's explicit-allocator]] convention, where every allocating API takes an `Allocator` and surfaces failure as a value rather than panicking. (This is a cross-language design critique, not an embedded-Rust claim.)

## Connections

- [[NoStd]] — the attribute that opts a crate *out* of `std`.
- [[RustCoreLibrary]] — the platform-agnostic subset of `std`; what `no_std` falls back to.
- [[RustRuntime]] — the pre-main initialization layer embedded inside `std`.
- [[HostedEnvironment]] — the execution regime `std` assumes underneath.
- [[BareMetalProgramming]] — the regime where `std` is *not* available.
- [[HeapAllocation]] — one of the things `std` brings on by default; `no_std` makes it opt-in.
- [[RustLanguage]] — the language whose default library `std` is.
- [[ZigAllocator]] — contrasting explicit-allocator model that surfaces OOM as a value, not a panic.
- [[zig-why-zig-vs-rust-d-cpp]] — source for the OOM-panic critique of `std`.
