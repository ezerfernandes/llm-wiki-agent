---
title: "Struct (C)"
type: concept
tags: [c-language, aggregate-type, struct]
sources: [dis-1-6-structs]
last_updated: 2026-05-17
---

# Struct (C)

A **struct** in [[CLanguage|C]] is the second **aggregate** data type after the [[CArray|array]] — a *heterogeneous* bundle of named fields ([[StructMember|members]]) of possibly-different types, treated as a single coherent unit. Per [[dis-1-6-structs|Dive into Systems Ch 1.6]]: *"a `struct` is a type used to represent a heterogeneous collection of data; it's a mechanism for treating a set of different types as a single, coherent unit."*

## Defining vs. declaring vs. accessing

Three-step usage discipline introduced in [[dis-1-6-structs|Ch 1.6]]:

1. **Define the type** with [[StructDefinition|`struct <name> { <fields> };`]] outside any function — no storage is allocated, only a type is introduced.
2. **Declare variables** using the two-word type name: `struct studentT student1, student2;`.
3. **Access fields** with the [[MemberAccessOperator|dot operator `.`]]: `student1.age`, `student1.name`, `student1.name[3]`.

## Headline semantic rules ([[dis-1-6-structs|Ch 1.6]])

- **Structs are [[LValue|lvalues]].** Whole-struct assignment `student2 = student1;` is legal and copies every byte — including the bytes of any embedded array field like `char name[64]`. This is the sharp contrast with [[CArray|arrays]], whose names are not lvalues and cannot be assigned.
- **Structs pass to functions by [[PassByValue|value]].** Mutations to a struct parameter inside the function do **not** persist in the caller, *even for embedded array fields*. This reconciles with [[dis-1-4-functions|Ch 1.4]]'s pass-by-value rule and re-contradicts [[dis-1-5-arrays-strings|Ch 1.5]]'s array-by-reference exception.
- **[[SizeOf|`sizeof(struct ...)`]] reveals byte footprint.** For `struct studentT { char name[64]; int age; float gpa; int grad_yr; }`, `sizeof` reports ≥ 76 bytes; the compiler may insert alignment padding making the actual value larger.

## Canonical example

```c
struct studentT {
    char name[64];
    int age;
    float gpa;
    int grad_yr;
};

struct studentT student1;
strcpy(student1.name, "Kwame Salter");
student1.age = 20;
```

## Connections

- [[CArray]] — the *homogeneous* aggregate; structs are the *heterogeneous* counterpart.
- [[StructMember]] — a single named, typed field inside a struct.
- [[StructDefinition]] — the `struct <name> { ... };` type-introduction syntax.
- [[MemberAccessOperator]] — the dot operator `.` for field access on a struct value.
- [[ArrowOperator]] — `->` for field access on a *pointer* to a struct, deferred to Ch 2.
- [[Typedef]] — the convenience for dropping the `struct` keyword from type names, deferred to Ch 2.
- [[ArrayOfStructs]] — `struct studentT class[30];`, deferred to Ch 2.
- [[StructAssignment]] — the lvalue-enabled whole-record copy `s2 = s1;`.
- [[PassByValue]] — applies to structs (re-establishes [[dis-1-4-functions|Ch 1.4]]'s rule).
- [[PassByReference]] — *contrast*: does not apply to bare struct values, only to pointer-to-struct (Ch 1.7).
- [[SizeOf]] — operator now applied to struct types.
- [[LValue]] — explains why struct assignment is legal and array assignment isn't.
- [[CLanguage]] — the host language.
- [[dis-1-6-structs]] — chapter of origin.
