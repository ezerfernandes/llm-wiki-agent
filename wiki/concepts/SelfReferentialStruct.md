---
title: "Self-Referential Struct (C)"
type: concept
tags: [c-language, struct, pointer, linked-data-structure]
sources: [dis-2-7-structs]
last_updated: 2026-05-17
---

# Self-Referential Struct (C)

A **self-referential struct** is a [[CStruct|struct]] type containing one or more [[StructPointerField|pointer fields]] whose pointed-at type is the *same* struct type. Per [[dis-2-7-structs|Dive into Systems Ch 2.7]] §2.7.5 this is the construct that enables *"building linked data structures (linked lists, trees, graphs) without contiguous memory requirements"* — the load-bearing primitive for the [[LinkedDataStructure|linked-data-structure]] use case [[dis-2-2-pointers|Ch 2.2]] enumerated as one of the five reasons [[Pointer|pointers]] exist.

## The canonical pattern

```c
struct node {
    int data;            // the element this node carries
    struct node *next;   // pointer to the next node (or NULL)
};
```

The `next` field declares a pointer to `struct node` *while `struct node` is still being defined* — legal in [[CLanguage|C]] because a pointer to an incomplete type has a known size (one machine word). A *non-pointer* `struct node next;` would be illegal (the type would have to contain itself, with infinite size) — this is why the **pointer indirection** is essential.

## Why it requires non-contiguity

Each `struct node` is allocated **independently** on the [[HeapSection|heap]] via its own [[Malloc|`malloc(sizeof(struct node))`]] call:

```c
struct node *head = malloc(sizeof(struct node));
head->data = 10;
head->next = NULL;
```

The nodes can sit *anywhere* in the heap — the `next` pointers stitch them into a logical sequence regardless of physical layout. This is the load-bearing contrast with [[CArray|arrays]], where the N elements must be *contiguous*: arrays support O(1) random access via [[ArrayIndexing|`arr[i]` = base + i × stride]] precisely because of contiguity; linked structures trade O(1) random access for the ability to grow/shrink one element at a time without reallocating the whole structure.

## Multi-pointer variants

The pattern generalizes to multiple `struct node *` fields for richer topologies:

- **Doubly-linked list**: `struct node *prev; struct node *next;` — bidirectional traversal.
- **Binary tree**: `struct node *left; struct node *right;` — branching to two children.
- **N-ary tree**: `struct node *children[K];` — array of child pointers.
- **Graph node**: `struct node *neighbors[K];` or a linked list of edge structs.

All share the same construction discipline — each node `malloc`'d independently, pointer fields wired up post-allocation.

## Termination convention

The **end** of a linked structure is marked by [[NullPointer|`NULL`]] in the relevant pointer field — `last_node->next = NULL;` signals "no further nodes." This is the same [[NullTerminator|sentinel]] discipline as [[CString|C-strings]]' `'\0'`, generalized to pointer fields: a known invalid value marks the end so traversal code can detect it without an external length count.

## Heap-vs-stack memory layout

| Storage | What lives there |
|---|---|
| [[StackSection|Stack]] | The `head` (or `root`) pointer — typically a local variable. |
| [[HeapSection|Heap]] | All the nodes themselves — one `malloc` per node. |

A linked list with N nodes uses N + 1 heap allocations (with N + 1 [[HeapMetadata|heap headers]] — the same overhead profile as [[ArrayOfArrays|array of arrays]]) plus one stack slot for the head pointer.

## Connections

- [[CStruct]] — the underlying type.
- [[StructPointerField]] — the pointer-typed field is the enabling mechanism.
- [[Pointer]] / [[NullPointer]] — the linking mechanism and the termination sentinel.
- [[LinkedList]] — the simplest self-referential structure; the chapter's worked example.
- [[LinkedDataStructure]] — the broader family (lists, trees, graphs).
- [[Malloc]] / [[Free]] / [[SizeOf]] — per-node heap-allocation machinery.
- [[ArrowOperator]] — the operator for accessing fields through `next` / `prev` / `left` / `right` pointers.
- [[CArray]] — *contrast*: contiguous fixed-capacity vs. non-contiguous growable.
- [[HeapSection]] / [[StackSection]] — the storage breakdown.
- [[HeapMetadata]] / [[HeapFragmentation]] — the per-allocation overhead implication.
- [[CLanguage]] — host language.
- [[dis-2-7-structs]] — chapter of origin (§2.7.5).
- [[dis-2-2-pointers]] — chapter that named [[LinkedDataStructure|linked dynamic data structures]] as one of pointers' five use cases.
- [[dis-2-4-dynamic-memory]] — chapter that supplied the per-node `malloc`/`free` machinery.
