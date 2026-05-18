---
title: "Buffering, Synchrony, and Safety in MPI"
type: concept
tags: [mpi, message-passing, semantics, performance, deadlock]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# Buffering and Synchrony in MPI

The semantic and performance behavior of [[MPI]] send/receive depends on **where the message bytes live between sender and receiver**. [[parproc-ch08-introduction-to-mpi]] §8.7 is the chapter's deep dive into this layering.

## Three layers of abstraction

[[parproc-ch08-introduction-to-mpi]] §8.7.1, on a TCP/IP cluster:

> *"It is extremely import to keep in mind the levels of abstraction here. The OS's TCP/IP stack is running at the Session, Transport and Network layers of the network. MPI — meaning the MPI internals — is running above the TCP/IP stack, in the Application layers at A and B. And the MPI user-written application could be considered to be running at a 'Super-application' layer, since it calls the MPI internals."*

```
+----------------------------------+
|  User MPI program  (Super-app)   |  <- calls MPI_Send / MPI_Recv
+----------------------------------+
|  MPI internals     (App layer)   |  <- writes to / reads from socket
+----------------------------------+
|  OS TCP/IP stack   (Session+)    |  <- moves bytes over the wire
+----------------------------------+
|  Network hardware                |
+----------------------------------+
```

## What `MPI_Init` does (on TCP/IP)

*"MPI at node A will have set up a TCP/IP socket to B during the user program's call to `MPI_Init()`. The other end of the socket will be a corresponding one at B. This setting up of this socket pair as establishing a connection between A and B."*

So `MPI_Init` opens persistent TCP sockets between every pair of MPI processes (or some subset, depending on implementation).

## What `MPI_Send` does

*"When node A calls `MPI_Send()`, MPI will write to the socket, and the TCP/IP stack will transmit that data to the TCP/IP socket at B. The TCP/IP stack at B will then send whatever bytes come in to MPI at B."*

## What `MPI_Recv` does

*"Think of what happens the MPI application at B calls `MPI_Recv()`, requesting to receive from A, with a certain tag T. Say the first argument is named x, i.e. the data to be received is to be deposited at x. If MPI sees that it already has a message of tag T, it will have its `MPI_Recv()` function return the message to the caller, i.e. to the MPI application at B. **If no such message has arrived yet, MPI won't return to the caller yet, and thus the caller blocks.**"*

## Trap 1: TCP coalesces messages

[[parproc-ch08-introduction-to-mpi]] §8.7.1:

> *"In TCP/IP the totality of bytes sent by A to B during lifetime of the connection is considered one long message. So for instance if the MPI program at A calls `MPI_Send()` five times, the MPI internals will write to the socket five times, but the bytes from those five messages will not be perceived by the TCP/IP stack at B as five messages, but rather as just one long message (in fact, only part of one long message, since more may be yet to come)."*

MPI's internal job at B is to **re-parse message boundaries** from the inbound TCP byte stream and queue them as discrete logical messages:

> *"MPI at B continually reads that 'long message' and breaks it back into MPI messages, keeping them ready for calls to `MPI_Recv()` from the MPI application program at B. Note carefully that phrase, keeping them ready; it refers to the fact that the order in which the MPI application program requests those messages may be different from the order in which they arrive."*

So **MPI implements its own message-framing protocol on top of TCP**, plus a queue for out-of-order matching by tag/source.

## Trap 2: OS buffer is finite (flow control)

> *"The buffer space the OS at B has set up for receiving data is limited. As A is sending to B, the TCP layer at B is telling its counterpart at A when A is allowed to send more data."*

When the receiver's OS buffer fills, the sender's `write()` call blocks — and so `MPI_Send` may block too, **even if the implementation is nominally buffered**.

## The exact MPI standard send semantics

[[parproc-ch08-introduction-to-mpi]] §8.7.1:

> *"Technically, the MPI standard states that `MPI_Send(x,...)` will return only when it is safe for the application program to write over the array which it is using to store its message, i.e. x. As we have seen, there are various ways to implement this, with performance implications. Similarly, `MPI_Recv(y,...)` will return only when it is safe to read y."*

So the MPI-standard guarantee is **buffer-reusability**, not **delivery**:

- `MPI_Send` returns when `x` is safe to overwrite (the bytes are buffered somewhere or already arrived).
- `MPI_Recv` returns when `y` is safe to read (the bytes have been deposited).

These are *not* the same event.

## The performance cost of buffering

> *"Note that buffering slows everything down. In our TCP scenario above, `MPI_Recv()` at B must copy messages from the OS' buffer space to the MPI application program's program variables, e.g. x above. This is definitely a blow to performance."*

This OS-buffer → app-buffer copy is the **per-message overhead** MPI on TCP cannot avoid. The chapter motivates [[Infiniband]] / RDMA as the cure:

> *"That in fact is why networks developed specially for parallel processing typically include mechanisms to avoid the copying. Infiniband, for example, has a Remote Direct Memory Access capability, meaning that A can write directly to x at B."*

So **on Infiniband with RDMA, the OS-buffer → app-buffer copy is eliminated** — A's network adapter writes directly into B's application-layer destination address.

## Synchrony and [[Deadlock|deadlock]]

[[parproc-ch08-introduction-to-mpi]] §8.7.2 names two failure modes:

### 1. Synchronous tag-mismatch deadlock

> *"With synchronous communication, deadlock is a real risk. Say A wants to send two messages to B, of types U and V, but that B wants to receive V first. Then A won't even get to send V, because in preparing to send U it must wait for a notice from B that B wants to read U — a notice which will never come, because B sends such a notice for V first."*

Both ranks block forever, each waiting for the other to make progress.

### 2. Buffer exhaustion (even with async)

> *"Even with buffering, as buffer space is always by nature finite. A program can fail if it runs out of buffer space, either at the sender or the receiver."*

The chapter points at the LLNL `unsafe.c` example which deliberately overwhelms receiver buffers on a chosen platform.

## "Unsafe" in MPI terminology

> *"In MPI terminology, asynchronous communication is considered **unsafe**. The program may run fine on most systems, as most systems are buffered, but fail on some systems. Of course, as long as you know your program won't be run in nonbuffered settings, it's fine, and since there is potentially such a performance penalty for doing things synchronously, most people are willing to go ahead with their 'unsafe' code."*

So *"safe"* in MPI ≠ *"will not deadlock"* — *"safe"* means *"correct under any conforming MPI implementation, including synchronous-only ones."* Most production MPI code is **technically unsafe** (relying on the buffered behavior of the actual implementation) and most authors accept this.

## How to write safe code

Three idioms:

- **Lower-rank-sends-first.** In an exchange, the rank with the smaller rank sends first; the larger rank receives first. Breaks circular waiting.
- **`MPI_Sendrecv` / `MPI_Sendrecv_replace`.** A single call that posts both halves of an exchange atomically; the implementation is responsible for finding a safe ordering. *"A more convenient, safer and possibly faster alternative."* ([[parproc-ch08-introduction-to-mpi]] §8.7.4).
- **[[NonblockingComm|`MPI_Isend` / `MPI_Irecv`]] + `MPI_Wait`.** Post both halves nonblockingly; let MPI sort out the order; wait for both to complete.

## Connections
- [[MPI]] — host library.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.7).
- [[MPISend]] / [[MPIRecv]] — the calls whose semantics this page details.
- [[NonblockingComm]] — the "living dangerously" `MPI_Isend` / `MPI_Irecv` escape hatch.
- [[Deadlock]] — the failure mode synchronous semantics enable.
- [[Infiniband]] — the RDMA-capable fabric that bypasses the OS-buffer copy.
- [[parproc-ch07-message-passing-systems]] — Ch7's RDMA discussion.
- [[Latency]] / [[Bandwidth]] — buffering trades latency for bandwidth efficiency.
