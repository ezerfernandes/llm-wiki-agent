---
title: "Dive into Systems — Ch 1.6 Structs"
type: source
tags: [book, dive-into-systems, c-language, structs]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C1-C_intro/structs.html
---

## Summary

Section 1.6 of [[DiveIntoSystems]] (sixth content section of Ch 1 *By the C, the Beautiful C*) introduces the second **aggregate** [[CLanguage|C]] type after [[dis-1-5-arrays-strings|Ch 1.5]]'s [[CArray|array]]: the **[[CStruct|struct]]**, a *heterogeneous* bundle of named fields of possibly-different types treated as a single coherent unit. Per the chapter, *"a `struct` is a type used to represent a heterogeneous collection of data; it's a mechanism for treating a set of different types as a single, coherent unit."* The section codifies a three-step usage discipline — **define the type** outside any function, **declare variables** of that type, **access fields** via [[MemberAccessOperator|dot notation `.`]] — and surfaces three load-bearing semantic rules: (1) **structs are [[LValue|lvalues]]**, so whole-struct assignment `student2 = student1;` copies every field's bytes (including any array-typed fields like `name[64]`) — a sharp contrast with [[CArray|array]] names, which are *not* lvalues and cannot be assigned; (2) **structs pass to functions [[PassByValue|by value]]** — the chapter's explicit reconciliation with [[dis-1-4-functions|Ch 1.4]]'s pass-by-value rule and *re-contradiction* with [[dis-1-5-arrays-strings|Ch 1.5]]'s array exception, mutations to a struct parameter inside the function do **not** persist in the caller, including mutations to embedded array fields; (3) **[[SizeOf|`sizeof`]] reveals the struct's memory footprint** — for `struct studentT { char name[64]; int age; float gpa; int grad_yr; }` the chapter measures ≥ 76 bytes (64 + 4 + 4 + 4), foreshadowing the alignment / padding story of later chapters. Pointer-to-struct access via the **arrow operator `->`**, arrays of structs, and `typedef` are *referenced* but **deferred** to Ch 2 *A Deeper Dive Into C*.

## Key Claims

- **A [[CStruct|struct]] is a *heterogeneous* aggregate type.** Per the chapter: *"a `struct` is a type used to represent a heterogeneous collection of data; it's a mechanism for treating a set of different types as a single, coherent unit."* Contrast with [[CArray|arrays]] from [[dis-1-5-arrays-strings|Ch 1.5]] which are *homogeneous* (one element type) — structs let fields hold different types (`char name[64]` + `int age` + `float gpa` + `int grad_yr` in one record).
- **Three-step usage discipline.** (1) **Define** the struct *type* outside any function with `struct <name> { <field> <name>; ... };` near the top of the file; (2) **Declare** variables `struct <name> var1, var2;` using the *two-word* type name `struct studentT`; (3) **Access** individual fields with `<var>.<field>` dot notation. Definition is a *type* declaration, not a variable declaration — no storage allocated until step 2.
- **Field access uses the [[MemberAccessOperator|dot operator `.`]].** Given `struct studentT student1;`, the expression `student1.age` has type `int`, `student1.name` has type `char []`, and `student1.name[3]` has type `char`. The dot operator binds tighter than most other operators and chains naturally with array indexing.
- **Structs are [[LValue|lvalues]] — whole-struct assignment is legal.** `student2 = student1;` copies *every byte* of `student1` into `student2` — all fields, including the entire `name[64]` array embedded in the struct. The chapter's headline contrast with [[dis-1-5-arrays-strings|Ch 1.5]]'s [[CArray|array]] rule: an array name is *not* an lvalue, so `arr1 = arr2;` is illegal and the programmer must use [[Strcpy|`strcpy`]] or an explicit loop. **A struct holding an array breaks that restriction transitively** — embedding `char name[64]` inside `struct studentT` and then assigning struct-to-struct *does* copy the name array's bytes.
- **Structs pass to functions [[PassByValue|by value]].** Per the chapter: *"if the function changes the field values of a struct parameter, the changes to the parameter's field values have no effect on the corresponding field values of the argument."* This explicitly **reconciles with [[dis-1-4-functions|Ch 1.4]]'s pass-by-value rule** and *re-contradicts* [[dis-1-5-arrays-strings|Ch 1.5]]'s array-by-reference exception. Even when the struct *contains* an array field, that array is copied (because the array is *embedded* in the struct, not a separate object reached by pointer). Worked example: `int checkID(struct studentT s, int min_age)` mutating `s.age = min_age + 1;` does nothing to the caller's `student`.
- **[[SizeOf|`sizeof`]] reports the struct's full byte footprint.** `sizeof(struct studentT)` for the four-field student example reports **at least 76 bytes** (`64 + 4 + 4 + 4`); the actual value may be larger because of alignment padding the compiler inserts between fields. The chapter notes this foreshadows the layout-and-alignment story deferred to later chapters.
- **Invalid-lvalue counterexamples.** The chapter enumerates expressions that are *not* lvalues and therefore cannot appear on the left of `=`: `x + 1 = 8;` (arithmetic-result is not addressable), `arr = "hello";` (array name is not assignable — use [[Strcpy|`strcpy`]]), `student1.name = student2.name;` (the *field* `name` is itself an array, so the same array-not-an-lvalue rule applies even through a struct).
- **Embedded-array footgun on pass-by-value.** When a struct contains a statically-sized array field (`char name[64]`), passing the struct to a function copies the entire array. *"When structs contain statically declared array fields, the entire array is copied when passing the struct to functions. Changes to array contents within the function don't persist afterward."* This is the explicit contradiction with [[dis-1-5-arrays-strings|Ch 1.5]]'s array-by-reference rule: passing a bare `char name[64]` would pass by reference (array-name decay to pointer), but passing the *struct that contains it* copies the array.
- **Arrow operator, arrays of structs, and typedef deferred.** The chapter explicitly references Section 2 (*A Deeper Dive Into C*) for pointer-to-struct field access via [[ArrowOperator|`->`]], for arrays of structs, and for the [[Typedef|`typedef`]] convenience that lets the programmer drop the `struct` keyword from the type name. Ch 1.6 stays with the minimum-viable surface.

## Key Quotes

> "A `struct` is a type used to represent a heterogeneous collection of data; it's a mechanism for treating a set of different types as a single, coherent unit." — the chapter's definition: structs are the *heterogeneous* counterpart to [[dis-1-5-arrays-strings|Ch 1.5]]'s [[CArray|homogeneous arrays]].

> "If the function changes the field values of a struct parameter, the changes to the parameter's field values have no effect on the corresponding field values of the argument." — the explicit reconciliation with [[dis-1-4-functions|Ch 1.4]]'s [[PassByValue|pass-by-value]] rule and the contradiction with [[dis-1-5-arrays-strings|Ch 1.5]]'s array-by-reference exception.

> "Number of bytes in student struct: 76." — output of `printf("%lu\n", sizeof(struct studentT));` for the canonical four-field student example (`char name[64]; int age; float gpa; int grad_yr;`) — the chapter's first sighting of struct-as-bytes that the [[MemoryHierarchy|memory hierarchy]] / layout chapters will build on.

## Worked examples

**Struct definition + variable declaration + field access:**

```c
struct studentT {
    char name[64];
    int age;
    float gpa;
    int grad_yr;
};

int main(void) {
    struct studentT student1, student2;

    strcpy(student1.name, "Kwame Salter");
    student1.age = 18 + 2;
    student1.gpa = 3.5;
    student1.grad_yr = 2020;

    // Whole-struct assignment — copies every byte
    student2 = student1;
    strcpy(student2.name, "Frances Allen");
    student2.grad_yr = student1.grad_yr + 1;

    printf("%lu\n", sizeof(struct studentT));  // 76 (or more, with padding)
    return 0;
}
```

**[[PassByValue|Pass-by-value]] for structs — mutations do not persist:**

```c
int checkID(struct studentT s, int min_age) {
    int ret = 1;
    if (s.age < min_age) {
        ret = 0;
        s.age = min_age + 1;   // changes only the local copy
    }
    printf("%s is %d years old\n", s.name, s.age);
    return ret;
}
// caller's student.age is unchanged after checkID(student, 18);
```

**Invalid-lvalue counterexamples (compile errors):**

```c
x + 1 = 8;                     // arithmetic result is not addressable
arr = "hello";                 // array name not an lvalue — use strcpy
student1.name = student2.name; // field is an array — same rule applies
```

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 1.6 (6th content section after [[dis-1-1-getting-started|Ch 1.1]] / [[dis-1-2-input-output|Ch 1.2]] / [[dis-1-3-conditionals-loops|Ch 1.3]] / [[dis-1-4-functions|Ch 1.4]] / [[dis-1-5-arrays-strings|Ch 1.5]]).
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-1-1-getting-started]] — supplied the [[CPrimitiveType|primitive types]] (`int`, `float`, `char`) that struct fields are built **of**, and the [[SizeOf|`sizeof`]] operator now applied to struct types.
- [[dis-1-4-functions]] — supplied the [[PassByValue|pass-by-value]] rule this chapter **honors** for structs (in contrast to [[dis-1-5-arrays-strings|Ch 1.5]]'s array exception).
- [[dis-1-5-arrays-strings]] — supplied the [[CArray|array]] type now usable as a struct field, and the [[Strcpy|`strcpy`]] function used to write into a struct's `char name[64]` field; structs *re-establish* the [[PassByValue|pass-by-value]] rule that arrays broke.
- [[CLanguage]] — adds the *heterogeneous* aggregate type ([[CStruct|struct]]) alongside the *homogeneous* aggregate ([[CArray|array]]).
- [[CStruct]] — the chapter's headline type: a heterogeneous bundle of named fields.
- [[StructMember]] — a named, typed field inside a struct definition.
- [[StructDefinition]] — the `struct <name> { ... };` declaration syntax that introduces the *type* (no storage allocated).
- [[MemberAccessOperator]] — the dot operator `.` for reading and writing a struct field given a struct *value* or *variable*.
- [[LValue]] — the addressable-storage-location concept that explains why `student1 = student2;` is legal (structs are lvalues) and why `arr = arr2;` is not (array names are not lvalues).
- [[StructAssignment]] — whole-struct copy `s2 = s1;` — the chapter's lvalue-discipline counterexample to the array rule.
- [[SizeOf]] — operator now applied to struct types: `sizeof(struct studentT) == 76`, with padding-may-make-it-bigger caveat.
- [[ArrowOperator]] — pointer-to-struct field access `p->field`, *referenced and deferred to Ch 2*.
- [[Typedef]] — the `typedef struct { ... } StudentT;` convenience that lets the programmer drop the `struct` keyword, *referenced and deferred to Ch 2*.
- [[ArrayOfStructs]] — `struct studentT class[30];`, *referenced and deferred to Ch 2*.
- [[PassByValue]] — the chapter's headline reconciliation with [[dis-1-4-functions|Ch 1.4]]'s rule: structs *do* pass by value (and so does the entire array embedded in a struct field).
- [[PassByReference]] — *contrast*: bare arrays from [[dis-1-5-arrays-strings|Ch 1.5]] pass by reference; an array *embedded in a struct* does not.
- [[Python]] — contrast: closest analog is a Python `dataclass` or a `dict`; both pass by object-reference (no whole-record copy on assignment), and both are mutable through any reference.

## Contradictions

- **Reconciles with [[dis-1-4-functions|Ch 1.4]]'s [[PassByValue|pass-by-value]] rule and re-contradicts [[dis-1-5-arrays-strings|Ch 1.5]]'s array-by-reference exception.** Ch 1.4 said "pass by value, always"; Ch 1.5 carved out arrays; Ch 1.6 *closes the carve-out for structs* — even when a struct *contains* an array, the struct (and the array embedded in it) is copied on call. The reconciliation is mechanical: the array-by-reference rule only fires when an array *name* decays to a pointer at the call boundary; embedding the array inside a struct prevents that decay because the call boundary sees a *struct* value, not an *array* value. Recorded as a chapter-level pedagogical layering, not a wiki-internal contradiction. The full reconciliation is deferred to Ch 1.7's pointer chapter.
- **Lvalue-discipline asymmetry between [[CStruct|struct]] and [[CArray|array]] surfaces here.** Ch 1.5 established that array names are not lvalues; Ch 1.6 establishes that struct names *are* lvalues, even when those structs *contain* arrays. This is a [[CLanguage|C]] language design choice (and one of its sharper edges): wrapping an array in a struct gives you the assignment / pass-by-value semantics that the array alone refuses. Not a wiki contradiction — both rules are simultaneously true.
- No contradictions with existing concept pages.
