---
title: "ODS Ch.4: Skiplists"
type: source
tags: [book, data-structures, skiplists, randomization]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 4
pages: "83-100"
---

## Summary
The skiplist is a beautiful randomized data structure that gives O(log n) expected time for all List and SSet operations through a stack of geometrically-thinning singly-linked lists. Heights are determined by independent coin tosses: an element appears in L_r with probability 2^(−r). Two applications: **SkiplistSSet** (sorted set with expected O(log n) find/add/remove) and **SkiplistList** (random-access list with expected O(log n) get/set/add/remove). Lemma 4.1: the expected length of any search path is at most 2·log n + O(1).

## Key Claims
- **Construction by geometric sampling.** L_0 holds all n elements; element x is included in L_r if r consecutive coin tosses come up heads. Expected height of any node is 1; expected total space is O(n).
- **Search-path bound.** Lemma 4.1: the expected length of the search path from sentinel to any node is at most 2·log n + O(1). Proof postponed to §4.4.
- **SkiplistSSet** implements SSet operations in O(log n) expected time. Search descends right-then-down: at each level, advance while u.next[r].x < x; otherwise drop to level r−1.
- **SkiplistList** uses the same skeleton but stores element *count* in each next-pointer instead of values; supports get(i)/set(i)/add(i,x)/remove(i) in O(log n) expected.
- **Coin tosses simulated with `pick_height()`**: pick a random 32-bit integer z and return the count of trailing 1 bits — equivalent to flipping coins until tails.
- **No rebalancing**, no rotations: simplicity is the headline feature. The randomness in *node heights* (not in input order) is what bounds search-path length.

## Key Quotes
> "The efficiency of skiplists relies on their use of randomization."
> "The expected length of the search path for any node, u, in L_0 is at most 2 log n + O(1) = O(log n)."

## Connections
- [[ods-03-linked-lists]] — base layer of the skiplist is exactly an SLList.
- [[ods-07-random-binary-search-trees]] — sibling randomized SSet via random insertion order.
- [[ods-09-red-black-trees]] — deterministic alternative with worst-case O(log n).
- [[ods-01-introduction]] — interfaces (SSet) defined here; randomization analysis tools introduced here.
- [[probability]] / [[binomial-coefficient]] — coin-toss expectation analysis.

## Contradictions
None.
