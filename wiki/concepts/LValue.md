---
title: "LValue (C)"
type: concept
tags: [c-language, semantics]
sources: [dis-1-6-structs]
last_updated: 2026-05-17
---

# LValue (C)

An **lvalue** (historically *"left-value"*) in [[CLanguage|C]] is an expression that designates an addressable storage location — something that can legally appear on the **left** side of an assignment. Per [[dis-1-6-structs|Dive into Systems Ch 1.6]]: *"an lvalue represents a memory storage location appearing on the left side of assignment statements."*

## What is and isn't an lvalue

**Valid lvalues:**
- Plain variables: `x = 8;`
- Array *elements* (not array names): `arr[3] = 7;`
- Struct *variables*: `student1 = student2;` (whole-struct assignment is legal)
- Struct *fields* of non-array type: `student1.age = 20;`

**Invalid lvalues** (per [[dis-1-6-structs|Ch 1.6]]):
- Arithmetic-result expressions: `x + 1 = 8;` — the sum has no permanent address.
- Array *names*: `arr = "hello";` — the base address of a fixed-capacity array can't change; use [[Strcpy|`strcpy(arr, "hello")`]] instead.
- Struct fields *whose type is an array*: `student1.name = student2.name;` — `name` is `char []`, inheriting the array-not-an-lvalue rule.

## Why it matters here

[[dis-1-6-structs|Ch 1.6]] introduces the lvalue concept specifically to explain the asymmetry between [[CStruct|structs]] and [[CArray|arrays]]:

| Aggregate | Whole-record assignment? |
|---|---|
| `struct studentT s1, s2;` then `s1 = s2;` | **Legal** — structs are lvalues |
| `int arr1[10], arr2[10];` then `arr1 = arr2;` | **Illegal** — array names are not lvalues |

Wrapping an array inside a struct *promotes* its assignability transitively: `s1 = s2;` *does* copy the bytes of an embedded `char name[64]` field, even though writing `s1.name = s2.name;` directly would not compile.

## Connections

- [[CStruct]] — *is* an lvalue (enables whole-struct assignment).
- [[CArray]] — array *name* is *not* an lvalue (cannot be assigned).
- [[MemberAccessOperator]] — `.` expressions inherit the lvalue-ness of the field type.
- [[StructAssignment]] — the lvalue-enabled whole-record copy.
- [[Strcpy]] — the workaround for the array-not-an-lvalue rule on strings.
- [[CLanguage]] — host language.
- [[dis-1-6-structs]] — chapter of origin.
