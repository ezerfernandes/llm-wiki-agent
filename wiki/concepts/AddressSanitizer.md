---
title: "AddressSanitizer (ASan)"
type: concept
tags: [c-debugging, tooling, memory-errors, dynamic-analysis, compiler-instrumentation]
sources: [dis-3-3-valgrind]
last_updated: 2026-05-17
---

# AddressSanitizer

**AddressSanitizer (ASan)** is a **compile-time-instrumented** memory-error detector for [[CLanguage|C]] / C++ programs, originally developed at Google (Konstantin Serebryany et al., 2012) and shipped with both [[GCC|`gcc`]] (`-fsanitize=address`) and `clang`. It is the **canonical modern alternative** to [[Valgrind]] / [[Memcheck]] for catching heap [[BufferOverflow|buffer overflows]], [[UseAfterFree|use-after-free]], [[DoubleFree|double-free]], and [[MemoryLeak|leaks]] (the latter via the optional `-fsanitize=leak` companion).

[[dis-3-3-valgrind|DIS Ch 3.3]] does **not** mention ASan — this page exists to record the field's actual landscape, since most modern C code is ASan-instrumented in CI even when [[Valgrind]] is also run.

## ASan vs Memcheck (the headline tradeoff)

| Dimension | [[Memcheck]] (Valgrind) | AddressSanitizer |
|---|---|---|
| **Instrumentation point** | Runtime — dynamic binary translation | Compile time — `-fsanitize=address` |
| **Recompilation needed** | No | Yes |
| **Slowdown** | ~10–50× | ~2× |
| **Memory overhead** | ~2–3× | ~3× (shadow memory) |
| **Stack-allocation errors** | Poor coverage | Full coverage (red zones around stack frames) |
| **Globals overflows** | No coverage | Full coverage |
| **Heap overflows** | Full | Full |
| **Use-after-free** | Full (free queue) | Full (quarantine) |
| **Uninitialized reads** | Full ([[UninitializedReadError]] V-bits) | None on ASan alone; needs **MemorySanitizer** (`-fsanitize=memory`, different tool) |
| **Production-ready** | No (too slow) | Sometimes (release builds with ASan have shipped at Google / Chrome) |

**Rule of thumb**: use ASan in CI on every commit; use [[Memcheck]] when you need uninitialized-read detection or can't recompile (third-party binaries, JITs).

## How it works (one-line)

The compiler inserts **shadow-memory** checks before every load and store: each 8 bytes of application memory has a corresponding 1-byte shadow value indicating which bytes are accessible. [[Malloc|`malloc`]] / [[Free|`free`]] are replaced with versions that update the shadow and surround allocations with **red zones** (poisoned bytes) that catch off-by-one overflows. Stack frames similarly get red zones inserted by the compiler around each local.

## Invocation

```bash
gcc -fsanitize=address -g program.c    # build with ASan
./a.out                                # ASan checks at runtime; errors → stderr + abort
ASAN_OPTIONS=detect_leaks=1 ./a.out    # enable leak detection (default on Linux)
```

Errors print a stack trace + faulting address with `==PID==ERROR: AddressSanitizer:` prefix — same general anatomy as [[Memcheck]] but compile-time-instrumented.

## Limits

- **Doesn't catch [[UninitializedReadError|uninitialized reads]]** — that's MemorySanitizer's job (`-fsanitize=memory`), and the two cannot be combined in a single binary.
- **Requires source recompilation** — won't help with third-party closed-source binaries or already-compiled images.
- **Memory overhead** makes it impractical for memory-constrained embedded targets.

## Connections

- [[Valgrind]] / [[Memcheck]] — the older, runtime-instrumented alternative; covered in [[dis-3-3-valgrind|DIS Ch 3.3]].
- [[BufferOverflow]] / [[UseAfterFree]] / [[DoubleFree]] / [[MemoryLeak]] — the heap-side bug classes ASan catches (matching Memcheck's coverage).
- [[UninitializedReadError]] — the class ASan **does not** catch on its own; MemorySanitizer fills that gap.
- [[Malloc]] / [[Free]] — the API ASan replaces with shadow-aware wrappers.
- [[StackSection]] / [[DataSection]] — the program-memory regions ASan covers that [[Memcheck]] does not.
- [[GccDashG]] / [[DebugSymbol]] — prerequisite for source-line mapping in ASan output.
- [[CompilerWarnings]] — `-Wall` / `-Wextra` are the static analog; ASan complements them at runtime.

## Sources

- [[dis-3-3-valgrind]] mentions [[Valgrind]] as the heap-error detector but does **not** cover ASan; this page is the wiki's own treatment of the alternative tool every C programmer in 2026 also uses.
