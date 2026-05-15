---
title: "ODS Ch.14: External Memory Searching"
type: source
tags: [book, data-structures, b-trees, external-memory]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 14
pages: "275-300"
---

## Summary
Final chapter shifts the cost model. The **external memory model** (introduced in §14) charges only for block transfers between RAM and disk; computation inside RAM is free. RAM is ~2,500× faster than SSD and ~160,000× faster than disk; each disk read pulls a full 4096-byte block. The chapter introduces **B-trees** — generalizations of 2-4 trees where every internal node has between B and 2B children — fitting one node per disk block. find/add/remove run in O(log_B n) block transfers. With B = 256 and 4-byte keys, a B-tree node is exactly 4 KiB, matching disk-block size.

## Key Claims
- **External memory model.** External memory is divided into blocks of B words; transferring a block takes constant time. Internal-memory computation is free. The internal-memory size is typically O(B + log_B n) — enough for one block plus the recursion stack.
- **BlockStore** abstraction encapsulates disk: `read_block`, `write_block`, `place_block`, `free_block`. Implementations can use a simple file with a free list.
- **B-tree definition**: rooted tree where every leaf has the same depth; every non-root internal node has between B and 2B children (root has 2..2B). Each node stores up to 2B−1 keys in sorted order.
- **Height bound**. h ≤ log_B ℓ + 1 — base-B logarithm of the number of leaves. For B = 256 and n = 2^32, h ≤ 5.
- **Operations** all walk the height of the tree, doing one block read/write per level. Add(x): descend to leaf, insert; if overflow split node into two, propagate split up — same shape as 2-4 tree, generalized to B-2B branching. Remove(x): same as 2-4 tree merge/redistribute, generalized.
- **Amortized B-tree analysis** (§14.2.4) bounds total split/merge work over a sequence of operations.
- **Why this matters**: when n exceeds RAM, *log_B n is what counts*, and B is large (≈256–1024 for typical disk blocks). Even billion-row indexes fit in 4–5 levels.

## Key Quotes
> "Computations performed within the internal memory are free; they take no time at all."
> "The notion of external memory includes a large number of possible different devices, each of which has its own block size and is accessed with its own collection of system calls."

## Connections
- [[ods-06-binary-trees]] — B-trees generalize binary search trees.
- [[ods-09-red-black-trees]] — 2-4 trees are special case (B = 2); red-black trees simulate them in main memory.
- [[ods-05-hash-tables]] — alternative external-memory dictionary, but worse for range queries.
- [[ods-01-introduction]] — defines the SSet interface B-trees implement.
- [[ods-13-data-structures-for-integers]] — sibling chapter; both target asymptotically-better-than-log-n SSets in their respective cost models.

## Contradictions
None.
