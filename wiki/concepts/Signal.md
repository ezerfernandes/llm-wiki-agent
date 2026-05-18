---
title: "Signal (POSIX Asynchronous Notification)"
type: concept
tags: [posix, unix, signal, ipc, operating-system, c]
sources: [dis-3-4-gdb-advanced]
last_updated: 2026-05-17
---

# Signal (POSIX Asynchronous Notification)

[[OperatingSystem|POSIX]] mechanism for **asynchronous notification** of a [[Process|process]] — the [[OperatingSystem|kernel]]'s way of interrupting a running program to deliver one of a small set of named events. Signals carry **no payload** beyond their identity; the receiving process consults a per-signal **disposition** (default action / ignore / custom handler) installed via `signal()` or `sigaction()`.

Surfaced in [[dis-3-4-gdb-advanced|DIS Ch 3.4]] as the substrate of [[GdbSignalControl|`signal` / `handle` / `info signal`]] — the debugger's signal-control family. Formal *Dive into Systems* coverage of `signal()` / `sigaction()` / signal masks deferred to Ch 9+ ([[OperatingSystem|OS chapters]]).

## Canonical signals (selected)

| Signal | Default | Cause |
|---|---|---|
| `SIGINT` (2) | Terminate | Ctrl-C from terminal. |
| `SIGQUIT` (3) | Terminate + core dump | Ctrl-\ from terminal. |
| `SIGILL` (4) | Terminate + core | Illegal instruction. |
| `SIGABRT` (6) | Terminate + core | `abort()` / `assert()` failure. |
| `SIGFPE` (8) | Terminate + core | Arithmetic exception (e.g., divide-by-zero on x86). |
| `SIGKILL` (9) | Terminate | **Uncatchable** — the kernel-issued kill. |
| `SIGSEGV` (11) | Terminate + core | [[SegmentationFault|Segfault]] — invalid memory access. |
| `SIGBUS` (10/7) | Terminate + core | Bus error — misaligned access / mapped-file truncation. See [[SIGBUS]]. |
| `SIGPIPE` (13) | Terminate | Write to a pipe with no readers. |
| `SIGALRM` (14) | Terminate | `alarm()` / `setitimer()` timer expiry. |
| `SIGTERM` (15) | Terminate | Polite kill — catchable, for cleanup. |
| `SIGUSR1` / `SIGUSR2` | Terminate | Application-defined. |
| `SIGCHLD` | Ignore | Child [[Process|process]] state change. |
| `SIGSTOP` | Stop | **Uncatchable** — suspend the process. |
| `SIGCONT` | Continue | Resume a stopped process. |

## How GDB sees signals

When a signal arrives at a debuggee, [[GDB]] **intercepts** it (via [[Ptrace|`ptrace`]]). Per-signal policy (set via [[GdbSignalControl|`handle <SIG> ...`]]):

- `stop` / `nostop` — halt the debuggee or let it run.
- `print` / `noprint` — print a notification line.
- `pass` / `nopass` — forward to the program's handler or swallow.

Default: `SIGSEGV` / `SIGBUS` / `SIGFPE` `stop+print+nopass`; `SIGINT` / `SIGTERM` `stop+print+pass`; `SIGCHLD` / `SIGALRM` / `SIGURG` typically `nostop+print+pass`.

## Why it matters

- **The asynchrony point in an otherwise synchronous program** — signals are the only way the kernel interrupts user code outside a [[SystemCall|system call]]. Makes them the substrate for timeouts, async termination, parent-child coordination, and crash recovery.
- **The hooking layer for [[GDB]]** — every fatal signal (`SIGSEGV` / `SIGBUS` / `SIGFPE`) gives the debugger its halt opportunity for post-crash inspection.
- **The escape hatch for the `kill(getpid(), SIGSTOP)` self-pause idiom** — the [[GdbAttach|attach-window]] pattern in [[dis-3-4-gdb-advanced|Ch 3.4]].

## Related

- [[Kill]] — `kill(pid, sig)` C primitive — sends a signal.
- [[GdbSignalControl]] — debugger-side `signal` / `handle` / `info signal` family.
- [[SIGBUS]] — bus-error signal — canonical Ch 3.4 example.
- [[SegmentationFault]] — `SIGSEGV` — paired fatal signal.
- [[Process]] / [[ProcessID]] — what signals are addressed to.
- [[Fork]] — paired primitive; `SIGCHLD` is the fork/wait coordination signal.
- [[OperatingSystem]] — owner of the signal-delivery machinery.
- [[Ptrace]] — kernel mechanism by which [[GDB]] intercepts signals.
