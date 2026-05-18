---
title: "CompareExchange"
type: concept
tags: [algorithm, sorting, parallel-computing, primitive]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# CompareExchange

Also called **compare-split**. A fundamental primitive in parallel sorting: two nodes pool their combined data, then the lower-ID node keeps the lower half and the higher-ID node keeps the upper half.

## Pseudocode

```
send all my data to partner
receive all my partner's data
if I have a lower id than my partner:
    I keep the lower half of the pooled data
else:
    I keep the upper half of the pooled data
```

In the shared-memory bubble-sort context, this reduces to:

```c
if (x[i] > x[j])
    swap x[i] and x[j];
```

## Role in Sorting Networks

Compare-exchange is the building block of several parallel sorting algorithms:

- **[[BitonicMergesort]]** — pairwise compare-exchanges on bitonic sequences produce two bitonic halves with all-lower ≤ all-upper.
- **[[Hyperquicksort]]** — each partner pair in a hypercube subcube performs a compare-exchange to split data around a broadcast pivot.
- **[[OddEvenTransposition]]** — alternating odd/even phases of compare-exchanges on adjacent element pairs.
- **[[BubbleSort]]** — the inner loop is a sequence of compare-exchange operations.

## Connections

- [[BitonicMergesort]] — uses compare-exchange as its core operation.
- [[Hyperquicksort]] — partner-data exchange and split in each hypercube round.
- [[OddEvenTransposition]] — adjacent-element compare-exchanges in alternating phases.
- [[BubbleSort]] — compare-exchange on pairs in the inner loop.
- [[parproc-ch12-parallel-sorting]] — §12.2.4 source.
- [[MPI]] — typical implementation vehicle for the distributed compare-exchange.
