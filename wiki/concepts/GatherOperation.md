---
title: "Gather Operation (Thrust)"
type: concept
tags: [thrust, cuda, permutation, parallel-computing, c-plus-plus]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Gather Operation (Thrust)

[[Thrust]]'s parallel **permutation primitive** that reads source elements at positions given by a map and writes them sequentially to a destination: `dst[i] = src[map[i]]`. Header: `<thrust/gather.h>`.

> *"Scatter and gather operations basically act as permuters."* ([[parproc-ch06-thrust-programming]] §6.7)

## Signature

```cpp
thrust::gather(map_begin, map_end, src_begin, dst_begin);
```

For each `i` in `[0, map_end - map_begin)`, reads `src[map[i]]` and writes it to `dst[i]`. The destination length equals the map length; the source must be large enough to accommodate every `map[i]` index.

## Worked example ([[parproc-ch06-thrust-programming]] §6.7)

```cpp
int x[5] = {12, 13, 5, 8, 88};
int m[5] = {3, 2, 4, 1, 0};
thrust::device_vector<int> dx(x, x+5), dm(m, m+5), ddst(5);
thrust::gather(dm.begin(), dm.end(), dx.begin(), ddst.begin());
// ddst now holds: 8, 5, 88, 13, 12
//   ddst[0] = x[m[0]] = x[3] = 8
//   ddst[1] = x[m[1]] = x[2] = 5
//   ddst[2] = x[m[2]] = x[4] = 88
//   ddst[3] = x[m[3]] = x[1] = 13
//   ddst[4] = x[m[4]] = x[0] = 12
```

## Inverse — [[ScatterOperation|`scatter`]]

`gather` writes `dst[i] = src[map[i]]`; `scatter` writes `dst[map[i]] = src[i]`. Under an invertible map they undo each other.

Why does Thrust ship both? ([[parproc-ch06-thrust-programming]] §6.7):

> *"You might think that, having one of the scatter/gather operations available might make the other redundant, but it's handy to have both, because one might be copying between two vectors of different sizes. Say for instance the source vector is larger than the destination one. Then only some elements from the source will be copied, so a scatter operation won't work, as it would require all source elements to be mapped. Thus a gather is useful. The opposite would be true if the destination vector is larger."*

## Counting iterators work as the map

Unlike `scatter` (which takes only `map_begin`), `gather` takes both `map_begin` *and* `map_end`, so a [[CountingIterator|`thrust::counting_iterator`]] map has a well-defined virtual end. The Thrust-distribution matrix-transpose example in [[parproc-ch06-thrust-programming]] §6.9 (Code 2) exploits this:

```cpp
thrust::counting_iterator<size_t> indices(0);
thrust::gather(
    thrust::make_transform_iterator(indices, transpose_index(n, m)),
    thrust::make_transform_iterator(indices, transpose_index(n, m)) + dst.size(),
    src.begin(),
    dst.begin());
```

— a fully fused implementation: counting iterator + transform iterator + gather, no intermediate map array.

## See also

- [[ScatterOperation]] — inverse permutation primitive.
- [[PermutationIterator]] — lazy form of gather.
- [[CountingIterator]] — works as the gather map.
- [[TransformIterator]] — for fused gather-after-transform.
- [[Thrust]] — host library.
- [[parproc-ch06-thrust-programming]] — §6.7, §6.9.
