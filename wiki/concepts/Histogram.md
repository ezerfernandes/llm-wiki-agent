---
title: "Histogram"
type: concept
tags: [statistics, data-mining, image-processing, parallel-computing]
sources: [parproc-ch14-statistics-data-mining]
last_updated: 2026-05-17
---

# Histogram

A discrete frequency table that partitions a range of values into intervals (bins) and counts how many data points fall into each bin. It is the simplest estimator of a [[ProbabilityDensityFunction]]; scaled to total area 1, it approximates f(x) as a step function.

## Image Histogram (CUDA)

In image processing, a histogram counts how many pixels have each intensity level (one "interval" per level, so no bin-width issue). The serial pseudocode is:

```
for i = 1,...,numintenslevels:
    count = 0
    for row = 1,...,numrows:
        for col = 1,...,numcols:
            if image[row][col] == i: count++
    hist[i] = count
```

This is embarrassingly parallel: in OpenMP, threads handle blocks of rows; in CUDA, threads handle individual pixels (parallelizing the nested row/col loops).

## Podlozhnyuk's CUDA Histogram Algorithm

Naively parallelizing the pixel loop creates write conflicts on the shared histogram array — a major performance problem. Victor Podlozhnyuk (NVIDIA, 2007) devised a subhistogram-merge strategy:

- Each thread (or warp) maintains its own **subhistogram** in shared memory.
- After all pixels are processed, subhistograms within a block are merged, then merged across blocks using `atomicAdd()`.
- Careful access ordering eliminates shared-memory **bank conflicts**.

Two variants:
- **histogram64**: one subhistogram per thread; 64 intensity levels (6-bit data); 1 byte per count; 192 threads/block (16K shared memory / 192 ≈ 85 bytes/thread — fits 64 bytes of histogram plus overhead).
- **histogram256**: one subhistogram per warp; full 256 intensity levels (8-bit data); 4 bytes per count; table is 256 rows × 32 columns (one column per thread in the warp), 4 bytes per entry.

The 64-level restriction in histogram64 stems from NVIDIA's recommendation of 128–256 threads/block and the 16K shared memory limit; 256 intensity levels × 1 byte/thread × 192 threads = 192 bytes/thread, which exceeds 85 bytes. histogram256 resolves this by switching to per-warp granularity. (§14.2.2, [[parproc-ch14-statistics-data-mining]])

## Connections

- [[ProbabilityDensityFunction]] — histogram is its discrete/crude estimator.
- [[KernelDensityEstimation]] — the smooth alternative to histogram density estimation.
- [[CUDA]] — Podlozhnyuk's algorithm is a CUDA optimization case study.
- [[BankConflict]] — the key hardware hazard that histogram64/256 designs around.
- [[parproc-ch14-statistics-data-mining]] — primary source (§14.2.2).
- [[parproc-ch05-cuda-gpu-programming]] — CUDA shared memory and bank conflict concepts introduced.
