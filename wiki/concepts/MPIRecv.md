---
title: "MPI_Recv"
type: concept
tags: [mpi, message-passing, point-to-point, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI_Recv

The fundamental point-to-point receive call in [[MPI]]. Seven arguments (six match [[MPISend|`MPI_Send`]] + one output `status`):

```c
int MPI_Recv(void *buf,
             int count,
             MPI_Datatype datatype,
             int source,
             int tag,
             MPI_Comm comm,
             MPI_Status *status);
```

[[parproc-ch08-introduction-to-mpi]] §8.3.3.4 walks the arguments using `MPI_Recv(othermin, 2, MPI_INT, i, MYMIN_MSG, MPI_COMM_WORLD, &status)`:

| Argument | Meaning |
|---|---|
| `buf = othermin` | *"the received message is to be placed at our location othermin."* |
| `count = 2`, `datatype = MPI_INT` | *"two objects of MPI_INT type are to be received."* |
| `source = i` | *"receive only messages from node i. If we did not care what node we received a message from, we could specify the value MPI_ANY_SOURCE."* |
| `tag = MYMIN_MSG` | *"receive only messages of type MYMIN_MSG. If we did not care what type of message we received, we would specify the value MPI_ANY_TAG."* |
| `comm = MPI_COMM_WORLD` | The communicator. |
| `status = &status` | Output struct (see below). |

## Wildcards

- **`MPI_ANY_SOURCE`** — match a message from any rank in the communicator.
- **`MPI_ANY_TAG`** — match a message with any tag.

After a wildcard receive, the actual sender and tag are recoverable from the `MPI_Status` struct.

## `MPI_Status` struct

[[parproc-ch08-introduction-to-mpi]] §8.3.3.4: *"An MPI struct containing information about the received message. Its primary fields of interest are MPI_SOURCE, which contains the identity of the sending node, and MPI_TAG, which contains the message type."*

| Field | Meaning |
|---|---|
| `status.MPI_SOURCE` | Actual sender's rank (relevant after `MPI_ANY_SOURCE`). |
| `status.MPI_TAG` | Actual tag (relevant after `MPI_ANY_TAG`). |
| (queried via `MPI_Get_count`) | Actual element count of the received message. |

## Variable-length receives: `MPI_Get_count`

The receive buffer's `count` is an **upper bound** — actual messages can be smaller. To learn how many elements actually arrived:

```c
MPI_Status status;
MPI_Recv(buf, MAX_N, MPI_INT, source, tag, comm, &status);
int actual_count;
MPI_Get_count(&status, MPI_INT, &actual_count);
```

[[parproc-ch08-introduction-to-mpi]] §8.4 uses this pattern in the 0-removal stream-compaction example: each worker sends back a variable-length list of nonzero elements, and the manager uses `MPI_Get_count` to learn how many per chunk.

## Blocking semantics

[[parproc-ch08-introduction-to-mpi]] §8.7.1: *"If no such message has arrived yet, MPI won't return to the caller yet, and thus the caller blocks."*

So `MPI_Recv` is unconditionally blocking — it waits until a matching message (by source rank, tag, and communicator) arrives in the MPI internals' queue.

## Performance cost: the buffer copy

*"MPI_Recv at B must copy messages from the OS' buffer space to the MPI application program's program variables, e.g. x above. This is definitely a blow to performance. That in fact is why networks developed specially for parallel processing typically include mechanisms to avoid the copying. Infiniband, for example, has a Remote Direct Memory Access capability, meaning that A can write directly to x at B."* ([[parproc-ch08-introduction-to-mpi]] §8.7.1).

So **`MPI_Recv` on TCP/IP has a mandatory copy** OS-buffer → app-buffer; [[Infiniband]] RDMA bypasses this with zero-copy direct writes into the application's buffer.

## Connections
- [[MPI]] — host library.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.3.3.4 / §8.4 / §8.7.1).
- [[MPISend]] — matching send.
- [[MPICommunicator]] — `comm` argument scoping.
- [[BufferingMPI]] — semantics of the receive-side buffer + the OS→app copy.
- [[NonblockingComm]] — `MPI_Irecv` variant + `MPI_Probe` for peeking.
- [[Infiniband]] — RDMA avoids the buffer-copy overhead.
- [[Deadlock]] — wrong receive ordering vs sender can deadlock.
- [[SPMD]] — typical pattern: `if (me == 0) MPI_Recv(...) else MPI_Send(...)`.
