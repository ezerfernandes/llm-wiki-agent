---
title: "GDB Signal Control (`signal` / `handle` / `info signal`)"
type: concept
tags: [gdb, debugger, c-debugging, signals, signal-handling, sigbus, sigsegv]
sources: [dis-3-4-gdb-advanced]
last_updated: 2026-05-17
---

# GDB Signal Control (`signal` / `handle` / `info signal`)

[[GDB]] command family for **sending, intercepting, and inspecting [[Signal|POSIX signals]]** in the debuggee — the substrate that turns signal-driven control flow into a debuggable surface. Introduced by [[dis-3-4-gdb-advanced|DIS Ch 3.4]] alongside [[GdbAttach|attach]] and [[GdbFollowFork|follow-fork-mode]] as one of the three **systems-level extensions** of basic single-process debugging.

## Three sub-features

### 1. Send a signal — `signal <SIG>`

Deliver a [[Signal|signal]] to the running debuggee:

```text
(gdb) signal SIGCONT      # resume a stopped process (e.g., after kill(getpid(), SIGSTOP))
(gdb) signal SIGUSR1      # trigger the user-defined handler
(gdb) signal SIGALARM     # simulate an alarm timer firing
```

Equivalent to running `kill -<SIG> <pid>` from a shell, but **routed through the debugger** so signal handlers can be stepped through.

### 2. Intercept a signal — `handle <SIG> stop`

Make [[GDB]] **halt the debuggee** when `<SIG>` is delivered — the signal-equivalent of a [[Breakpoint|breakpoint]]:

```text
(gdb) handle SIGBUS stop      # halt when the program hits a bus error
(gdb) handle SIGUSR1 stop     # halt at user-signal delivery to debug the handler
(gdb) handle SIGPIPE nostop   # don't halt on broken-pipe (common nuisance)
```

Modifiers (each can be `stop` / `nostop`, `print` / `noprint`, `pass` / `nopass`): whether to halt, whether to print a notification, whether to forward the signal to the program's handler after [[GDB]] inspects it.

### 3. Inspect signal handling — `info signal`

```text
(gdb) info signal            # full table of all signals with stop/print/pass state
(gdb) info SIGALRM           # state for one specific signal
```

The reflection layer over [[GDB]]'s signal-handling configuration — mirrors [[GdbInfo|`info breakpoints`]] / [[GdbInfo|`info registers`]] in role.

## Canonical use cases

- **`SIGSEGV` / [[SegmentationFault|segfault]] post-mortem** is automatic — [[GDB]] halts by default. `handle SIGSEGV nostop pass` lets the program's [[Signal|signal handler]] try recovery while still printing a trace.
- **`SIGBUS` (misaligned access)**: *"if a program tries to access memory with a misaligned memory address for the type it is accessing, it receives a `SIGBUS` signal"* ([[dis-3-4-gdb-advanced|Ch 3.4]]) — distinct from [[SegmentationFault|`SIGSEGV`]] (invalid address). See [[SIGBUS]].
- **Pairing with [[GdbAttach|`attach`]]**: after attaching to a self-paused process (`kill(getpid(), SIGSTOP)`), `signal SIGCONT` is the standard resume.
- **Debugging signal handlers**: `handle SIGUSR1 stop` + [[Breakpoint|breakpoint]] in the handler function — observe state both at delivery and inside the handler body.
- **Suppressing noisy signals**: `handle SIGPIPE nostop noprint` for socket / pipe programs that intentionally get many `SIGPIPE`s.

## Why it matters

- **Brings signal-driven code under deterministic debugging** — without `handle`, signal handlers run **asynchronously** outside [[GDB]]'s usual single-step model.
- **Surfaces the [[OperatingSystem|kernel]] / debugger interaction**: signal delivery is one of the rare events where the [[OperatingSystem|OS]] interrupts a [[Process|process]] asynchronously; [[GDB]] mediates the interruption.
- **Sets up Ch 9+'s [[OperatingSystem|OS]] coverage**: when *Dive into Systems* formalizes [[Signal|signals]] / `signal()` / `sigaction()` / signal masks, this primitive is the debugger view of all of it.

## Related

- [[GDB]] — host tool.
- [[Signal]] — [[OperatingSystem|POSIX]] signal mechanism — the underlying primitive.
- [[SIGBUS]] — bus-error signal raised on misaligned access — canonical `handle SIGBUS stop` use case.
- [[SegmentationFault]] — `SIGSEGV`; the corpus's other canonical fatal signal.
- [[Kill]] — `kill(pid, sig)` C primitive — what `signal <SIG>` is the debugger version of.
- [[GdbAttach]] — sibling Ch 3.4 feature; pairs via `signal SIGCONT` to resume self-paused processes.
- [[GdbFollowFork]] — sibling Ch 3.4 feature; pairs via `SIGCHLD` for fork/wait flows.
- [[GdbInfo]] — sibling reflection family; `info signal` lives in the same namespace as `info breakpoints` / `info registers`.
- [[Ptrace]] — kernel mechanism behind the scenes — signal delivery routes through `ptrace` when the debuggee is traced.
