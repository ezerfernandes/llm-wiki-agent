---
title: "Dive into Systems — 13.4.2 Message Passing"
type: source
tags: [textbook, operating-systems, ipc, message-passing, pipe, socket, named-pipe, fifo]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C13-OS/ipc_msging.html
---

## Summary

**Second sub-leaf of [[dis-13-4-ipc|Ch 13.4]]** — formalizes the **[[MessagePassing|message-passing]]** IPC family: *"processes with private virtual address spaces can communicate ... by sending and receiving messages to one another."* The OS provides a **channel abstraction**: one process writes into one end of the channel; another reads from the other end. **Two concrete channels** introduced:

- **[[Pipe|Pipes]]** — *"a one-way communication channel for two processes running on the same machine."* One end handles sending (writing), the other handles receiving (reading). Classic shell-pipeline example: `cat foo.c | grep factorial` — bash uses the `pipe` [[SystemCall|system call]] to create the channel; `cat` writes the file content to the pipe's output end while `grep` reads from the input end.

- **[[Socket|Sockets]]** — *"a two-way communication channel, which means that each end of a socket can be used for both sending and receiving messages."* Sockets support communication between processes on the same machine *or* across networks via [[TCP|TCP/IP]] protocols.

13.4.2 confines itself to the **foundational concepts**; named-pipe (FIFO) machinery, `mkfifo`, message queues, file descriptor mechanics, and blocking semantics are beyond the section's scope. The pivot vs signals: pipes/sockets carry **arbitrary byte streams**, not a fixed enumeration of event types — overcoming [[dis-13-4-1-signals|13.4.1]]'s 32-signal namespace limitation.

## Key Claims

- **[[MessagePassing|Message passing]] definition**: *"processes with private virtual address spaces can communicate ... by sending and receiving messages to one another."*
- **The OS provides the channel abstraction** — not the two communicating processes themselves; both processes interact with the channel via OS-mediated [[SystemCall|system calls]].
- **[[Pipe|Pipe]] = one-way channel between two same-machine processes** — write-end + read-end. Created by the `pipe` [[SystemCall|system call]].
- **[[Pipe|Pipe]] canonical use**: shell pipelines. `cat foo.c | grep factorial` — bash creates a pipe, `cat` writes to the write-end, `grep` reads from the read-end.
- **[[Socket|Socket]] = two-way channel** — each endpoint can both send and receive. Spans same-machine *and* network (via [[TCP|TCP/IP]]) — generalizing pipes off the local host.
- **Arbitrary byte stream** — unlike [[Signal|signals]]' fixed namespace, message-passing channels carry arbitrary application data.

## Key Quotes

> "Processes with private virtual address spaces can communicate ... by sending and receiving messages to one another." — definition of message passing.

> "A pipe is a one-way communication channel for two processes running on the same machine." — definition of a pipe.

> "A socket is a two-way communication channel, which means that each end of a socket can be used for both sending and receiving messages." — definition of a socket.

## Connections

- [[DiveIntoSystems]] — second sub-leaf of Ch 13.4; **123rd ingested DIS chapter**.
- [[dis-13-4-ipc]] — parent hub.
- [[dis-13-4-1-signals]] — prior sibling. Signals' fixed namespace motivates message passing's byte-stream channel.
- [[dis-13-4-3-shared-memory]] — next sibling. Shared memory eliminates the per-message copy overhead of message passing.
- [[MessagePassing]] — **new concept page**; canonical anchor for the OS-channel IPC family.
- [[Pipe]] — **new concept page**; one-way same-machine channel via the `pipe` syscall.
- [[NamedPipe]] — **new concept page**; the FIFO variant (named via filesystem path, created via `mkfifo`) — forward-referenced; 13.4.2 confines coverage to anonymous pipes.
- [[Socket]] — pre-existing concept page (if any) or forward reference; the two-way / cross-network generalization.
- [[InterprocessCommunication]] — parent umbrella concept.
- [[SystemCall]] — `pipe` is the channel-creation syscall; `read` / `write` operate on the resulting file descriptors.
- [[Process]] — the participants on either end of the channel.

## Contradictions

- None.
