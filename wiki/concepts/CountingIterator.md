---
title: "Counting Iterator (Thrust)"
type: concept
tags: [thrust, cuda, iterator, c-plus-plus, fancy-iterator]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Counting Iterator (Thrust)

A [[FancyIterator|fancy iterator]] that **virtualizes the integer sequence `0, 1, 2, ...` without materializing it**. Header: `<thrust/iterator/counting_iterator.h>`.

> *"Counting iterators play the same role as `thrust::sequence()`, but without actually setting up an array, thus avoiding the memory issues."* ([[parproc-ch06-thrust-programming]] §6.8)

## Construction

```cpp
thrust::counting_iterator<int> seqb(0);          // virtual: 0, 1, 2, ...
thrust::counting_iterator<int> seqe = seqb + n;  // one-past-end
```

`*seqb == 0`, `*(seqb+1) == 1`, etc. — the values are *computed from the iterator's internal offset*, not loaded from memory.

## Use case 1: replacing `thrust::sequence()`

Where Ch6 §6.4 writes:

```cpp
thrust::device_vector<int> seq(n);
thrust::sequence(seq.begin(), seq.end(), 0);
thrust::copy_if(dx.begin(), dx.end(), seq.begin(), out.begin(), ismultk(k));
```

a counting iterator eliminates the `seq` array entirely:

```cpp
thrust::counting_iterator<int> seqb(0);
thrust::copy_if(dx.begin(), dx.end(), seqb, out.begin(), ismultk(k));
```

Saves *n* `int` of device memory and *n* writes during the initial `sequence()` fill. Used this way in [[parproc-ch06-thrust-programming]] §6.10's adjacency-matrix transformation.

## Use case 2: implementing the missing parallel-for

> *"Thrust has no direct parallel loop facilities."* ([[parproc-ch06-thrust-programming]] §6.4)

The idiomatic replacement is `thrust::for_each` over a counting-iterator range with a functor that uses the index:

```cpp
thrust::counting_iterator<int> seqb(0);
thrust::counting_iterator<int> seqe = seqb + n;
thrust::for_each(seqb, seqe, my_functor(args));   // calls my_functor(i) for i = 0..n-1, in parallel
```

This is the implementation strategy of [[parproc-ch06-thrust-programming]] §6.9's faster matrix-transpose Code 1.

## Gotcha — works with `gather()` not `scatter()`

`thrust::gather(map_begin, map_end, src, dst)` takes both endpoints of the map range, so a counting-iterator map has a well-defined end. `thrust::scatter(src_begin, src_end, map, dst)` takes only `map_begin` and walks for `src_end - src_begin` steps — *"the compiler encounters problems with determining where the end of the counting sequence is"* ([[parproc-ch06-thrust-programming]] §6.8.1). The Thrust-distribution matrix-transpose example in §6.9 uses `gather()` for exactly this reason.

## See also

- [[FancyIterator]] — fancy-iterator family.
- [[Thrust]] — host library.
- [[TransformIterator]] — typically composed with a counting iterator for index-based fusion.
- [[parproc-ch06-thrust-programming]] — §6.8, §6.9, §6.10.
