---
title: "Linked List (C)"
type: concept
tags: [c-language, struct, pointer, linked-data-structure, data-structure]
sources: [dis-2-7-structs]
last_updated: 2026-05-17
---

# Linked List (C)

A **linked list** is the simplest [[LinkedDataStructure|linked dynamic data structure]] — a chain of [[SelfReferentialStruct|self-referential struct]] *nodes*, each holding a payload (`data`) and a [[Pointer|pointer]] (`next`) to the next node, terminated by [[NullPointer|`NULL`]]. Per [[dis-2-7-structs|Dive into Systems Ch 2.7]] §2.7.5 the linked list is the worked example for self-referential structs and the foundation for the broader [[LinkedDataStructure|linked-data-structure]] family ([[CLanguage|C]] trees, graphs).

## The node type

```c
struct node {
    int data;
    struct node *next;
};
```

The `data` field carries the element (here `int`; in practice any type, including pointer fields for variable-size payloads). The `next` field links to the next node — `NULL` for the last node.

## The head pointer

A linked list is *referred to* by a single **head pointer** — a `struct node *` variable (typically on the [[StackSection|stack]]) that points at the first node. An empty list is `head = NULL;`. Functions that mutate the list either receive `struct node **head` (so they can update the caller's head pointer — [[dis-2-3-pointers-functions|Ch 2.3]] pass-by-pointer recipe at one extra level of indirection) or return the new head.

## Construction by prepending

Ch 2.7's worked example builds a list by **prepending to the head** — the O(1) insertion idiom:

```c
struct node *head = NULL;       // empty list

// add first node
head = malloc(sizeof(struct node));
head->data = 10;
head->next = NULL;

// prepend two more nodes via a loop
struct node *temp;
for (int i = 0; i < 2; i++) {
    temp = malloc(sizeof(struct node));
    temp->data = i;
    temp->next = head;    // new node points at current head
    head = temp;          // update head to new node
}
// Final order (head→tail): 1, 0, 10
```

Note the **order reversal** — iteration values `0, 1` produce list order `1, 0, ...` because each new node becomes the *new head*. Appending to the tail would preserve input order but require O(N) traversal each time (unless the list maintains a separate tail pointer).

## Traversal

Walk the chain via the `next` field until reaching `NULL`:

```c
struct node *curr = head;
while (curr != NULL) {
    printf("%d\n", curr->data);
    curr = curr->next;
}
```

The [[NullPointer|`NULL`]]-check is the termination test — the same sentinel discipline as [[CString|C-strings]]' [[NullTerminator|`'\0'`]].

## Cleanup

Each node is independently [[Malloc|`malloc`]]'d, so each needs its own [[Free|`free`]]. **Save the next pointer before freeing the current node** — accessing `curr->next` after `free(curr)` is [[UseAfterFree|use-after-free]]:

```c
struct node *curr = head;
while (curr != NULL) {
    struct node *next = curr->next;  // save before free
    free(curr);
    curr = next;
}
head = NULL;
```

## Comparison with arrays

| Property | [[CArray|Array]] | Linked list |
|---|---|---|
| Memory layout | Contiguous | Non-contiguous (one node per `malloc`) |
| Random access `[i]` | O(1) | O(N) (walk N links) |
| Insert / delete at head | O(N) (shift) | O(1) |
| Insert / delete at end | O(1) amortized (if size known) | O(N) (without tail pointer) |
| Memory overhead | Just the elements | + one pointer per node + per-allocation [[HeapMetadata|heap header]] |
| Resizing | Realloc all elements | Add/remove one node |
| Cache locality | Excellent (prefetcher-friendly) | Poor (each node is a cache miss) |

The linked list trades random-access speed and cache locality for *flexibility* — growable one element at a time, without copying existing data.

## Connections

- [[SelfReferentialStruct]] — the underlying type pattern.
- [[CStruct]] — the node is a struct.
- [[StructPointerField]] — `next` is a struct pointer field.
- [[Pointer]] / [[NullPointer]] — the linking mechanism and the termination sentinel.
- [[ArrowOperator]] — the field-access operator (`curr->next`, `curr->data`) used throughout linked-list code.
- [[Malloc]] / [[Free]] / [[SizeOf]] — per-node heap-allocation machinery.
- [[LinkedDataStructure]] — the broader family.
- [[CArray]] / [[DynamicallyAllocatedArray]] — the *contrast* data structure.
- [[HeapSection]] / [[StackSection]] — nodes on the heap, head pointer on the stack.
- [[UseAfterFree]] / [[DanglingPointer]] — the failure modes of incorrect cleanup ordering.
- [[CLanguage]] — host language.
- [[dis-2-7-structs]] — chapter of origin (§2.7.5).
- [[dis-2-2-pointers]] — chapter that named linked dynamic data structures as one of pointers' five use cases.
- [[dis-2-4-dynamic-memory]] — chapter that supplied the per-node `malloc`/`free` machinery.
