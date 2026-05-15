---
title: "ODS Ch.3: Linked Lists"
type: source
tags: [book, data-structures, linked-lists, pointers]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 3
pages: "61-82"
---

## Summary
Pointer-based implementations of the List interface. The trade-off vs. array-based: get(i)/set(i) become O(1+min{i,n−i}) instead of O(1), but adding or removing at any *referenced* node is O(1). Three structures: **SLList** (singly-linked, supports Stack and FIFO Queue in O(1)), **DLList** (doubly-linked with a sentinel **dummy** node, supports Deque in O(1)), and **SEList** (Space-Efficient: a doubly-linked list whose nodes are small ArrayDeques of size ≤ b+1, getting nearly array-like space efficiency while keeping pointer-style modifiability).

## Key Claims
- **Linked-list trade-off.** Lose O(1) random access; gain O(1) splice/insert/remove given a node reference. Holds for *any* position in the list.
- **SLList implements Stack + FIFO Queue in O(1)/op** by maintaining `head` and `tail` pointers plus `n`. Push/pop on head; FIFO add/remove use tail/head respectively.
- **DLList Deque trick**: a single **dummy sentinel** node turns every list into a non-empty cycle, eliminating null-checks on head and tail and reducing the special-case count substantially.
- **DLList random access is O(1+min{i, n−i})** by walking from the closer end via dummy.next or dummy.prev.
- **SEList** stores blocks of an ArrayDeque inside each linked-list node; with block size √n it gives O(1) wasted space per node and amortized O(1+min{i,n−i}/b) for random-access ops. Adding/removing only locally rebalances neighbouring blocks via spread/gather operations.
- **Amortized analysis of spread/gather** (§3.3.5) parallels the array-doubling argument from [[ods-02-array-based-lists]].

## Key Quotes
> "The primary disadvantage is that we lose the ability to access any element using get(i) or set(i,x) in constant time."
> "Perhaps the cleanest way to take care of all these special cases in a DLList is to introduce a dummy node."

## Connections
- [[ods-02-array-based-lists]] — primary alternative implementation of the List interface.
- [[ods-01-introduction]] — defines List, Stack, Queue, Deque interfaces.
- [[ods-04-skiplists]] — augments singly-linked lists with extra pointers for O(log n) random access.
- [[ods-05-hash-tables]] — ChainedHashTable uses linked lists as bucket containers.
- [[ods-13-data-structures-for-integers]] — BinaryTrie threads its leaves into a doubly-linked list.

## Contradictions
None.
