---
title: "Made With ML — NumPy"
type: source
tags: [foundations, made-with-ml, numpy, arrays, broadcasting, course]
date: 2026-05-15
source_file: raw/madewithml/foundations-numpy.md
---

## Summary
Hands-on lesson on [[NumPy]] arrays as the foundation for all subsequent numerical computing in the course. Covers array creation (`np.array`, `zeros`, `ones`, `eye`, `random.random`), inspecting `dtype` / `shape` / `size` / `ndim`, indexing (positional, slice, integer-array, boolean), arithmetic (elementwise +, -, *, /), the dot product (`np.dot` / `@`), axis-aware reductions (`sum(axis=0/1)`, `min`, `max`, `mean`, `median`, `var`, `std`), broadcasting rules, transpose, reshape (and the `-1` placeholder for "infer this dim"), joining (`concatenate`, `stack`), and expanding/reducing dimensions (`expand_dims`, `squeeze`). Emphasizes that NumPy is C-backed and operates on contiguous typed buffers, which is why it dramatically outperforms Python loops on numeric workloads.

## Key Claims
- Arrays are typed and contiguous; this is why vectorized NumPy beats Python list arithmetic by 1-2 orders of magnitude on the same data.
- Axis semantics are fixed: `axis=0` aggregates along rows (collapses the row dim) producing one value per column; `axis=1` aggregates along columns producing one value per row.
- Broadcasting lets shapes (3,) and (2,3) interact without explicit replication — the smaller array is conceptually stretched along the missing leading dim. This is a memory/compute optimization, not a syntactic convenience.
- The `-1` argument to `reshape` is a placeholder meaning "infer this dimension from the total element count and the other dims" — eliminates a lot of arithmetic in dynamic-batch ML code.
- Dot product `np.dot(a, b)` (or `a @ b`) is the building block of linear layers in neural networks; the rest of the course leans on this operation continuously.
- `expand_dims` / `squeeze` are the canonical way to align tensor ranks for broadcasting without duplicating data.

## Key Quotes
> "NumPy is the fundamental package for scientific computing with Python."

> "Broadcasting allows us to apply arithmetic operations to arrays of different shapes."

## Connections
- [[GokuMohandas]] — author.
- [[MadeWithML]] — parent course.
- [[NumPy]] — the library itself.
- [[NDArray]] — the central data structure.
- [[Broadcasting]] — implicit-replication rule for shape-different operations.
- [[DotProduct]] — `np.dot` / `@` operator; building block of linear layers.
- [[Python]] — prerequisite lesson.
- [[pandas]] — successor lesson; pandas Series/DataFrame are built on NumPy arrays.
- [[PyTorch]] — successor lesson; `torch.Tensor` mirrors the NumPy API closely with autograd added.
- [[TravisOliphant]] / [[StefanVanDerWalt]] — NumPy maintainers (entity pages may exist later).

## Contradictions
None — fundamentals lesson.
