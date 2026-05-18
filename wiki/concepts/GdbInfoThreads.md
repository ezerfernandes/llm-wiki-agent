---
title: "GDB `info threads` (Thread Enumeration)"
type: concept
tags: [gdb, debugging, threads, multithreading, pthreads, c, dive-into-systems]
sources: [dis-3-6-gdb-pthreads]
last_updated: 2026-05-17
---

# GDB `info threads`

[[GDB]] sub-command that **enumerates all active threads in the debuggee** — the entry point to thread-aware debugging. A specialization of [[GdbInfo|`info`]]'s reflection family for [[Pthreads|pthreads]] / kernel-thread state.

## Output

One row per thread. Columns:

| Field | Meaning |
|---|---|
| `*` (leading marker) | Present only on the **current** thread (the one [[GdbBacktrace|`bt`]] / [[GdbPrint|`print`]] / [[GdbInfo|`info locals`]] currently resolve against) |
| GDB thread number | The integer used in [[GdbThreadSwitch|`thread <N>`]] and `break ... thread <N>` |
| [[Pthreads|`pthread_t`]] ID | The library-side handle [[Pthreads|`pthread_create`]] writes back |
| LWP ID | The kernel-side [[LightweightProcess|lightweight-process]] scheduling ID |
| Position | Source file:line where the thread is currently paused |

Most implementations maintain a 1:1 correspondence between the three IDs; platforms vary.

## Use cases

- **Confirm thread inventory** after [[Pthreads|`pthread_create`]] calls — has the expected pool started?
- **Identify the triggering thread** after a [[Breakpoint|breakpoint]] halt — `*` marks it.
- **Find the GDB number** to feed [[GdbThreadSwitch|`thread <N>`]] or `break ... thread <N>` before issuing thread-targeted commands.
- **Diagnose deadlocks** in combination with [[GdbThreadApply|`thread apply all bt`]] — `info threads` shows *where* each thread is paused, the apply-all-bt shows *how it got there*.

## Diagnostic toggle

[[GdbSet|`set print thread-events on`]] makes [[GDB]] emit a notification line when threads are **created** or **terminate** during the session — separately from `info threads`, which is a point-in-time snapshot.

## Connections

- [[dis-3-6-gdb-pthreads]] — *Dive into Systems* Ch 3.6 *Debugging Multi-threaded Programs* introduces this command.
- [[GDB]] — the host debugger.
- [[GdbInfo]] — parent reflection-command family.
- [[GdbThreadSwitch]] — the natural next command after `info threads` (pick a thread number and switch into it).
- [[GdbThreadApply]] — the broadcast complement (`thread apply all bt` for a full multi-thread snapshot).
- [[Pthreads]] — the threading library whose threads this command reflects over.
- [[Breakpoint]] — `info threads` is most useful immediately after a breakpoint halt to identify which thread tripped it.
- [[Thread]] — the abstraction being enumerated.
