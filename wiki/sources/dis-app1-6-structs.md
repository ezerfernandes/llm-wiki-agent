---
title: "Dive into Systems — Appendix 1.6 Structs (for Java Programmers)"
type: source
tags: [book, dive-into-systems, c-language, java, structs, cross-walk]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix1/structs.html
---

## Summary

Appendix 1.6 of [[DiveIntoSystems]] is the [[Java]]-programmer's retelling of [[dis-1-6-structs|Ch 1.6]]. Introduces the [[CStruct|`struct`]] as *"a mechanism for treating a set of different types as a single, coherent unit"* — the closest C analog to a Java class with no methods, no inheritance, no constructor. The **value-vs-reference semantics gap** is the section's load-bearing Java-vs-C delta: in C, `s2 = s1` copies all fields; in Java, the same statement copies a reference. See [[JavaVsC]] for the consolidated cross-walk.

## Key Claims (Java-vs-C deltas)

- **C structs ≈ Java classes minus methods, inheritance, constructors, GC.** *"Treating a set of different types as a single, coherent unit."* Just heterogeneous fields glued together.
- **Field-access syntax is identical** — both use the [[MemberAccessOperator|dot operator]]: `student.age = 20;` (Java) ≡ `student1.age = 20;` (C).
- **Whole-record assignment works in C; in Java it copies a reference**: *"`student2 = student1;` copies all field values."* In Java, `s2 = s1;` makes both names refer to the same object. **This is the major semantics delta** Java programmers must internalize.
- **C structs pass to functions [[PassByValue|by value]] — the entire struct is copied.** Java method calls pass object references — modifications inside the method *do* affect the caller's object. *"Changes to the parameter's fields only modify values in the parameter's memory locations, not in the argument's memory locations"* in C.
- **C exposes struct memory layout via [[SizeOf|`sizeof(struct studentT)`]].** Java abstracts this entirely — no `sizeof`, no addressable layout.
- **No methods, no constructor, no inheritance** in C structs. Java's full OO toolkit has no struct analog; the closest equivalent is a class with only fields and no methods (a "data carrier"), recently formalized in Java 14+ as **records**.

## Key Quote

> *"In C, `student2 = student1;` copies all field values."* — the value-semantics rule that catches Java programmers used to reference assignment.

## Worked example — define, assign, pass

```c
struct studentT {
    char name[64];
    int age;
    float gpa;
};

void birthday(struct studentT s) {   // s is a copy
    s.age++;                          // modifies the COPY, not the caller's
}

int main(void) {
    struct studentT s1 = {"Alice", 20, 3.8};
    struct studentT s2 = s1;          // full-field copy (incl. name[64])
    birthday(s1);                     // s1.age still 20 after this call
    printf("size = %zu\n", sizeof(struct studentT));  // ≥ 76, alignment-dependent
    return 0;
}
```

Java equivalent: `Student s2 = s1;` copies the reference; `birthday(s1);` *can* mutate the caller's object (because objects are heap-allocated and passed by reference).

## Connections

- [[DiveIntoSystems]] — Appendix 1 sister of [[dis-1-6-structs|Ch 1.6]].
- [[dis-1-6-structs]] — the Python-cross-walk sibling.
- [[JavaVsC]] — consolidated cross-walk table.
- [[Java]] — Java's class-with-fields model is the closest analog; reference-vs-value semantics is the load-bearing delta.
- [[CStruct]] / [[StructDefinition]] / [[StructMember]] / [[MemberAccessOperator]] / [[StructAssignment]] / [[LValue]] / [[PassByValue]] / [[SizeOf]] / [[ArrowOperator]] / [[Typedef]] / [[ArrayOfStructs]] — reused unchanged from Ch 1.6.

## Contradictions

- None. Pure Java-perspective retelling of [[dis-1-6-structs|Ch 1.6]].
