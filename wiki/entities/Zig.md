---
title: "Zig"
type: entity
tags: [zig, programming-language, systems-programming, toolchain, compiler]
sources: [zig-getting-started, zig-in-depth-overview, zig-why-zig-vs-rust-d-cpp, zig-build-system-guide, zig-code-examples, zig-tools]
last_updated: 2026-06-07
---

# Zig

Zig is a general-purpose, systems programming language and an accompanying toolchain for maintaining robust, optimal, and reusable software. It positions itself as a modern alternative to [[CLanguage|C]] — small, explicit, with no hidden control flow or hidden memory allocations — while shipping a [[Compiler|compiler]] that can also build C/C++ code and cross-compile out of the box. The project is stewarded by the [[ZigSoftwareFoundation]] and its source lives on Codeberg (`codeberg.org/ziglang/zig`).

## Design philosophy & feature highlights

Per [[zig-in-depth-overview]], Zig is deliberately a **small, simple language** — its entire syntax fits in a 580-line PEG grammar — so effort goes into the application rather than the language. Its defining guarantees and features:

- **[[NoHiddenControlFlow|No hidden control flow]], no hidden allocations, no preprocessor, no macros.** Control flow happens only via keywords and explicit function calls — no operator overloading, no exceptions, no property accessors.
- **Performance and safety, choose two.** Four [[ZigBuildModes|build modes]] (`Debug`, `ReleaseSafe`, `ReleaseFast`, `ReleaseSmall`) mixable down to scope granularity, with runtime safety checks that crash rather than invoke [[UndefinedBehavior]]. Zig claims to be *faster than C* via whole-program compilation, carefully chosen illegal behavior (signed **and** unsigned overflow are illegal), a direct [[SIMD]] vector type, and real std data structures.
- **[[ZigOptional|Optional types]] (`?T`)** replace null pointers; unadorned pointers cannot be null.
- **[[ErrorUnion|Errors as values]] (`!T`)** that cannot be ignored, with `try`/`catch`/`switch`, error sets, and error return traces.
- **[[DeferStatement|defer / errdefer]]** for verifiable, scope-based resource cleanup.
- **[[ManualMemoryManagement|Manual memory management]] with explicit [[ZigAllocator|allocators]]** — the std lib works even freestanding.
- **[[Comptime|Compile-time code execution]], reflection, and generics** (a generic is a function returning a `type`); see also [[Metaprogramming]].
- **[[CInterop|First-class C interop]]** via `@cImport`/translate-c, plus `export` for C-ABI libraries; Zig is also a clang-compatible C compiler that **ships ~97 libc targets**.
- **[[CrossCompilation|First-class cross-compilation]]** — any Tier 3+ host can target any Tier 3+ target with no separate cross toolchain.
- **Integrated build system & package manager** — `build.zig` models the project as a DAG of steps ([[ZigBuildSystem]]); `build.zig.zon` pins hash-addressed dependencies ([[ZigPackageManager]]); both written in Zig. See [[ZigToolchain]].

Zig is self-hosted but builds from source using only a system C/C++ toolchain and [[LLVM]] (via a WebAssembly-based bootstrap), and aims to be friendly to package maintainers (system-integration flags, reproducible non-debug builds).

## Positioning vs C++, D, and Rust

Per [[zig-why-zig-vs-rust-d-cpp]], the case for Zig existing alongside C++, D, and Rust rests on a set of contrasts:

- **No hidden control flow** — D's `@property` functions, operator overloading (C++/D/Rust), and exceptions (C++/D/Go) can all make innocuous-looking code secretly call functions or skip statements; Zig forbids all three so control flow is always visible. See [[NoHiddenControlFlow]].
- **No hidden allocations** — there is no `new` keyword; the heap is a library concept, not a language feature. Contrast Go's allocating `defer` and resizable goroutine stacks, C++ coroutines' heap allocation, and Rust's std APIs that panic on out-of-memory with allocator-accepting APIs treated as "an afterthought" (rust-lang/rust#29802). Hidden allocations are framed as the enemy of **code reusability**. See [[ZigAllocator]] and [[RustStandardLibrary]].
- **A portable language for libraries** — because C is the de-facto portable language, Zig makes C-ABI conformance straightforward while preventing common implementation bugs, and is designed so "the laziest thing a programmer can do is handle errors correctly." See [[CInterop]] and [[ErrorUnion]].
- **Build system + package manager for existing projects** — Zig's tooling can replace autotools/cmake/make/scons/ninja and add native-dependency management even for 100%-C/C++ codebases (e.g. porting ffmpeg so it builds anywhere from a ~50 MiB download), eliminating the system dependencies that other package managers leave behind. See [[ZigBuildSystem]].
- **Simplicity / no macros** — C++, Rust, and D are large enough that one ends up "debugging one's knowledge of the programming language"; Zig has no macros yet implements features like formatted printing in the std library (whereas Rust bakes `format!` into the compiler). See [[Comptime]] and [[Metaprogramming]].

## Distribution model

Per [[zig-getting-started]], Zig is shipped as **self-contained archives** that can be placed anywhere on the filesystem; **multiple versions coexist without issue**. There are two channels:

- **Tagged releases** — recommended for projects that have dependencies and benefit from stability.
- **Development (nightly) builds** — for contributors helping develop Zig itself. Nightly users should read the `master` documentation.

Install paths documented on the getting-started page:
- **Direct download** + manual `PATH` setup (PowerShell `Machine`/`User` env vars on Windows; `export PATH=$PATH:...` in a shell rc on Linux/macOS/BSD).
- **Package managers** — Windows: WinGet (`winget install -e --id zig.zig`), Chocolatey (`choco install zig`), Scoop (`scoop install zig`, plus a `zig-dev` build); macOS: [[Homebrew]] (`brew install zig`), [[MacPorts]] (`sudo port install zig`); Linux: many distro managers.
- **Building from source** — documented in the project `README.md`.

## Tooling & getting started

The single CLI driver is `zig` (see [[ZigToolchain]]). The canonical "hello world" is `zig init` (scaffolds `build.zig`, `build.zig.zon`, `src/main.zig`, `src/root.zig`) followed by `zig build run`. Editor integration beyond syntax highlighting is provided by the [[ZigLanguageServer]] (ZLS, `zigtools/zls`). The official [[zig-tools]] catalog enumerates the editor ecosystem: ZLS as the recommended LSP layer, plus per-editor plugins (mostly syntax highlighters) for VS Code, Visual Studio, Sublime Text, Vim, Emacs, Kate, and the JetBrains family (ZigBrains / Fleet), many maintained under the official `ziglang` org on Codeberg.

## Connections

- [[ZigToolchain]] — the `zig` compiler/build-system CLI.
- [[ZigBuildSystem]] — build system (DAG of steps), even for C/C++ projects.
- [[ZigPackageManager]] — `build.zig.zon`, hash-pinned native dependencies.
- [[ZigBuildModes]] — `Debug`/`ReleaseSafe`/`ReleaseFast`/`ReleaseSmall`.
- [[ZigLanguageServer]] — recommended editor/LSP integration.
- [[ZigSoftwareFoundation]] — the non-profit behind the language.
- [[CLanguage]] — the language Zig aims to improve upon and interoperate with.
- [[Compiler]] — Zig ships an optimizing, multi-target compiler.
- [[CrossCompilation]] — first-class capability of the Zig toolchain.
- [[NoHiddenControlFlow]] — Zig's core design principle.
- [[Comptime]] — compile-time execution, reflection, and generics.
- [[ErrorUnion]] — error handling as values (`!T`, `try`, `catch`).
- [[ZigOptional]] — `?T` optional types replacing null.
- [[DeferStatement]] — `defer`/`errdefer` resource management.
- [[ZigAllocator]] — explicit allocator passing; no hidden allocations.
- [[ManualMemoryManagement]] — Zig's memory model.
- [[ZigSlice]] — `[]T` slices.
- [[CInterop]] — `@cImport`, `zig cc`, bundled libc, C-ABI export.
- [[Metaprogramming]] — done via comptime, not macros.
- [[LLVM]] — codegen backend and from-source build dependency.
- [[zig-getting-started]] — official onboarding source.
- [[zig-in-depth-overview]] — canonical feature tour of the language.
- [[zig-why-zig-vs-rust-d-cpp]] — rationale essay contrasting Zig with C++, D, and Rust.
- [[zig-build-system-guide]] — official reference for `zig build` and `build.zig`.
- [[zig-code-examples]] — official curated code samples (leak detection, C interop, comptime generics).
- [[zig-tools]] — official catalog of editor/LSP integrations (ZLS plus per-editor plugins).
