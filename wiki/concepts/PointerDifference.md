---
title: "Pointer Difference (C)"
type: concept
tags: [c-language, pointers, pointer-arithmetic, ptrdiff_t]
sources: [dis-2-9-4-pointer-arithmetic]
last_updated: 2026-05-17
---

# Pointer Difference (C)

**Pointer difference** is the subtractive companion of [[PointerIncrement|pointer increment]] — given two pointers of the same type into the same array, `p1 - p2` returns the **number of elements** (not bytes) between them. The result is of standard type `ptrdiff_t` (signed, defined in `<stddef.h>`).

This is the symmetric inverse of the [[PointerArithmetic|pointer-arithmetic]] rule: if `p2 + n == p1`, then `p1 - p2 == n`. [[dis-2-9-4-pointer-arithmetic|DIS Ch 2.9.4]] does not treat this case explicitly, but the operation is the natural completion of the *element-count* mental model the chapter establishes.

## The rule

Given `T *p1, *p2` both pointing within the same array (or to one-past-the-end):

```
p1 - p2  ==  (byte-address-of(p1) - byte-address-of(p2)) / sizeof(T)
```

The compiler divides the raw byte distance by [[SizeOf|`sizeof(T)`]] so the answer is in **elements**. The type system enforces matched pointee types — `int *` and `char *` cannot be subtracted without a cast (the byte-distance / element-size division would be ambiguous).

```c
int arr[10];
int *p1 = &arr[7];
int *p2 = &arr[2];
ptrdiff_t d = p1 - p2;    /* d == 5  — five int-elements apart */
                          /* NOT 20  (would be 5 * sizeof(int) bytes) */
```

## The valid-domain rule

Pointer subtraction is **only defined** when both pointers point into the same array (treating a non-array object as an array of one element) or to one past its end. Subtracting pointers into **different** arrays is [[UndefinedBehavior|undefined behavior]] in standard [[CLanguage|C]] — even though most platforms produce a sensible numeric answer, the language does not require it.

## The three valid operations recap

[[PointerArithmetic|Pointer arithmetic]] supports exactly three forms of subtraction; `p1 - p2` is the third:

| Operation | Operands | Result |
|---|---|---|
| `ptr - n` | pointer − integer | pointer |
| `ptr + n` | pointer + integer | pointer |
| `p1 - p2` | pointer − pointer (same type, same array) | `ptrdiff_t` (signed element count) |

What's missing: `ptr + ptr` (no meaning), `n - ptr` (no meaning), `p1 + p2` (no meaning). Subtraction is the only operator that takes two pointers as operands.

## Why `ptrdiff_t` and not `int`

`ptrdiff_t` is **signed** (the difference can be negative if `p2` comes after `p1`) and **wide enough** to hold the difference between any two pointers into the largest representable array on the platform — typically a signed equivalent of [[SizeT|`size_t`]] (`long` on 64-bit Unix). Using `int` for pointer differences is the classic 32-bit-truncation bug on arrays larger than 2 GiB.

```c
#include <stddef.h>   /* for ptrdiff_t */
ptrdiff_t d = p1 - p2;
printf("%td\n", d);   /* %td is the format specifier for ptrdiff_t */
```

## The canonical use cases

1. **Substring offset** — `char *match = strstr(haystack, needle); ptrdiff_t off = match - haystack;` reports the position of the match in the original string.
2. **Two-cursor iteration distance** — `while (read < write) { ... read++; }` paired with `ptrdiff_t consumed = read - start;` for progress reports.
3. **Slice length from boundary pointers** — `ptrdiff_t len = end - begin;` is the standard iterator-distance idiom in [[CPlusPlus|C++]]-style [[CLanguage|C]] APIs that pass `(begin, end)` pairs instead of `(base, length)`.

## Doesn't apply to `void *`

Same restriction as [[PointerIncrement|increment]]: [[VoidPointer|`void *`]] subtraction is not standardized — the compiler has no `sizeof(*p)` to divide the byte difference by. Cast to a concrete type first, or to `char *` for byte-distance.

## Connections

- [[dis-2-9-4-pointer-arithmetic]] — defining source (chapter establishes the element-count model that grounds this operation).
- [[PointerArithmetic]] — the umbrella mechanism; this page is the subtractive specialization.
- [[PointerIncrement]] — the additive companion (`p2 + n` and `p1 - p2` are inverses).
- [[Pointer]] / [[PointerType]] — the value class and type-matching rule.
- [[SizeOf]] — the divisor that turns byte-distance into element-count.
- [[SizeT]] — the unsigned size type; `ptrdiff_t` is its signed counterpart.
- [[VoidPointer]] — the type pointer-difference cannot operate on.
- [[CArray]] / [[ArrayDecay]] — the array context where pointer differences are defined.
- [[UndefinedBehavior]] — subtracting pointers into different arrays.
- [[CLanguage]] / [[DiveIntoSystems]].
