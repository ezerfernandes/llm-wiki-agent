---
title: "Why Zig When There is Already C++, D, and Rust?"
type: source
tags: [zig, language-design, comparison, c, cpp, rust, d, philosophy]
date: 2026-06-07
source_file: https://ziglang.org/learn/why_zig_rust_d_cpp/
---

## Summary
The official Zig rationale essay arguing why a new systems language is worth building alongside C++, D, and Rust. It is organized around a set of "no hidden …" guarantees (no hidden control flow, no hidden allocations) plus pitches for an optional standard library, portability for libraries, a build-system-as-package-manager, simplicity (no macros), and a self-contained toolchain. Each section contrasts a specific Zig design decision against how C++, D, Rust, and Go handle the same concern.

## Key Claims
- **No hidden control flow.** "If Zig code doesn't look like it's jumping away to call a function, then it isn't." In `var a = b + c.d; foo(); bar();` it is guaranteed that only `foo()` then `bar()` are called, without knowing any types. Counterexamples: D's `@property` functions (field-access syntax can call a function on `c.d`); operator overloading in C++/D/Rust (so `+` can call a function); throw/catch exceptions in C++/D/Go (so `foo()` can throw and skip `bar()`). The stated purpose is readability. (Caveat: even Zig's `foo()` could deadlock and skip `bar()`, possible in any Turing-complete language.) Links to [[NoHiddenControlFlow]].
- **No hidden allocations.** Zig has no `new` keyword and no language feature that uses a heap allocator; the entire heap concept is managed by library/application code, not the language. If you never initialize a heap allocator, the program will not heap-allocate. Every std feature that allocates accepts an `Allocator` parameter, so the std library supports freestanding targets (e.g. `std.ArrayList`, `std.AutoHashMap` work for bare-metal). Custom allocators make manual memory management easy: a debug allocator detects use-after-free / double-free and prints leak stack traces; an arena allocator frees many allocations at once. Counterexamples: Go's `defer` allocates to a function-local stack (can OOM inside a loop); C++ coroutines heap-allocate to call a coroutine; Go function calls can heap-allocate because goroutine stacks resize; Rust's main std APIs panic on OOM and the allocator-accepting APIs are "an afterthought" (cites rust-lang/rust#29802); GC languages hide allocations everywhere. The core problem with hidden allocations is that it kills **reusability** of code across deployment environments. Links to [[ZigAllocator]], [[ManualMemoryManagement]].
- **First-class support for no standard library.** The std library is entirely optional and only compiled in per used API. Zig has equal support for linking libc or not; it is friendly to bare-metal and high-performance work. Example: Zig WebAssembly programs can use normal std features yet still produce the tiniest binaries among Wasm-targeting languages.
- **A portable language for libraries.** Code reuse is a holy grail undermined in practice. Real-time apps disqualify any GC / non-deterministic dependency; languages that make ignoring errors easy tempt re-implementation; C is currently the most portable/versatile language so any language unable to interact with C risks obscurity. Zig aims to be the new portable library language by (a) making C-ABI conformance for external functions straightforward and (b) adding safety + design that prevents common implementation bugs. Zig is designed so "the laziest thing a programmer can do is handle errors correctly." Links to [[CInterop]], [[ErrorUnion]].
- **A package manager and build system for existing projects.** Zig is a toolchain, not just a language, shipping a build system + package manager useful even for traditional C/C++ projects. It can replace autotools, cmake, make, scons, ninja, and adds a package manager for native dependencies — even when 100% of the codebase is C/C++. Example: porting ffmpeg to the Zig build system lets you compile ffmpeg on/for any supported system using only a ~50 MiB Zig download, including cross-compilation. System package managers (apt-get, pacman, homebrew) are great for end users but insufficient for developers; a language-specific package manager can be the difference between zero and many contributors, especially on Windows where there is no package manager and C/C++ dependencies can be fatal. Even building Zig itself trips up contributors on the LLVM dependency. Emphasis: "Other languages have package managers but they do not eliminate pesky system dependencies like Zig does." Links to [[ZigBuildSystem]].
- **Simplicity / no macros.** C++, Rust, and D have so many features that they distract from the application — "debugging one's knowledge of the programming language instead of debugging the application." Zig has no macros yet expresses complex programs clearly and non-repetitively. Even Rust has special-case macros like `format!` implemented in the compiler itself; in Zig the equivalent function is implemented in the standard library with no special-case compiler code. Links to [[Comptime]], [[Metaprogramming]].
- **Tooling.** Zig downloads as binary archives for Linux, Windows, macOS: install by extracting a single archive (no system config); statically compiled (no runtime deps); uses LLVM for optimized release builds while using Zig's own backends for faster compilation; has a backend that outputs C code; out-of-the-box cross-compilation to most major platforms; ships libc source compiled on demand for any supported platform; build system with concurrency and caching; compiles C and C++ with libc support; drop-in GCC/Clang CLI compatibility via `zig cc`; includes a Windows resource compiler. Links to [[ZigToolchain]].

## Key Quotes
> "If Zig code doesn't look like it's jumping away to call a function, then it isn't." — opening of the "No hidden control flow" section
> "The entire concept of the heap is managed by library and application code, not by the language." — on no hidden allocations
> "Zig is designed such that the laziest thing a programmer can do is handle errors correctly." — on portability for libraries
> "Other languages have package managers but they do not eliminate pesky system dependencies like Zig does." — on the build-system-as-package-manager pitch
> "Zig has no macros yet is still powerful enough to express complex programs in a clear, non-repetitive way." — on simplicity

## Connections
- [[Zig]] — this is the canonical positioning/rationale document for the language; informs the entity's comparison section.
- [[NoHiddenControlFlow]] — the essay's lead argument and Zig's central design principle, contrasted against D `@property`, operator overloading (C++/D/Rust), and exceptions (C++/D/Go).
- [[ZigAllocator]] — "no hidden allocations" is sourced here, including the Go `defer`/goroutine-stack, C++ coroutine, and Rust OOM-panic counterexamples.
- [[ManualMemoryManagement]] — explicit heap management and custom (debug/arena) allocators.
- [[CInterop]] — C-ABI conformance is central to the "portable language for libraries" claim.
- [[ErrorUnion]] — "laziest thing is to handle errors correctly" underpins the library-reuse argument.
- [[Comptime]] / [[Metaprogramming]] — the "no macros, yet `format!` is in the std lib not the compiler" simplicity argument.
- [[ZigBuildSystem]] — the build-system-as-package-manager pitch for existing C/C++ projects (ffmpeg, ~50 MiB download).
- [[ZigToolchain]] — the self-contained tooling list (statically compiled, `zig cc`, bundled libc, cross-compilation).
- [[CrossCompilation]] — out-of-the-box cross-compilation is a headline tooling feature.
- [[CLanguage]] — framed as the incumbent portable language Zig wants to interoperate with and supersede.
- [[Compiler]] / [[CompilerOptimization]] — LLVM for optimized release builds vs Zig's own fast backends; a C-output backend.
- [[LLVM]] — named as the optimized-release backend and the dependency that trips up contributors building Zig itself.
- [[RustLanguage]] — contrasted on operator overloading, OOM-panic std APIs, and compiler-baked `format!`.
- [[RustStandardLibrary]] — directly contrasted: Rust's main std APIs panic on OOM and allocator-accepting APIs are "an afterthought" (rust-lang/rust#29802).
- D and C++ — contrasted via `@property` (D), operator overloading (both), exceptions (both), and feature bloat; neither has a dedicated wiki page (left as prose to avoid broken links).

## Contradictions
- None. This source is consistent with the existing Zig pages ([[zig-in-depth-overview]], [[zig-getting-started]]); it reinforces and supplies the comparative rationale behind their feature lists rather than conflicting with them.
