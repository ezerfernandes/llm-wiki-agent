---
title: "Hillis-Steele Scan"
type: concept
tags: [parallel-computing, algorithm, prefix-scan, data-parallel]
sources: [parproc-ch10-parallel-prefix-problem]
last_updated: 2026-05-17
---

# Hillis-Steele Scan

A data-parallel algorithm for computing a [[PrefixScan|prefix scan]] in $\log_2 n$ rounds, introduced in the parallel-computing literature by Danny Hillis and Guy Steele. Assumes one thread per element (n = p). Also called the **naive parallel scan** or **Kogge-Stone scan** in hardware contexts.

## Algorithm (n = 8, inclusive sum)

At step $k$ ($k = 1, 2, ..., \log_2 n$), every position $j \geq 2^{k-1}$ adds the element $2^{k-1}$ positions to its left:

- **Step 1** (distance 1): $x_1 \leftarrow x_0+x_1$, $x_2 \leftarrow x_1+x_2$, ..., $x_7 \leftarrow x_6+x_7$
- **Step 2** (distance 2): $x_2 \leftarrow x_0+x_2$, $x_3 \leftarrow x_1+x_3$, ..., $x_7 \leftarrow x_5+x_7$
- **Step 3** (distance 4): $x_4 \leftarrow x_0+x_4$, $x_5 \leftarrow x_1+x_5$, $x_6 \leftarrow x_2+x_6$, $x_7 \leftarrow x_3+x_7$

After step 3, $x_7$ holds $a_0+a_1+\cdots+a_7$ (the full prefix sum). The correctness argument: $x_7$'s contents after successive steps are $a_6+a_7$ → $a_4+a_5+a_6+a_7$ → $a_0+\cdots+a_7$.

For general n, the number of steps is $\lfloor \log_2 n \rfloor$ (or $\log_2 n$ when n is a power of 2).

## Read-after-write hazard: red/black buffers

Because step $k$ reads and writes the same array, the result of a position updated early in step $k$ could be read by a later position in the same step (a race). The standard fix is the **red/black (double-buffer) method**: maintain two arrays and alternate which is the input and which is the output on each step. Odd steps write to the "black" array; even steps write to the "red" array. ([[parproc-ch10-parallel-prefix-problem]] §10.2, footnote 1.)

## Complexity

| Dimension | Cost |
|---|---|
| Depth (span) | $O(\log n)$ |
| Total work | $O(n \log n)$ |
| Sequential baseline | $O(n)$ |

Total work exceeds the sequential baseline. Load balancing degrades each round: at step $k$, only $n - 2^{k-1}$ threads do useful work; the rest are idle. Synchronisation between steps adds overhead, especially on multi-block GPU configurations.

## Comparison with Blelloch

| Property | Hillis-Steele | [[BlellochScan\|Blelloch]] |
|---|---|---|
| Depth | $O(\log n)$ | $O(\log n)$ |
| Work | $O(n \log n)$ | $O(n)$ |
| Passes | 1 | 2 (up-sweep + down-sweep) |
| Load balance | Poor (idle threads grow) | Better |
| Simplicity | Simpler to implement | More complex |

Hillis-Steele is preferred when $n$ is small or implementation simplicity matters. Blelloch is preferred on GPU where total work determines throughput (work-efficient).

## See also

- [[PrefixScan]] — the general primitive; algorithm comparison table.
- [[BlellochScan]] — the work-efficient two-pass alternative.
- [[parproc-ch10-parallel-prefix-problem]] — §10.2 (derivation and worked example).
