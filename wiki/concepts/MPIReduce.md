---
title: "MPI_Reduce"
type: concept
tags: [mpi, message-passing, collective-ops, reduce, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI_Reduce

All-to-one [[CollectiveCommunication|collective]] reduction in [[MPI]]:

```c
int MPI_Reduce(const void *sendbuf, void *recvbuf,
               int count, MPI_Datatype datatype,
               MPI_Op op,
               int root, MPI_Comm comm);
```

Every rank contributes `sendbuf`; the operation `op` is applied across all contributions; the result lands in `recvbuf` **only at the `root` rank**. Other ranks' `recvbuf` is unmodified.

## Worked example from Dijkstra

[[parproc-ch08-introduction-to-mpi]] §8.6.3:

```c
MPI_Reduce(mymin, overallmin, 1, MPI_2INT, MPI_MINLOC, 0, MPI_COMM_WORLD);
```

> *"At this point all nodes in this group participate in a 'reduce' operation. The type of reduce operation is MPI_MINLOC, which means that the minimum value among the nodes will be computed, and the index attaining that minimum will be recorded as well. Each node contributes a value to be checked, and an associated index, from a location mymin in their programs; the type of the pair is MPI_2INT. The overall min value/index will be computed by combining all of these values at node 0, where they will be placed at a location overallmin."*

This single line replaces the hand-written `findoverallmin` function from §8.3.2 — workers no longer `MPI_Send` their per-chunk mins to node 0, and node 0 no longer `MPI_Recv`s and compares them one by one.

## The reduce-operation table

[[parproc-ch08-introduction-to-mpi]] §8.6.3 lists 12 built-in operations:

| `op` | Meaning |
|---|---|
| `MPI_MAX` | element-wise max |
| `MPI_MIN` | element-wise min |
| `MPI_SUM` | element-wise sum |
| `MPI_PROD` | element-wise product |
| `MPI_LAND` | wordwise boolean and |
| `MPI_LOR` | wordwise boolean or |
| `MPI_LXOR` | wordwise exclusive or |
| `MPI_BAND` | bitwise boolean and |
| `MPI_BOR` | bitwise boolean or |
| `MPI_BXOR` | bitwise exclusive or |
| `MPI_MAXLOC` | max value **and** location (rank or programmer-supplied index) |
| `MPI_MINLOC` | min value **and** location |

`MAXLOC` / `MINLOC` operate on **pair types** like `MPI_2INT` — each contribution is a `(value, index)` tuple; the reduction returns both the extremal value *and* the index attaining it.

## User-defined operations

Beyond the 12 built-ins, applications can register their own reduction operations via `MPI_Op_create(...)` taking a user-defined function pointer + a *commutative* flag. Required mathematical property: **associativity** (commutativity optional but enables more aggressive scheduling).

## Implementation: O(log P) tree

For an associative `op`, the canonical implementation is a **reduction tree**:

```
step 0:   pairs of leaves combine
step 1:   pairs of step-0 outputs combine
...
step log P: root holds the global result
```

`log P` rounds; each round uses dedicated point-to-point sends in a logical [[Hypercube]]-style schedule.

## Reduce + Bcast = [[MPIAllreduce|`MPI_Allreduce`]]

The very common idiom *"compute a reduction, then distribute the result back to everyone"* is collapsed into [[MPIAllreduce]] in one call:

```c
MPI_Reduce  (mymin, overallmin, 1, MPI_2INT, MPI_MINLOC, 0, MPI_COMM_WORLD);
MPI_Bcast   (overallmin, 1, MPI_2INT, 0, MPI_COMM_WORLD);
// equivalent to:
MPI_Allreduce(mymin, overallmin, 1, MPI_2INT, MPI_MINLOC, MPI_COMM_WORLD);
```

[[parproc-ch08-introduction-to-mpi]] §8.6.3: *"Again, these can be optimized for particular platforms."*

## Connections
- [[MPI]] — host library.
- [[CollectiveCommunication]] — class.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.6.3).
- [[MPIAllreduce]] — reduce + broadcast collapsed.
- [[MPIBcast]] — the inverse-direction (one → all) collective.
- [[MPIGather]] — the *concatenating* all-to-one collective (no reduction op).
- [[AllReduce]] — the deep-learning collective primitive; an `MPI_Allreduce`-with-`MPI_SUM` over gradient vectors is its canonical realization.
- [[ReductionClause]] — OpenMP's shared-memory analog.
- [[PrefixScan]] — the running-result generalization (`MPI_Scan` / `MPI_Exscan` in MPI).
- [[Hypercube]] — the logical topology O(log P) reduction trees use.
- [[MPICommunicator]] — scoping.
