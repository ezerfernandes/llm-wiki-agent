---
title: "Process (operating system)"
type: concept
tags: [os, concurrency, processes]
sources: [parproc-ch01-intro-parallel-processing, dis-13-2-processes, dis-13-1-booting-running]
last_updated: 2026-05-17
---

# Process

A **process** is *"an instance of a program running in the system, which includes the program's binary executable code, data, and execution context"* ([[dis-13-2-processes|DIS Ch 13.2]]). The execution context — saved [[CpuRegister|register]] values, [[StackPointer|stack pointer]], current instruction — is what makes a *running* program distinct from a *stored* one on disk. Each process gets a private [[ProcessMemory|address space]], a [[ProcessControlBlock|process-table entry]] (PCB), an open-file table, and at least one thread of execution. The basic unit of multitasking on Unix / Windows / etc.

## State machine (DIS 13.2)

[[ProcessState|Four-state life cycle]] — **Ready / Running / Blocked / Exited** — with transitions driven by [[Scheduler|scheduler]] decisions, [[SystemCall|syscall]] blocking, [[Signal|signal]] delivery, and [[Exit|`exit`]] calls. Only Ready processes are scheduling candidates; Blocked processes wait for an event before becoming Ready again.

## Kernel data structure

Each process has a **[[ProcessControlBlock|PCB]]** holding [[ProcessID|PID]], address-space info, saved register snapshot, allocated resources (open files), and current [[ProcessState|state]]. A [[ContextSwitch|context switch]] is the OS reading the outgoing PCB and writing the incoming one onto the CPU.

## C-surface API (POSIX)

The three [[SystemCall|system calls]] that operate on processes:

- **[[Fork|`fork()`]]** — duplicate the calling process; child receives an exact copy of address + execution state; returns twice (`0` to child, child [[ProcessID|PID]] to parent).
- **[[Exec|`execvp(filename, argv)`]]** — overlay the calling process's image with a new program; preserves [[ProcessID|PID]], reinitializes everything else; returns only on failure.
- **[[Wait|`wait` / `waitpid`]]** — reap a terminated child, freeing its [[Zombie|zombie]] PCB and reading its [[ExitStatus|exit status]].

[[Exit|`exit`]] terminates and notifies the parent via [[Signal|`SIGCHLD`]]. The canonical Unix process-spawn pattern is **[[Fork|`fork`]] + [[Exec|`exec`]] + [[Wait|`wait`]]** — every shell command is dispatched this way.

## Hierarchy

Every process except [[Init|`init`]] (PID 1) has a parent. `init` is created at boot and is the ancestor of all user processes. Orphans are re-parented to `init`, which periodically [[Wait|`wait`s]] to reap them.

## Mechanism vs policy

[[dis-13-2-processes|DIS 13.2]]'s load-bearing split: [[ContextSwitch|context switching]] is the **mechanism** (how the OS swaps process state); [[Scheduler|scheduling]] is the **policy** (which Ready process runs next). [[Multiprogramming|Multiprogramming]] switches on I/O blocks; [[Timesharing|timesharing]] adds quantum-bounded preemption.

## Threads vs processes

[[parproc-ch01-intro-parallel-processing]] frames threads as *"similar to a process in an operating system (OS), but with much less overhead … in the typical implementation, a thread is a special case of an OS process. But the key difference is that the various threads of a program share memory."*

R's [[Snow]] package builds its cluster on top of independent OS processes communicating via TCP/IP sockets — message-passing at the OS-process level even though the program logically looks parallel.

## Connections

- [[dis-13-2-processes]] — canonical Ch 13.2 treatment (state machine + PCB + fork/exec/wait).
- [[dis-13-1-booting-running]] — names [[Process]] as the OS state container for a running program.
- [[ProcessState]] — the four-state life cycle.
- [[ProcessControlBlock]] — the per-process kernel data structure.
- [[ProcessID]] — unique identifier inside the PCB.
- [[ProcessMemory]] — the address-space half of process state.
- [[Fork]] / [[Exec]] / [[Wait]] / [[Exit]] — the POSIX [[SystemCall|syscall]] surface.
- [[Scheduler]] / [[ProcessScheduling]] — policy half.
- [[ContextSwitch]] — mechanism half.
- [[Multiprogramming]] / [[Timesharing]] — switch triggers.
- [[Signal]] — `SIGCHLD` and friends.
- [[Zombie]] / [[Init]] — termination & adoption.
- [[Thread]] / [[Snow]] / [[parproc-ch01-intro-parallel-processing]] — process-vs-thread framing.
