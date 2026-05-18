---
title: "Hyperquicksort"
type: concept
tags: [algorithm, sorting, parallel-computing, hypercube, message-passing]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# Hyperquicksort

Distributed [[Quicksort]] variant designed for hypercube topologies, generalized to any message-passing system with a power-of-2 number of nodes. Originally developed for hypercube architectures (see [[parproc-ch07-message-passing-systems]] for hypercube definitions).

## Algorithm

Precondition: each PE holds some chunk of the array to be sorted. After sorting, each PE holds a sorted chunk such that (1) each chunk is itself in sorted order, and (2) for all i < j, every element at PE i is less than every element at PE j.

For a d-cube with d rounds:

```
for i = d downto 1:
    for each i-cube:
        root of the i-cube broadcasts its median to all PEs in the i-cube (serves as pivot)
        consider the two (i-1)-subcubes of this i-cube:
            each pair of partners in the (i-1)-subcubes exchanges data
            lower-numbered PE keeps data ≤ pivot
            higher-numbered PE keeps data > pivot
```

After d such steps the array is sorted globally across PEs. If sorted output is needed at a single node (e.g. node 0), a final gather collects the chunks; if sorting is an intermediate step in a distributed computation the chunks may remain distributed.

## Implementation Notes

- To avoid deadlock in MPI, the lower-numbered partner should send then receive, and the higher-numbered partner should receive then send. Alternatively, use `MPI_SendRcv()`.
- The algorithm requires the number of PEs to be a power of 2.
- Load balancing depends on pivot quality; the median is the ideal pivot but computing the true median is expensive — approximate medians (e.g. median of a sample) are used in practice.

## Connections

- [[Quicksort]] — the sequential algorithm this extends to distributed memory.
- [[CompareExchange]] — the partner-data-exchange-and-split primitive used in each round.
- [[parproc-ch12-parallel-sorting]] — §12.1.3 source.
- [[parproc-ch07-message-passing-systems]] — hypercube topology and terminology.
- [[MPI]] — typical implementation vehicle; `MPI_SendRcv` recommended for deadlock avoidance.
- [[LoadBalancing]] — pivot quality determines work balance across subcubes.
