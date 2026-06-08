---
title: "Stream merge (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, algorithms, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Stream_merge
---

## Summary
The task asks the programmer to merge two (and then N) already-sorted streams of items into a single sorted output stream, reading from external sources such as disk or network. The key constraint is memory efficiency: streams may be very large, so they must be consumed incrementally rather than loaded entirely into memory. The core insight is to buffer just one item per stream and repeatedly emit the smallest, refilling only the stream that was drained.

## Task Requirements
- Implement a 2-stream merge: read two sorted input streams and write one sorted output stream.
- Common 2-stream algorithm: keep one buffered item from each source, select the minimum, write it, then fetch a new item from the stream it came from.
- Implement an N-stream merge: generalize to N sorted sources.
- Common N-stream algorithm: keep the buffered items together with their source descriptors in a heap to efficiently select the minimum.
- Assume streams are very big — process them as streams, never reading an entire stream into memory.

## Language Coverage
35 languages implement this task, spanning systems and scripting languages alike. Representative implementations include C, C++, Rust, Go, Java, C#, Python, Haskell, Ruby, Perl, and Tcl.

## Connections
- [[MergeSort]] — the merge step here is exactly the combine phase of merge sort.
- [[Heap]] — the N-stream variant uses a min-heap to pick the smallest buffered item across sources.
- [[PriorityQueue]] — abstraction commonly backing the heap-based selection.
- [[ExternalSorting]] — merging sorted runs from disk is a building block of external/k-way sorting.
- [[Iterator]] — lazy, incremental consumption of each stream avoids loading data into memory.

## Contradictions
- None — reference task page.
