---
title: "Dive into Systems — Ch 3.1 Debugging with GDB"
type: source
tags: [dive-into-systems, c-debugging, gdb, debugger, breakpoints, stack-frame, tooling]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C3-C_debug/gdb.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 3.1** of *[[DiveIntoSystems]]* — **opens Ch 3 *C Debugging Tools***, the chapter [[dis-2-10-summary|Ch 2.10]] forward-referenced for the **two debugging tools** Ch 2.4–2.6 named-failure-mode-by-failure-mode. Delivers the **first** of the two — **[[GDB|GNU GDB]]** as a general-purpose [[CLanguage|C]] [[Debugger|debugger]] — with [[Valgrind]] (the memory-error tool) deferred to Ch 3.2.

Promotes [[GDB]] from a forward-ref stub (the toolchain-inventory mention in [[rust-embedded-book-intro-tooling|Embedded Rust Ch I.4]]) to the corpus's **first-class GDB workflow page**. Frames GDB as *"a program that controls the execution of another program… it allows programmers to see what their programs are doing as they run"* — a [[Debugger|debugger]] is itself a process that runs another process under inspection, with the OS supplying the [[Ptrace|tracing]] machinery (named-and-deferred to later OS chapters).

Codifies the **GDB workflow**: (1) compile with [[GccDashG|`-g`]] [[DebugSymbol|debug-info]] and **no [[CompilerOptimization|optimization]]** (`-O2` is *"often very difficult to debug because sequences of optimized machine code often do not clearly map back to C source code"*); (2) launch `gdb ./a.out`; (3) set a [[Breakpoint|breakpoint]] with `break`; (4) [[GdbRun|`run`]] until breakpoint; (5) inspect with [[GdbPrint|`print`]] / [[GdbList|`list`]] / [[GdbDisplay|`display`]]; (6) advance with [[StepDebug|`next` / `step` / `continue`]]; (7) walk frames with [[GdbBacktrace|`bt`]] / [[GdbFrame|`frame`]]; (8) fix bugs, recompile, repeat.

## Key Claims

- **Defines a [[Debugger|debugger]]**: *"a program that controls the execution of another program… it allows programmers to see what their programs are doing as they run."* GDB is the canonical Unix C debugger.
- **Two bug taxonomies a debugger addresses**: (a) **logic bugs** — program runs to completion but produces wrong output, requiring inspection of state at suspected mis-step locations; (b) **crashes** — typically [[SegmentationFault|segfaults]] in C, requiring [[GdbBacktrace|stack-trace]] inspection at the crash site (or a [[CoreFile|core file]] post-mortem).
- **Compile flag discipline**: [[GccDashG|`gcc -g`]] embeds [[DebugSymbol|debug symbols]] — source-line numbers, variable names, types — that map binary addresses back to source. Without `-g`, GDB sees only addresses. `-g3` enables enhanced debugging (macro information). **Avoid `-O2`** and friends during debugging — optimized code reorders / eliminates / inlines instructions, breaking the binary-↔-source correspondence.
- **Six core commands**: `break` (set [[Breakpoint|breakpoint]]) / `run` (start program) / `cont` (resume after pause) / `next` (step over function calls) / `step` (step into function calls) / `print` (display variable value). Plus `list` (show source context), `where` / `bt` (call stack), `frame N` (switch [[StackFrame|frame]]), `display` (auto-print on each pause), `quit` (exit).
- **`next` vs `step` distinction**: both advance one source line, but `next` treats called functions as *one step* (skip over function body) while `step` *enters* the called function. The chapter's headline navigation primitive — *"to inspect function internals, use `step`; to treat them as opaque, use `next`."*
- **[[StackFrame|Stack-frame]] inspection** — GDB's [[GdbBacktrace|`backtrace`]] (alias `bt` / `where`) prints the active call stack ([[ExecutionStack|execution stack]]) with frame indices; `frame N` switches the inspection context to frame `N`, so `print var` in a chosen frame reads that activation's [[LocalVariable|locals]] and [[FunctionParameter|parameters]] — operationalizing the [[dis-1-4-functions|Ch 1.4]] stack-of-frames model **at runtime through a debugger lens**.
- **[[CoreFile|Core file]] post-mortem**: when a crashed program produces a core file (OS dump of process memory + register state at crash), `gdb ./a.out core` opens GDB on the post-mortem dump and `bt` / `print` work as in a live session — the canonical *"the bug happened, the program is gone, but I can still ask questions"* recovery path.
- **[[DataDisplayDebugger|DDD]]** mentioned as a GUI wrapper around GDB — the *"point-and-click"* alternative to the command-line interface for users who prefer visual breakpoint setting and variable inspection panels.

## Key Quotes

> "A debugger is a program that controls the execution of another program… it allows programmers to see what their programs are doing as they run." — opening definition of a [[Debugger|debugger]].

> "Compiler-optimized code is often very difficult to debug because sequences of optimized machine code often do not clearly map back to C source code." — justification for compiling with `-g` and **without** [[CompilerOptimization|`-O2`]] during debugging.

> "To inspect the function's behavior, use `step` instead of `next`." — the chapter's load-bearing navigation distinction.

## Connections

- [[DiveIntoSystems]] — book; this is **Ch 3.1**, opening Ch 3 *C Debugging Tools*.
- [[dis-2-10-summary|Ch 2.10 Summary]] — the forward-reference that named *"two debugging tools"* — [[GDB]] (this section) and [[Valgrind]] (Ch 3.2). This source **delivers** the GDB half of that promise.
- [[GDB]] — **promoted** from entity stub ([[rust-embedded-book-intro-tooling]] forward-ref) to fully treated debugger.
- [[Debugger]] — **new concept page** defining the debugger category.
- [[Breakpoint]] — **new concept page**; the chapter's primary control primitive.
- [[StepDebug]] — **new concept page**; the `next` vs `step` vs `continue` distinction.
- [[GdbBacktrace]] — **new concept page**; the `bt` / `where` / `frame N` stack-walk command family.
- [[CoreFile]] — **new concept page**; OS-dumped process state for post-mortem debugging.
- [[DebugSymbol]] — **new concept page**; what `-g` embeds, what GDB consumes.
- [[GccDashG]] — **new concept page**; the `gcc -g` invocation that makes debugging possible.
- [[DataDisplayDebugger]] — **new concept page**; DDD, the GUI wrapper.
- [[CompilerOptimization]] — **new concept page**; why `-O2` is debug-hostile.
- [[StackFrame]] — already in wiki (from [[dis-1-4-functions|Ch 1.4]]); this chapter operationalizes frame inspection at runtime.
- [[ExecutionStack]] / [[FunctionCall]] / [[ReturnStatement]] — what `backtrace` walks.
- [[SegmentationFault]] — the crash class GDB diagnoses (named at [[dis-2-2-pointers|Ch 2.2]]'s null-deref discussion, [[dis-2-4-dynamic-memory|Ch 2.4]]'s use-after-free, [[dis-1-5-arrays-strings|Ch 1.5]]'s buffer-overflow).
- [[GCC]] — the compiler whose `-g` flag GDB depends on.
- [[CLanguage]] — the language GDB primarily debugs (also handles C++, Objective-C, Go, Rust, Pascal, …).
- [[Valgrind]] — the **complementary** tool (Ch 3.2): GDB inspects program *behavior*, Valgrind inspects *memory access correctness*; together they form the **C debugging dyad** Ch 2.10 named.

## Contradictions

None — this is the first GDB workflow page in the corpus. The [[GDB]] entity stub from [[rust-embedded-book-intro-tooling]] is **expanded in-place** rather than duplicated; the *Embedded Rust* angle (GDB-over-remote-serial-protocol driving [[OpenOCD]] / [[ProbeRs]]) and the *Dive into Systems* angle (GDB on a hosted Unix program, local process under [[Ptrace|`ptrace`]]) are **non-overlapping use cases** of the same tool, so no conflict.
