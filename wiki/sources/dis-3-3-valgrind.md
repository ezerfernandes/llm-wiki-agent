---
title: "Dive into Systems — Ch 3.3 Debugging Memory with Valgrind"
type: source
tags: [dive-into-systems, c-debugging, valgrind, memcheck, memory-errors, heap, tooling]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C3-C_debug/valgrind.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 3.3** of *[[DiveIntoSystems]]* — the **second of the two debugging tools** [[dis-2-10-summary|Ch 2.10]] forward-referenced (the first being [[GDB]] in [[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]]). Introduces [[Valgrind]] and its default tool [[Memcheck]], framed as the **heap-memory-error detector** complementing [[GDB]]'s general-purpose [[Debugger|debugger]] role. The chapter's headline framing: *"Valgrind's Memcheck debugging tool highlights heap memory errors in programs."*

Catalogues the **four classes of heap errors** [[Memcheck]] catches — [[UninitializedReadError|uninitialized reads]], invalid [[Pointer|pointer]] [[DereferenceOperator|dereferences]] / out-of-bounds heap access, [[UseAfterFree|use-after-free]] (including freeing already-freed memory), and [[MemoryLeak|memory leaks]] — and operationalizes the workflow: compile with [[GccDashG|`gcc -g`]] (debug symbols), run via `valgrind -v ./a.out` (or redirect with `>& output.txt` for long output), optionally pass `--leak-check=yes` for per-leak detail.

Codifies the **three-part error-message anatomy** — error type / size, the source-level stack trace (function + file:line) of the offending access, and the allocation-site stack trace of the related heap chunk — and the **explicit scope boundary**: *"Valgrind does not detect stack memory access errors at the same granularity as it does with heap memory, and it does not detect memory access errors with global data memory."* The chapter recommends combining [[Valgrind]] with [[GDB]] — set a [[Breakpoint|breakpoint]] at the line Valgrind flagged, then inspect with `print` / `bt` to find the root cause.

## Key Claims

- **Tool framing**: *"Valgrind's [[Memcheck]] debugging tool highlights heap memory errors in programs."* [[Valgrind]] is the framework, [[Memcheck]] is the **default tool** (other tools — `cachegrind`, `callgrind`, `helgrind` — exist but are not covered here). `--tool=memcheck` is implicit.
- **Four heap-error classes detected**: (1) **[[UninitializedReadError|uninitialized memory reads]]** — accessing values from heap memory that hasn't been initialized (e.g., `x = ptr[3]` when that array index hasn't been assigned); (2) **invalid memory access** — *"reading (getting) or writing (setting) a value at an unallocated memory location, which often indicates an array out-of-bounds error"* — the [[BufferOverflow|buffer-overflow]] / under-run failure mode; (3) **[[UseAfterFree|use-after-free]]** including *"freeing already freed memory"* (i.e., [[DoubleFree|double-free]]); (4) **[[MemoryLeak|memory leaks]]** — *"a chunk of allocated heap memory space that is not referred to by any pointer variable in the program, and thus it cannot be freed."*
- **Two-step workflow**: (1) compile with [[GccDashG|`gcc -g`]] to embed [[DebugSymbol|debug symbols]] so Valgrind can map machine addresses back to source line numbers; (2) run `valgrind -v ./a.out` — the `-v` (verbose) flag adds extra diagnostic info, the default tool is [[Memcheck]]. Output goes to stderr; redirect with `valgrind -v ./a.out >& output.txt` when the trace is long.
- **`--leak-check=yes` for per-leak detail**: by default Memcheck prints a leak *summary* (counts); adding `--leak-check=yes` enables per-leak stack traces showing **where each leaked chunk was originally allocated**, turning the count into an actionable fix list.
- **Error-message anatomy (three parts)**: each Memcheck error has (a) **error type and size** (e.g., *"Invalid write of size 1"*); (b) **stack trace** at the offending access (function + file:line) showing **where the error happened**; (c) **allocation context** (function + file:line) showing **where the related heap chunk was originally `malloc`'d** — answering both *what went wrong* and *where the bad pointer came from*.
- **Worked sample output**: a representative error block from a `valgrindbadprog.c` example:
  ```
  ==31059== Invalid write of size 1
  ==31059==    at 0x4006C5: foo (valgrindbadprog.c:29)
  ==31059==  Address 0x52045c5 is 0 bytes after a block of size 5 alloc'd
  ==31059==    at 0x4C2DB8F: malloc
  ```
  The leading `==PID==` prefix tags every Valgrind output line with the inferior's PID — distinguishing Valgrind diagnostics from the program's own stdout/stderr.
- **Scope boundary — heap only**: *"Valgrind does not detect stack memory access errors at the same granularity as it does with heap memory, and it does not detect memory access errors with global data memory."* Out-of-bounds writes to a [[StackSection|stack]]-allocated array or [[GlobalVariable|globals]] in the [[DataSection|data section]] are largely invisible to [[Memcheck]] — for those, alternatives like [[AddressSanitizer]] (`-fsanitize=address`, not covered in this chapter) are needed. **This is the chapter's only explicit limitation note.**
- **Why heap-only**: Memcheck works by instrumenting every memory access at runtime via dynamic binary translation; it tracks per-byte allocation state (allocated / addressable / defined) for heap chunks because those are mediated by [[Malloc|`malloc`]] / [[Free|`free`]] which it intercepts, but the stack frame layout is invisible at this level.
- **Errors are crashes-in-waiting**: *"these errors result in erroneous program behavior or program crashing"* — the chapter's load-bearing motivation for running Valgrind on every C program before shipping, since the same bug may be silent on one run (memory happens to be zero, allocation happens to be padded) and fatal on the next.
- **Combine with [[GDB]]**: the recommended workflow when Memcheck flags an error at `file:N` is to fire up `gdb ./a.out`, set `break file:N` (using the [[GdbBreak|`break`]] command from [[dis-3-2-gdb-commands|Ch 3.2]]), `run` until halt, then [[GdbBacktrace|`bt`]] + [[GdbPrint|`print`]] to inspect locals. Closes the loop with Ch 3.1 / 3.2's GDB workflow.

## Key Quotes

> "Valgrind's Memcheck debugging tool highlights heap memory errors in programs." — chapter framing.

> "A memory leak is a chunk of allocated heap memory space that is not referred to by any pointer variable in the program, and thus it cannot be freed." — the corpus's clean operational definition of [[MemoryLeak|memory leak]].

> "[Invalid memory access is] reading (getting) or writing (setting) a value at an unallocated memory location, which often indicates an array out-of-bounds error." — the heap-side [[BufferOverflow|buffer-overflow]] characterization.

> "Valgrind does not detect stack memory access errors at the same granularity as it does with heap memory, and it does not detect memory access errors with global data memory." — the scope boundary.

> "These errors result in erroneous program behavior or program crashing." — the motivation for running Valgrind defensively.

## Connections

- [[DiveIntoSystems]] — book; this is **Ch 3.3**, the [[Valgrind]] companion to the [[dis-3-1-gdb|Ch 3.1]] + [[dis-3-2-gdb-commands|Ch 3.2]] [[GDB]] block.
- [[dis-2-10-summary]] — forward-referenced *"two debugging tools"*; **this source delivers the second one** ([[Valgrind]]), completing the pair.
- [[dis-3-1-gdb]] / [[dis-3-2-gdb-commands]] — the [[GDB]] sibling pair; Ch 3.3 explicitly recommends pairing Valgrind output with GDB inspection.
- [[Valgrind]] — **promoted from forward-ref stub** ([[dis-2-10-summary|Ch 2.10]] / [[dis-3-1-gdb|Ch 3.1]] / [[MemoryLeak]] / [[UseAfterFree]] mentions) **to fully treated tool**.
- [[Memcheck]] — **new concept page**; the default Valgrind tool, the actual heap-error detector.
- [[UninitializedReadError]] — **new concept page**; the *first* of Memcheck's four error classes — reading from heap memory that was never assigned. The class of bug that's *silent if memory happens to be zero, catastrophic otherwise*.
- [[MemoryLeak]] — already in wiki ([[dis-2-4-dynamic-memory]]); this source supplies the canonical detection tool and refines the *unreachable-chunk* definition.
- [[UseAfterFree]] — already in wiki ([[dis-2-4-dynamic-memory]]); this source supplies the canonical detection tool and includes [[DoubleFree|double-free]] under the same Memcheck umbrella (*"freeing already freed memory"*).
- [[BufferOverflow]] — already in wiki; this source supplies the heap-side detection tool (*"array out-of-bounds error"* on heap chunks). Stack-side buffer overflows fall outside Memcheck's scope.
- [[Malloc]] / [[Free]] — already in wiki; the API Memcheck intercepts to track per-byte allocation state.
- [[GccDashG]] — already in wiki; the prerequisite build flag for Valgrind's source-line mapping (same as for [[GDB]]).
- [[DebugSymbol]] — already in wiki; what `-g` embeds, what Valgrind reads to print `file:line` instead of raw addresses.
- [[GDB]] / [[GdbBacktrace]] / [[GdbPrint]] / [[Breakpoint]] — already in wiki; the recommended **next-step inspection chain** after Memcheck flags an error.
- [[HeapSection]] / [[StackSection]] / [[DataSection]] — already in wiki; Memcheck instruments **only** the heap; stack and data sections are out of scope.
- [[AddressSanitizer]] — **not covered** in this chapter, but flagged as the canonical alternative for stack/global coverage in the [[Valgrind]] / [[Memcheck]] pages.

## Contradictions

- None. Purely additive — extends [[MemoryLeak]] / [[UseAfterFree]] / [[BufferOverflow]] / [[DoubleFree]] with their canonical **detection tool**, completes [[dis-2-10-summary|Ch 2.10]]'s promised two-debugger pair, and promotes [[Valgrind]] from forward-ref stub to first-class page. Ch 3.1 / 3.2 framed [[GDB]] as the **general-purpose** debugger; Ch 3.3 frames [[Valgrind]] as the **memory-specific** debugger — orthogonal use cases of the same workflow stage (compile with `-g`, run, inspect).
