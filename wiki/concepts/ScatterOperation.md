---
title: "Scatter Operation (Thrust)"
type: concept
tags: [thrust, cuda, permutation, parallel-computing, c-plus-plus]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Scatter Operation (Thrust)

[[Thrust]]'s parallel **permutation primitive** that writes source elements into a destination array at positions given by a map: `dst[map[i]] = src[i]`. Header: `<thrust/scatter.h>`.

> *"Scatter and gather operations basically act as permuters."* ([[parproc-ch06-thrust-programming]] §6.7)

## Signature

```cpp
thrust::scatter(src_begin, src_end, map_begin, dst_begin);
```

For each `i` in `[0, src_end - src_begin)`, writes `src[i]` to `dst[map[i]]`. The map length must equal the source length; the destination must be large enough to accommodate every `map[i]` index.

## Worked example ([[parproc-ch06-thrust-programming]] §6.7)

```cpp
int x[5] = {12, 13, 5, 8, 88};
int m[5] = {3, 2, 4, 1, 0};
thrust::device_vector<int> dx(x, x+5), dm(m, m+5), ddst(5);
thrust::scatter(dx.begin(), dx.end(), dm.begin(), ddst.begin());
// ddst now holds: 88, 8, 13, 12, 5
//   x[0]=12 went to position 3
//   x[1]=13 went to position 2
//   x[2]=5  went to position 4
//   x[3]=8  went to position 1
//   x[4]=88 went to position 0
```

## Inverse — [[GatherOperation|`gather`]]

`scatter` writes `dst[map[i]] = src[i]`; `gather` writes `dst[i] = src[map[i]]`. They are inverse operations under the same map (modulo invertibility).

Why does Thrust ship both? ([[parproc-ch06-thrust-programming]] §6.7):

> *"You might think that, having one of the scatter/gather operations available might make the other redundant, but it's handy to have both, because one might be copying between two vectors of different sizes. Say for instance the source vector is larger than the destination one. Then only some elements from the source will be copied, so a scatter operation won't work, as it would require all source elements to be mapped. Thus a gather is useful. The opposite would be true if the destination vector is larger."*

## Application — matrix transpose ([[parproc-ch06-thrust-programming]] §6.7.1)

Row-major-stored matrix; element at linear index `i` is row `r = i/nc`, col `c = i%nc`; transposed index is `c*nr + r`. Build the map via a [[Functor|functor]] applied with `thrust::transform`, then call `scatter`. The improved §6.8.1 version inlines the map computation via a [[TransformIterator|transform iterator]] (fusion).

## Gotcha — counting iterators don't work as the map

`thrust::counting_iterator` can serve as the *map* in `gather` (which takes `(map_begin, map_end)`) but **not in `scatter`** (which takes only `map_begin` and walks for `src_end - src_begin` steps):

> *"The compiler encounters problems with determining where the end of the counting sequence is. There is similar code in the examples directory that comes with Thrust, and that one uses `gather()` instead of `scatter()`."* ([[parproc-ch06-thrust-programming]] §6.8.1)

## Disambiguation from Ch1's [[ScatterGather]]

The Ch1 *scatter/gather* pattern is a **manager-worker programming model**: one node parcels work to many workers, then collects results. The Thrust `scatter`/`gather` operations are **permutation primitives on a single device's memory**. Same names, different abstraction levels.

## See also

- [[GatherOperation]] — inverse permutation primitive.
- [[PermutationIterator]] — lazy form of gather.
- [[Thrust]] — host library.
- [[ScatterGather]] — Ch1's manager-worker pattern (disambiguated above).
- [[parproc-ch06-thrust-programming]] — §6.7, §6.7.1, §6.8.1.
