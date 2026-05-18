---
title: "GDB `follow-fork-mode` (Fork-Aware Debugging)"
type: concept
tags: [gdb, debugger, c-debugging, fork, process, multi-process]
sources: [dis-3-4-gdb-advanced]
last_updated: 2026-05-17
---

# GDB `follow-fork-mode` (Fork-Aware Debugging)

[[GDB]] setting that controls which side of a [[Fork|`fork()`]] system call the debugger follows — the single primitive that makes [[GDB]] usable for **multi-process programs**. Default: **parent**. *"By default, GDB follows the parent after a call to `fork()`"* ([[dis-3-4-gdb-advanced|DIS Ch 3.4]]).

## Commands

| Command | Effect |
|---|---|
| `set follow-fork-mode parent` | Default — debugger continues with the parent after [[Fork|`fork()`]]; child runs unsupervised. |
| `set follow-fork-mode child` | Debugger switches to the **new child** after [[Fork|`fork()`]]; parent runs unsupervised. |
| `show follow-fork-mode` | Print the current setting. |

After [[Fork|`fork()`]] returns, only one of {parent, child} is under debugger control. The unfollowed side continues executing as a normal [[Process|process]] — unaffected by [[Breakpoint|breakpoints]] in the [[GDB]] session.

## Why a setting and not automatic

`fork()` returns **once in each [[Process|process]]** — the parent gets the child's [[ProcessID|PID]], the child gets `0`. The debugger can only single-step **one [[Process|process]] at a time**, so the user must choose. Setting `follow-fork-mode child` is the **debug-the-newly-spawned-worker** workflow (e.g., a shell forking to `exec` a command, a server forking per connection); leaving it on `parent` is the **debug-the-supervisor** workflow.

## Combining with other Ch 3.4 features

- **`attach <pid>` after fork**: leave `follow-fork-mode = parent`, let the program fork, find the child via [[Ps|`ps`]], then `attach <child_pid>` from a second [[GDB]] session — debugs both simultaneously.
- **`handle SIGCHLD stop`**: combined with [[GdbSignalControl|signal control]], pause the parent when the child terminates, inspect the parent's reaping logic.
- **`detach-on-fork off`** (advanced): GDB keeps both processes under control simultaneously; out of scope for [[dis-3-4-gdb-advanced|Ch 3.4]] but mentioned in the [[GDB]] manual.

## Why it matters

- **First corpus exposure to multi-process debugging** — every prior [[GDB]] section ([[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]]) assumed a single-process target.
- **Substrate for OS-chapters' fork()-based examples** — when Ch 9+ introduces [[Fork|`fork()`]] / `exec()` / `wait()`, `follow-fork-mode` is the debugging primitive that makes those programs inspectable.
- **The user-facing tip of [[Ptrace|`ptrace`]]'s `PTRACE_O_TRACEFORK` option** — the kernel mechanism the setting toggles.

## Related

- [[GDB]] — host tool.
- [[Fork]] — the [[OperatingSystem|POSIX]] system call this setting controls.
- [[Process]] / [[ProcessID]] — what fork creates two of.
- [[GdbAttach]] — alternative for getting the second process under debugger control.
- [[GdbSignalControl]] — sibling Ch 3.4 feature; pairs naturally with [[Fork|`fork()`]] flows via `SIGCHLD` / `SIGSTOP`.
- [[Ptrace]] — kernel mechanism behind the scenes.
- [[GdbSet]] — generic setter family — `follow-fork-mode` is in [[GDB]]'s config namespace, not the variable namespace.
