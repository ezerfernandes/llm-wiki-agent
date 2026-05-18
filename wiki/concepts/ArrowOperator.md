---
title: "Arrow Operator (C `->`)"
type: concept
tags: [c-language, struct, pointer, operator]
sources: [dis-1-6-structs, dis-2-7-structs]
last_updated: 2026-05-17
---

# Arrow Operator (C `->`)

The **arrow operator** `->` accesses a [[StructMember|struct field]] given a **pointer to a struct**, rather than a struct value. It is shorthand for *dereference-then-dot*: `p->field` is equivalent to `(*p).field`.

[[dis-1-6-structs|Dive into Systems Ch 1.6]] **references** the arrow operator and **defers** its full treatment to Section 2 (*A Deeper Dive Into C*), which introduces pointers in detail. Ch 1.6 itself stays with the dot operator on struct values.

## Equivalence

```c
struct studentT s;
struct studentT *p = &s;

// These two lines are identical in behavior:
p->age   = 20;
(*p).age = 20;
```

The arrow form is the idiomatic [[CLanguage|C]] notation — the parenthesized-dereference-then-dot is technically equivalent but unusual in practice.

## Why it exists

[[CLanguage|C]]'s [[MemberAccessOperator|dot operator]] requires a struct *value* on its left. Operator precedence makes `*p.field` parse as `*(p.field)` (the wrong meaning), so the parenthesized form `(*p).field` is required. The arrow operator was introduced as a more readable shorthand that also avoids the precedence trap.

## Relationship to [[PassByValue|pass-by-value]] for structs

The arrow operator is what allows a function to *mutate* a struct in the caller — passing `&student` (a pointer) to a function with parameter `struct studentT *s` lets the function write through `s->age = 21;` to the caller's struct. This is the [[CLanguage|C]] idiom for *output parameters* on structs, and the workaround for the [[CStruct|struct-pass-by-value]] rule [[dis-1-6-structs|Ch 1.6]] establishes.

## Status in [[dis-1-6-structs|Ch 1.6]]

**Deferred.** The chapter references arrow-operator semantics as the natural extension of dot-operator semantics to pointers, but does not develop pointer mechanics until Ch 1.7 / Ch 2.

## Full treatment in [[dis-2-7-structs|Ch 2.7]]

[[dis-2-7-structs|Ch 2.7]] §2.7.2 finally delivers the operator with the [[Pointer|pointer]] / [[Malloc|dynamic-memory]] toolkit Ch 2.2–2.6 supplied. The operator is presented explicitly as shorthand: *"while technically correct, the syntax `(*sptr).field` is cumbersome. C provides the **arrow operator** as shorthand."*

```c
struct studentT *sptr = malloc(sizeof(struct studentT));
sptr->grad_yr = 2021;   // idiomatic
(*sptr).grad_yr = 2021; // technically equivalent
```

Ch 2.7 §2.7.3 then makes the operator part of its **compositional field-access rule** — *"start from the outermost variable type and use its type syntax to access individual parts."* For nested pointer-fields-in-structs:

| Expression | Outermost type | Rule |
|---|---|---|
| `sptr->age` | struct pointer + int field | `->` |
| `sptr->name` | struct pointer + `char *` field | `->` |
| `sptr->name[2]` | struct pointer + `char *` + `char` | `->` then `[]` |

§2.7.4 extends the operator to **arrays-of-pointers-to-structs**: `struct studentT *class[40]; class[5] = malloc(...); class[5]->age = 21;` — index first (to get the pointer), then arrow (to access the struct's field through the pointer).

§2.7.5 makes the operator the canonical traversal idiom for [[LinkedList|linked lists]] and other [[LinkedDataStructure|linked data structures]] — `curr->next`, `curr->data`, `head->next->next` — the arrow chain *is* the navigation primitive for [[SelfReferentialStruct|self-referential]] structures.

## Connections

- [[MemberAccessOperator]] — the value-operand counterpart `.`.
- [[CStruct]] — the operator's pointed-at type.
- [[StructMember]] — what the operator selects.
- [[PassByValue]] — the rule the arrow operator (used with pointer-to-struct parameters) lets callers work around.
- [[PassByReference]] — the convention enabled by passing `&struct` to a function.
- [[CLanguage]] — host language.
- [[PointerToStruct]] — the operand type the operator selects through.
- [[SelfReferentialStruct]] / [[LinkedList]] / [[LinkedDataStructure]] — the use cases where chained `->` access becomes the navigation primitive.
- [[StructPointerField]] — pointer fields in structs, accessed through this operator's compositional rule.
- [[dis-1-6-structs]] — chapter where the operator is first mentioned (deferred to Ch 2 for full treatment).
- [[dis-2-7-structs]] — chapter that delivers the full treatment.
