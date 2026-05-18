---
title: "size_t (C)"
type: concept
tags: [c-language, types, stdlib]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# `size_t` (C)

**`size_t`** is the [[CLanguage|C]] standard library's **unsigned integer type for sizes** — the type returned by [[SizeOf|`sizeof`]] and the parameter type of size-taking standard-library functions ([[Malloc|`malloc`]], `memcpy`, `strlen`, `fread`, ...). Defined in `<stddef.h>` (and re-exported from `<stdlib.h>` / `<string.h>` / others).

The standard guarantees:

- **Unsigned** — no negative sizes; legal range is `[0, SIZE_MAX]`.
- **Large enough for any object** — `sizeof(largest_possible_object)` is representable.
- **Platform-width** — 32 bits on a 32-bit platform, 64 bits on a 64-bit platform (typical).

## Why a dedicated type

[[Malloc|`malloc`]] takes a `size_t`, not an `int`, because:

1. **An `int` can be negative** — `malloc(-1)` would silently convert to a huge unsigned value, surprising the caller.
2. **A 32-bit `int` can't represent every legal allocation on a 64-bit platform** — `malloc((size_t)5 * 1024 * 1024 * 1024)` allocates 5 GiB on a 64-bit system; a 32-bit `int` parameter would have truncated to a few hundred MiB.
3. **`sizeof` always returns `size_t`** — matching types means no implicit conversion at the call site.

## Common pitfalls

- **Mixing signed and unsigned** — `for (int i = strlen(s) - 1; i >= 0; i--)` is broken when `s` is empty: `strlen("") - 1` is `(size_t)-1` ≈ `SIZE_MAX`, the loop runs forever (until `i` underflows). Use signed `int` for loop counters when subtracting, or `size_t` with `for (size_t i = strlen(s); i > 0; i--) { ... s[i-1] ... }`.
- **Printf format** — `%d` / `%u` is wrong for `size_t`. Use `%zu` (C99+) for unsigned `size_t`. Old code uses `(unsigned long)` casts.
- **Negative sentinel** — *some* libraries use `(size_t)-1` as a "no result" sentinel (`mbstowcs`, `time`); this works only because `size_t` wraps modulo `SIZE_MAX + 1`.

## In [[dis-2-4-dynamic-memory|DIS Ch 2.4]]

`malloc(sizeof(int) * 20)`: both factors are `size_t`, the product is `size_t`, the call signature matches without conversion. The chapter doesn't dwell on `size_t` explicitly — but every allocation example uses it implicitly through [[SizeOf|`sizeof`]].

## Connections

- [[SizeOf]] — the operator that produces `size_t` values.
- [[Malloc]] / [[Calloc]] / [[Realloc]] — the standard allocators that take `size_t` parameters.
- [[CLanguage]] / [[StandardLibrary]] / [[dis-2-4-dynamic-memory]] / [[DiveIntoSystems]].
