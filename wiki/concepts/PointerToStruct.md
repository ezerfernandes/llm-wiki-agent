---
title: "Pointer to Struct (C)"
type: concept
tags: [c-language, struct, pointer, dynamic-memory]
sources: [dis-2-7-structs]
last_updated: 2026-05-17
---

# Pointer to Struct (C)

A **pointer to a struct** is a [[Pointer|pointer]]-typed variable whose pointed-at type is a [[CStruct|struct]]. Per [[dis-2-7-structs|Dive into Systems Ch 2.7]] this is the construct that *finally* delivers the [[ArrowOperator|`->`]] operator [[dis-1-6-structs|Ch 1.6]] named-and-deferred, and that admits [[Malloc|heap-allocated]] structs alongside [[StackSection|stack-allocated]] ones.

## Declaration and allocation

```c
struct studentT s;             // struct on the stack
struct studentT *sptr;         // pointer to struct (uninitialized)

sptr = malloc(sizeof(struct studentT));   // struct on the heap
if (sptr == NULL) { exit(1); }            // Ch 2.4 OOM discipline
```

The [[SizeOf|`sizeof(struct studentT)`]] expression *"ensures sufficient space for all field values"* — the canonical [[dis-2-4-dynamic-memory|Ch 2.4]] heap-allocation pattern applied to a struct type.

## Memory location

| Form | Variable storage | Struct storage |
|---|---|---|
| `struct studentT s;` | [[StackSection|stack]] | stack (same slot) |
| `struct studentT *sptr = malloc(...);` | [[StackSection|stack]] (the pointer) | [[HeapSection|heap]] (the struct) |
| `&s` passed around | stack | stack |

The pointer-to-struct enables a struct to outlive the [[StackFrame|stack frame]] that created it — the heap-allocation use case for [[Pointer|pointers]] that [[dis-2-2-pointers|Ch 2.2]] enumerated.

## Field access

Two equivalent forms, the [[ArrowOperator|arrow]] preferred:

```c
sptr->grad_yr  = 2021;   // idiomatic
(*sptr).grad_yr = 2021;  // technically correct, "cumbersome" per Ch 2.7
```

Operator precedence forces the parentheses in the dereference form (`*sptr.grad_yr` parses as `*(sptr.grad_yr)` — the wrong meaning, and a type error since `sptr` is not a struct).

## Function-parameter idiom

Passing a struct *by pointer* is the canonical [[CLanguage|C]] idiom for both (a) **mutation** — callee writes through `s->field` to affect the caller's struct, the [[ArrowOperator|`->`]]-equivalent of [[dis-2-3-pointers-functions|Ch 2.3]]'s pass-by-pointer recipe — and (b) **efficiency** — avoids copying the entire struct's bytes that [[PassByValue|pass-by-value]] would entail (one of the five use cases [[dis-2-2-pointers|Ch 2.2]] enumerated for pointers).

```c
void age_one_year(struct studentT *s) {
    s->age += 1;   // mutates caller's struct
}

struct studentT alice = { ... };
age_one_year(&alice);   // pass address; alice.age now incremented
```

## Connections

- [[CStruct]] — the pointed-at type.
- [[Pointer]] — the general mechanism specialized here.
- [[ArrowOperator]] — `->` for field access through the pointer.
- [[DereferenceOperator]] — `*` for the verbose `(*sptr).field` form.
- [[AddressOfOperator]] — `&s` to obtain a pointer to a stack-allocated struct.
- [[Malloc]] / [[SizeOf]] / [[Free]] — heap-allocation machinery.
- [[HeapSection]] / [[StackSection]] — the static-vs-dynamic memory layout.
- [[PassByPointer]] — the calling convention this construct uses.
- [[PassByValue]] — the *avoided* convention (copying the whole struct).
- [[NullPointer]] — the post-`free` and post-OOM discipline.
- [[StructPointerField]] — *contrast*: a pointer field *inside* a struct vs. a pointer *to* a struct.
- [[SelfReferentialStruct]] — the special case where the pointed-at type matches the containing struct.
- [[ArrayOfStructs]] — combined with this construct in the dynamic and array-of-pointers forms.
- [[CLanguage]] — host language.
- [[dis-2-7-structs]] — chapter that delivers the full treatment.
- [[dis-1-6-structs]] — chapter that introduced structs and named-and-deferred this construct.
- [[dis-2-2-pointers]] — chapter that introduced pointers in general.
- [[dis-2-4-dynamic-memory]] — chapter that introduced `malloc`/`sizeof`/`free`.
