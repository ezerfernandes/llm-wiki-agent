---
title: "File Descriptor"
type: concept
tags: [unix, io, kernel]
sources: [dis-app2-12-io-redirect]
last_updated: 2026-05-18
---

# File Descriptor

A **file descriptor** (fd) is a small non-negative integer that the [[OperatingSystem|kernel]] hands a process as a handle to an open file, [[ShellPipe|pipe]], socket, or device. The process passes the fd back to syscalls (`read(fd, buf, n)`, `write(fd, buf, n)`, `close(fd)`) and the kernel resolves it through the process's open-file table.

## Three reserved fds

| fd | Stream |
|---|---|
| **0** | [[Stdin]] |
| **1** | [[Stdout]] |
| **2** | [[Stderr]] |

[[IORedirection|Shell redirection]] (`>`, `<`, `2>`, `2>&1`) is shell sugar for **`dup2`**-ing one fd onto another before [[Exec|exec'ing]] the child program — the program itself sees fd 1 (or 2, etc.) but the kernel has rerouted it.

## Connections

- [[StandardStream]] — the fd-0/1/2 trio.
- [[IORedirection]] — the shell-level rewriting mechanism.
- [[ShellPipe]] / [[Pipe]] — pipe endpoints are file descriptors.
- [[OperatingSystem]] — kernel-side mechanism (Ch 13).
- [[dis-app2-12-io-redirect]] — source.
