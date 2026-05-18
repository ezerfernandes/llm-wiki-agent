---
title: "`kill()` (POSIX Signal Sending)"
type: concept
tags: [posix, unix, signal, system-call, operating-system, c]
sources: [dis-3-4-gdb-advanced]
last_updated: 2026-05-17
---

# `kill()` (POSIX Signal Sending)

[[OperatingSystem|POSIX]] [[SystemCall|system call]] that **sends a [[Signal|signal]] to a [[Process|process]]** (or process group). Signature: `int kill(pid_t pid, int sig)`. Despite the name, *not* primarily about termination — `kill` delivers **any** signal, including the harmless `SIGUSR1` / `SIGCONT` / `0` (existence-check).

Used in [[dis-3-4-gdb-advanced|DIS Ch 3.4]] as the C-side primitive behind the **self-pause idiom** for [[GdbAttach|attach-mode debugging]]:

```c
#include <signal.h>
#include <unistd.h>
...
kill(getpid(), SIGSTOP);   // suspend self until SIGCONT arrives
```

The companion `raise(sig)` is the short-form for `kill(getpid(), sig)`.

## Argument forms

| `pid` | Effect |
|---|---|
| `> 0` | Send `sig` to the [[Process|process]] with [[ProcessID|PID]] `pid`. |
| `0` | Send to every process in the caller's process group. |
| `-1` | Send to every process the caller can signal. |
| `< -1` | Send to every process in process group `\|pid\|`. |

## `sig` argument

Any standard [[Signal|signal]] number (`SIGUSR1`, `SIGSTOP`, `SIGTERM`, `SIGKILL`, …) — see [[Signal]] for the canonical table. `sig == 0` is the **probe form**: doesn't deliver anything but returns the same error codes — useful for *"does this PID exist and am I allowed to signal it?"* checks.

## Why it matters here

- **The self-pause idiom** `kill(getpid(), SIGSTOP)` is the [[dis-3-4-gdb-advanced|Ch 3.4]] pattern for opening a guaranteed [[GdbAttach|attach window]] — the program halts itself before reaching the suspect region, the developer attaches, and [[GdbSignalControl|`signal SIGCONT`]] from inside [[GDB]] resumes.
- **The kill(1) shell utility** is a thin user-facing wrapper around `kill(2)` — `kill -STOP 12345` from a shell does the same as `kill(12345, SIGSTOP)` from C.
- **Companion to [[Fork|`fork()`]] / [[Signal|signal handlers]]** — once [[OperatingSystem|OS]] chapters formalize the [[Process|process]] model, `kill` is the cross-process notification primitive.

## Related

- [[Signal]] — what `kill` sends.
- [[Process]] / [[ProcessID]] — what `kill` is addressed to.
- [[GdbSignalControl]] — the debugger-side version of `kill` — `signal <SIG>` from inside [[GDB]] is `kill(<debuggee_pid>, SIG)` routed through the debugger.
- [[GdbAttach]] — consumer of the `kill(getpid(), SIGSTOP)` self-pause idiom.
- [[Fork]] — paired primitive — `kill(child_pid, SIGTERM)` is the canonical parent-stops-child pattern.
- [[OperatingSystem]] — owner of the system call.
