---
title: "GDB `thread apply all <cmd>` (Broadcast to All Threads)"
type: concept
tags: [gdb, debugging, threads, multithreading, pthreads, c, dive-into-systems, deadlock]
sources: [dis-3-6-gdb-pthreads]
last_updated: 2026-05-17
---

# GDB `thread apply all <cmd>`

[[GDB]] command that **runs a [[GDB]] command in the context of every thread**, printing each thread's result in turn. The broadcast counterpart to [[GdbThreadSwitch|`thread <N>`]]'s point-switch — instead of switching to one thread, run the same inspection across all of them.

## Canonical form

```
(gdb) thread apply all bt
```

Prints **every thread's** [[GdbBacktrace|backtrace]] — a full multi-thread call-stack snapshot — without manually iterating [[GdbThreadSwitch|`thread N`]] + [[GdbBacktrace|`bt`]] for each thread.

## Generalization

```
(gdb) thread apply all <cmd>
(gdb) thread apply <N> <M> <cmd>     # specific thread list
```

`<cmd>` is any [[GDB]] command — [[GdbBacktrace|`bt`]] is the dominant use, but [[GdbInfo|`info locals`]], [[GdbPrint|`print expr`]], or [[CpuRegister|`info registers`]] also broadcast.

## Why `bt` is the headline pairing

- **Deadlock diagnosis** — every thread waiting on a [[Mutex|mutex]] in `pthread_mutex_lock` shows up at the same wait frame; the cycle is visible at a glance.
- **Livelock / starvation** — threads stuck spinning on the same condition variable surface in the multi-thread `bt`.
- **Cross-thread heisenbug localization** — *"which thread was where when the assertion fired?"* — global stop-the-world plus `thread apply all bt` answers in one command.

## Workflow

1. [[Breakpoint|Breakpoint]] hits (default stop-the-world pauses **all** threads).
2. [[GdbInfoThreads|`info threads`]] — confirm thread inventory and find the triggering thread.
3. `thread apply all bt` — snapshot every thread's call stack.
4. [[GdbThreadSwitch|`thread <N>`]] — drill into the most suspicious thread.
5. [[GdbBacktrace|`bt`]] / [[GdbPrint|`print`]] / [[GdbInfo|`info locals`]] — inspect.

## Connections

- [[dis-3-6-gdb-pthreads]] — *Dive into Systems* Ch 3.6 *Debugging Multi-threaded Programs* introduces this command.
- [[GDB]] — the host debugger.
- [[GdbInfoThreads]] — pre-broadcast: lists the threads `apply all` will visit.
- [[GdbThreadSwitch]] — the point-switch complement; `thread apply all` broadcasts instead of switching.
- [[GdbBacktrace]] — the dominant `<cmd>` operand; `thread apply all bt` is the canonical deadlock-diagnostic primitive.
- [[Pthreads]] — the threading library whose threads are being broadcast over.
- [[Mutex]] — deadlocks visible in `thread apply all bt` typically show every thread blocked in `pthread_mutex_lock`.
- [[Thread]] — the abstraction being broadcast over.
- [[Breakpoint]] — the default stop-the-world breakpoint behaviour is what makes the global snapshot meaningful.
