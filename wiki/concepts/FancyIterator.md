---
title: "Fancy Iterators (Thrust)"
type: concept
tags: [thrust, cuda, iterator, c-plus-plus, fusion, parallel-computing]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Fancy Iterators (Thrust)

[[Thrust]]'s umbrella term for **special iterators that virtualize work** — they look like iterators over an array but produce values on-the-fly without materializing the array, or co-iterate parallel arrays, or discard their writes. The five fancy iterators ship in `<thrust/iterator/*.h>`.

> *"Since each Thrust call invokes considerable overhead, Thrust offers some special iterators to reduce memory access time and memory space requirements."* ([[parproc-ch06-thrust-programming]] §6.8)

## The five fancy iterators

| Iterator | Header | Role | Detail page |
|---|---|---|---|
| **Counting** | `<thrust/iterator/counting_iterator.h>` | virtual `0, 1, 2, ...` without materializing an array | [[CountingIterator]] |
| **Transform** | `<thrust/iterator/transform_iterator.h>` | applies a functor lazily; implements **fusion** | [[TransformIterator]] |
| **Zip** | `<thrust/iterator/zip_iterator.h>` | co-iterates parallel arrays as tuples | [[ZipIterator]] |
| **Discard** | `<thrust/iterator/discard_iterator.h>` | output `/dev/null` for side-effecting `transform()` calls | [[DiscardIterator]] |
| **Permutation** | `<thrust/iterator/permutation_iterator.h>` | virtual `gather()` via an index map | [[PermutationIterator]] |

## Why "fancy"?

Plain Thrust iterators (`thrust::device_vector<int>::iterator`) work like C pointers — they walk a real array in memory. Fancy iterators **fake the array**:

- The counting iterator's `*it` returns `(it's offset)`, not a memory load.
- The transform iterator's `*it` returns `F(*underlying_it)`, computed when read.
- The zip iterator's `*it` returns `tuple(*it1, *it2, ...)`, gathering from multiple underlyings.
- The discard iterator's `*it = x` is a no-op.
- The permutation iterator's `*it` does `src[map[i]]` on read.

This **lazy / virtual** quality is what saves the memory traffic: the consuming algorithm streams values as it reads, never materializing the intermediate.

## Fusion via transform iterator

The canonical fancy-iterator win ([[parproc-ch06-thrust-programming]] §6.8.1). Instead of:

```cpp
thrust::transform(seq.begin(), seq.end(), dmap.begin(), F);    // stage 1
thrust::scatter(src.begin(), src.end(), dmap.begin(), dst.begin());  // stage 2
```

write:

```cpp
thrust::scatter(src.begin(), src.end(),
    thrust::make_transform_iterator(seq.begin(), F),
    dst.begin());
```

> *"Essentially our use of `make_transform_iterator()` is telling Thrust, 'Don't apply `F()` to `seq` yet. Instead, perform that operation as you go along, and feed each result of `F()` directly into `scatter()`.' That word **direct** is the salient one here; it means we save n memory reads and n memory writes. Moreover, we save the overhead of the kernel call, if our backend is CUDA."*

A footnote clarifies the residual cost: *"We are still writing to temporary storage, but that will probably be in registers (since we don't create the entire map at once), thus fast to access."*

## Constraints

- **Functors used with transform iterators must inherit from `thrust::unary_function<In, Out>`.** Otherwise the iterator's value-type trait deduction fails. *"It won't work without this!"* ([[parproc-ch06-thrust-programming]] §6.8.1).
- **Counting iterators work with `gather()` but not `scatter()`.** `gather()` takes `(map_begin, map_end)` for the map range so the counting iterator's virtual end is well-defined; `scatter()` takes only `map_begin` (it walks for `src_end - src_begin` steps) — *"the compiler encounters problems with determining where the end of the counting sequence is."* ([[parproc-ch06-thrust-programming]] §6.8.1).

## Counter-example — fancy isn't always faster

[[parproc-ch06-thrust-programming]] §6.9's timing comparison shows a hand-rolled `thrust::for_each` + raw-pointer functor beating the full fancy-iterator stack (counting + transform-iterator + gather) by ~2× on the OpenMP back end. The takeaway: **fancy iterators carry their own overhead** (the iterator-trait machinery, the lazy-evaluation wrapping). They win when memory traffic dominates; they lose when the inner work is small enough that the per-element overhead exceeds the saved traffic. See [[Thrust]] for the timing table.

## See also

- [[Thrust]] — host library.
- [[CountingIterator]] / [[TransformIterator]] / [[ZipIterator]] / [[DiscardIterator]] / [[PermutationIterator]] — individual variants.
- [[Functor]] — provides the per-element operation transform iterators consume.
- [[parproc-ch06-thrust-programming]] — §6.8, §6.8.1, §6.9.
