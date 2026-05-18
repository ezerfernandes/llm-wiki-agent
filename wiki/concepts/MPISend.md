---
title: "MPI_Send"
type: concept
tags: [mpi, message-passing, point-to-point, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI_Send

The fundamental point-to-point send call in [[MPI]]. Six arguments:

```c
int MPI_Send(const void *buf,
             int count,
             MPI_Datatype datatype,
             int dest,
             int tag,
             MPI_Comm comm);
```

[[parproc-ch08-introduction-to-mpi]] §8.3.3.3 walks the arguments using the call `MPI_Send(mymin, 2, MPI_INT, 0, MYMIN_MSG, MPI_COMM_WORLD)`:

| Argument | Meaning |
|---|---|
| `buf = mymin` | *"the address at which these bytes begin."* |
| `count = 2`, `datatype = MPI_INT` | *"our set of bytes to be sent consists of 2 objects of type MPI_INT."* |
| `dest = 0` | *"we are sending to node 0."* |
| `tag = MYMIN_MSG` | *"the message type, programmer-defined."* |
| `comm = MPI_COMM_WORLD` | *"the node group to which the message is to be sent."* |

## Why typed messages?

[[parproc-ch08-introduction-to-mpi]] §8.3.3.3 explains the seemingly-redundant `count` + `datatype` pair:

> *"Why did the designers of MPI bother to define data types? The answer is that we want to be able to run MPI on a heterogeneous set of machines, with MPI serving as the 'broker' between them in case different architectures among those machines handle data differently."*

Two heterogeneity sources:

1. **Endianness** — Intel little-endian vs Sun SPARC big-endian. *"If our set of nodes included machines of both types, straight transmission of sequences of 8 bytes might mean that some of the machines literally receive the data backwards!"*
2. **Word width** — 32-bit vs 64-bit machines, *"some major problems would occur if no conversion were done."*

## Common MPI datatypes

| Type | C equivalent |
|---|---|
| `MPI_CHAR` | `char` |
| `MPI_INT` | `int` |
| `MPI_LONG` | `long` |
| `MPI_FLOAT` | `float` |
| `MPI_DOUBLE` | `double` |
| `MPI_2INT` | `(int, int)` pair (for `MAXLOC`/`MINLOC` reductions) |
| `MPI_BYTE` | uninterpreted bytes (no conversion) |

## Return semantics

The exact MPI standard guarantee ([[parproc-ch08-introduction-to-mpi]] §8.7.1):

> *"`MPI_Send(x,...)` will return only when it is safe for the application program to write over the array which it is using to store its message, i.e. x."*

So *"send returned"* means *"my send buffer is reusable"* — **not** *"the receiver has the data."* The buffering layer (OS socket buffer, MPI internal buffer, or — on small messages — direct copy into the network adapter) can decouple these two events. In particular:

- On a buffered implementation, `MPI_Send` returns *as soon as the bytes are safely copied somewhere else* (could be still in flight, or sitting in the receiver's OS buffer).
- On a synchronous implementation, `MPI_Send` does not return until the receiver has matched it with a corresponding `MPI_Recv`.
- The application program **cannot tell which mode it is in** from the call alone — making `MPI_Send` correctness-portable but performance-non-portable.

## Can it block?

Yes. *"If the platform and MPI implementation is that of the TCP/IP network context described above, then the send call will return when its call to the OS' `write()` (or equivalent, depending on OS) returns, but that could be delayed if the OS' buffer space is full. On the other hand, another implementation could require a positive response from B before allowing the send call to return."* ([[parproc-ch08-introduction-to-mpi]] §8.7.1).

## Variants

- [[MPIRecv|`MPI_Recv`]] — matching receive.
- `MPI_Ssend` — explicitly *synchronous* send: only returns when matched.
- `MPI_Bsend` — *buffered* send: explicitly use the user-provided buffer.
- `MPI_Rsend` — *ready* send: caller asserts receiver is already ready.
- [[NonblockingComm|`MPI_Isend`]] — nonblocking variant; returns immediately, completion checked via `MPI_Wait`/`MPI_Probe`.

## Connections
- [[MPI]] — host library.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.3.3.3 / §8.7.1).
- [[MPIRecv]] — matching receive.
- [[MPICommunicator]] — `comm` argument scoping.
- [[BufferingMPI]] — semantics of when send returns.
- [[NonblockingComm]] — `MPI_Isend` variant.
- [[Deadlock]] — synchronous tag mismatch can deadlock a pair of sends.
- [[SPMD]] — every rank can call `MPI_Send`, scoped by `if (me == ...)` branches.
