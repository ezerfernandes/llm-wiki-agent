---
title: "MPI Communicator"
type: concept
tags: [mpi, message-passing, api, scoping, group]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI Communicator

A **communicator** is the [[MPI]] object that names a *group of processes* and provides the *context* within which messages and collectives are scoped. Every MPI communication call takes a communicator argument; the call applies only to the ranks in that communicator.

[[parproc-ch08-introduction-to-mpi]] §8.3.3.2:

> *"`MPI_COMM_WORLD` is our node group, termed a communicator in MPI parlance. MPI allows the programmer to subdivide the nodes into groups, to facilitate performance and clarity of code. Note that for some operations, such as barriers, the only way to apply the operation to a proper subset of all nodes is to form a group. The totality of all groups is denoted by `MPI_COMM_WORLD`."*

## The default: `MPI_COMM_WORLD`

The universal communicator containing every MPI process the job was launched with. Available immediately after `MPI_Init`; valid until `MPI_Finalize`.

## Ranks within a communicator

Each process gets a 0-based **rank** within each communicator it belongs to. The rank in `MPI_COMM_WORLD` is the "global" rank; the same process may have a *different* rank in any sub-communicator it joins.

```c
int world_rank, sub_rank;
MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
MPI_Comm_rank(subcomm, &sub_rank);
// world_rank and sub_rank are generally different
```

## Creating a sub-communicator: the 4-call recipe

[[parproc-ch08-introduction-to-mpi]] §8.6.10 walks an even-split-of-`nnodes` example:

```c
MPI_Group worldgroup, subgroup;
MPI_Comm  subcomm;

int nn2 = nnodes / 2;
int *subranks = malloc(nn2 * sizeof(int));
int start = (me < nn2) ? 0 : nn2;
for (int i = 0; i < nn2; i++) subranks[i] = i + start;

/* 1. Extract the group object from MPI_COMM_WORLD. */
MPI_Comm_group(MPI_COMM_WORLD, &worldgroup);

/* 2. Build a sub-group from the chosen ranks. */
MPI_Group_incl(worldgroup, nn2, subranks, &subgroup);

/* 3. Wrap the sub-group in a new communicator. */
MPI_Comm_create(MPI_COMM_WORLD, subgroup, &subcomm);

/* 4. Learn my rank in the new group. */
int subme;
MPI_Group_rank(subgroup, &subme);
```

> *"You would then use **subcomm** instead of `MPI_COMM_WORLD` whenever you wish to, say, broadcast only to that group."*

## Why subdivide?

Three reasons named or implied by [[parproc-ch08-introduction-to-mpi]] §8.6.10:

1. **Operations on a proper subset.** *"For some operations, such as barriers, the only way to apply the operation to a proper subset of all nodes is to form a group."* A collective always involves *all* ranks in its communicator — to apply a collective to a subset, you need a sub-communicator.
2. **Performance.** Restricting collectives to smaller groups reduces fan-out cost from O(log P) to O(log K) where K << P.
3. **Code clarity.** *"To facilitate performance and clarity of code."* Algorithms with phase-natural sub-groups (rows of a 2D grid, halves of a divide-and-conquer split) read more naturally with explicit sub-communicators.

## Virtual topologies

[[parproc-ch08-introduction-to-mpi]] §8.6.10 mentions: *"MPI includes a number of functions for use in creating communicators. Some set up a virtual 'topology' among the nodes. For instance, many physics problems consist of solving differential equations in two- or three-dimensional space, via approximation on a grid of points. In two dimensions, groups may consist of rows in the grid."*

The relevant API surface: `MPI_Cart_create` (Cartesian grid topology), `MPI_Cart_coords` / `MPI_Cart_rank` (rank ↔ grid-coords mapping), `MPI_Graph_create` (arbitrary graph topology). These create communicators that carry topology metadata, so the MPI implementation can optimize message routing for the assumed structure.

## Lifecycle

- `MPI_Comm_create` / `MPI_Comm_split` — create.
- `MPI_Comm_dup` — copy (creates a fresh communication context with the same group).
- `MPI_Comm_free(&comm)` — destroy.

Communicators are MPI handles (opaque pointers to runtime objects); they are not safely shareable across `MPI_Finalize` boundaries.

## Connections
- [[MPI]] — host library.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.3.3.2 / §8.6.10).
- [[CollectiveCommunication]] — collectives scope to a communicator.
- [[MPISend]] / [[MPIRecv]] — `comm` argument scoping point-to-point.
- [[MPIBcast]] / [[MPIReduce]] / [[MPIAllreduce]] / [[MPIGather]] / [[MPIAllgather]] / [[MPIScatter]] / [[MPIBarrier]] — all scope to a communicator.
- [[SPMD]] — every rank in the communicator executes the same line.
- [[Hypercube]] — Cartesian-topology communicators map naturally to hypercube subdivisions.
