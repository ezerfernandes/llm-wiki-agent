---
title: "Array of Structs (C)"
type: concept
tags: [c-language, struct, array]
sources: [dis-1-6-structs, dis-2-7-structs]
last_updated: 2026-05-17
---

# Array of Structs (C)

An **array of structs** in [[CLanguage|C]] is a contiguous run of `N` instances of a [[CStruct|struct]] type — the natural composition of the two aggregate types introduced in [[dis-1-5-arrays-strings|Ch 1.5]] and [[dis-1-6-structs|Ch 1.6]]:

```c
struct studentT class[30];        // 30 contiguous studentT records

strcpy(class[0].name, "Kwame Salter");
class[0].age = 20;
class[0].gpa = 3.5;
class[0].grad_yr = 2020;
```

Each element is a full struct; combined access uses [[ArrayIndexing|array indexing]] followed by the [[MemberAccessOperator|dot operator]] — `class[i].field`. The expression `class[i]` denotes a struct *variable* (an [[LValue|lvalue]]), so `class[1] = class[0];` is legal whole-struct assignment.

## Memory layout

The array occupies `30 * sizeof(struct studentT)` consecutive bytes — for the chapter's 76-byte student struct, at least 2280 bytes total (possibly more with per-record padding). This is the natural extension of [[dis-1-5-arrays-strings|Ch 1.5]]'s *"C dictates the array layout in program memory"* rule to aggregate element types.

## Calling-convention nuance

Because arrays-of-X follow the [[PassByReference|pass-by-reference]] rule from [[dis-1-5-arrays-strings|Ch 1.5]] (the array name decays to a pointer to the first element), passing a `struct studentT class[]` argument to a function lets the callee *mutate* records in the caller's array — even though passing an individual `struct studentT` element by value would not. The element-vs-array distinction inherits the same pass-by-value-vs-reference asymmetry as scalars-vs-arrays.

## Status in [[dis-1-6-structs|Ch 1.6]]

**Deferred.** Ch 1.6 references arrays of structs as a natural extension but defers worked examples and the calling-convention discussion to Section 2 (*A Deeper Dive Into C*).

## Full treatment in [[dis-2-7-structs|Ch 2.7]] §2.7.4

Ch 2.7 delivers the **three-form taxonomy** of arrays of structs:

| Form | Declaration | Element type | Access | Storage |
|---|---|---|---|---|
| Static | `struct studentT class1[40];` | `struct studentT` | `class1[i].field` | [[StackSection|stack]] (or globals) |
| Dynamic single block | `struct studentT *class2 = malloc(sizeof(struct studentT) * 15);` | `struct studentT` | `class2[i].field` | [[HeapSection|heap]] (one big allocation) |
| Array of pointers | `struct studentT *class3[40]; class3[5] = malloc(sizeof(struct studentT));` | `struct studentT *` | `class3[i]->field` | array on stack, structs on heap |

The **first two forms share the access syntax** — `[i].field` works on both, the same syntactic unification [[dis-2-4-dynamic-memory|Ch 2.4]] established for plain `arr[i]` access on static and dynamic [[DynamicallyAllocatedArray|1D arrays]]. The **third form requires `[i]->field`** because each element is itself a [[Pointer|pointer]] needing dereferencing.

### Function parameters

[[ArrayDecay|Array decay]] applies: passing a static `class1[]` or a dynamic single-block `class2` to a function declared as `void f(struct studentT *classroom, int size)` copies the base address. Callee mutations on `classroom[i].field` persist to the caller:

```c
void updateAges(struct studentT *classroom, int size) {
    for (int i = 0; i < size; i++) {
        classroom[i].age += 1;   // visible to caller
    }
}
```

**Type-compatibility caveat**: form 3 (array of pointers) is `struct studentT **` after decay — **not** assignable to a parameter declared as `struct studentT *`. The chapter is explicit: *"`classroom3` (array of pointers) cannot be passed to a function expecting `struct studentT` arrays."*

### Per-form cleanup

| Form | Cleanup |
|---|---|
| Static | No cleanup (stack-allocated, freed on scope exit) |
| Dynamic single block | One `free(class2);` releases all elements |
| Array of pointers | `free(class3[i])` per element first, then no `free` for `class3` itself (stack-allocated array) |

The array-of-pointers form is the most flexible (variable-sized struct elements, sparse arrays, easy element swap by pointer assignment) at the cost of N+1 [[HeapMetadata|heap headers]] and the per-element cleanup burden — the [[ArrayOfArrays|array-of-arrays]] tradeoff pattern restated.

## Connections

- [[CStruct]] — the element type.
- [[CArray]] — the outer aggregate.
- [[ArrayIndexing]] — `class[i]` access.
- [[MemberAccessOperator]] — `class[i].field` field selection.
- [[PassByReference]] — the rule that applies when passing an array-of-structs to a function.
- [[PassByValue]] — the rule that applies to a *single* struct element.
- [[StructAssignment]] — `class[i] = class[j];` is legal because `class[i]` is an lvalue.
- [[Malloc]] / [[Free]] / [[SizeOf]] — heap-allocation machinery for the dynamic forms.
- [[ArrayDecay]] — explains why static and dynamic single-block forms share a function-parameter signature.
- [[DynamicallyAllocatedArray]] — the syntactic-unification parallel from [[dis-2-4-dynamic-memory|Ch 2.4]] (plain arrays).
- [[ArrayOfArrays]] — the parallel multi-allocation pattern from [[dis-2-5-arrays|Ch 2.5]] (2D arrays).
- [[PointerToStruct]] — element type of the *array-of-pointers* form.
- [[ArrowOperator]] — the access operator for the *array-of-pointers* form (`class3[i]->field`).
- [[HeapMetadata]] — the per-allocation overhead in the array-of-pointers form.
- [[dis-1-6-structs]] — chapter where arrays of structs are first mentioned (deferred to Ch 2 for full treatment).
- [[dis-2-7-structs]] — chapter that delivers the full three-form treatment.
