---
title: "GDB `whatis` (Type Query)"
type: concept
tags: [debugging, gdb, c-language, debugging-primitive, type-inspection]
sources: [dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB `whatis` (Type Query)

The [[GDB]] command that **reports the static type of an expression without evaluating it**. Useful when [[CompilerOptimization|optimization]], [[Typedef|typedef]], implicit conversion, or pointer indirection has obscured what a sub-expression actually is.

## Syntax

```text
whatis <expr>
```

[[dis-3-2-gdb-commands|Ch 3.2]] example: `whatis (x + 3.4)` → `type = double` — confirming that the integer + floating-point sum is **promoted to `double`** (the [[CTypePromotion|usual arithmetic conversions]]).

## What `whatis` reports

| Input | Output |
|---|---|
| `whatis x` (where `x` is `int`) | `type = int` |
| `whatis (x + 3.4)` | `type = double` |
| `whatis p` (where `p` is `int *`) | `type = int *` |
| `whatis *p` | `type = int` |
| `whatis func` | `type = int (int, char *)` (function signature) |
| `whatis my_struct.field` | the field's type |
| `whatis my_typedef_name` | `type = my_typedef_name` (does **not** chase typedefs) |

For typedef chasing, GDB also offers `ptype` — `ptype` resolves typedefs and prints struct/union member layouts, while `whatis` stops at the first level.

## Use cases

- **Implicit promotion debugging** — confirming that `i / 2.0` is `double`, not `int`.
- **Pointer-type confirmation** — `whatis ptr` to check what `ptr` actually points at before doing a [[TypeCast|cast]].
- **Function signature lookup** — `whatis printf` reports its prototype without opening `<stdio.h>`.
- **Macro expansion sanity check** — when `-g3` ([[GccDashG]]) embedded macro info, `whatis` after `macro expand` shows the expanded type.

## `whatis` vs `ptype`

- **`whatis expr`** — one-level type, fast, no struct expansion.
- **`ptype expr`** — full type, chases typedefs, expands struct members with their offsets and types.

```text
(gdb) whatis s
type = studentT
(gdb) ptype s
type = struct studentT {
    char name[64];
    int age;
    double gpa;
}
```

For deep struct inspection use `ptype`; for quick *"what type is this expression?"* use `whatis`.

## Connections

- [[dis-3-2-gdb-commands]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool.
- [[GdbPrint]] — the *value* sibling; `whatis` is the *type* slice.
- [[GdbInfo]] — `info types` lists all known types.
- [[Typedef]] / [[CTypePromotion]] — the language features `whatis` clarifies.
- [[TypeCast]] / [[VoidPointer]] — what `whatis` helps you choose correctly.
- [[DebugSymbol]] — type info source ([[GccDashG|`gcc -g`]] embeds it).
