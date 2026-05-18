---
title: "Run-Length Encoding"
type: concept
tags: [compression, parallel-computing, prefix-scan, data-representation]
sources: [parproc-ch10-parallel-prefix-problem]
last_updated: 2026-05-17
---

# Run-Length Encoding

A lossless compression scheme that represents runs of consecutive identical values as a (count, value) pair instead of repeating the value. Abbreviated **RLE**.

## Encoding format

Given a sequence of values, consecutive identical values form a **run**. The compressed representation alternates run-counts and run-values:

```
original:    2 2 2 0 0 5 0 0
compressed:  3 2 2 0 1 5 2 0
             ^   ^ ^   ^ ^ ^
             |   | |   | | value of 3rd run (0)
             |   | |   | count of 3rd run (2)
             |   | |   value of 2nd run (5)
             |   | count of 2nd run (1)
             |   value of 1st run (2)
             count of 1st run (3)
```

The compressed array is about half the length of the original when there are many runs.

## Parallel decompression via prefix scan

Decompressing RLE in parallel maps onto [[PrefixScan|prefix scan]] naturally ([[parproc-ch10-parallel-prefix-problem]] §10.5–10.6):

1. **Extract run-counts** from the compressed array (even-indexed elements).
2. **Exclusive prefix sum** of the run-counts gives the starting offset in the output array for each run.
3. **Parallel fill**: each run $j$ writes `run-count[j]` copies of `run-value[j]` starting at `offset[j]`.

Steps 2–3 can execute in parallel across all runs simultaneously.

### OpenMP implementation (§10.5)

```c
// parprfsum: parallel prefix sum of run-counts -> tmp[]
parprfsum(tmp+1, nx2+1, z);
tmp[0] = 0;
#pragma omp parallel
{ #pragma omp for
  for (j = 0; j < nx2; j++) {
      int start = tmp[j];        // starting offset for run j
      int val   = x[2*j+1];     // run value
      int nrun  = x[2*j];       // run length
      for (k = 0; k < nrun; k++) y[start+k] = val;
  }
}
```

### Thrust implementation (§10.6)

Uses `copy_if` with an `iseven` predicate to extract run-counts, then `thrust::inclusive_scan` to build end-offsets, then derives start-offsets.

```cpp
// iseven functor: selects even-indexed elements (run-counts)
struct iseven { bool operator()(const int i) { return (i % 2) == 0; } };

thrust::device_vector<int> out(nx);
thrust::device_vector<int> seq(nx);
thrust::sequence(seq.begin(), seq.end(), 0);

// copy even-indexed elements of dx into out
auto newend = thrust::copy_if(dx.begin(), dx.end(), seq.begin(), out.begin(), iseven());
thrust::inclusive_scan(out.begin(), out.end(), out.begin());
// out now holds cumulative end-positions of each run
```

## Relationship to stream compaction

RLE decompression is a special case of the general [[StreamCompaction|stream compaction / scatter]] pattern: compute output positions via prefix scan of per-element counts, then scatter values. The same three-phase structure (count → scan → scatter) applies.

## See also

- [[PrefixScan]] — the scan primitive that makes parallel RLE decompression efficient.
- [[StreamCompaction]] — related scatter-by-offset pattern.
- [[Thrust]] — `inclusive_scan`, `copy_if` used in §10.6.
- [[OpenMP]] — `parprfsum` + `omp for` used in §10.5.
- [[parproc-ch10-parallel-prefix-problem]] — §10.5 (OpenMP), §10.6 (Thrust).
