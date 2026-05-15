---
title: "ODS Ch.8: Scapegoat Trees"
type: source
tags: [book, data-structures, trees, balanced-bst, amortized-analysis]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 8
pages: "165-176"
---

## Summary
ScapegoatTree is a binary search tree balanced via **partial rebuilding**: when an insert causes a node to exceed the depth bound log_(3/2) q, walk up to find a "scapegoat" — an unbalanced ancestor where one child has more than 2/3 of the descendants — and rebuild that whole subtree into a perfectly balanced one. Maintains a counter q ≥ n that upper-bounds the number of nodes; after enough deletions (n < q/2) the entire tree is rebuilt and q reset. Gives **amortized O(log n) per operation** with worst-case O(log n) for find and amortized O(log n) for add/remove, while keeping deterministic guarantees and simple invariants (no colors, no rotations).

## Key Claims
- **Scapegoat invariant**: q/2 ≤ n ≤ q, and tree height ≤ log_(3/2) q < log_(3/2) 2n.
- **rebuild(u)** runs in O(size(u)) by packing u's subtree into an array and recursively building a balanced tree from the array. Resulting subtree has minimum possible height.
- **Insertion**. add(x) in O(log n) worst case for the BST insert; if the new node exceeds depth log_(3/2) q, walk up looking for a scapegoat w with size(w.child)/size(w) > 2/3 and rebuild w.parent's subtree. Amortized cost of the rebuild is O(log n).
- **Removal**. Standard BST delete; if 2n < q, rebuild entire tree and reset q ← n.
- **Why "scapegoat"**: when balance violates, you blame an ancestor and rebuild *that subtree*, leaving the rest of the tree untouched.
- **Operations and properties**: find(x) is O(log n) worst-case; add(x), remove(x) are O(log n) amortized. Deterministic — no randomization required.

## Key Quotes
> "A ScapegoatTree keeps itself balanced by partial rebuilding operations."
> "When something goes wrong, the first thing people tend to do is find someone to blame (the scapegoat). Once blame is firmly established, we can leave the scapegoat to fix the problem."

## Connections
- [[ods-06-binary-trees]] — base BinarySearchTree extended with scapegoat-rebuild logic.
- [[ods-07-random-binary-search-trees]] — randomized alternative with similar performance.
- [[ods-09-red-black-trees]] — strictly stronger guarantee (worst-case O(log n) for add/remove) at higher implementation complexity.
- [[ods-02-array-based-lists]] — amortized analysis style is identical (charge expensive ops to many cheap ones).

## Contradictions
- The same partial-rebuild idea works in many other contexts; the chapter argues it should be in everyone's toolbox alongside red-black and AVL trees, despite its lower textbook profile.
