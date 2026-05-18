---
title: "Struct Pointer Field (C)"
type: concept
tags: [c-language, struct, pointer, dynamic-memory]
sources: [dis-2-7-structs]
last_updated: 2026-05-17
---

# Struct Pointer Field (C)

A **struct pointer field** is a [[StructMember|struct field]] whose declared type is a [[Pointer|pointer]] — e.g., a `char *name` field inside a `struct personT`. Per [[dis-2-7-structs|Dive into Systems Ch 2.7]] §2.7.3 such fields require **separate [[Malloc|`malloc`]] calls** beyond the struct allocation itself — a **two-step heap-allocation discipline** that is the chapter's headline complexity bump.

## The two-step malloc rule

```c
struct personT {
    char *name;    // pointer field — needs its own heap buffer
    int   age;
};

struct personT p1;
p1.name = malloc(sizeof(char) * 8);   // step 1: allocate the buffer the field points at
strcpy(p1.name, "Zhichen");           // step 2: write into the buffer
p1.age = 21;
```

The [[Malloc|`malloc`]] that allocated `p1` (none in this stack-allocated example) *does not* allocate space for the bytes `p1.name` points at — only the pointer slot itself. Forgetting to `malloc` the field separately leaves `p1.name` as an uninitialized [[DanglingPointer|dangling pointer]] — writing through it via [[Strcpy|`strcpy`]] reliably [[SegmentationFault|segfaults]] or corrupts unrelated memory.

## Contrast with embedded arrays

Compare with [[dis-1-6-structs|Ch 1.6]]'s `struct studentT { char name[64]; ... }`:

| Form | Memory layout | Allocation |
|---|---|---|
| `char name[64];` (embedded array) | 64 bytes *inside* the struct | implicit — part of `sizeof(struct studentT)` |
| `char *name;` (pointer field) | 8 bytes *inside* the struct (the pointer); buffer elsewhere | explicit `malloc` for the buffer |

The embedded-array form is *simpler* (one allocation, bounded size); the pointer-field form is *more flexible* (size known only at runtime) at the cost of two allocations and matching cleanup.

## Compositional field access

Pointer fields trigger the **compositional access rule** Ch 2.7 §2.7.3 articulates: *"start from the outermost variable type and use its type syntax to access individual parts."*

For `struct personT p1;` and `struct personT *p2 = &p1;`:

| Access | Outermost type | Inner type | Syntax |
|---|---|---|---|
| `p1.age` | struct variable | `int` | `.` |
| `p2->age` | struct pointer | `int` | `->` |
| `p1.name` | struct variable | `char *` | `.` |
| `p2->name` | struct pointer | `char *` | `->` |
| `p1.name[2]` | struct variable, `char *`, `char` | element | `.` then `[]` |
| `p2->name[2]` | struct pointer, `char *`, `char` | element | `->` then `[]` |

Each step uses the syntax dictated by the *current* type after the previous operator.

## Cleanup discipline

Each `malloc` needs a matching [[Free|`free`]] — the [[dis-2-4-dynamic-memory|Ch 2.4]] rule applied recursively. For a heap-allocated struct with pointer fields, **free the inner buffers first, then the struct itself** (the same outer-to-inner-then-back discipline as [[ArrayOfArrays|array of arrays]]):

```c
struct personT *p = malloc(sizeof(struct personT));
p->name = malloc(sizeof(char) * 8);
// ... use ...
free(p->name);   // inner first
free(p);         // outer last
```

Reversing the order is a [[UseAfterFree|use-after-free]]: after `free(p)`, dereferencing `p->name` is undefined behavior.

## Connections

- [[CStruct]] — the containing aggregate.
- [[StructMember]] — the general member concept; this is the pointer-typed specialization.
- [[Pointer]] / [[PointerType]] / [[PointerDeclaration]] — the field's type.
- [[Malloc]] / [[Free]] / [[SizeOf]] — the heap-allocation machinery applied per-field.
- [[CString]] / [[Strcpy]] — the canonical `char *name` use case.
- [[DanglingPointer]] / [[UseAfterFree]] — the failure modes from forgetting the two-step rule.
- [[MemoryLeak]] — the failure mode from forgetting to `free` the inner buffers.
- [[MemberAccessOperator]] / [[ArrowOperator]] — the access operators used in the compositional rule.
- [[PointerToStruct]] — *contrast*: pointer *to* a struct vs. pointer *inside* a struct (often used together).
- [[CLanguage]] — host language.
- [[dis-2-7-structs]] — chapter of origin (§2.7.3).
- [[dis-2-4-dynamic-memory]] — chapter that introduced the `malloc`/`free` discipline.
- [[dis-1-6-structs]] — chapter that used embedded-array fields instead (the simpler contrast).
