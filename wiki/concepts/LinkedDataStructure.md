---
title: "Linked Data Structure (C)"
type: concept
tags: [c-language, pointers, data-structures]
sources: [dis-2-2-pointers, dis-2-7-structs]
last_updated: 2026-05-17
---

# Linked Data Structure (C)

A **linked data structure** in [[CLanguage|C]] is a collection of dynamically allocated nodes — typically [[CStruct|structs]] — connected via [[Pointer|pointer]] fields. Per [[dis-2-2-pointers|DIS Ch 2.2]] this is the fourth of the five use cases [[Pointer|pointers]] unlock: *"create linked dynamic data structures."*

Canonical examples: **linked lists** (each node holds a `next` pointer), **trees** (each node holds child pointers), **graphs** (each node holds an adjacency list of pointers).

## The shape

A minimal singly-linked list node:

```c
struct node {
    int value;
    struct node *next;   /* pointer to the next node, or NULL at the tail */
};
```

The recursive type works precisely because [[Pointer|pointer]] types have a fixed size known before the pointee type is fully defined — the compiler can size `struct node` without yet knowing what `struct node` looks like.

## Why pointers are required

[[CArray|Arrays]] (the [[dis-1-5-arrays-strings|Ch 1.5]] aggregate type) have three properties that *prevent* them from serving as linked structures:

| [[CArray|Array]] property | Why linked structures need the opposite |
|---|---|
| Contiguous in memory | Linked nodes are scattered across the [[HeapSection|heap]] |
| Fixed capacity at compile time | Linked structures grow / shrink at runtime |
| Size is part of the type | Nodes are added one at a time, independently |

[[Pointer|Pointers]] solve all three — each node lives wherever [[Malloc|`malloc`]] put it; the `next` pointer connects them; growth is one `malloc` at a time.

## The two-feature dependency

Linked data structures sit at the intersection of **two** Ch 2 features:

1. **[[Pointer|Pointers]]** (this section, Ch 2.2) — the *link* mechanism between nodes.
2. **[[DynamicMemoryAllocation|Dynamic memory allocation]]** (Ch 2.4, deferred) — the *create-a-new-node-at-runtime* mechanism.

[[dis-2-2-pointers|Ch 2.2]] introduces only the first half. Full linked-list code requires both, so the canonical examples (insert / delete / traverse) are deferred to Ch 2.4 or later.

## The `NULL`-terminated sentinel idiom

Linked structures conventionally use [[NullPointer|`NULL`]] as the end-of-chain marker:

```c
struct node *head = NULL;   /* empty list */

/* later, with a populated list */
struct node *cur = head;
while (cur != NULL) {       /* the canonical traversal */
    printf("%d\n", cur->value);
    cur = cur->next;
}
```

The `cur != NULL` guard combines [[NullPointer|`NULL`]] (as end-marker), [[DereferenceOperator|dereference]] (via [[ArrowOperator|`->`]]), and [[ShortCircuitEvaluation|short-circuit]] guard discipline into a single idiom — every loop iteration's first move is *"are we still on the list?"*

## Three idiomatic linked structures

| Structure | Per-node pointers | Used for |
|---|---|---|
| **Singly-linked list** | `next` | Stacks, queues, sequences with cheap front-insert |
| **Doubly-linked list** | `next`, `prev` | Sequences with cheap bidirectional traversal / mid-list removal |
| **Binary tree** | `left`, `right` | BSTs, heaps, expression trees |

All three depend on the same Ch 2.2 mechanics.

## Status update from [[dis-2-7-structs|Ch 2.7]]

[[dis-2-7-structs|Ch 2.7]] §2.7.5 **finally delivers** the *concrete operations* this page deferred — [[SelfReferentialStruct|self-referential structs]] are formally introduced as the type construct, and the [[LinkedList|linked list]] worked example walks the full *prepend-to-head* build idiom with [[Malloc|`malloc`]] / [[ArrowOperator|`->`]] / [[NullPointer|`NULL`]]-termination wired together. The two-feature dependency this page named is now fully on the page in [[dis-2-7-structs|Ch 2.7]] (Ch 2.2 pointers + Ch 2.4 dynamic memory + Ch 1.6 / 2.7 structs).

## What this page doesn't cover (yet)

- **Doubly-linked variants and tree algorithms** — Ch 2.7 stays with singly-linked lists; trees / graphs noted as *"linked data structures (linked lists, trees, graphs)"* but not worked through.
- **Cycle detection and memory-leak hazards** — the *who frees what* discipline for shared nodes.

## Connections

- [[CLanguage]] — the language.
- [[Pointer]] — the *link* primitive.
- [[NullPointer]] — the end-of-chain sentinel.
- [[CStruct]] — the *node* aggregate type.
- [[ArrowOperator]] — the readable per-node field access (`cur->value`, `cur->next`).
- [[DynamicMemoryAllocation]] — the *create-a-node* mechanism; deferred to Ch 2.4.
- [[HeapSection]] — where the nodes live.
- [[DereferenceOperator]] — how `cur->value` reaches the pointed-to node.
- [[ShortCircuitEvaluation]] — what makes `while (cur != NULL && cur->value != target)` safe.
- [[SelfReferentialStruct]] — the enabling type construct, formally introduced in [[dis-2-7-structs|Ch 2.7]].
- [[LinkedList]] — the simplest member of the family; Ch 2.7's worked example.
- [[dis-2-2-pointers]] — defining source (names linked structures as a Ch 2 use case).
- [[dis-2-7-structs]] — the chapter that delivers the concrete mechanism.
