---
title: "Dereference Operator (C `*`)"
type: concept
tags: [c-language, operators, pointers, memory]
sources: [dis-2-2-pointers]
last_updated: 2026-05-17
---

# Dereference Operator (`*`)

The unary **`*`** operator in [[CLanguage|C]] **dereferences** a [[Pointer|pointer]] — it accesses the value at the [[CMemoryAddress|memory address]] the pointer holds. Per [[dis-2-2-pointers|DIS Ch 2.2]]: given `ptr = &x;`, the expression `*ptr` *"is the memory location `ptr` points to."*

```c
int x;
int *ptr;

ptr = &x;   /* initialize ptr to the address of x */
*ptr = 8;   /* WRITE: the memory location ptr points to is assigned 8; x is now 8 */
int y = *ptr + 3;  /* READ: y == 11 */
```

## The dual role of `*`

The same lexeme `*` plays two distinct syntactic roles in [[CLanguage|C]]:

| Context | Role | Example |
|---|---|---|
| **Declaration** | Part of the [[PointerType|pointer type]] | `int *ptr;` declares `ptr` as *pointer to int* |
| **Expression** | The **dereference operator** | `*ptr = 8;` writes through the pointer |

This is the dual-role disambiguation [[dis-2-2-pointers|Ch 2.2]] makes its central learning objective. Inside an expression, `*ptr` *is* the pointee — usable as both an lvalue (left of `=`) and an rvalue.

## The two `=` views with `ptr`

`*` is what flips between *modifying the pointer* and *modifying the pointee*:

```c
int x = 5, y = 10;
int *ptr;

ptr = &x;     /* ptr now points to x; x and y unchanged */
*ptr = 99;    /* writes through ptr; x is now 99; ptr unchanged */
ptr = &y;     /* ptr now points to y; x and y unchanged */
*ptr = 42;    /* writes through ptr; y is now 42; ptr unchanged */
```

Same `=` syntax, same variable name `ptr` on the left, but the unary `*` decides whether the *pointer* (rewired) or the *pointee* (written through) is modified.

## Safety: never dereference invalid pointers

[[dis-2-2-pointers|Ch 2.2]] flags three failure modes — all **undefined behavior**, typically a [[SegmentationFault|segmentation fault]]:

```c
int *ptr;
*ptr = 6;    /* CRASH: ptr uninitialized — holds garbage address */

ptr = NULL;
*ptr = 6;    /* CRASH: cannot dereference NULL */

ptr = 20;
*ptr = 6;    /* CRASH: 20 is almost certainly not a valid address */
```

The defensive idiom — using [[ShortCircuitEvaluation|short-circuit]] from [[dis-1-3-conditionals-loops|Ch 1.3]]:

```c
if (ptr != NULL) {
    *ptr = 6;
}
```

## Inverse of `&`

`*` and [[AddressOfOperator|`&`]] are conceptual inverses on lvalues:

```c
int x = 5;
int y = *(&x);   /* y == 5 — &x produces the address, *( ) reads it back */
```

For any addressable variable `x`, `*(&x)` is `x`. The chain doesn't extend in the other direction (`&(*p)` is `p` only when `p` is itself addressable / non-null, and there are subtler corner cases) — but for normal code the *"address-of then dereference cancels"* identity is the mental model.

## Static-type discipline

The pointee type a dereference yields is determined by the [[PointerType|pointer's static type]]:

- `int *p; *p` → has type `int`
- `char *p; *p` → has type `char`
- `struct studentT *p; *p` → has type `struct studentT`

The [[ArrowOperator|`->`]] operator is shorthand for the struct-pointer case: `p->field` ≡ `(*p).field`.

## Not to be confused with

- **Multiplication** — `a * b` (binary infix). Position disambiguates: unary prefix = dereference, binary infix = multiplication.
- **The declaration `*`** — same lexeme, declaration position; spells the [[PointerType|pointer type]] (see [[PointerDeclaration]]).

## Connections

- [[CLanguage]] — the language.
- [[Pointer]] — what `*` dereferences.
- [[AddressOfOperator]] — the inverse operator (`&` produces an address; `*` reads from it).
- [[PointerDeclaration]] — the *declaration* role of `*`.
- [[PointerType]] — determines the static type the dereference yields.
- [[NullPointer]] — must never be dereferenced.
- [[SegmentationFault]] — the typical runtime consequence of misuse.
- [[ArrowOperator]] — `p->field` ≡ `(*p).field`; the dereference-then-dot shorthand.
- [[LValue]] — `*ptr` is an lvalue, which is why `*ptr = 8;` works.
- [[ShortCircuitEvaluation]] — what makes `if (p != NULL && *p == 0)` safe.
- [[dis-2-2-pointers]] — defining source.
