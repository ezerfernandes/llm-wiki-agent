---
title: "ODS Ch.9: Red-Black Trees"
type: source
tags: [book, data-structures, trees, balanced-bst]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 9
pages: "177-202"
---

## Summary
Red-black trees are simulated 2-4 trees: BSTs in which each node is colored red or black, with two invariants — every root-to-leaf path has the same number of black nodes (**black-height**), and no two red nodes are adjacent (**no-red-edge**). Together these force height ≤ 2·log n, give worst-case O(log n) add/remove, and bound the amortized number of rotations per update at constant. RBTs are the workhorse SSet in production library code (Java Collections Framework, parts of the C++ STL, Linux kernel). The chapter develops them via 2-4 trees first (cleaner intuition), then maps to left-leaning red-black trees (each red node leans left; corresponds to a 2-, 3-, or 4-node).

## Key Claims
- **Three properties making red-black trees popular** (over skiplists, treaps, scapegoat trees):
  1. height ≤ 2 log n;
  2. add/remove run in O(log n) **worst-case** time;
  3. amortized rotations per add/remove is O(1) — the time to *find* x dominates the time to update around it.
- **2-4 tree primer**: every internal node has 2, 3, or 4 children; all leaves at the same depth. Height ≤ log n. add(leaf) splits overflowing nodes upward; remove(leaf) merges/redistributes underflowing nodes upward.
- **Red-black mapping**: each 2-node = black; 3-node = black with one red child; 4-node = black with two red children. Black-height equals 2-4-tree height.
- **Cost of niceness**: implementation is the most complex of the SSets in this book — careful case analysis for rotations and recolorings during add and remove is required (the bug surface is large).

## Key Quotes
> "Red-black trees are one of the most widely used data structures. They appear as the primary search structure in many library implementations."
> "Maintaining a bound of 2 log n on the height is not easy. It requires a careful analysis of a number of cases. We must ensure that the implementation does exactly the right thing in each case."

## Connections
- [[ods-06-binary-trees]] — base BinarySearchTree, extended with color invariants.
- [[ods-07-random-binary-search-trees]] / [[ods-08-scapegoat-trees]] — alternative balancing strategies (randomized / amortized).
- [[ods-04-skiplists]] — sibling SSet with simpler implementation but only expected guarantees.
- [[ods-14-external-memory-searching]] — B-trees are 2-4 trees generalized to disk-block degree.
- [[ods-01-introduction]] — defines SSet interface red-black trees implement.

## Contradictions
- Strictly better than skiplists/treaps/scapegoat trees on worst-case bounds — but the implementation is significantly more complex. The book frames this as a deliberate engineering trade-off.
