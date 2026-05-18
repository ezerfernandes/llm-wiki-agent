---
title: "Memcheck (Valgrind Tool)"
type: concept
tags: [c-debugging, valgrind, memory-errors, heap, dynamic-analysis, tooling]
sources: [dis-3-3-valgrind]
last_updated: 2026-05-17
---

# Memcheck

**Memcheck** is [[Valgrind]]'s **default tool** — the per-byte heap-state tracker that detects [[UninitializedReadError|uninitialized reads]], invalid [[Pointer|pointer]] [[DereferenceOperator|dereferences]] / out-of-bounds heap access, [[UseAfterFree|use-after-free]] (including [[DoubleFree|double-free]]), and [[MemoryLeak|memory leaks]]. When a programmer says *"run it under Valgrind,"* they almost always mean *"run it under Memcheck."*

Per [[dis-3-3-valgrind|DIS Ch 3.3]]: *"Valgrind's Memcheck debugging tool highlights heap memory errors in programs."*

## What Memcheck tracks

For every byte of heap memory, Memcheck maintains two bits of shadow state:

| Bit | Meaning |
|---|---|
| **A** (addressable) | Is this byte inside a currently-allocated heap chunk? Set by [[Malloc|`malloc`]], cleared by [[Free|`free`]]. |
| **V** (valid / defined) | Has this byte been *written* since allocation? Tracked at bit granularity for ultra-fine uninitialized-read detection. |

Every load and store the program executes is checked against this shadow state — addressable=0 → invalid access error; addressable=1 but valid=0 → uninitialized read error.

## The four error classes

1. **[[UninitializedReadError|Uninitialized read]]** — V-bit clear at load time. Memcheck propagates V-bits through arithmetic, so an uninitialized byte that's added to a known value is still flagged as uninitialized — error reported only when the value is *used in a branch or syscall*, suppressing false positives on innocent copies.
2. **Invalid read / write** — A-bit clear at access time. Heap-side [[BufferOverflow|buffer overflow]], use-after-free, or wild-pointer dereference. Memcheck also pads each allocation with a red zone of A=0 bytes so off-by-one overruns are caught.
3. **[[UseAfterFree|Use-after-free]] and double-free** — touching or re-`free`ing a chunk after [[Free|`free`]]. Memcheck delays actual reuse of freed chunks (free queue) so most UAF accesses still hit A=0 memory and get caught.
4. **[[MemoryLeak|Leaks]]** — at exit, Memcheck walks the heap and classifies chunks by reachability:
   - **definitely lost** — no pointer reaches it (the canonical leak — fix this).
   - **indirectly lost** — only reachable through other definitely-lost chunks (fix the parent and these go away).
   - **possibly lost** — pointer found but points into the middle of a chunk (ambiguous — could be valid for interior-pointer designs).
   - **still reachable** — pointer found at exit, just never `free`d (often benign — globals freed implicitly by process exit).

## Invocation

[[Memcheck]] is selected by **default**; the explicit form is `valgrind --tool=memcheck ./a.out`. Useful flags from [[dis-3-3-valgrind|Ch 3.3]] + standard knowledge:

| Flag | Effect |
|---|---|
| `--tool=memcheck` | Explicit selection (default). |
| `-v` | Verbose mode (DIS Ch 3.3's recommended baseline). |
| `--leak-check=yes` / `=full` | Per-leak stack traces showing each chunk's [[Malloc|`malloc`]] site. |
| `--show-leak-kinds=all` | Report all four leak classes (default is `definite,possible`). |
| `--track-origins=yes` | For uninitialized reads, walk back to find *where* the uninitialized value was first computed (much slower, very useful). |
| `--show-reachable=yes` | Treat *still-reachable* chunks as errors too (strict mode). |
| `--error-exitcode=N` | Exit with code N if any errors found (CI integration). |

## Error format

Every Memcheck error is the three-part block from [[dis-3-3-valgrind|Ch 3.3]]:

```
==31059== Invalid write of size 1
==31059==    at 0x4006C5: foo (valgrindbadprog.c:29)
==31059==  Address 0x52045c5 is 0 bytes after a block of size 5 alloc'd
==31059==    at 0x4C2DB8F: malloc
```

(error type/size, access stack trace, allocation context). The `==PID==` prefix separates Memcheck diagnostics from the program's own output.

## Scope and limits

- **Heap only** — per [[dis-3-3-valgrind|Ch 3.3]] *"Valgrind does not detect stack memory access errors at the same granularity as it does with heap memory, and it does not detect memory access errors with global data memory."*
- **Slowdown** — ~10–50× runtime cost. Practical for unit tests and short programs; impractical for production hot paths.
- **No recompilation** — works on any unmodified binary (contrast [[AddressSanitizer]] which is build-time).

## Connections

- [[Valgrind]] — the host framework; Memcheck is one tool among several (cachegrind / callgrind / helgrind not covered in [[dis-3-3-valgrind|Ch 3.3]]).
- [[UninitializedReadError]] — the V-bit-driven detection class unique to Memcheck.
- [[MemoryLeak]] / [[UseAfterFree]] / [[DoubleFree]] / [[BufferOverflow]] — the heap-side bug taxonomy Memcheck catches.
- [[Malloc]] / [[Free]] — the intercepted API; the substrate for A-bit / V-bit shadow tracking.
- [[AddressSanitizer]] — the compiler-instrumented alternative; faster, stack/global coverage, requires recompilation.
- [[GccDashG]] / [[DebugSymbol]] — the build-side prerequisite for source-line mapping.
- [[GDB]] — the recommended next step once Memcheck flags an error (set a [[Breakpoint|breakpoint]] at the flagged line, [[GdbBacktrace|`bt`]] / [[GdbPrint|`print`]] for root cause).
- [[DiveIntoSystems]] / [[dis-3-3-valgrind]] — introducing source.
