---
title: "Dive into Systems — Ch 3.6 Debugging Multi-threaded Programs"
type: source
tags: [book, textbook, dive-into-systems, debugging, gdb, pthreads, threads, concurrency, multithreading]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C3-C_debug/gdb_pthreads.html
---

## Summary

Chapter 3.6 of *[[DiveIntoSystems]]* — closes Ch 3 *C Debugging Tools* by extending the [[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]] / [[dis-3-4-gdb-advanced|Ch 3.4]] / [[dis-3-5-gdb-assembly|Ch 3.5]] [[GDB]] block from **single-threaded** to **multi-threaded** programs. Frames debugging concurrent programs as fundamentally harder: multiple execution streams, thread interactions, races, and non-determinism complicate the linear *"set a breakpoint and step"* workflow Ch 3.1 codified. Surfaces three concrete coping recommendations (minimize active thread count during development, include the thread ID in debug output, scope verbose logging to one thread) and introduces the **[[GDB]] thread-debugging vocabulary** layered on top of [[Pthreads]]: (1) [[GdbInfoThreads|`info threads`]] to list all active threads (with `*` marking the current one), (2) [[GdbThreadSwitch|`thread <number>`]] to switch the inspection context to a specific thread's [[StackFrame|stack]] / [[LocalVariable|locals]] / [[CpuRegister|registers]], (3) thread-qualified breakpoints (`break <location> thread <N>`) that fire **only** when the named thread reaches the location, (4) [[GdbThreadApply|`thread apply all <command>`]] to broadcast a GDB command across all threads (e.g., [[GdbBacktrace|`thread apply all bt`]] for a snapshot of every thread's call stack), and (5) the diagnostic toggle `set print thread-events` for thread-creation / termination notifications. Names the **three thread identifiers** [[GDB]] tracks — the [[Pthreads|`pthread_t`]] library ID, the kernel-side **LWP ID** (lightweight process scheduling ID), and [[GDB]]'s own **GDB thread number** (the one users name in commands). Notes the default **stop-the-world breakpoint behaviour** — when **any** thread hits a [[Breakpoint|breakpoint]], **all** threads pause — and that [[GdbSet|`set`]]-configurable scheduler-locking can flip this to *pause only the triggering thread* for observing real concurrency. Worked example: a five-thread race on a shared `count += i` accumulator with thread-qualified breakpoints reveals interleaved updates. **Promotes [[Pthreads]] from forward-ref stub to first-class concept** (the corpus's first ingest of [[Pthreads]] from this book — full coverage in Ch 14). **4 new concept pages** ([[Pthreads]] promoted; [[GdbInfoThreads]]; [[GdbThreadSwitch]]; [[GdbThreadApply]]).

## Key Claims

- **Multi-threaded debugging is fundamentally harder than single-threaded debugging.** *"Debugging concurrent programs presents unique challenges due to multiple execution streams and thread interactions."* Three practical mitigations during development: minimize the number of threads, include the **thread ID in debug print output**, and limit verbose logging to **one** specific thread to suppress interleaved noise.
- **[[GDB]] tracks each thread by three distinct identifiers** — the [[Pthreads|`pthread_t`]] **Pthreads library ID** (the value `pthread_create` writes back), the kernel's **LWP ID** ([[OperatingSystem|OS]]-level [[LightweightProcess|lightweight-process]] scheduling ID), and [[GDB]]'s own **GDB thread number** — *"the identifier used within GDB commands (primary for debugging)"*. On most platforms the three IDs maintain a 1:1 correspondence, but implementations vary.
- **[[GdbInfoThreads|`info threads`]]** lists all active threads in the debuggee. The current thread is marked with `*`. Per-row columns: GDB thread number, [[Pthreads|`pthread_t`]] ID, LWP ID, and the source-line position the thread is paused at.
- **[[GdbThreadSwitch|`thread <number>`]]** switches the [[GDB]] inspection context to the named thread. After switching, [[GdbBacktrace|`bt`]] / [[GdbPrint|`print`]] / [[GdbInfo|`info locals`]] / [[GdbList|`list`]] resolve against that thread's [[StackFrame|stack frame]] and [[LocalVariable|local-variable]] [[VariableScope|scope]] — the multi-threaded analog of [[GdbBacktrace|`frame N`]]'s single-thread frame switch.
- **Thread-qualified breakpoints** via `break <location> thread <number>` fire **only** when the named thread reaches the location — other threads passing through that line are not halted. The targeted refinement of an otherwise global [[Breakpoint|breakpoint]] when debugging a specific thread's view of a [[Race|race]] or a thread-local logic bug.
- **[[GdbThreadApply|`thread apply all <command>`]]** broadcasts a [[GDB]] command across every thread. Canonical use: `thread apply all bt` — full multi-threaded call-stack snapshot (every thread's [[GdbBacktrace|backtrace]] printed in one go), the corpus's first **deadlock-and-livelock diagnostic primitive**.
- **`set print thread-events` on** makes [[GDB]] print a notification line when threads are **created** or **terminate** — useful for confirming thread lifecycle timing during debugging.
- **Default stop-the-world behaviour**: when **any** [[Breakpoint|breakpoint]] is reached, **all** threads pause. Configurable via scheduler-locking ([[GdbSet|`set scheduler-locking`]] modes) so that hitting a [[Breakpoint|breakpoint]] pauses **only** the triggering thread while other threads continue — needed when observing real concurrency patterns or interleavings the global stop would mask.
- **Worked example — racing five threads on shared `count`**: thread-specific breakpoints on `count += i` at line 77 reveal that different threads see different values of `count` at the same iteration index — the canonical [[RaceCondition|race-condition]] symptom and the entry point to [[Mutex|mutex]]-protected critical sections (full treatment deferred to Ch 14).

## Key Quotes

> *"Debugging concurrent programs presents unique challenges due to multiple execution streams and thread interactions."*

> *"When debugging multithreaded programs, the GDB user must keep track of which threads exist when issuing commands."*

> *"By default, reaching any breakpoint pauses all threads."*

## Connections

- [[DiveIntoSystems]] — Ch 3.6 of the book; **closes Ch 3 *C Debugging Tools*** as the **five-section debugging-tools block**: Ch 3.1 (narrative [[GDB]]) + Ch 3.2 ([[GDB]] reference) + Ch 3.3 ([[Valgrind]]) + Ch 3.4 (advanced [[GDB]]) + Ch 3.5 (assembly-level [[GDB]]) + Ch 3.6 (multi-threaded [[GDB]]). Six sections total in Ch 3.
- [[dis-3-1-gdb]] / [[dis-3-2-gdb-commands]] — the single-threaded [[GDB]] foundation Ch 3.6 generalizes.
- [[dis-3-4-gdb-advanced]] — the immediately structural sibling; Ch 3.4 covered cross-**process** features ([[Fork|`fork()`]] / [[Signal|signals]] / [[GdbAttach|attach]]), Ch 3.6 covers cross-**thread** features (`info threads` / `thread N` / `thread apply all`). The two cover [[GDB]]'s *"workflows beyond the single-process line-stepper"* in orthogonal directions.
- [[dis-3-5-gdb-assembly]] — the previous Ch 3 section (drops to assembly-instruction level); Ch 3.6 instead generalizes laterally to multi-threaded programs.
- [[GDB]] — the tool whose vocabulary is being extended to thread-aware debugging.
- [[Pthreads]] — promoted from forward-ref stub to first-class concept page in this ingest; the threading library [[GDB]]'s thread-debugging commands reflect over. Full coverage deferred to Ch 14.
- [[GdbInfoThreads]] — new concept; the entry point to thread-aware debugging.
- [[GdbThreadSwitch]] — new concept; `thread <N>` switches the inspection context (the multi-thread analog of [[GdbBacktrace|`frame N`]]).
- [[GdbThreadApply]] — new concept; `thread apply all <cmd>` broadcasts a [[GDB]] command across every thread.
- [[GdbInfo]] — extended with the `info threads` sub-command form (already named in the [[GdbInfo]] sub-command list, now fully treated here).
- [[GdbBreakpointManagement]] — extended with the `break <loc> thread <N>` qualifier.
- [[GdbSet]] — extended with `set scheduler-locking` and `set print thread-events`.
- [[Breakpoint]] — extended with the thread-qualified form and the default-stop-the-world semantics.
- [[Thread]] — the abstraction the chapter operates over.
- [[RaceCondition]] — the bug class the worked five-thread `count += i` example surfaces.
- [[parproc-ch01-intro-parallel-processing]] — the corpus's existing first-class [[Pthreads]] coverage (Pacheco *Parallel Processing*); Ch 3.6 is *Dive into Systems*'s **first** [[Pthreads]] sighting (full coverage in DIS Ch 14).

## Contradictions

None. Ch 3.6 strictly extends the [[GDB]] vocabulary from prior Ch 3 sections — every command added (`info threads` / `thread N` / `thread apply all` / `break ... thread N` / `set scheduler-locking` / `set print thread-events`) is **new**. The default-stop-the-world breakpoint behaviour is not a revision but a clarification of the prior single-threaded `break` semantics ([[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]]) generalized to N threads.
