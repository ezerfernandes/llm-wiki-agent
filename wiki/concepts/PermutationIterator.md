---
title: "Permutation Iterator (Thrust)"
type: concept
tags: [thrust, cuda, iterator, c-plus-plus, fancy-iterator, permutation]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Permutation Iterator (Thrust)

A [[FancyIterator|fancy iterator]] that **virtualizes a `gather` operation**: given a source iterator and a map iterator, `*pit` returns `src[map[i]]` on read, without materializing the gathered array. Header: `<thrust/iterator/permutation_iterator.h>`.

## Construction

```cpp
auto pit = thrust::make_permutation_iterator(src.begin(), map.begin());
// *pit          == src[ map[0] ]
// *(pit + i)    == src[ map[i] ]
```

The permutation iterator is the lazy form of [[GatherOperation|`thrust::gather`]]:

```cpp
// Eager — materializes a gathered copy:
thrust::gather(map.begin(), map.end(), src.begin(), dst.begin());

// Lazy — streams gathered values into the consuming algorithm:
thrust::transform(
    thrust::make_permutation_iterator(src.begin(), map.begin()),
    thrust::make_permutation_iterator(src.begin(), map.end()),
    dst.begin(), F);
```

## Position in Ch6

[[parproc-ch06-thrust-programming]] §6.8 lists permutation iterators among the four named "fancy" iterators only in passing — the chapter's worked examples use [[CountingIterator|counting]] / [[TransformIterator|transform]] / [[DiscardIterator|discard]] iterators in depth and lean on the explicit `thrust::gather` / `thrust::scatter` calls (§6.7) for permutation work. The permutation iterator is the lazy companion to those operations when you want to **read** a permuted view without producing the gathered array.

## See also

- [[FancyIterator]] — fancy-iterator family.
- [[GatherOperation]] — the eager counterpart.
- [[ScatterOperation]] — the inverse permutation primitive.
- [[Thrust]] — host library.
- [[parproc-ch06-thrust-programming]] — §6.8.
