---
title: "Compiler Optimization"
type: concept
tags: [compilation, gcc, performance, debugging, c-language]
sources: [dis-3-1-gdb]
last_updated: 2026-05-17
---

# Compiler Optimization

**Compiler optimization** is the family of program-transformation passes a compiler applies to make generated code faster, smaller, or both — while preserving observable behavior per the language's [[AsIfRule|*as-if* rule]]. In [[GCC|`gcc`]] the dial is the `-O<level>` flag. [[dis-3-1-gdb|DIS Ch 3.1]] introduces optimization specifically as the **debug-hostile** axis paired against [[GccDashG|`-g`]] debug-info — *"compiler-optimized code is often very difficult to debug because sequences of optimized machine code often do not clearly map back to C source code."*

## The `-O<N>` levels in GCC

| Level | Behavior |
|---|---|
| `-O0` | No optimization. Direct one-to-one source-to-machine-code translation. **Default for debugging.** |
| `-O1` | Basic optimizations — dead-code elimination, simple register allocation, no time-expensive passes. |
| `-O2` | Standard production optimization — function inlining, loop unrolling, [[ConstantFolding|constant folding]], strength reduction, register allocation. **Conventional release flag.** |
| `-O3` | Aggressive — vectorization, more aggressive inlining, function cloning. May *enlarge* code. |
| `-Os` | Optimize for size — like `-O2` but excludes size-increasing transformations. |
| `-Oz` | Like `-Os` but more aggressive size reduction (also surfaces in `rustc` via [[OptLevel|`opt-level`]]). |
| `-Ofast` | `-O3` plus *unsafe* math reorderings (may violate IEEE-754). |
| `-Og` | Optimize for *debugging* — applies optimizations that don't impair the debugger. The intermediate option for *"I want some speed but still want `print var` to work."* |

## Why optimization breaks debugging

Five mechanisms [[dis-3-1-gdb|Ch 3.1]] alludes to:

- **Instruction reordering** — the compiler interleaves independent instructions for ILP / cache behavior; single-stepping jumps around the source non-monotonically.
- **Inlining** — called functions disappear into the caller; setting a breakpoint at the callee may never fire because the call site no longer exists.
- **Dead-code elimination** — entire variables that don't affect output get removed; [[GdbPrint|`print var`]] shows `<optimized out>`.
- **Loop transformations** — loop unrolling, vectorization, and loop-invariant code motion reshape the control-flow graph so source-line execution counts diverge from the source.
- **Register promotion** — a local that the source places on the stack may live entirely in a register; no memory address to inspect.

[[dis-3-1-gdb|Ch 3.1]]'s rule of thumb: **debug at `-O0 -g`**. If a bug only reproduces at `-O2`, that's evidence either of an [[UndefinedBehavior|undefined-behavior]] bug whose manifestation is optimization-sensitive, or (rarely) a compiler bug. In either case, the debugging discipline is **bisect the optimization level** (`-O1`, `-O2`, individual passes via `-f<pass>` / `-fno-<pass>`) to isolate which transformation surfaces the bug.

## Why optimization matters anyway

[[DiveIntoSystems]] motivates optimization throughout Chs 5–11 (architecture, memory hierarchy, parallelism): a modern CPU's effective performance comes from the compiler's exploitation of [[InstructionLevelParallelism|ILP]], [[CacheHierarchy|cache locality]], and [[SIMD|vector units]]. Production code with `-O2` is often **2–5× faster** than `-O0` code on the same machine; on tight numeric loops `-O3` with vectorization can be `10×+`.

The unifying lesson [[dis-3-1-gdb|Ch 3.1]] sets up: **the same flag that produces fast code makes that code opaque to a source-level debugger**. The discipline is to debug at `-O0 -g`, then re-test at `-O2`, and use [[Valgrind]] / sanitizers (deferred) when a bug is optimization-specific.

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[GccDashG]] — the orthogonal axis (`-g`) optimization interacts with.
- [[GCC]] — the compiler whose `-O` flag this concept centers on.
- [[GDB]] / [[Debugger]] — the tool optimization makes harder to use.
- [[DebugSymbol]] — present even at `-O2 -g` but partially decoupled from runtime state.
- [[OptLevel]] — the Rust-side analogue (`rustc -C opt-level=<N>`) the [[TheEmbeddedRustBook|Embedded Rust]] corpus covers.
- [[CompilationProcess]] — optimization happens at the [[CompilationStage|compile stage]].
- [[UndefinedBehavior]] — the class of bugs whose manifestation is most optimization-sensitive.
- [[Valgrind]] — sibling debugging tool; less perturbed by `-O2` than GDB (still benefits from `-g` for line numbers).
- [[CompilerWarnings]] — `-Wall -Wextra` is the *static* analog; `-O<N>` is the *runtime-performance* dial.
