---
title: "Dive into Systems — 13.2 Processes"
type: source
tags: [textbook, operating-systems, processes, fork, exec, wait, scheduling, signals]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C13-OS/processes.html
---

## Summary

**Second leaf of Ch 13 *The Operating System*** of [[DiveIntoSystems]]. Section 13.2 operationalizes the [[Process|process]] abstraction the prior leaf [[dis-13-1-booting-running|13.1]] only named — defining a process as *"an instance of a program running in the system, which includes the program's binary executable code, data, and execution context"*, codifying the **four-state life-cycle** ([[ProcessState|Ready / Running / Blocked / Exited]]) and the OS-side bookkeeping (the **[[ProcessControlBlock|process control block]]**), separating **mechanism** ([[ContextSwitch|context switch]]) from **policy** ([[Scheduler|scheduling]]), and giving the [[CLanguage|C]]-surface POSIX [[SystemCall|system-call]] interfaces — [[Fork|`fork`]] (duplicate), [[Exec|`exec`]] (overlay), [[Wait|`wait`]] (reap) — that user code uses to create, replace, and synchronize processes. Introduces [[Multiprogramming|multiprogramming]] and [[Timesharing|timesharing]] as the two-layer story for keeping the CPU busy and ends with the **[[WallTime|wall time]] vs [[CPUTime|CPU time]]** distinction that makes process-aware benchmarking possible.

## Key Claims

- A **[[Process|process]]** = binary executable code + data + execution context (register values, stack location, current instruction); *"an instance of a program running in the system."*
- The OS maintains per-process state in a **[[ProcessControlBlock|process control block]]** (PCB): [[ProcessID|PID]], address-space information, execution-state register snapshot, allocated resources (open files), and current [[ProcessState|process state]].
- **Four process states** with explicit transitions: **Ready** (could run, not currently scheduled) ↔ **Running** (on CPU) ↔ **Blocked** (waiting for an event like disk I/O) → **Exited** (terminated, awaiting cleanup). A process reaches *Ready* via creation, event completion (unblock), or [[Timesharing|time-slice]] expiration.
- **Mechanism vs policy**: [[ContextSwitch|context switching]] is the *mechanism* (how the OS saves/restores process state); **[[Scheduler|scheduling]]** is the *policy* (which Ready process gets the CPU and for how long). Only Ready processes are scheduling candidates.
- **[[Multiprogramming]]**: multiple processes coexist; OS switches when one blocks on I/O, keeping the CPU busy. **[[Timesharing]]**: a multiprogramming variant where each process gets a short *time slice / quantum* (typically milliseconds), giving the illusion of exclusive system access while sharing fairly.
- **[[Fork|`fork()`]]** creates a new [[Process|process]] by **duplicating the caller** — child receives *"an exact copy of its parent's address and execution state"*; returns **twice**: `0` to the child, child's [[ProcessID|PID]] to the parent (or `-1` on failure in the parent only). Both parent and child resume from the fork return point; their output may interleave in **six possible orderings** in the worked print example.
- **Process hierarchy**: every process except [[Init|`init`]] has a parent; [[Init|`init`]] is the first user-level process created at boot and ancestor of all processes.
- **[[Exec|`execvp(char *filename, char *argv[])`]]** overlays the calling process's image with a new program — *"overwrites the process's address space with the specified executable"* and reinitializes execution state to the program's first instruction. On success it **never returns**; only an error returns from `exec`. The canonical pattern is **[[Fork|`fork`]] + [[Exec|`exec`]]**: parent forks, child execs.
- **[[Exit|`exit`]]** terminates a process, cleans up most state, and signals the parent via **[[Signal|`SIGCHLD`]]**. The terminated process becomes a **[[Zombie|zombie]]** in the [[ProcessState|Exited]] state until reaped.
- **[[Wait|`wait`]]** reaps a zombie child; if the child has not yet exited the parent enters the [[ProcessState|Blocked]] state until [[Signal|`SIGCHLD`]] arrives. **`waitpid(pid, ...)`** waits for a specific child. Shell foreground vs background execution (`a.out` vs `a.out &`) differs in whether the shell calls `wait` synchronously or installs it in a [[Signal|signal handler]].
- A **[[Signal|signal]]** is *"a software interrupt that the OS delivers to a process"*; the receiver runs handler code. Canonical signals: `SIGKILL` (terminate), `SIGINT` (Ctrl-C), `SIGCHLD` (child state change), `SIGSEGV` ([[SegmentationFault|segfault]]), `SIGFPE` (FP exception).
- **[[WallTime|Wall time]]** = total elapsed seconds from start to finish (Running + Blocked + Ready) — *contaminated* by concurrent processes. **[[CPUTime|CPU time]]** = time the process actually held the CPU — independent of other processes. The two-clock split is the foundation for honest [[Benchmarking|benchmarking]] on a [[Multiprogramming|multiprogrammed]] system.

## Key Quotes

> "an instance of a program running in the system, which includes the program's binary executable code, data, and execution context." — definition of a process.

> "fork returns 0 to the child and the child's PID to the parent" — the dual-return that branches parent/child code paths from a single source line.

> "Each recursive call creates new stack frames" — paraphrased: every successful `exec` reinitializes execution state to the program's first instruction; the process's prior code/data/stack are discarded.

> "a software interrupt that the OS delivers to a process" — definition of a signal.

> Mechanism vs policy: context switching is **how** the OS swaps process state; scheduling is **which** process gets the CPU and for how long.

## Connections

- [[DiveIntoSystems]] — second leaf of Ch 13 *The Operating System*; **119th ingested DIS chapter**.
- [[dis-13-1-booting-running]] — sibling first leaf; named [[Process]] / [[ContextSwitch]] / [[SystemCall]] / [[KernelMode]] / [[UserMode]] but treated them as the program-startup mechanism. 13.2 turns the [[Process]] noun into a state machine with a life cycle, an OS data structure ([[ProcessControlBlock|PCB]]), and a [[CLanguage|C]]-level [[SystemCall|syscall]] API.
- [[Process]] — **substantially extended in place** from the prior parallel-processing stub into the canonical OS-textbook treatment (four-state life cycle + PCB + fork/exec/wait API).
- [[ProcessState]] — **new concept page**; the four-state diagram (Ready / Running / Blocked / Exited).
- [[ProcessControlBlock]] — **new concept page**; the per-process kernel data structure.
- [[Fork]] — **extended in place**; adds the full Ch 13.2 semantics (six-interleaving worked example, copy-on-write of address + execution state, `init` as root of the process hierarchy).
- [[Exec]] — **new concept page**; the `execvp` overlay primitive paired with [[Fork]] in the canonical process-spawn pattern.
- [[Wait]] — **new concept page**; the reaper that consumes [[Zombie]] state and unblocks the parent.
- [[Scheduler]] — **new concept page**; the *policy* half of [[ContextSwitch]]'s *mechanism*.
- [[ProcessScheduling]] — **new concept page**; the dispatch discipline that picks which [[ProcessState|Ready]] process runs next.
- [[Multiprogramming]] — **new concept page**; multiple coexisting processes, OS-switched when one blocks.
- [[Zombie]] — **new concept page**; terminated-but-unreaped state.
- [[Init]] — **new concept page**; the root of the process hierarchy.
- [[WallTime]] / [[CPUTime]] — **new concept pages**; the two clocks the chapter contrasts.
- [[ContextSwitch]] — reused; 13.2 sharpens the *mechanism* framing.
- [[Timesharing]] — reused; 13.2 names quantum / time slice exactly as the parallel-processing appendix did.
- [[Signal]] — reused and **extended in place** with the `SIGCHLD` / wait-handler shell-background story.
- [[Exit]] — reused; the C-library function the chapter pairs with the wait/zombie story.
- [[ProcessID]] / [[SystemCall]] / [[Kernel]] / [[KernelMode]] / [[UserMode]] / [[OperatingSystem]] — reused from prior ingests.
- [[ProcessMemory]] — reused; the address-space half of the per-process state.

## Contradictions

- None. 13.2 extends 13.1's [[Process]] noun into a full state machine; consistent with the [[parproc-appA-systems-issues|ParProc appendix]] treatment of [[ContextSwitch]] / [[Timesharing]] (which 13.2 reuses verbatim) and the [[parproc-ch01-intro-parallel-processing|ParProc Ch 1]] *thread-as-special-case-of-process* framing.
