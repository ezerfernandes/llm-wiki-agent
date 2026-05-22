---
title: "Message Passing (IPC)"
type: concept
tags: [operating-system, ipc, posix, unix, pipe, socket, channel]
sources: [dis-13-4-2-message-passing, dis-13-4-ipc]
last_updated: 2026-05-18
---

# Message Passing (IPC)

The middle of the three [[InterprocessCommunication|IPC]] families ([[dis-13-4-2-message-passing|DIS Ch 13.4.2]]): the [[OperatingSystem|OS]] provides a **channel abstraction** between two [[Process|processes]] — *"the OS implements an abstraction of a message communication channel that is used by a process to exchange messages with another process."* Unlike [[Signal|signals]]' fixed namespace, the channel carries **arbitrary byte streams**; unlike [[SharedMemoryIPC|shared memory]], every send/receive is OS-mediated (one syscall per operation).

## Concrete channels

| Channel | Direction | Scope | Syscall |
|---|---|---|---|
| [[Pipe]] | One-way | Same machine, related processes | `pipe(2)` |
| [[NamedPipe\|Named pipe (FIFO)]] | One-way | Same machine, any processes (filesystem name) | `mkfifo(3)` |
| [[Socket]] | Two-way | Same machine *or* network ([[TCP\|TCP/IP]]) | `socket(2)` |

## Pipe — the canonical example

*"A pipe is a one-way communication channel for two processes running on the same machine"* — one end handles writing, the other reading. The shell pipeline is the universal example:

```bash
cat foo.c | grep factorial
```

Bash calls `pipe()` to create the channel, [[Fork|`fork()`]]s twice, redirects `cat`'s `stdout` to the write-end and `grep`'s `stdin` to the read-end via [[Dup2|`dup2`]], then [[Exec|`execvp`]]s each program. Neither `cat` nor `grep` knows a pipe is involved — both see ordinary file descriptors.

## Socket — the two-way generalization

*"A socket is a two-way communication channel, which means that each end of a socket can be used for both sending and receiving messages."* Sockets extend the channel abstraction across machines via [[TCP|TCP/IP]] — the same `read` / `write` syscalls work whether the peer is the next process on the local host or a server on the other side of the network.

## Why use message passing?

- **Arbitrary byte stream** — overcomes the [[Signal|signal]] family's fixed 32-signal namespace.
- **OS-managed synchronization** — the channel handles producer / consumer coordination (blocking on empty read, etc.); no application-level [[Mutex|mutex]] needed.
- **Process-isolation safe** — neither side can corrupt the other's [[AddressSpace|address space]]; only the channel content crosses.

## Limitations

- **Per-message copy overhead** — every `write` copies bytes into the kernel; every `read` copies them out. For high-bandwidth coupling, [[SharedMemoryIPC|shared memory]] wins.

## Related

- [[InterprocessCommunication]] — parent umbrella concept.
- [[Pipe]] — anonymous same-machine channel.
- [[NamedPipe]] — FIFO variant via filesystem path.
- [[Socket]] — two-way / cross-network generalization.
- [[Signal]] — adjacent IPC family; fixed-namespace event notification.
- [[SharedMemoryIPC]] — adjacent IPC family; faster but app-synchronized.
- [[SystemCall]] — `pipe` / `socket` / `mkfifo` are syscalls.
- [[dis-13-4-2-message-passing]] — primary source.
