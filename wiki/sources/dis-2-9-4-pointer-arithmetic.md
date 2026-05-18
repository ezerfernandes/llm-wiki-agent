---
title: "Dive into Systems — Ch 2.9.4 Pointer Arithmetic"
type: source
tags: [c-language, pointer-arithmetic, arrays, array-decay, void-pointer, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/advanced_pointer_arithmetic.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **fourth subsection of [[dis-2-9-advanced|Ch 2.9]]** of *[[DiveIntoSystems]]* — finally delivers the [[PointerArithmetic|pointer-arithmetic]] mechanism that [[dis-2-2-pointers|Ch 2.2]] named-and-deferred, [[dis-2-5-arrays|Ch 2.5]] silently relied on for its `arr[i] == *(arr + i)` identity, and [[dis-2-4-dynamic-memory|Ch 2.4]] presupposed when establishing the static-vs-dynamic indexing parity. Codifies (a) the **[[PointerIncrement|type-scaled-increment]] rule** — `ptr++` advances by `sizeof(*ptr)` bytes, not one byte: incrementing a `char *` advances by 1, an `int *` by 4, a `double *` by 8 — *"the compiler generates code to add the appropriate number of bytes"*; (b) the **general N-scaling identity** `ptr + N` points `N` elements (not bytes) beyond the current element, which is exactly what makes [[ArrayIndexing|`arr[i]` ≡ `*(arr + i)`]] type-correct across pointer types; (c) the **dynamic-2D divergence** — single-`malloc` of `N*M` ints permits continuous pointer-arithmetic traversal of all elements (rows are contiguous), [[ArrayOfArrays|array-of-arrays]] via N+1 mallocs requires resetting the pointer at each row (rows live in separate heap chunks); (d) the **anti-recommendation** — *"in most cases, we recommend against using pointer arithmetic to access array elements: it's easy to make errors and more difficult to debug when you do."* Closes the [[dis-2-2-pointers|Ch 2.2]] deferral list (`void *` resolved in [[dis-2-9-3-voidstar|Ch 2.9.3]], pointer arithmetic resolved here).

## Key Claims

- **Pointer arithmetic is type-scaled, not byte-scaled.** *"When incremented, a pointer points to the next storage location **of the type it points to**."* `cptr++` on a `char *` advances by 1; `iptr++` on an `int *` advances by 4 (on a typical platform); `dptr++` on a `double *` advances by 8. The pointer **type** — not the literal `+1` — decides the byte stride.
- **The compiler emits the byte-count code.** *"A programmer can simply write `ptr++` to make a pointer point to the next element value. The compiler generates code to add the appropriate number of bytes."* `ptr + N` is similarly auto-scaled: *"`ptr + N` makes the pointer point `N` storage locations beyond its current value (or makes it point to `N` elements beyond the current element)."* The element-count abstraction is the load-bearing convenience — programmers think in elements, the compiler thinks in bytes.
- **This is the mechanism behind [[ArrayIndexing|`arr[i]` == `*(arr + i)`]].** [[dis-2-5-arrays|Ch 2.5]]'s identity is now grounded — `arr + i` computes `base + i * sizeof(*arr)` automatically, so `*(arr + i)` reaches element `i` for any pointed-to type. The indexing operator is syntactic sugar over pointer arithmetic; both forms compile to the same address calculation.
- **Iteration pattern: walk by incrementing.** The chapter's worked example sets a pointer to `&arr[0]` (or the array name itself via [[ArrayDecay|decay]]) then `*ptr = value; ptr++;` per iteration. Functionally equivalent to `arr[i] = value;` — same generated address arithmetic, different syntactic skin.
- **Single-`malloc` 2D arrays support continuous traversal.** When all `N*M` ints live in one contiguous chunk, *"the pointer only needs to be initialized to point to the base address, and then pointer arithmetic will correctly access any element"* — one `ptr++` walks across row boundaries without resetting.
- **Array-of-arrays 2D forms require per-row reset.** When *"a program uses multiple `malloc` calls to dynamically allocate individual rows … then the pointer must be reset to point to the address of the starting element of every row"* — the [[ArrayOfArrays|N+1-allocation]] form lays rows in non-contiguous heap chunks, so cross-row arithmetic walks into unrelated memory or [[SegmentationFault|segfaults]].
- **The chapter's standing recommendation: don't.** *"In most cases, we recommend against using pointer arithmetic to access array elements: it's easy to make errors and more difficult to debug when you do."* Prefer [[ArrayIndexing|`arr[i]`]] — same generated code, clearer intent, easier to keep in bounds.

## Key Quotes

> "When incremented, a pointer points to the next storage location *of the type it points to*. For example, incrementing an integer pointer (`int *`) makes it point to the next `int` storage address (the address four bytes beyond its current value)." — the **type-scaled-increment** rule.

> "A programmer can simply write `ptr++` to make a pointer point to the next element value. The compiler generates code to add the appropriate number of bytes." — the **element-count abstraction**: programmer thinks elements, compiler emits bytes.

> "`ptr + N` makes the pointer point `N` storage locations beyond its current value (or makes it point to `N` elements beyond the current element)." — generalizes increment to arbitrary offsets while preserving the elements-not-bytes semantics.

> "If the 2D array is allocated as a single `malloc` of total rows times columns space … then all the rows are in contiguous memory … the pointer only needs to be initialized to point to the base address, and then pointer arithmetic will correctly access any element." — the **single-malloc continuous traversal** rule.

> "If … a program uses multiple `malloc` calls to dynamically allocate individual rows … then the pointer must be reset to point to the address of the starting element of every row." — the **array-of-arrays per-row reset** rule.

> "In most cases, we recommend against using pointer arithmetic to access array elements: it's easy to make errors and more difficult to debug when you do." — the chapter's closing **anti-recommendation**.

## Worked Example (from the chapter)

```c
char letters[N];
int  numbers[N];
char *cptr;
int  *iptr;
int   i;

cptr = &(letters[0]);   /* or simply: cptr = letters; via array decay */
iptr = numbers;         /* array decay: numbers -> &numbers[0] */

for (i = 0; i < N; i++) {
    *cptr = 'a' + i;    /* write through char pointer */
    *iptr = i * 3;      /* write through int pointer  */
    cptr++;             /* advance 1 byte  (sizeof(char)) */
    iptr++;             /* advance 4 bytes (sizeof(int))  */
}
```

Equivalent to `letters[i] = 'a' + i; numbers[i] = i * 3;` — same generated address arithmetic, different syntactic skin. The chapter uses the example to make the type-scaled stride visible.

## Connections

- [[DiveIntoSystems]] — the source textbook; this section is its Ch 2.9.4.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — the authors.
- [[dis-2-9-advanced]] — the hub page that forwards to this subsection.
- [[dis-2-9-3-voidstar]] — the **prior** subsection ([[VoidPointer|`void *`]]).
- [[dis-2-2-pointers]] — names-and-defers pointer arithmetic; Ch 2.9.4 resolves the deferral.
- [[dis-2-5-arrays]] — silently relies on pointer arithmetic for the `arr[i] == *(arr + i)` identity and the [[ArrayOfArrays|array-of-arrays]] / single-`malloc` 2D tradeoff; Ch 2.9.4 supplies the underlying mechanism.
- [[dis-2-4-dynamic-memory]] — establishes the static-vs-dynamic indexing parity that pointer arithmetic makes work for both forms.
- [[PointerArithmetic]] — the **new** concept page introduced here (the umbrella mechanism).
- [[PointerIncrement]] — the **new** concept page for `ptr++` / `ptr + N` / `ptr += N` (the type-scaled-stride forms).
- [[PointerDifference]] — the **new** concept page for `p1 - p2` (element-count distance — *not* covered by Ch 2.9.4 itself but the symmetric companion of increment; included for completeness).
- [[Pointer]] / [[PointerType]] — the value class and type system the arithmetic operates over.
- [[ArrayDecay]] — the mechanism that makes `arr` usable as the pointer the arithmetic starts from.
- [[ArrayIndexing]] — `arr[i]` is *defined as* `*(arr + i)`; this section grounds that definition.
- [[VoidPointer]] — the type-erased pointer that **cannot** be the operand of pointer arithmetic (no `sizeof(*p)` available); arithmetic requires a concrete pointee type.
- [[MultidimensionalArray]] / [[ArrayOfArrays]] / [[RowMajorOrder]] — the 2D cases where pointer-arithmetic continuity vs per-row reset differs.
- [[DereferenceOperator]] — the partner operator; `*(p + i)` is the underlying form of `p[i]`.
- [[SizeOf]] — what the compiler multiplies `N` by to convert element offsets into byte offsets.
- [[BufferOverflow]] — the failure mode of off-by-one pointer arithmetic; the chapter's anti-recommendation rationale.

## Contradictions

- None. Ch 2.9.4 is purely additive — it *explains* the mechanism [[dis-2-5-arrays|Ch 2.5]]'s [[ArrayIndexing|`arr[i] == *(arr + i)`]] identity exposed and resolves the pointer-arithmetic deferral [[dis-2-2-pointers|Ch 2.2]] flagged. The *recommendation against* using pointer arithmetic at the call site is a **style preference**, not a contradiction of the mechanism's correctness.
