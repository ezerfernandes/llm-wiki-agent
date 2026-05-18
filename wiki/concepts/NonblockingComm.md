---
title: "Nonblocking Communication (MPI)"
type: concept
tags: [mpi, message-passing, async, performance, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# Nonblocking Communication

The [[MPI]] "living dangerously" variants of [[MPISend|`MPI_Send`]] / [[MPIRecv|`MPI_Recv`]] that **return immediately** rather than waiting for completion. [[parproc-ch08-introduction-to-mpi]] §8.7.3:

> *"If one is sure that there will be no problems of buffer overflow and so on, one can use variant send and receive calls provided by MPI, such as `MPI_Isend()` and `MPI_Irecv()`. The key difference between them and `MPI_Send()` and `MPI_Recv()` is that they return immediately, and thus are termed **nonblocking**. Your code can go on and do other things, not having to wait."*

The `I` prefix stands for *Immediate*.

## API surface

```c
int MPI_Isend(const void *buf, int count, MPI_Datatype datatype,
              int dest, int tag, MPI_Comm comm,
              MPI_Request *request);

int MPI_Irecv(void *buf, int count, MPI_Datatype datatype,
              int source, int tag, MPI_Comm comm,
              MPI_Request *request);

int MPI_Wait (MPI_Request *request, MPI_Status *status);
int MPI_Probe(int source, int tag, MPI_Comm comm, MPI_Status *status);
int MPI_Test (MPI_Request *request, int *flag, MPI_Status *status);
```

The `MPI_Request` handle returned by `MPI_Isend`/`MPI_Irecv` represents the *pending operation*. `MPI_Wait` blocks on it until completion; `MPI_Test` polls non-blockingly; `MPI_Probe` peeks at the matching message without consuming it.

## The safety contract

[[parproc-ch08-introduction-to-mpi]] §8.7.3 spells out the user's obligations:

> *"This does mean that at A you cannot touch the data you are sending until you determine that it has either been buffered somewhere or has reached x at B. Similarly, at B you can't use the data at x until you determine that it has arrived. Such determinations can be made via `MPI_Wait()`. In other words, you can do your send or receive, then perform some other computations for a while, and then call `MPI_Wait()` to determine whether you can go on. Or you can call `MPI_Probe()` to ask whether the operation has completed yet."*

So the rule is **don't touch the buffer until you've confirmed completion** — touching means reading the receive buffer or writing/reading the send buffer.

## When to use

Nonblocking calls exist to **overlap communication and computation**:

```c
MPI_Request reqs[2];
MPI_Isend(send_buf, n, MPI_DOUBLE, peer, 0, comm, &reqs[0]);
MPI_Irecv(recv_buf, n, MPI_DOUBLE, peer, 0, comm, &reqs[1]);

compute_unrelated_thing();   // happens in parallel with the comm

MPI_Waitall(2, reqs, MPI_STATUSES_IGNORE);  // now both buffers are ready
use(send_buf);  use(recv_buf);
```

On a network with hardware-offloaded send/receive (e.g. [[Infiniband]] with HCA-driven RDMA), the comm makes progress in the background while the CPU does `compute_unrelated_thing` — yielding near-perfect overlap.

## Other escape from sync deadlock

`MPI_Isend` + `MPI_Irecv` is also the canonical fix for the [[BufferingMPI|synchronous-deadlock]] pattern: both ranks post their nonblocking sends first (which return immediately), then both post their nonblocking receives, then both `MPI_Wait`. No rank ever blocks waiting for a peer's *initiation*, so the circular-wait deadlock cannot form.

## Why is it called "living dangerously"?

The §8.7.3 section heading. Two senses:

1. **Buffer-reuse risk.** If the user touches the send buffer before completion, data sent over the wire may be corrupted (with no error report).
2. **Buffer-overflow risk.** Even with nonblocking calls, the OS-level buffer space is finite; pushing too many `MPI_Isend`s without matching completions can still exhaust resources.

The chapter's pragma: only use nonblocking calls *"if one is sure that there will be no problems of buffer overflow and so on."*

## Related: `MPI_Sendrecv` (the *safe* alternative)

For pure exchange patterns, the chapter recommends [[BufferingMPI|`MPI_Sendrecv` / `MPI_Sendrecv_replace`]] in §8.7.4 instead. It is *"a more convenient, safer and possibly faster alternative"* — a *single blocking* call that posts a send + receive together and lets MPI find a deadlock-free ordering.

## Connections
- [[MPI]] — host library.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.7.3).
- [[MPISend]] / [[MPIRecv]] — the blocking variants.
- [[BufferingMPI]] — semantics this page contrasts against.
- [[Deadlock]] — the synchronous-deadlock pattern nonblocking calls avoid.
- [[Infiniband]] — fabrics with hardware-offloaded sends gain the most from nonblocking overlap.
