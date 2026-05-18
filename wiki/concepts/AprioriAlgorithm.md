---
title: "Apriori Algorithm"
type: concept
tags: [data-mining, algorithms, parallel-computing]
sources: [parproc-ch14-statistics-data-mining]
last_updated: 2026-05-17
---

# Apriori Algorithm

A breadth-first search algorithm for finding all frequent itemsets in a transaction database. Developed in the context of [[ItemsetAnalysis]] and [[MarketBasketProblem|market basket analysis]].

## Algorithm

Starting from F₁ (the set of frequent 1-itemsets whose support exceeds the threshold), the algorithm builds up to larger itemsets level by level:

```
set F_1 to the set of 1-item itemsets whose support exceeds the threshold
for i = 2 to b:
    F_i = ∅
    for each I in F_{i-1}:
        for each K in F_1:
            Q = I ∪ K
            if support(Q) exceeds support threshold:
                add Q to F_i
    if F_i is empty: break
return ∪_i F_i
```

The **support** of an association rule I → J is the proportion of records containing both I and J. The **confidence** is the proportion containing J among those containing I — i.e., P(J|I).

## Pruning Principle

The key monotonicity property: if an itemset is not frequent (support < threshold), adding further items makes it even less frequent. Infrequent itemsets are pruned and their branches terminated. This prunes the exponentially large candidate space.

## Parallelization

Both inner `for` loops are embarrassingly parallel in the basic form — candidate generation and support counting are independent per candidate. In shared-memory settings, critical sections protect writes to F_i. In message-passing settings, a manager node stores F_i.

As refinements accumulate (e.g., hash trees for accounting), the algorithm becomes less embarrassingly parallel. Storage for F_i and associated data structures may exceed one node's memory, and coordination costs grow. Matloff notes the considerable research literature on this topic. (§14.1.4, [[parproc-ch14-statistics-data-mining]])

## Connections

- [[ItemsetAnalysis]] — the general problem this algorithm solves.
- [[MarketBasketProblem]] — canonical motivating application.
- [[parproc-ch14-statistics-data-mining]] — primary source (§14.1.3–14.1.4).
- [[OpenMP]] — shared-memory parallelization of inner loops.
- [[MPI]] — message-passing parallelization with manager node for F_i.
