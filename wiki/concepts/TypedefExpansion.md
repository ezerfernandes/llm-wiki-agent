---
title: "typedef — Three Canonical Patterns (C)"
type: concept
tags: [c-language, typedef, type-alias, struct, enum]
sources: [dis-2-9-1-advanced-switch]
last_updated: 2026-05-17
---

# `typedef` — Three Canonical Patterns (C)

[[dis-2-9-1-advanced-switch|DiS Ch 2.9.1]] formally introduces [[Typedef|`typedef`]] (after [[dis-1-6-structs|Ch 1.6]] named-and-deferred it and [[dis-2-7-structs|Ch 2.7]] used it sparingly) and codifies **three canonical aliasing patterns** plus the **combined struct-typedef one-liner** as the idiomatic form most production [[CLanguage|C]] codebases use.

```c
typedef existing_type_name new_type_alias_name;
```

## Pattern 1 — Alias an [[CEnum|`enum`]]

```c
enum class_year { FROSH, SOPH, JUNIOR, SENIOR };
typedef enum class_year classYr;

classYr yr;   // shorthand for `enum class_year yr;`
```

Without `typedef`, every variable declaration carries the verbose two-word `enum class_year` form. With it, `classYr` becomes a first-class single-word type name.

## Pattern 2 — Alias a [[CStruct|`struct`]]

The Ch 2.9.1 form drops the verbose `struct studentT` prefix:

```c
struct studentT { char name[30]; classYr year; float gpa; };
typedef struct studentT studentT;

studentT student;   // not `struct studentT student;`
```

## Pattern 3 — Alias a primitive width

```c
typedef unsigned long long ull;
ull num;   // shorthand for `unsigned long long num;`
```

Common in code that uses fixed-width integer types — the [[StdintLibrary|`<stdint.h>`]] header is built entirely from this pattern (`typedef long int32_t;` etc.).

## The combined struct-typedef one-liner — the idiomatic form

```c
typedef struct studentT {
    char name[30];
    classYr year;
    float gpa;
} studentT;
```

**One declaration defines both** the struct type and its alias — eliminating the separate `typedef` line. The struct tag (`studentT`) and the typedef alias (`studentT`) can share the same name in [[CLanguage|C]] because they live in **different namespaces** (the "struct tag" namespace and the "ordinary identifier" namespace). Most modern [[CLanguage|C]] codebases use this form.

A common variant **omits the struct tag entirely**, useful when the type is never used in [[SelfReferentialStruct|self-referential]] form:

```c
typedef struct {
    char name[30];
    int age;
} Person;
```

The trade-off: without a struct tag, you cannot write `struct Person *p` inside the struct's own definition — which means **self-referential** types (linked lists, trees) must keep the tag form: `typedef struct node { int data; struct node *next; } Node;`.

## Why these aliases matter

Per [[dis-2-9-1-advanced-switch|Ch 2.9.1]]: `typedef` *enhances readability and reduces verbosity*. The cost is purely syntactic — the alias is a compile-time substitution with no runtime effect. The benefits compound at scale: a codebase that types 1000 `studentT *` declarations saves 7000 characters over `struct studentT *`.

## Comparison with the underlying [[Typedef]] page

The existing [[Typedef]] concept page covered the **two struct-aliasing forms** (alias after definition / alias inline). This page extends the taxonomy with the **enum-aliasing** and **primitive-width-aliasing** patterns introduced in Ch 2.9.1 and frames all three plus the combined one-liner under a single rule: *"`typedef` creates a type alias — a single word stands in for any existing type expression"*.

## Connections

- [[dis-2-9-1-advanced-switch]] — source.
- [[Typedef]] — the underlying concept page; this page is its Ch 2.9.1 expansion.
- [[CStruct]] / [[StructDefinition]] — the most common typedef target.
- [[CEnum]] — the enum-aliasing pattern.
- [[SelfReferentialStruct]] — the use case that requires keeping the struct tag.
- [[CPrimitiveType]] — primitive-width aliasing.
- [[CLanguage]] / [[DiveIntoSystems]].
