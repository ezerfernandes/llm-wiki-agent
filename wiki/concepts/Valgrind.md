---
title: "Valgrind"
type: concept
tags: [c-debugging, tooling, memory-errors, heap, dynamic-analysis, instrumentation]
sources: [dis-3-3-valgrind, dis-2-10-summary, dis-3-1-gdb]
last_updated: 2026-05-17
---

# Valgrind

**Valgrind** is a **dynamic binary-instrumentation framework** for [[CLanguage|C]] / C++ programs whose flagship tool [[Memcheck]] detects **heap memory errors** — the [[UninitializedReadError|uninitialized reads]], invalid pointer dereferences, [[UseAfterFree|use-after-free]] (including [[DoubleFree|double-free]]), and [[MemoryLeak|memory leaks]] that [[GDB]] only sees as their downstream effects (a [[SegmentationFault|segfault]], a wrong output value, a corrupt allocator state).

Per [[dis-3-3-valgrind|DIS Ch 3.3]]: *"Valgrind's Memcheck debugging tool highlights heap memory errors in programs."* It is the **second of the two debugging tools** [[dis-2-10-summary|Ch 2.10]] forward-referenced — [[GDB]] being the first (delivered in [[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]]).

## What it catches (the four heap-error classes)

1. **[[UninitializedReadError|Uninitialized memory reads]]** — `x = ptr[3]` when that heap byte was never written. *Silent if the byte happens to be zero, catastrophic otherwise* — the class of bug that disappears under a debugger.
2. **Invalid heap access** — *"reading (getting) or writing (setting) a value at an unallocated memory location, which often indicates an array out-of-bounds error"* — the heap-side [[BufferOverflow|buffer overflow]] / under-run.
3. **[[UseAfterFree|Use-after-free]]** (including *"freeing already freed memory"*, i.e. [[DoubleFree|double-free]]) — touching or re-`free`ing a chunk after [[Free|`free`]].
4. **[[MemoryLeak|Memory leaks]]** — *"a chunk of allocated heap memory space that is not referred to by any pointer variable in the program, and thus it cannot be freed."*

## Workflow

```bash
gcc -g valgrindbadprog.c          # compile with debug symbols (DebugSymbol)
valgrind -v ./a.out               # default tool = memcheck; -v adds verbose info
valgrind -v ./a.out >& output.txt # redirect for long traces
valgrind --leak-check=yes ./a.out # per-leak stack traces (allocation site of each)
```

- `-g` ([[GccDashG]]) is the prerequisite — without [[DebugSymbol|debug symbols]] Valgrind prints raw addresses instead of `file:line`.
- `--tool=memcheck` is implicit (the default); other tools exist (`cachegrind`, `callgrind`, `helgrind`) but [[dis-3-3-valgrind|Ch 3.3]] does not cover them.
- `--leak-check=yes` upgrades the leak summary into per-leak detail.

## Error-message anatomy

Every [[Memcheck]] diagnostic is a three-part block tagged with the inferior's PID:

```
==31059== Invalid write of size 1
==31059==    at 0x4006C5: foo (valgrindbadprog.c:29)
==31059==  Address 0x52045c5 is 0 bytes after a block of size 5 alloc'd
==31059==    at 0x4C2DB8F: malloc
```

1. **What** — error type + size (`Invalid write of size 1`).
2. **Where it happened** — function + file:line of the bad access (`foo` at `valgrindbadprog.c:29`).
3. **Where the chunk came from** — allocation-site stack trace, so you can audit the `malloc` that handed out the bad pointer.

The `==PID==` prefix separates Valgrind output from the program's own stdout/stderr.

## Scope boundary

Per [[dis-3-3-valgrind|Ch 3.3]]: *"Valgrind does not detect stack memory access errors at the same granularity as it does with heap memory, and it does not detect memory access errors with global data memory."*

- **Heap** ([[HeapSection]]) — fully covered. [[Malloc|`malloc`]] / [[Free|`free`]] are intercepted so per-byte state (allocated / addressable / defined) is tracked.
- **Stack** ([[StackSection]]) — best-effort, much coarser. Out-of-bounds writes to a `char buf[16]` local often slip through.
- **Globals** ([[DataSection]]) — out of scope.

For full coverage including stack and globals, [[AddressSanitizer]] (`-fsanitize=address`, compiler-instrumented at build time) is the canonical alternative. ASan is *faster* (~2× vs Valgrind's ~10–50×) and catches stack errors, but requires recompilation; Valgrind runs on any unmodified binary.

## How it works (one-line)

Valgrind is a **dynamic binary translator**: it loads the program into a synthetic CPU, recompiles every basic block on the fly into instrumented intermediate code, then runs that. The instrumentation tracks per-byte metadata. The cost is the famous ~10–50× slowdown; the payoff is **no recompilation needed** and **catches errors that never trigger a visible failure**.

## Workflow integration with [[GDB]]

[[dis-3-3-valgrind|Ch 3.3]]'s recommended chain:
1. Run `valgrind --leak-check=yes ./a.out` — get the failing `file:N`.
2. Set [[GDB]] breakpoint there: `gdb ./a.out` → `break file:N` → `run`.
3. Inspect with [[GdbBacktrace|`bt`]] / [[GdbPrint|`print`]] / [[GdbInfo|`info locals`]] to find the root cause.

Valgrind finds *where*; GDB explains *why*.

## Connections

- [[Memcheck]] — Valgrind's default tool, the actual heap-error detector. *"Valgrind"* in casual usage almost always means *"Valgrind running Memcheck."*
- [[UninitializedReadError]] — first of the four classes Memcheck detects.
- [[MemoryLeak]] / [[UseAfterFree]] / [[DoubleFree]] / [[BufferOverflow]] — the failure modes Valgrind makes diagnosable; previously cataloged by [[dis-2-4-dynamic-memory|Ch 2.4]] without a detection tool, now paired with one.
- [[Malloc]] / [[Free]] — the allocator API Valgrind intercepts.
- [[GDB]] / [[GdbBacktrace]] / [[GdbPrint]] / [[Breakpoint]] — the inspection tools to chain after Valgrind localizes an error.
- [[GccDashG]] / [[DebugSymbol]] — the build-side prerequisite for source-line mapping.
- [[AddressSanitizer]] — the canonical alternative; faster, stack/global coverage, requires recompilation.
- [[HeapSection]] / [[StackSection]] / [[DataSection]] — the three [[ProcessMemory|program-memory regions]]; Valgrind covers only the first with full fidelity.
- [[DiveIntoSystems]] / [[dis-3-3-valgrind]] / [[dis-2-10-summary]] — introducing sources.
