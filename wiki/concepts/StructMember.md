---
title: "Struct Member (C)"
type: concept
tags: [c-language, struct]
sources: [dis-1-6-structs]
last_updated: 2026-05-17
---

# Struct Member (C)

A **struct member** (also called a **field**) is one of the named, typed slots declared inside a [[CStruct|struct]] definition. Per [[dis-1-6-structs|Dive into Systems Ch 1.6]] the syntax is:

```c
struct <struct_name> {
    <field 1 type> <field 1 name>;
    <field 2 type> <field 2 name>;
    ...
};
```

Each member has its own type — members may be [[CPrimitiveType|primitive types]] (`int`, `float`, `char`), [[CArray|arrays]] (`char name[64]`), or even other structs. The chapter's canonical example bundles four heterogeneous members into `struct studentT`:

```c
struct studentT {
    char name[64];   // member: array of 64 char
    int age;         // member: int
    float gpa;       // member: float
    int grad_yr;     // member: int
};
```

## Access

Members are read and written via the [[MemberAccessOperator|dot operator]] `student1.age` for a struct *value* or *variable*, or the [[ArrowOperator|arrow operator]] `p->age` for a *pointer to struct* (deferred to Ch 2). Member type is determined by the field's declared type:

| Expression | Type |
|---|---|
| `student1` | `struct studentT` |
| `student1.age` | `int` |
| `student1.name` | `char []` |
| `student1.name[3]` | `char` |

## Padding and layout

[[dis-1-6-structs|Ch 1.6]] notes that the compiler may insert alignment padding *between* members so each member sits on its preferred boundary; this is why [[SizeOf|`sizeof(struct ...)`]] may exceed the naive sum of member sizes. The deep layout story is deferred to later chapters of [[DiveIntoSystems]].

## Connections

- [[CStruct]] — the aggregate type members live inside.
- [[StructDefinition]] — the syntax that lists members.
- [[MemberAccessOperator]] — `.` access for struct-value field reads/writes.
- [[ArrowOperator]] — `->` access for pointer-to-struct field reads/writes (Ch 2).
- [[CPrimitiveType]] — typical member types.
- [[CArray]] — member type that triggers the embedded-array pass-by-value rule.
- [[SizeOf]] — used to inspect total struct footprint including padding.
- [[dis-1-6-structs]] — chapter of origin.
