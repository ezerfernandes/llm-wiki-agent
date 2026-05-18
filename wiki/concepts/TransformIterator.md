---
title: "Transform Iterator (Thrust)"
type: concept
tags: [thrust, cuda, iterator, fusion, c-plus-plus, fancy-iterator]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Transform Iterator (Thrust)

A [[FancyIterator|fancy iterator]] that applies a [[Functor|functor]] **lazily** as the consuming algorithm reads. It implements **fusion**: combining `thrust::transform()` with a following algorithm into a single streaming pass that never materializes the intermediate array. Header: `<thrust/iterator/transform_iterator.h>`.

> *"If your code first calls `thrust::transform()` and then makes another Thrust call on the result, you can combine them, which the Thrust people call **fusion**."* ([[parproc-ch06-thrust-programming]] §6.8)

## Construction via `make_transform_iterator`

The type of a transform iterator is *"horrendous to write"*, so Thrust provides a helper:

```cpp
thrust::make_transform_iterator(underlying_iter, F)
```

— produces an iterator whose `*it` returns `F(*underlying_iter)`, computed on read.

## The fusion idiom ([[parproc-ch06-thrust-programming]] §6.8.1)

Without fusion (two passes, intermediate array):

```cpp
thrust::transform(seq.begin(), seq.end(), dmap.begin(), F);     // pass 1
thrust::scatter(src.begin(), src.end(), dmap.begin(), dst.begin());  // pass 2
```

With fusion (one pass, no intermediate):

```cpp
thrust::scatter(src.begin(), src.end(),
    thrust::make_transform_iterator(seq.begin(), F),
    dst.begin());
```

> *"Don't apply `F` to `seq` yet. Instead, perform that operation as you go along, and feed each result of `F` directly into `scatter()`. That word **direct** is the salient one here; it means we save n memory reads and n memory writes. Moreover, we save the overhead of the kernel call, if our backend is CUDA."*

The dropped intermediate `dmap` array no longer exists; the values it would have held are computed in **registers** as `scatter()` reads them and written immediately to `dst`.

## Required functor base class

The functor passed to `make_transform_iterator` **must inherit from `thrust::unary_function<In, Out>`** so the iterator-trait machinery can deduce the iterator's value type:

```cpp
struct transidx : public thrust::unary_function<int, int> {
    const int nr, nc;
    __host__ __device__ transidx(int _nr, int _nc) : nr(_nr), nc(_nc) {}
    __host__ __device__ int operator()(int i) {
        return (i % nc) * nr + (i / nc);
    }
};
```

> *"Note that we also had to be a little bit more elaborate with data typing issues, writing the first line of our struct declaration as `struct transidx : public thrust::unary_function<int, int>`. It won't work without this!"* ([[parproc-ch06-thrust-programming]] §6.8.1)

A 2-argument variant for binary functors is `thrust::binary_function<In1, In2, Out>`.

## When fusion is *not* a win

[[parproc-ch06-thrust-programming]] §6.9's timing comparison shows the full fusion stack (counting iterator → transform iterator → gather) **losing** to a hand-rolled `for_each` + raw-pointer-functor implementation by ~2× on OpenMP. The transform-iterator machinery carries non-trivial per-element overhead; it wins when memory traffic dominates the inner work but loses when the inner work is small. See [[Thrust]] for the timing table.

## See also

- [[FancyIterator]] — fancy-iterator family.
- [[CountingIterator]] — frequently composed as the transform iterator's underlying source.
- [[Functor]] — must inherit `thrust::unary_function` to be transform-iterator-compatible.
- [[Thrust]] — host library, fusion discussion.
- [[parproc-ch06-thrust-programming]] — §6.8, §6.8.1, §6.9.
