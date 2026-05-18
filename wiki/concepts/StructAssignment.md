---
title: "Struct Assignment (C)"
type: concept
tags: [c-language, struct]
sources: [dis-1-6-structs]
last_updated: 2026-05-17
---

# Struct Assignment (C)

**Struct assignment** is the [[CLanguage|C]] operation `s2 = s1;` that copies every byte of one [[CStruct|struct]] variable into another. Per [[dis-1-6-structs|Dive into Systems Ch 1.6]], structs are [[LValue|lvalues]], so the assignment is **legal** and **field-by-field** (semantically) — the result has the same value in every member as the source.

## Worked example

```c
struct studentT student1, student2;

strcpy(student1.name, "Kwame Salter");
student1.age = 20;
student1.gpa = 3.5;
student1.grad_yr = 2020;

student2 = student1;   // copies name (all 64 bytes), age, gpa, grad_yr

strcpy(student2.name, "Frances Allen");  // diverges only after the copy
student2.grad_yr = student1.grad_yr + 1; // student2.grad_yr == 2021
```

After `student2 = student1;` the two structs are independent — mutating `student2`'s fields does not affect `student1`'s.

## Why this works for structs but not arrays

The asymmetry with [[CArray|arrays]] is the chapter's headline contrast:

| Aggregate | Whole-record assignment? |
|---|---|
| `struct studentT s1, s2;` | `s1 = s2;` — **legal** |
| `int arr1[10], arr2[10];` | `arr1 = arr2;` — **illegal** |

The reason: a struct variable is an [[LValue|lvalue]] (addressable, assignable); an array *name* is not. Embedding an array inside a struct *transitively* promotes the array's assignability — `s1 = s2;` copies the embedded `char name[64]` even though writing `s1.name = s2.name;` directly would fail.

## Implementation

Struct assignment is compiled as a byte-wise memory copy of `sizeof(struct ...)` bytes from source to destination — typically lowering to a `memcpy` or equivalent inline copy. The cost scales with the struct's full size including any [[StructMember|array members]] and alignment padding.

## Connections

- [[CStruct]] — the type the operation acts on.
- [[LValue]] — the property that makes struct assignment legal.
- [[CArray]] — the *contrast* — array names are not lvalues, so no `arr1 = arr2;`.
- [[SizeOf]] — the byte count copied by struct assignment.
- [[PassByValue]] — closely related: function-call parameter binding for a struct argument is effectively a struct assignment into the parameter slot.
- [[dis-1-6-structs]] — chapter of origin.
