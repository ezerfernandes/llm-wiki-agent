---
title: "Radix Sort"
type: concept
tags: [algorithm, sorting, parallel-computing, cuda]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# Radix Sort

A non-comparison sort that treats bucket assignment as a function of a datum's bits rather than its value relative to other elements. A special case of [[SamplingBucketSort|bucket sort]] where bucket boundaries are determined by bit patterns rather than by sampling.

## Principle

With k threads, each datum's bucket is determined by its lower log₂(k) bits. For example, with 16 threads, the lower 4 bits determine the bucket. As long as data is roughly uniform under the mod-k operation, no sampling step is needed — the bucket sizes will be approximately equal.

Buckets are formed one bit at a time, using a **segmented scan** operation (see [[PrefixScan]]).

## GPU Implementation

The CUDPP GPU library implements radix sort. The buckets are formed one bit at a time using segmented scan (Ch10 / §12.6). This makes radix sort particularly efficient on GPUs, where prefix scan primitives are natively supported.

## Connections

- [[SamplingBucketSort]] — radix sort is bucket sort with bit-level bucket boundaries; no sampling needed when data is uniform.
- [[PrefixScan]] — segmented scan is the key primitive in CUDPP's implementation.
- [[CUDA]] — GPU implementation via CUDPP.
- [[parproc-ch12-parallel-sorting]] — §12.6 source.
