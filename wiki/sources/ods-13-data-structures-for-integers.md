---
title: "ODS Ch.13: Data Structures for Integers"
type: source
tags: [book, data-structures, tries, integers]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 13
pages: "257-274"
---

## Summary
SSet implementations specialized to w-bit integer keys. Three structures of strictly increasing sophistication. **BinaryTrie** stores n integers as root-to-leaf paths in a binary tree of depth w; leaves are doubly-linked into a sorted list, with auxiliary `jump` pointers to handle missing children — gives O(w) add/remove/find. **XFastTrie** speeds up find from O(w) to O(log w) by hashing the trie's nodes by prefix and binary-searching levels — but at the cost of O(n·w) space. **YFastTrie** restores O(n) space and O(log w) for add/remove by storing only one-in-w "representatives" in an XFastTrie and partitioning the rest into Treap-style buckets.

## Key Claims
- **BinaryTrie**: each integer x ∈ {0,...,2^w−1} is a root-to-leaf path; leaves are linked into a sorted doubly-linked list. find/add/remove all O(w). Space O(n·w) in the worst case.
- **The jump pointer trick**: each interior node u with a missing child stores a pointer u.jump to the smallest leaf in its (would-be) subtree larger than x (or symmetrically the largest smaller). This lets find(x) cut off at the first missing branch and jump straight to the linked-list neighbour.
- **XFastTrie**: store the set of trie *prefixes at each level* in a hash table. find(x) does binary search over the w levels (log w hash lookups), each finding the deepest existing prefix of x; jump pointer then completes the search.
- **YFastTrie**: SSet built by storing every w-th element (a "representative") in an XFastTrie and bucketing the remaining elements between representatives in a treap or skiplist of size O(w). find(x) → O(log w); add/remove → O(log w) expected, since updates rebalance buckets and only sometimes promote/demote a representative.
- **All three SSets beat the O(log n) bound** of comparison-based balanced BSTs whenever w = o(log² n).

## Key Quotes
> "The BinaryTrie performs all three SSet operations in O(w) time. This is not very impressive, since any subset of {0,...,2^w − 1} has size n ≤ 2^w, so that log n ≤ w."
> "The XFastTrie speeds up the search in a BinaryTrie by using hashing. With this speedup, the find(x) operation runs in O(log w) time."

## Connections
- [[ods-06-binary-trees]] — BinaryTrie is a binary tree over key bits.
- [[ods-03-linked-lists]] — leaves of the trie form a doubly-linked sorted list.
- [[ods-05-hash-tables]] — XFastTrie hashes prefixes per level.
- [[ods-07-random-binary-search-trees]] — YFastTrie's bucket structure can be a treap.
- [[ods-11-sorting-algorithms]] — radix-sort exploits the same per-bit indexing as the trie.
- [[modulo-operator]] — bit-extraction via shift and mod.

## Contradictions
- The XFastTrie's O(n·w) space is impractical for large w; YFastTrie restores O(n) but adds implementation complexity. The chapter frames this trie family as primarily a theoretical contribution — a constructive proof that integer SSet operations can beat the comparison-tree lower bound.
