---
title: "Pass-by-Reference"
type: concept
tags: [c-language, functions, arrays, calling-convention]
sources: [dis-1-5-arrays-strings, dis-2-5-arrays]
last_updated: 2026-05-17
---

# Pass-by-Reference

**Pass-by-reference** is the parameter-passing convention in which a [[Function|function]] receives *the storage location* of its caller's argument — not a copy of the value — so that **mutations performed inside the function are visible to the caller**.

In [[CLanguage|C]] strictly speaking *every* parameter is passed by value (see [[PassByValue]]) — but for [[CArray|arrays]] the *value* that gets copied at the call boundary is the array's **base address**, which gives pass-by-reference semantics for array elements without [[CLanguage|C]] having a `&`-style reference type the way C++ does.

## How [[dis-1-5-arrays-strings|Ch 1.5]] sets up the contradiction

Per [[dis-1-4-functions|Ch 1.4]] of [[DiveIntoSystems]], the universal rule was: *"any change to a parameter's value in the function is not visible to the caller."* Ch 1.5 immediately shows a counterexample:

```c
void test(int a[], int size) {
    if (size > 3) {
        a[3] = 8;   // VISIBLE to caller — array elements persist
    }
    size = 2;       // NOT VISIBLE — int parameter follows pass-by-value
}
```

The chapter's framing: *arrays pass by reference*. The mechanistic explanation (the array name **decays** to a pointer to its first element, and that *pointer* is what is passed by value) is deferred to Ch 1.6's pointer chapter.

## What's actually being copied

| Parameter type | What's copied at the call | Effect of mutation |
|---|---|---|
| `int size` | The integer value | Local-only |
| `int a[]` (= `int *a`) | The **base address** of the array | Mutation of `a[i]` visible to caller |
| `int *p` (Ch 1.6) | The pointer value | Mutation of `*p` visible to caller |

So the [[PassByValue|pass-by-value]] rule is *not actually violated* — it is just that the *value* being copied for an array parameter is a *pointer*, and mutations through that pointer reach the caller's storage.

## Why this matters

Pass-by-reference is the only way to get an *output parameter* in [[CLanguage|C]] — a function that needs to "return" more than one value, or to modify a caller's variable, must take an [[CArray|array]] or (Ch 1.6) a pointer parameter. It is also why [[Scanf|`scanf`]] takes `&x` rather than `x` — the `&` makes the value-being-copied an *address* rather than the integer itself.

## Cross-walk

- C++ has explicit reference parameters: `void f(int& x)` — pure pass-by-reference for scalars too.
- Java passes object references by value (object-reference semantics): mutating the *object* is visible, reassigning the *parameter* is not.
- [[Python]] passes object references by value: mutating a mutable object (`list`, `dict`) is visible; rebinding the parameter is not.
- [[CLanguage|C]] does not have a `reference` type — pass-by-reference is achieved *manually* by passing arrays or pointers.

## The decay-grounded restatement (Ch 2.5)

[[dis-2-5-arrays|Ch 2.5]] re-supplies the mechanism behind the [[dis-1-5-arrays-strings|Ch 1.5]] exception with explicit array-decay language: *"when passing an array to a function, C copies the value of the base address to the parameter. That is, both the parameter and the argument refer to the same memory locations."* The *value* being copied is the **decayed pointer** — `int arr[N]` becomes `int *` at the call boundary (see [[ArrayDecay]]). Pass-by-reference for arrays is thus pass-by-value of the decayed pointer; the mutation visibility follows from the two sides now naming the same memory through that pointer. Ch 2.5 also extends this story to [[DynamicallyAllocatedArray|dynamically-allocated arrays]] — they accept the same `int *` / `int arr[]` parameter signature as static arrays because the dynamic array's name *already is* a pointer to its first element.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.3 *Arrays and Functions* declares the array-pass-by-reference rule and contrasts it with the scalar [[PassByValue|pass-by-value]] rule from [[dis-1-4-functions|Ch 1.4]].
- [[dis-2-5-arrays]] — Ch 2.5 grounds the rule mechanistically via [[ArrayDecay|array decay]] and the *"C copies the value of the base address to the parameter"* quote; extends it to [[DynamicallyAllocatedArray|dynamically-allocated arrays]] and to [[MultidimensionalArray|multidimensional arrays]] (where the *decayed type* — `int (*)[M]` vs. `int **` — matters for parameter signatures).
