---
title: "Discard Iterator (Thrust)"
type: concept
tags: [thrust, cuda, iterator, c-plus-plus, fancy-iterator, side-effect]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Discard Iterator (Thrust)

A [[FancyIterator|fancy iterator]] that **silently discards all writes** — the iterator equivalent of `/dev/null`. Header: `<thrust/iterator/discard_iterator.h>`.

> *"Sometimes we call `transform()` but don't need its output. Discard iterators then act in a manner similar to `/dev/null`."* ([[parproc-ch06-thrust-programming]] §6.8)

## Use case — side-effecting transform

Pass `thrust::make_discard_iterator()` as the output parameter when the work is in the [[Functor|functor]]'s side effects and the algorithm's nominal output is uninteresting. Saves both the **memory space** of the discarded output array and the **memory bandwidth** of writing to it.

[[parproc-ch06-thrust-programming]] §6.10 (adjacency-matrix transformation) uses this pattern:

```cpp
thrust::transform(ones.begin(), newend, seq2b,
    thrust::make_discard_iterator(),
    makerow(newmat.begin(), nc));
```

The `makerow` functor writes 2-column edge-list rows into `newmat` as a side effect of being invoked on each element. `transform()`'s formal output is never consumed:

> *"The construction of the output matrix, `newmat`, is actually done as a side effect of calling `makerow()`. For this reason, we've set our third parameter to `thrust::make_discard_iterator()`. Since we never use the output from `transform()` itself, and it thus would be wasteful — of both memory space and memory bandwidth — to store that output in a real array."*

## Alternative — use `thrust::for_each` instead

When the work is purely side-effecting, `thrust::for_each(begin, end, F)` is the more idiomatic choice — there is no output to discard in the first place. [[parproc-ch06-thrust-programming]] §6.9 makes this explicit:

> *"The `for_each()` function does what the name implies: it calls a function/functor for each element in a sequence, doing so in a parallel manner. Note that this also obviates our earlier need to use a discard iterator."*

The discard iterator remains useful when you're *already* using `transform()` for a multi-input algorithm shape (e.g. 2-input transform over two ranges) that `for_each` doesn't directly support.

## See also

- [[FancyIterator]] — fancy-iterator family.
- [[Thrust]] — host library; `for_each` discussion.
- [[parproc-ch06-thrust-programming]] — §6.8 (definition), §6.9 (deprecation in favor of `for_each`), §6.10 (worked example).
