---
title: "Signal Handler (POSIX)"
type: concept
tags: [posix, unix, signal, signal-handler, sigaction, ipc, c, async-signal-safe]
sources: [dis-13-4-1-signals, dis-3-4-gdb-advanced]
last_updated: 2026-05-18
---

# Signal Handler (POSIX)

The **user-supplied callback** that runs when a [[Signal|POSIX signal]] is delivered to a [[Process|process]]. Installed via `signal(2)` or `sigaction(2)`; replaces or supplements the OS's default per-signal action.

> "Linux supports two different system calls that can be used to change the default behavior of a signal or to register a signal handler on a particular signal: `sigaction` and `signal`." — [[dis-13-4-1-signals|DIS Ch 13.4.1]]

## Standard prototype

```c
void handler_function(int signum);
```

A single `int` argument carries the signal number so one handler can multiplex multiple signals. Handlers may return normally (control resumes at the interrupted point) or terminate the process (`exit` / `_exit`).

## Installation — two APIs

| API | Trade-off |
|---|---|
| `signal(sig, handler)` | Simpler. Historical, behavior varies across UNIX flavors. Suitable for learning. |
| `sigaction(sig, &act, &oldact)` | POSIX-standard. Explicit flags, signal mask, optional `siginfo_t` payload. **Preferred for production.** |

## The four default actions (override target)

When **no** handler is registered, the OS applies one of four defaults:

1. **Terminate** the process (e.g., `SIGTERM`, `SIGINT`).
2. **Ignore** the signal (e.g., `SIGCHLD` by default).
3. **Block / stop** the process (e.g., `SIGSTOP`).
4. **Unblock / continue** the process (e.g., `SIGCONT`).

A custom handler **overrides** the default — *except* for `SIGKILL` and `SIGSTOP`, which **cannot be caught or ignored** (the OS guarantees its kill/stop authority).

## Canonical `SIGCHLD` reaping idiom

The pattern [[dis-13-4-1-signals|Ch 13.4.1]] highlights — *because the OS does not count signal occurrences, only that the signal happened*:

```c
void sigchld_handler(int signum) {
    int status;
    while (waitpid(-1, &status, WNOHANG) > 0) {
        // reap each zombie; loop because multiple children
        // exiting back-to-back may coalesce into one SIGCHLD
    }
}
```

The `WNOHANG` flag makes [[Wait|`waitpid`]] non-blocking; the loop drains every reapable [[Zombie|zombie]] child.

## Async-signal safety

Handlers run **asynchronously** — they can interrupt the main program at *any* instruction. Only a small set of syscalls / library functions are guaranteed safe to call from inside a handler (the **async-signal-safe** subset — `_exit`, `write`, `waitpid`, etc.). Calling `malloc`, `printf`, or other non-reentrant routines from a handler is undefined behavior. The standard workaround: handler sets a `volatile sig_atomic_t` flag; main loop checks the flag.

## Related

- [[Signal]] — what the handler responds to.
- [[Kill]] — the send-side primitive that triggers handler invocation in the receiver.
- [[SIGBUS]] — example of a fatal signal whose handler often only logs + `_exit`s.
- [[Wait]] / [[Zombie]] — the canonical `SIGCHLD` reaping pattern.
- [[SystemCall]] — `signal` and `sigaction` are syscalls.
- [[InterprocessCommunication]] — parent IPC family ([[Signal|signals]]).
- [[GdbSignalControl]] — debugger-side counterpart for inspecting handler installation / disposition.
- [[dis-13-4-1-signals]] — primary source.
- [[dis-3-4-gdb-advanced]] — GDB-side context where signals were first introduced.
