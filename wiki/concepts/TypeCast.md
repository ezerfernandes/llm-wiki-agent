---
title: "Type Cast (C)"
type: concept
tags: [c-language, types, casting, conversion, void-pointer]
sources: [dis-2-9-3-voidstar]
last_updated: 2026-05-17
---

# Type Cast (C)

A **type cast** in [[CLanguage|C]] is an explicit, programmer-supplied type conversion written `(target_type)expression`. Per [[dis-2-9-3-voidstar|DIS Ch 2.9.3]], it is the mechanism that lets [[VoidPointer|`void *`]] usefully participate in expressions: *"programmers must recast the parameter to access its actual type"* via `(type *)pointer`.

## Syntax

```c
(target_type)expression
```

- Parentheses around the **target type only** (not around the whole expression).
- Applied as a **unary prefix operator** — binds tighter than `*`, `&`, `+`, but looser than `()` (function call) and `[]` (subscript).

## The pointer-recast use case (Ch 2.9.3)

The headline application from [[dis-2-9-3-voidstar|Ch 2.9.3]]: converting a [[VoidPointer|`void *`]] to a concrete pointer type so it can be [[DereferenceOperator|dereferenced]]:

```c
void *args;
int num = *((int *)args);   // recast args to int *, then dereference

int *p = (int *)malloc(sizeof(int) * 10);    // recast malloc return
char *s = (char *)malloc(sizeof(char) * 20);
```

The recast adds a **pointee-type label** the compiler can use for:

1. **[[DereferenceOperator|Dereference]] yield type** — `*((int *)vp)` yields `int`.
2. **Pointer arithmetic stride** — `(int *)vp + 3` advances 12 bytes (3 × `sizeof(int)`); `(char *)vp + 3` advances 3 bytes.
3. **Member access** — `((struct studentT *)vp)->name` resolves the `name` field.

## The double-parens idiom

For the recast-then-dereference pattern, use double parentheses:

```c
*((T *)vp)    // recommended — explicit binding
```

Both `*((T *)vp)` and `*(T *)vp` parse identically (cast binds tighter than `*`), but the double-parens form makes the binding visible and is the corpus-recommended idiom from [[dis-2-9-3-voidstar|Ch 2.9.3]].

## What casts can do

| Cast | Example | Effect |
|---|---|---|
| **Pointer ↔ pointer** | `(int *)vp` | Reinterpret address as different pointee type — the headline `void *` use |
| **Numeric widening** | `(double)5` | Convert `int` → `double` (`5.0`) — usually implicit, but explicit is documentation |
| **Numeric narrowing** | `(int)3.7` | `double` → `int` (`3`) — truncation toward zero, not rounding |
| **Drop `const`** | `(char *)const_str` | Strip [[ConstQualifier|`const`]] qualifier — *dangerous*; writing through the result is undefined behavior if the original was truly const |

## What casts cannot do

- **Lie to the compiler safely** — `(double *)int_ptr` compiles, but `*(double *)int_ptr` reads 8 bytes from a region holding 4-byte `int`s. Undefined behavior at runtime.
- **Convert struct ↔ struct** — `(struct A)b` is illegal even if A and B have identical layouts; copy field-by-field or use [[Memcpy|`memcpy`]].
- **Cast away type-system violations** — a cast tells the compiler *"trust me"*; if you're wrong, the runtime catches you (or worse, silently corrupts).

## Implicit vs explicit casts

C performs *implicit* conversions in many contexts:

- Numeric: `int x = 3.7;` truncates without a cast (compiler may warn).
- Pointer: `int *p = malloc(sizeof(int));` — `void *` assigns to `int *` without an explicit cast in modern C.
- [[NullPointer|`NULL`]] assigns to any pointer type without a cast.

[[dis-2-9-3-voidstar|Ch 2.9.3]]'s `(int *)malloc(...)` form is **legacy / pedagogical** — the explicit cast makes the type conversion visible. Modern style omits it unless writing C++-compatible code (C++ requires the cast).

## Cast vs conversion vs coercion

Loose vocabulary; the corpus uses:

- **Cast** — the syntactic form `(T)e`.
- **Conversion** — the semantic operation (changing representation, e.g. `int` → `double`).
- **Coercion** — implicit conversion the compiler inserts automatically.

Pointer casts are pure *reinterpretation* — no bits change; only the compile-time type label changes. Numeric casts may rearrange bits (e.g. `int` → `float` rewrites to IEEE 754 form).

## Safety discipline

1. **Cast only when necessary.** Casts disable type-checking; minimize their scope.
2. **Document the why.** A cast in code should answer *"why is this safe?"* — typically with a comment about the upstream guarantee.
3. **Prefer compiler-checked alternatives.** `(int)3.7` → `floor(3.7)` or `(int)round(3.7)` when intent matters. `(char *)str` → fix the const-correctness instead of casting it away.

## Connections

- [[dis-2-9-3-voidstar]] — introducing source.
- [[VoidPointer]] — the headline cast target (`(T *)vp`).
- [[GenericPointer]] — the design pattern casts re-specialize.
- [[Pointer]] / [[PointerType]] — the type system casts navigate.
- [[DereferenceOperator]] — what the recast enables.
- [[Malloc]] — pre-modern code shows the explicit `(int *)malloc(...)` cast.
- [[ConstQualifier]] — casts can strip `const` (a code smell).
- [[CPrimitiveType]] — numeric casts navigate the primitive-type lattice.
- [[CLanguage]] / [[DiveIntoSystems]].
