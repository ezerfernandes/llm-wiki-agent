---
title: "`fork()` (POSIX Process Creation)"
type: concept
tags: [posix, unix, process, system-call, operating-system, c]
sources: [dis-3-4-gdb-advanced, dis-13-2-processes]
last_updated: 2026-05-17
---

# `fork()` (POSIX Process Creation)

[[OperatingSystem|POSIX]] [[SystemCall|system call]] that **creates a new [[Process|process]] by duplicating the calling one**. The signature: `pid_t fork(void)`. Returns **twice** — once in the parent (returning the child's [[ProcessID|PID]]) and once in the child (returning `0`). On failure, returns `-1` in the parent only. The kernel-level primitive behind every Unix command shell, every `exec`-based process launch, and every multi-process server.

Named-and-deferred in [[dis-3-4-gdb-advanced|DIS Ch 3.4]] for [[GDB]]'s [[GdbFollowFork|`set follow-fork-mode`]]; formally treated in [[dis-13-2-processes|DIS Ch 13.2]] *Processes*.

## DIS 13.2 semantics

The child receives *"an exact copy of its parent's address and execution state"* — same code, same data, same [[StackPointer|stack pointer]], same [[CpuRegister|register]] snapshot, same open file descriptors. Modern kernels defer the actual copy via copy-on-write. After `fork`, parent and child both **resume from the fork return point** — but with different return values, so the canonical `if (pid == 0) { child } else { parent }` idiom branches them onto different code paths from the same source line.

The textbook worked example shows that parent / child output may **interleave in six possible orderings** due to concurrent [[Scheduler|scheduling]] — the [[ContextSwitch|context-switch]] points are not user-controllable. Every process except [[Init|`init`]] (PID 1) descends from a `fork`.

## Canonical idiom

```c
#include <unistd.h>
#include <sys/wait.h>

pid_t pid = fork();
if (pid == -1) {
    perror("fork");
    exit(1);
} else if (pid == 0) {
    // child branch — pid == 0
    execl("/bin/ls", "ls", "-l", NULL);
    exit(127);  // only reached if exec fails
} else {
    // parent branch — pid == child PID
    int status;
    waitpid(pid, &status, 0);
}
```

The **child inherits** the parent's open file descriptors, signal-disposition table, environment, [[ProcessMemory|memory image]] (logically — kernels use copy-on-write to defer the actual copy). The child does **not** inherit pending signals, file locks, or timers.

## Why it matters for debugging

- [[GDB]] can only single-step one [[Process|process]] at a time — [[GdbFollowFork|`set follow-fork-mode child` / `parent`]] picks which side of the fork stays under the debugger.
- The unfollowed side runs **free of debugger control** — to debug both, attach a second [[GDB]] session via [[GdbAttach|`gdb <prog> <pid>`]] after finding the child's [[ProcessID|PID]] with [[Ps|`ps`]].
- `fork()` + `exec*()` is the canonical Unix **process spawn** pattern — shell command execution, `system()`, server worker spawning all go through it.

## Related

- [[dis-13-2-processes]] — canonical Ch 13.2 treatment.
- [[Process]] / [[ProcessID]] — what fork creates a new one of.
- [[Exec]] — paired primitive; the canonical Unix spawn pattern is **fork + exec**.
- [[Wait]] — paired primitive; the parent reaps the forked child via `wait` / `waitpid`.
- [[Init]] — PID 1; the root of the process tree fork descends.
- [[Zombie]] — what an unreaped forked child becomes after `exit`.
- [[ProcessControlBlock]] — the kernel duplicates this on fork.
- [[OperatingSystem]] — owner of the [[SystemCall|system call]].
- [[GdbFollowFork]] — debugger-side setting that controls which side of the fork [[GDB]] follows.
- [[GdbAttach]] — used to bring the unfollowed side under a second debugger session.
- [[Signal]] / [[Kill]] — paired primitives; `SIGCHLD` notifies the parent when a forked child terminates.
- [[CLanguage]] — host language of the API surface (`unistd.h`).
