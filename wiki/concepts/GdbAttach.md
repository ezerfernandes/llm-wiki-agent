---
title: "GDB `attach` (Debug a Running Process)"
type: concept
tags: [gdb, debugger, c-debugging, process, attach, ptrace]
sources: [dis-3-4-gdb-advanced]
last_updated: 2026-05-17
---

# GDB `attach` (Debug a Running Process)

[[GDB]] feature that **connects the debugger to an already-running [[Process|process]]** instead of launching a fresh one — the workflow opposite to [[GdbRun|`run`]]. Two equivalent entry forms: `gdb <executable> <pid>` at the shell, or `attach <pid>` from inside an existing [[GDB]] session. On attach, the target [[Process|process]] **pauses** (the kernel uses [[Ptrace|`ptrace`]] under the hood to halt it) — the developer can then [[GdbBacktrace|`bt`]] / [[GdbPrint|`print`]] / set [[Breakpoint|breakpoints]], then [[StepDebug|`cont`]] (or `detach`) to release the process.

## Workflow

```text
# in shell A — long-running program
$ ./a.out

# in shell B — find PID, then attach
$ ps -A | grep a.out
12345 pts/1   00:00:00 a.out
$ gdb ./a.out 12345
(gdb) bt           # inspect where the program currently is
(gdb) break foo
(gdb) cont         # let it run; halt when foo() called
(gdb) detach       # release without killing
```

Equivalent from a running [[GDB]] session: `attach 12345` / `detach` / `kill`.

## Self-pause idiom

A program can **pause itself** to give the developer a guaranteed attach window:

```c
#include <signal.h>
#include <unistd.h>
...
kill(getpid(), SIGSTOP);   // or: raise(SIGSTOP)
// suspect region follows — attach now, then `signal SIGCONT` to resume
```

The corpus's first **debugger-aware program design** pattern (from [[dis-3-4-gdb-advanced|DIS Ch 3.4]]). Resume from inside [[GDB]] with [[GdbSignalControl|`signal SIGCONT`]].

## Why it matters

- **Already-running services / daemons / servers** can't be restarted under [[GDB]] without dropping connections — `attach` debugs them in place.
- **Heisenbugs that only surface after warmup** (cache state, scheduling, accumulated input) need attach because [[GdbRun|`run`]] resets the world.
- **Multi-process debugging**: combined with [[GdbFollowFork|`follow-fork-mode`]], one [[GDB]] can chase either parent or child after a [[Fork|`fork()`]].
- **The OS-primitive surface**: `attach` is the user face of [[Ptrace|`ptrace(PTRACE_ATTACH, ...)`]] — the same kernel mechanism behind `strace`, `gdbserver`, and dynamic-instrumentation frameworks ([[dis-3-4-gdb-advanced|Ch 3.4]] names but defers the kernel-side coverage).

## Related

- [[GDB]] — host tool.
- [[GdbRun]] — the opposite-direction entry point (start fresh from `_start` → [[MainFunction|`main`]]).
- [[GdbFollowFork]] — controls which child of a [[Fork|forked]] process [[GDB]] follows after attach or run.
- [[GdbSignalControl]] — sibling Ch 3.4 feature; `signal SIGCONT` resumes after a self-pause.
- [[Ps]] — PID discovery utility.
- [[Process]] / [[ProcessID]] — what attach connects to.
- [[Ptrace]] — kernel mechanism under the hood (named-and-deferred to later OS chapters).
- [[Kill]] — C-side primitive behind the `kill(getpid(), SIGSTOP)` self-pause idiom.
