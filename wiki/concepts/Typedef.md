---
title: "typedef (C)"
type: concept
tags: [c-language, struct, type-alias]
sources: [dis-1-6-structs, dis-2-7-structs, dis-2-9-1-advanced-switch]
last_updated: 2026-05-17
---

# typedef (C)

`typedef` is the [[CLanguage|C]] keyword that introduces a **type alias** — a single-word name for an existing (potentially multi-word) type. Most commonly used with [[CStruct|structs]] to drop the verbose `struct <name>` prefix from variable declarations.

[[dis-1-6-structs|Dive into Systems Ch 1.6]] **references** `typedef` and **defers** its full treatment to Section 2 (*A Deeper Dive Into C*); the chapter itself uses the two-word `struct studentT` form throughout.

## Two idiomatic forms

**Form 1 — alias after the definition:**

```c
struct studentT {
    char name[64];
    int age;
    float gpa;
    int grad_yr;
};
typedef struct studentT StudentT;

StudentT s1;   // shorthand for `struct studentT s1;`
```

**Form 2 — define and alias in one shot:**

```c
typedef struct {
    char name[64];
    int age;
    float gpa;
    int grad_yr;
} StudentT;

StudentT s1;   // direct
```

Either way, the alias `StudentT` becomes interchangeable with `struct studentT` at declaration sites.

## Why it matters

Without `typedef`, every variable declaration of a struct type requires the two-word `struct <name>` form — verbose at scale. With `typedef`, idiomatic [[CLanguage|C]] codebases declare struct types once and use one-word aliases everywhere else. This is also how the standard library exposes opaque types like `size_t`, `FILE`, `time_t`, etc.

## Status in [[dis-1-6-structs|Ch 1.6]]

**Deferred.** Ch 1.6's worked examples stay with the explicit `struct studentT` two-word form to keep the focus on struct mechanics; `typedef` is a pure naming convenience and adds no semantics.

## Status in [[dis-2-7-structs|Ch 2.7]]

**Available but used sparingly.** Ch 2.7 introduces `typedef` as part of the active vocabulary alongside the deeper struct treatment but the chapter's worked examples continue to use the explicit `struct studentT` / `struct personT` / `struct node` two-word form to keep the [[Pointer|pointer]]-vs-struct type-spelling crisp. `typedef` becomes the load-bearing readability tool when [[SelfReferentialStruct|self-referential]] types appear (e.g., `typedef struct node Node;` lets the `next` field type drop the `struct` keyword in subsequent declarations: `Node *next;` rather than `struct node *next;`).

## Status in [[dis-2-9-1-advanced-switch|Ch 2.9.1]]

**Formally introduced.** Ch 2.9.1 codifies three canonical aliasing patterns — [[CEnum|enum]] alias (`typedef enum class_year classYr;`), [[CStruct|struct]] alias (`typedef struct studentT studentT;`), primitive-width alias (`typedef unsigned long long ull;`) — plus the **combined struct-typedef one-liner** `typedef struct studentT { ... } studentT;` as the idiomatic single-declaration form most production [[CLanguage|C]] code uses. See [[TypedefExpansion]] for the full taxonomy.

## Connections

- [[CStruct]] — the type `typedef` is most commonly applied to.
- [[CEnum]] — the [[dis-2-9-1-advanced-switch|Ch 2.9.1]] enum-aliasing target.
- [[TypedefExpansion]] — the Ch 2.9.1 three-pattern taxonomy + combined one-liner form.
- [[StructDefinition]] — the construct `typedef` typically wraps.
- [[CLanguage]] — host language.
- [[SelfReferentialStruct]] — the use case where `typedef struct node Node;` materially improves readability.
- [[dis-1-6-structs]] — chapter where `typedef` is first mentioned (deferred to Ch 2 for full treatment).
- [[dis-2-7-structs]] — chapter that uses it as part of the active vocabulary.
- [[dis-2-9-1-advanced-switch]] — chapter that formally codifies the three canonical aliasing patterns.
