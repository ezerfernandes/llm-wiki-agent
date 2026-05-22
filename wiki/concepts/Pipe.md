---
title: "Pipe (POSIX)"
type: concept
tags: [posix, unix, ipc, pipe, system-call, message-passing, shell]
sources: [dis-13-4-2-message-passing]
last_updated: 2026-05-18
---

# Pipe (POSIX)

[[OperatingSystem|POSIX]] anonymous **[[MessagePassing|message-passing]]** channel: *"a one-way communication channel for two processes running on the same machine"* ([[dis-13-4-2-message-passing|DIS Ch 13.4.2]]). Created by the `pipe(2)` [[SystemCall|system call]]; ordinarily shared between a [[Process|parent]] and its [[Fork|forked]] child by inheritance of file descriptors.

## API shape

```c
int fds[2];
if (pipe(fds) == -1) { perror("pipe"); exit(1); }
// fds[0] — read end
// fds[1] — write end
```

The pipe is a kernel-resident byte buffer. `write(fds[1], buf, n)` enqueues bytes; `read(fds[0], buf, n)` dequeues them.

## The shell-pipeline pattern

The canonical use case is the shell `|` operator:

```bash
cat foo.c | grep factorial
```

The shell:

1. Calls `pipe(fds)`.
2. [[Fork|`fork()`]]s twice — one child per command.
3. In the `cat` child: redirects `stdout` (`fd 1`) → `fds[1]` via [[Dup2|`dup2`]], closes both raw fds, [[Exec|`execvp`]]s `cat`.
4. In the `grep` child: redirects `stdin` (`fd 0`) → `fds[0]` via `dup2`, closes both raw fds, `execvp`s `grep`.
5. Closes both raw fds in the shell itself and [[Wait|`waitpid`]]s for both children.

Neither `cat` nor `grep` is pipe-aware — both see ordinary file descriptors. *"The bash shell uses the `pipe` system call to create the channel. The `cat` process writes to the pipe's output end while `grep` reads from the input end."*

## Properties

| Property | Value |
|---|---|
| Direction | One-way |
| Scope | Same machine, **related** processes only (inheritance via [[Fork]]) |
| Persistence | None — destroyed when last fd closes |
| Naming | Anonymous (no filesystem path) — see [[NamedPipe\|FIFO]] for the named variant |
| Capacity | Kernel-buffered; size is OS-dependent (typically 64 KB on Linux) |
| Blocking | `read` blocks on empty buffer; `write` blocks on full buffer |

## Pipe vs FIFO vs Socket

- [[Pipe|Pipe]] — anonymous, one-way, related processes only.
- [[NamedPipe|FIFO]] — same as pipe but **named** in the filesystem via `mkfifo`; unrelated processes can rendezvous on the path.
- [[Socket]] — two-way, spans network, more setup but more general.

## Related

- [[MessagePassing]] — parent family.
- [[NamedPipe]] — the named-via-filesystem variant.
- [[Socket]] — the two-way / cross-network generalization.
- [[Fork]] — the syscall that propagates pipe fds parent → child.
- [[Exec]] — preserves open fds across the image overlay.
- [[Wait]] — what the shell does after `fork` + `execvp`.
- [[InterprocessCommunication]] — umbrella concept.
- [[Signal]] — `SIGPIPE` is raised when writing to a pipe with no readers.
- [[dis-13-4-2-message-passing]] — primary source.
