---
title: "Pointer Increment (C)"
type: concept
tags: [c-language, pointers, pointer-arithmetic, iteration]
sources: [dis-2-9-4-pointer-arithmetic]
last_updated: 2026-05-17
---

# Pointer Increment (C)

**Pointer increment** is the special case of [[PointerArithmetic|pointer arithmetic]] that advances a [[Pointer|pointer]] by **one element of its pointed-to type**. Per [[dis-2-9-4-pointer-arithmetic|DIS Ch 2.9.4]]: *"when incremented, a pointer points to the next storage location **of the type it points to**."*

`ptr++` is the idiomatic "step to next element" cursor move — the pointer counterpart of `i++` in index-walking loops.

## The four increment forms

| Form | Effect | Result of expression |
|---|---|---|
| `ptr++` | Advance `ptr` by `sizeof(*ptr)`; return **old** value | Pre-increment address |
| `++ptr` | Advance `ptr` by `sizeof(*ptr)`; return **new** value | Post-increment address |
| `ptr--` | Retreat `ptr` by `sizeof(*ptr)`; return **old** value | Pre-decrement address |
| `--ptr` | Retreat `ptr` by `sizeof(*ptr)`; return **new** value | Post-decrement address |

Plus the compound forms: `ptr += N`, `ptr -= N` — multi-element steps. All four scale by [[SizeOf|`sizeof(*ptr)`]]; the literal `1` or `N` is in **element units**, not byte units.

## Byte stride per type (typical 64-bit platform)

```c
char   *cptr;  cptr++;   /* +1 byte  */
short  *sptr;  sptr++;   /* +2 bytes */
int    *iptr;  iptr++;   /* +4 bytes */
long   *lptr;  lptr++;   /* +8 bytes */
double *dptr;  dptr++;   /* +8 bytes */

struct studentT *stptr;
stptr++;                 /* +sizeof(struct studentT) bytes */
```

The compiler — not the programmer — knows the stride. Per [[dis-2-9-4-pointer-arithmetic|Ch 2.9.4]]: *"a programmer can simply write `ptr++` to make a pointer point to the next element value. The compiler generates code to add the appropriate number of bytes."*

## The canonical iteration pattern

```c
int arr[N];
int *p;

for (p = arr; p < arr + N; p++) {
    *p = compute();
}
```

Three moves: (1) initialize cursor to the array base (via [[ArrayDecay|decay]] or `&arr[0]`); (2) test against the one-past-end sentinel `arr + N`; (3) advance with `p++`. Equivalent to `for (int i = 0; i < N; i++) arr[i] = compute();` — same generated code, different syntactic skin.

The chapter's own worked example walks **two** arrays of different element types in parallel, exhibiting the type-scaled stride:

```c
char *cptr = letters;
int  *iptr = numbers;
for (int i = 0; i < N; i++) {
    *cptr = 'a' + i;
    *iptr = i * 3;
    cptr++;          /* +1 byte */
    iptr++;          /* +4 bytes */
}
```

## Increment vs. dereference precedence — the classic footgun

| Expression | Reading |
|---|---|
| `*ptr++` | Dereference, **then** post-increment the pointer (returns old value) — read element, advance cursor |
| `(*ptr)++` | Increment the **pointee** value, leave `ptr` unchanged |
| `*++ptr` | Pre-increment the pointer, **then** dereference — skip the current element |
| `++*ptr` | Increment the pointee value (pre-increment), leave `ptr` unchanged |

Postfix `++` / `--` bind tighter than unary `*`. The `*ptr++` form is the [[CLanguage|C]] idiom for "read current, advance cursor" — common in [[CString|string]] copy loops (`while ((*dst++ = *src++) != '\0');`).

## One-past-the-end is legal — but not dereferenceable

[[CLanguage|C]] permits computing a pointer **one past** the end of an array (`arr + N` for an `N`-element `arr`) — but **dereferencing it** is [[UndefinedBehavior|undefined behavior]]. The one-past-the-end address is for use as a loop sentinel (`p < arr + N`), not as a target of `*`. Going two-or-more past the end is itself undefined.

## Doesn't apply to `void *`

[[VoidPointer|`void *`]] **cannot be incremented** in standard [[CLanguage|C]] — the compiler has no `sizeof(*p)` to multiply the `1` by. Cast to a concrete pointer type first (or to `char *` for byte-stride walking). GCC permits `void *` increment as a non-standard extension treating it as `char *`.

## Connections

- [[dis-2-9-4-pointer-arithmetic]] — defining source.
- [[PointerArithmetic]] — the umbrella mechanism; this page is the increment-specialized form.
- [[PointerDifference]] — the subtractive companion operation.
- [[Pointer]] / [[PointerType]] — the value class and type system.
- [[DereferenceOperator]] — the partner operator; `*p++` combines both.
- [[ArrayDecay]] — produces the pointer that `++` walks.
- [[ArrayIndexing]] — `arr[i]` form that increment-style loops desugar to (and vice versa).
- [[SizeOf]] — the stride the compiler multiplies by.
- [[VoidPointer]] — the type increment cannot operate on.
- [[CString]] — the canonical use case (`while (*p) p++;` for length, `*dst++ = *src++` for copy).
- [[ForLoop]] / [[WhileLoop]] — the loop constructs that drive the cursor.
- [[UndefinedBehavior]] — dereferencing one-past-end or stepping past it.
- [[CLanguage]] / [[DiveIntoSystems]].
