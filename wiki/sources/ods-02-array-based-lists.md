---
title: "ODS Ch.2: Array-Based Lists"
type: source
tags: [book, data-structures, arrays, amortized-analysis]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 2
pages: "31-60"
---

## Summary
Implementations of the List and Queue interfaces backed by a single contiguous array. The fundamental tension: arrays give O(1) get/set but require shifting on add/remove and cannot resize without copy. The chapter resolves this with **amortized analysis** of doubling/halving — even though `resize()` is O(n), its total cost across m operations is O(m), giving O(1) amortized cost per operation. Covers ArrayStack (basic), ArrayQueue (modular indexing), ArrayDeque (front+back O(1)), DualArrayDeque (built from two stacks), and RootishArrayStack (space-efficient √n-block layout).

## Key Claims
- **ArrayStack**: get/set in O(1); add(i,x)/remove(i) in O(n−i) plus amortized O(1) for resize.
- **Resize policy**: grow when full (double the array); shrink when length(a) ≥ 3n (halve). The factor-3 hysteresis is what gives amortized O(1) — without it, alternating add/remove at the boundary forces O(n) resizes per op.
- **Amortization lemma (Lemma 2.1)**: any sequence of m add/remove on an empty ArrayStack incurs O(m) total resize cost. Proof: between successive resizes, n must change by at least n_i / 2.
- **ArrayQueue** uses modular arithmetic on a head pointer (j ← (j + 1) mod length(a)) so the queue can wrap around; resize when full.
- **ArrayDeque** generalizes to support front operations in O(min{i, n−i}) by choosing the cheaper end to shift toward.
- **DualArrayDeque** stacks two ArrayStacks back-to-back; rebalances when one is too small (factor-3 imbalance triggers a reshuffle).
- **RootishArrayStack** uses √n blocks of geometrically increasing sizes 1, 2, 3, ... → wastes only O(√n) space at any time vs O(n) for ArrayStack.

## Key Quotes
> "Although some individual operations are more expensive, the amortized cost, when amortized over all m operations, is only O(1) per operation."
> "If we ignore the cost of the potential call to resize(), then the cost of the add(i,x) operation is proportional to the number of elements we have to shift to make room for x."

## Connections
- [[ods-01-introduction]] — defines the List/Queue/Stack interfaces these implement.
- [[ods-03-linked-lists]] — pointer-based alternative with different cost trade-offs.
- [[ods-05-hash-tables]] — uses the same amortized doubling argument for ChainedHashTable resize.
- [[ods-10-heaps]] — BinaryHeap reuses the array-doubling strategy.
- [[matrices]] — backing arrays as 1-D analogue of matrix storage.

## Contradictions
None.
