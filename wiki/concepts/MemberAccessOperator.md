---
title: "Member Access Operator (C `.`)"
type: concept
tags: [c-language, struct, operator]
sources: [dis-1-6-structs]
last_updated: 2026-05-17
---

# Member Access Operator (C `.`)

The **member access operator** (the **dot operator**, `.`) reads or writes a [[StructMember|struct member]] given a [[CStruct|struct]] *value* or *variable*. Per [[dis-1-6-structs|Dive into Systems Ch 1.6]] the syntax is:

```
<variable name>.<field name>
```

The result has the field's declared type and (when the struct itself is an [[LValue|lvalue]]) is itself an lvalue — so the dot expression can appear on either side of `=`.

## Examples

For `struct studentT student1` with the canonical four fields:

```c
strcpy(student1.name, "Kwame Salter");   // write member: array
student1.age = 20;                        // write member: int
student1.gpa = 3.5;                       // write member: float
int yr = student1.grad_yr;                // read member: int
char first = student1.name[0];            // dot then array index
```

| Expression | Type |
|---|---|
| `student1.age` | `int` |
| `student1.name` | `char []` |
| `student1.name[3]` | `char` |

## Lvalue rules

The dot expression is an [[LValue|lvalue]] **when the underlying field type is itself addressable**. So `student1.age = 21;` works (the `int` slot is addressable), but `student1.name = student2.name;` does **not** compile — the field type `char []` is itself not an lvalue (array names are not lvalues), so the dot expression inherits that restriction. The fix is [[Strcpy|`strcpy(student1.name, student2.name)`]].

## Contrast with `->`

The dot operator works on a struct *value or variable*; for a *pointer to struct*, [[CLanguage|C]] provides the [[ArrowOperator|arrow operator `->`]] as a shorthand for `(*p).field`. [[dis-1-6-structs|Ch 1.6]] references `->` but defers it to Ch 2.

## Connections

- [[CStruct]] — the operator's operand type.
- [[StructMember]] — what the operator selects.
- [[ArrowOperator]] — the pointer-to-struct counterpart `->`, deferred to Ch 2.
- [[LValue]] — explains when `.` expressions can appear on the left of `=`.
- [[Strcpy]] — required to write into an array-typed member.
- [[dis-1-6-structs]] — chapter of origin.
