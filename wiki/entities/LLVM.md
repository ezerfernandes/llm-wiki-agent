---
title: "LLVM"
type: entity
tags: [llvm, compiler, toolchain, codegen, clang]
sources: [zig-in-depth-overview]
last_updated: 2026-06-07
---

# LLVM

LLVM is a widely used compiler infrastructure project providing reusable code-generation, optimization, and backend components, along with the Clang C/C++ frontend. Many systems languages — including [[Zig]] — use LLVM as a code-generation backend.

## Relationship to Zig

Per [[zig-in-depth-overview]], LLVM appears in two roles for [[Zig]]:

- **Build dependency** — although Zig is self-hosted, building the Zig compiler from source "only depends on system C/C++ toolchain and LLVM, using standard CMake build steps," made possible by a WebAssembly-based bootstrap process. (The page also notes a long-term goal of a C-based Zig interpreter to reduce this to an O(1) bootstrap step.)
- **C compiler / codegen** — Zig functions as a clang-compatible C compiler (`zig cc`), and the build system exposes LLVM-related debug output (`--verbose-llvm-ir`, `--verbose-llvm-bc`, `--verbose-llvm-cpu-features`), reflecting an LLVM-based code-generation path.

For size comparison, the overview notes that the Windows binary build of clang 8.0.0 from llvm.org is 132 MiB, versus Zig's ~50 MiB tarball that bundles a C compiler plus ~97 libc targets.

## Connections

- [[Zig]] — uses LLVM as a backend and a from-source build dependency.
- [[CInterop]] — Zig's clang-compatible `zig cc` C-compilation path.
- [[Compiler]] — LLVM is compiler infrastructure.
- [[CompilerOptimization]] — LLVM provides optimization passes.
- [[zig-in-depth-overview]] — source describing LLVM's role for Zig.
