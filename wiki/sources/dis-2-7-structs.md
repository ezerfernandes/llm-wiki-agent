---
title: "Dive into Systems — Ch 2.7 Structs"
type: source
tags: [c-language, struct, pointer, dynamic-memory, linked-list, textbook]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/structs.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s seventh section of *[[DiveIntoSystems]]* Ch 2 *A Deeper Dive Into C* — **returns to [[CStruct|structs]] with the full [[Pointer|pointer]] / [[Malloc|dynamic-memory]] toolkit Ch 2.2–2.6 supplied**, deepening [[dis-1-6-structs|Ch 1.6]]'s three-step dot-operator introduction along five axes:

1. **Review** of the [[StructDefinition|define-declare-access]] discipline plus the [[LValue|lvalue]] semantics of [[StructAssignment|whole-struct copy]] (`s2 = s1;`).
2. **[[PointerToStruct|Pointers to structs]]** with [[Malloc|`malloc(sizeof(struct studentT))`]] for heap allocation, and the [[ArrowOperator|`->`]] shorthand for `(*p).field`.
3. **[[StructPointerField|Pointer fields inside structs]]** requiring a **two-step malloc discipline** — one allocation for the struct, separate allocations for each pointer field.
4. **[[ArrayOfStructs|Arrays of structs]]** in all three forms — static `struct studentT class[40]`, dynamic `struct studentT *class = malloc(...)`, and array-of-pointers `struct studentT *class[40]` — with the per-form indexing/access rules.
5. **[[SelfReferentialStruct|Self-referential structs]]** — structs with a `struct node *next` field, the foundation for [[LinkedList|linked lists]], trees, and graphs.

The chapter's headline payoff is that *struct field access syntax is fully compositional* — **start from the outermost variable's type and use its type's syntax to access individual parts**, recursing through nested types. The [[ArrowOperator|`->`]] / [[Typedef|`typedef`]] / [[ArrayOfStructs|arrays of structs]] features [[dis-1-6-structs|Ch 1.6]] named-and-deferred are all delivered here.

## Key Claims

- **Struct review is [[dis-1-6-structs|Ch 1.6]] verbatim**: define type → declare variables (two-word `struct <name>` form) → access fields with [[MemberAccessOperator|`.`]]. Structs are [[LValue|lvalues]] so `s2 = s1;` copies all bytes; structs pass to functions by [[PassByValue|value]] (full copy) so callee mutations are invisible — but if a field is an [[CArray|array]] like `char name[64]`, passing **the field directly** ([[ArrayDecay|array decay]]) yields caller-visible mutation, while passing **the whole struct** copies the array bytes.
- **[[PointerToStruct|Pointer-to-struct]] requires its own [[PointerDeclaration|declaration]]** — `struct studentT *sptr;` — and [[Malloc|`malloc(sizeof(struct studentT))`]] for heap storage. The [[SizeOf|`sizeof`]] expression ensures *"sufficient space for all field values."*
- **Memory location depends on declaration form**: `struct studentT s;` puts the struct on the [[StackSection|stack]]; `struct studentT *sptr = malloc(...);` puts the struct on the [[HeapSection|heap]] with only the pointer on the stack.
- **The [[ArrowOperator|arrow operator `->`]] is shorthand for dereference-then-dot**: `sptr->grad_yr = 2021;` is equivalent to `(*sptr).grad_yr = 2021;`. The parenthesized form is *"cumbersome"*; the arrow form is idiomatic.
- **[[StructPointerField|Pointer fields inside structs]] require separate [[Malloc|`malloc`]] calls** — one for the struct itself, one for each dynamically-allocated pointer field. Example: `p1.name = malloc(sizeof(char) * 8); strcpy(p1.name, "Zhichen");` — the `name` field is a [[CString|C-string]] needing its own heap buffer.
- **Field access is compositional from the outermost type inward.** For `struct studentT s; struct studentT *sptr;` with a pointer field `char *name;`, the access rules are: `s.age` (struct, int) uses `.`; `sptr->age` (struct pointer, int) uses `->`; `s.name[2]` (struct, char*, char) combines `.` then `[]`; `sptr->name[2]` (struct pointer, char*, char) combines `->` then `[]`.
- **[[ArrayOfStructs|Arrays of structs]] have three forms**: (1) **static** `struct studentT class1[40]` — `class1[3].age = 21;` (index, then dot); (2) **dynamic single block** `struct studentT *class2 = malloc(sizeof(struct studentT) * 15);` — `class2[3].year = 2013;` (still array indexing with dot — the syntactic unification with static arrays that mirrors [[dis-2-4-dynamic-memory|Ch 2.4]]'s rule for plain dynamic arrays); (3) **array of pointers** `struct studentT *class3[40]; class3[5] = malloc(sizeof(struct studentT)); class3[5]->age = 21;` (index, then arrow — each element is a *pointer* to a heap struct).
- **Function parameters for arrays of structs** follow [[ArrayDecay|array decay]] / [[PassByReference|pass-by-reference]] — the base address is copied, so callee mutations on `classroom[i].age` persist to the caller. **Type compatibility**: a function expecting `struct studentT *classroom` (or `struct studentT classroom[]`) accepts forms (1) and (2) but **not** form (3) (array of pointers — `struct studentT **`).
- **[[SelfReferentialStruct|Self-referential structs]] enable [[LinkedDataStructure|linked dynamic data structures]]** — the `struct node { int data; struct node *next; };` pattern is *the foundation* for [[LinkedList|linked lists]], trees, and graphs. Nodes are heap-allocated individually via [[Malloc|`malloc(sizeof(struct node))`]]; the `next` field links them; the `head` pointer (often on the stack) anchors the list; the last node's `next` is [[NullPointer|`NULL`]] to terminate the chain. Memory is *non-contiguous* — the load-bearing contrast with [[CArray|arrays]].
- **The two list-construction idioms in the chapter**: (a) **prepend to head** — `temp = malloc(...); temp->next = head; head = temp;` (O(1), reverses input order); the chapter's worked-example loop builds a 3-node list by prepending.
- **[[Typedef|`typedef`]]** finally appears alongside its struct types throughout this section's examples (the deferred-from-Ch-1.6 feature). The chapter freely writes `struct studentT *sptr` rather than introducing a `StudentT` alias, but `typedef` is now part of the working vocabulary.

## Key Quotes

> "A `struct` represents a heterogeneous collection of different data types unified as a single coherent unit." — §2.7.1 (restating [[dis-1-6-structs|Ch 1.6]]).

> "When structs are passed to functions, a complete copy of all field bytes is copied to the parameter. Consequently, modifications to parameter fields don't affect the original argument — only changes to pointer fields affect external data." — §2.7.1 (the [[PassByValue|pass-by-value]] rule re-stated for the pointer-field era).

> "Using `sizeof` ensures sufficient space for all field values." — §2.7.2 ([[Malloc|`malloc(sizeof(struct ...))`]] discipline).

> "While technically correct, the syntax `(*sptr).field` is cumbersome. C provides the **arrow operator** as shorthand." — §2.7.2 (the [[ArrowOperator|`->`]] motivation).

> "To access field values appropriately, start from the outermost variable type and use its type syntax to access individual parts." — §2.7.3 (the **compositional field-access rule** — the chapter's load-bearing principle for nested struct/pointer/array types).

> "[Self-referential structs] enable building linked data structures (linked lists, trees, graphs) without contiguous memory requirements." — §2.7.5 (the [[LinkedList|linked-list]] motivation contrasting with [[CArray|array]] contiguity).

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 2.7, the seventh section of Ch 2.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-1-6-structs]] — Ch 1.6 *Structs* — the chapter Ch 2.7 *deepens*; supplies the define-declare-access discipline and the [[StructAssignment|whole-struct copy]] / [[PassByValue|pass-by-value]] rules that Ch 2.7 reuses without re-deriving.
- [[dis-2-2-pointers]] — Ch 2.2 *Pointers* — supplies the [[Pointer|pointer]] feature Ch 2.7 applies to structs; the [[ArrowOperator|`->`]] operator delivers the *pointer-to-struct* use case Ch 2.2 named-and-deferred.
- [[dis-2-3-pointers-functions]] — Ch 2.3 *Pointers and Functions* — supplies the [[PassByPointer|pass-by-pointer]] mechanism that arrays-of-structs and self-referential-struct functions use.
- [[dis-2-4-dynamic-memory]] — Ch 2.4 *Dynamic Memory Allocation* — supplies [[Malloc|`malloc`]] / [[Free|`free`]] / [[SizeOf|`sizeof`]] machinery that Ch 2.7 applies to struct allocation; the *"`arr[i]` syntax works on both static and dynamic arrays"* unification extends here to *"on both static and dynamic arrays of structs."*
- [[dis-2-5-arrays]] — Ch 2.5 *Arrays in C* — supplies [[ArrayDecay|array decay]] as the unifying primitive that explains why `struct studentT classroom[40]` and `struct studentT *classroom = malloc(...)` share function-parameter signatures.
- [[CStruct]] — the type Ch 2.7 deepens.
- [[ArrowOperator]] — `->` operator finally fully treated here (Ch 1.6 named-and-deferred).
- [[Typedef]] — finally usable here (Ch 1.6 named-and-deferred).
- [[MemberAccessOperator]] — `.` operator, the value-operand counterpart.
- [[StructMember]] — the named fields the operators select.
- [[StructDefinition]] — the type-introduction syntax.
- [[StructAssignment]] — whole-struct copy via `=`.
- [[PointerToStruct]] — **new concept** — pointer-typed variables referencing structs.
- [[StructPointerField]] — **new concept** — pointer-typed *fields inside* structs requiring two-step `malloc`.
- [[ArrayOfStructs]] — **expanded** — full three-form treatment now backed by Ch 2.7.
- [[SelfReferentialStruct]] — **new concept** — structs containing a pointer to their own type, enabling linked structures.
- [[LinkedList]] — **new concept** — the canonical use case for self-referential structs.
- [[LinkedDataStructure]] — the broader family ([[LinkedList|linked lists]], trees, graphs); Ch 2.2 named-and-deferred to here.
- [[Pointer]] / [[PointerDeclaration]] / [[DereferenceOperator]] / [[AddressOfOperator]] / [[NullPointer]] — pointer machinery from [[dis-2-2-pointers|Ch 2.2]] applied to structs.
- [[Malloc]] / [[Free]] / [[SizeOf]] — heap machinery from [[dis-2-4-dynamic-memory|Ch 2.4]].
- [[HeapSection]] / [[StackSection]] — the chapter's static-on-stack vs dynamic-on-heap rule.
- [[CString]] / [[Strcpy]] — the `char *name` field example uses [[Strcpy|`strcpy`]] into a separately-malloc'd buffer.
- [[CArray]] / [[ArrayIndexing]] / [[ArrayDecay]] / [[PassByReference]] / [[PassByValue]] — the array-side machinery that arrays-of-structs reuse.
- [[CLanguage]] — host language.

## Contradictions

None. Ch 2.7 *completes* [[dis-1-6-structs|Ch 1.6]]'s deferrals ([[ArrowOperator|`->`]], [[Typedef|`typedef`]], [[ArrayOfStructs|arrays of structs]]) and *extends* the [[dis-2-4-dynamic-memory|Ch 2.4]] / [[dis-2-5-arrays|Ch 2.5]] static-vs-dynamic unification from plain arrays to arrays of structs. The [[PassByValue|struct-pass-by-value]] rule from Ch 1.6 is restated unchanged; the *only* mutation channels are (a) passing a pointer to the struct, (b) passing an array field (which decays), (c) passing an array-of-structs (which decays to the base address). No prior claim overturned.
