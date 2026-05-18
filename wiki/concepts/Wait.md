---
title: "`wait` / `waitpid` (POSIX Child Reaping)"
type: concept
tags: [posix, unix, process, system-call, operating-system, c]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# `wait` / `waitpid` (POSIX Child Reaping)

[[OperatingSystem|POSIX]] [[SystemCall|system calls]] that let a parent [[Process|process]] **reap a terminated child** — collect its [[ExitStatus|exit status]] and free its [[ProcessControlBlock|PCB]] entry. Without `wait`, a child that has called [[Exit|`exit`]] persists in the [[ProcessState|Exited state]] as a [[Zombie|zombie]] indefinitely.

## Signatures

```c
#include <sys/wait.h>

pid_t wait(int *status);                    /* any child */
pid_t waitpid(pid_t pid, int *status, int options);  /* specific child */
```

- **`wait(&status)`** — blocks until **any** child terminates; returns the child's [[ProcessID|PID]] and writes its [[ExitStatus|exit status]] into `*status`.
- **`waitpid(pid, &status, options)`** — waits for the child with the given `pid`; `WNOHANG` option polls instead of blocking.

## Mechanism

1. Child calls [[Exit|`exit(n)`]]; OS releases most of the child's state but **keeps the PCB** so the [[ExitStatus|exit status]] survives.
2. OS sends the parent a [[Signal|`SIGCHLD`]] notification — *"a software interrupt that the OS delivers to a process"* ([[dis-13-2-processes|DIS 13.2]]).
3. Parent calls `wait` — if a [[Zombie|zombie]] child exists, `wait` reads its status and frees the PCB; otherwise the parent enters the [[ProcessState|Blocked]] state until `SIGCHLD` arrives.

## Foreground vs background — shell semantics

[[dis-13-2-processes|DIS 13.2]] illustrates with shell behavior:

- **`a.out`** (foreground) — shell `fork`s, child `exec`s `a.out`, shell calls `wait` synchronously → shell prompt blocks until the child exits.
- **`a.out &`** (background) — shell `fork`s, child `exec`s `a.out`, shell continues immediately. `wait` runs **inside the `SIGCHLD` handler** instead — so the shell still reaps the child eventually, but the user keeps interacting in the meantime.

The two modes share the same `fork` + `exec` + `wait` triad; only the **timing** of the `wait` differs.

## Status macros

The `int status` is encoded — use macros from `<sys/wait.h>`:

- `WIFEXITED(status)` — true if child terminated normally via [[Exit|`exit`]].
- `WEXITSTATUS(status)` — extract the exit-status byte.
- `WIFSIGNALED(status)` — terminated by a [[Signal|signal]].
- `WTERMSIG(status)` — which signal.

## Why `wait` exists

Two reasons, both [[dis-13-2-processes|DIS 13.2]]-named:

1. **Status delivery** — exit codes must survive the child until the parent reads them; only the PCB can store that.
2. **Synchronization** — the parent often *needs* to know its child finished before proceeding (the shell's foreground case).

Without `wait`, [[Zombie|zombies]] would accumulate until reboot. With it, the parent-child contract is closed.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[Fork]] / [[Exec]] — the spawn half of the fork-exec-wait triad.
- [[Process]] / [[ProcessID]] — what `wait` operates on.
- [[ProcessState]] — `wait` transitions parent to Blocked, child Exited → (gone).
- [[Zombie]] — the state `wait` cleans up.
- [[Signal]] — `SIGCHLD` is the notification that drives `wait`.
- [[Exit]] / [[ExitStatus]] — produces the value `wait` delivers.
- [[ProcessControlBlock]] — what `wait` finally frees.
- [[OperatingSystem]] / [[SystemCall]] / [[Kernel]].
- [[CLanguage]] — `<sys/wait.h>`.
