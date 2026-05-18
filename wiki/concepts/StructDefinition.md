---
title: "Struct Definition (C)"
type: concept
tags: [c-language, struct]
sources: [dis-1-6-structs]
last_updated: 2026-05-17
---

# Struct Definition (C)

A **struct definition** in [[CLanguage|C]] is the syntax that introduces a new aggregate *type*. Per [[dis-1-6-structs|Dive into Systems Ch 1.6]]:

```c
struct <struct_name> {
    <field 1 type> <field 1 name>;
    <field 2 type> <field 2 name>;
    ...
};
```

A definition declares a *type*, **not a variable** — no storage is allocated until the programmer separately declares variables of that type:

```c
struct studentT {        // step 1: define the type
    char name[64];
    int age;
    float gpa;
    int grad_yr;
};

struct studentT s1, s2;  // step 2: declare variables
s1.age = 20;             // step 3: access fields with the dot operator
```

## Placement convention

[[dis-1-6-structs|Ch 1.6]] places struct definitions *outside any function*, typically near the top of the file. This makes the type visible to every function in the translation unit; it parallels the *prototypes-at-top-of-file* convention introduced in [[dis-1-4-functions|Ch 1.4]] for [[FunctionPrototype|function prototypes]].

## Two-word type name

The introduced type is named with **two words**: `struct studentT`. The [[Typedef|`typedef`]] convenience (deferred to Ch 2) lets the programmer collapse this to a single word like `StudentT`.

## Connections

- [[CStruct]] — the aggregate type a definition introduces.
- [[StructMember]] — the named, typed fields a definition lists.
- [[Typedef]] — the convenience for one-word naming, deferred to Ch 2.
- [[FunctionPrototype]] — parallel *declare-types-at-top* idiom from [[dis-1-4-functions|Ch 1.4]].
- [[dis-1-6-structs]] — chapter of origin.
