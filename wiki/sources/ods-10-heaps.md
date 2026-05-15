---
title: "ODS Ch.10: Heaps"
type: source
tags: [book, data-structures, heaps, priority-queue]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 10
pages: "203-216"
---

## Summary
Two implementations of the priority Queue. **BinaryHeap** uses an implicit complete binary tree stored as an array via **Eytzinger's method** — root at index 0, children of i at 2i+1 and 2i+2, parent at (i−1)/2. Maintains the **heap-ordered** invariant (parent ≤ children), giving O(log n) add and remove via bubble-up and trickle-down. **MeldableHeap** is a randomized binary tree with a *meld(h1, h2)* operation that combines two heaps in O(log(n1+n2)) expected time by descending one or the other randomly at each step, supporting all priority Queue operations on top of it.

## Key Claims
- **Eytzinger's method** lays out a complete binary tree in array order without explicit pointers. left(i) = 2i+1; right(i) = 2i+2; parent(i) = (i−1)/2.
- **Heap-order**: a[i] ≥ a[parent(i)] for all i > 0 → root is minimum (or a[0] is min in min-heap formulation here). add(x) appends and bubbles up; remove() takes a[0], moves a[n−1] to root, and trickles down.
- **Cost**: add/remove are O(log n) since path length is bounded by height = O(log n) of a complete tree.
- **MeldableHeap** uses a binary-tree representation with random merge. merge(h1, h2): if either is nil return the other; otherwise pick the smaller root, recursively merge one of its children with the other heap (chosen by coin flip); reattach.
- **Amortized doubling** for the BinaryHeap's backing array follows the same argument as [[ods-02-array-based-lists]].
- **Heap-sort** (developed in [[ods-11-sorting-algorithms]]): n add followed by n remove sorts in O(n log n) — and is in-place since the BinaryHeap is array-backed.

## Key Quotes
> "Eytzinger's method allows us to represent a complete binary tree as an array by laying out the nodes of the tree in breadth-first order."
> "In a BinaryHeap the n elements are stored in an array a..."

## Connections
- [[ods-06-binary-trees]] — implicit binary-tree representation.
- [[ods-02-array-based-lists]] — same array-doubling resize machinery.
- [[ods-11-sorting-algorithms]] — heap-sort builds on BinaryHeap.
- [[ods-01-introduction]] — defines priority Queue interface.

## Contradictions
None.
