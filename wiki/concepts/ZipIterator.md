---
title: "Zip Iterator (Thrust)"
type: concept
tags: [thrust, cuda, iterator, c-plus-plus, fancy-iterator, tuple]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Zip Iterator (Thrust)

A [[FancyIterator|fancy iterator]] that **co-iterates two or more parallel arrays as a single sequence of tuples**. Header: `<thrust/iterator/zip_iterator.h>`.

> *"Zip iterators essentially 'zip' together two arrays (picture two halves of a zipper lining up parallel to each other as you zip up a coat). This is often useful when one needs to retain information on the position of an element within its array."* ([[parproc-ch06-thrust-programming]] §6.8)

## Mental model

Given two iterators `it_a` over array A and `it_b` over array B of equal length, a zip iterator produces a virtual sequence:

```
(A[0], B[0]), (A[1], B[1]), (A[2], B[2]), ...
```

The consuming algorithm sees tuples; the underlying arrays remain in their original storage.

## Construction

```cpp
auto zit = thrust::make_zip_iterator(
    thrust::make_tuple(it_a, it_b)
);
// *zit  is a thrust::tuple<A_value_type, B_value_type>
// thrust::get<0>(*zit) == A[i]
// thrust::get<1>(*zit) == B[i]
```

The standard use case is when the per-element computation needs **both the value and the index** (or two paired values from different arrays). The zip iterator avoids the alternative of allocating an explicit array of pairs.

## Typical pairing — value + index

Compose with a [[CountingIterator|counting iterator]] to carry the index alongside the value:

```cpp
thrust::counting_iterator<int> idx(0);
auto zit_begin = thrust::make_zip_iterator(thrust::make_tuple(dv.begin(), idx));
auto zit_end   = thrust::make_zip_iterator(thrust::make_tuple(dv.end(),   idx + dv.size()));
// functor receives thrust::tuple<int, int> — value and position
```

Ch6 of [[parproc-ch06-thrust-programming]] doesn't include a worked zip-iterator example — it only names the iterator and its rationale — but the pattern above is the documented Thrust idiom for "I need to know where each element came from."

## See also

- [[FancyIterator]] — fancy-iterator family.
- [[CountingIterator]] — frequently zipped with a value iterator to carry indices.
- [[Thrust]] — host library.
- [[parproc-ch06-thrust-programming]] — §6.8.
