---
title: "const Type Qualifier (C)"
type: concept
tags: [c-language, const, type-qualifier, constant]
sources: [dis-2-9-1-advanced-switch]
last_updated: 2026-05-17
---

# `const` Type Qualifier (C)

The **`const`** keyword is the [[CLanguage|C]] **type qualifier** that marks a variable as read-only after initialization. Unlike a [[CConstant|`#define`]] preprocessor substitution, a `const` variable has **storage**, a **type**, and a **scope** — it is a real variable the [[CCompiler|compiler]] type-checks and the linker can place in a read-only segment.

```c
const int N = 20;
const double PI = 3.14159;
const char *msg = "hello";  // pointer to const char
```

Attempting `N = 50;` after declaration is a **compile error**: *"assignment of read-only variable 'N'"*.

## `const` vs [[CConstant|`#define`]] — the three-axis split

[[dis-2-9-1-advanced-switch|DiS Ch 2.9.1]] frames constants primarily through [[CConstant|`#define`]] but the `const` qualifier is the typed alternative C codebases increasingly prefer:

| Axis | `#define N (20)` | `const int N = 20;` |
|---|---|---|
| **Mechanism** | Preprocessor textual substitution | Compiler-allocated read-only variable |
| **Type** | None (raw substitution) | `int` (type-checked) |
| **Scope** | File-global from `#define` line | Block / file / function (normal C scoping) |
| **Debugger** | Symbol gone after preprocessing | Visible by name |
| **Storage** | None — inlined literal | Variable storage (often optimized to a literal anyway) |
| **Address-of** | `&N` is meaningless | `&N` is a valid `const int *` |

## Pointer-related forms

`const` can qualify either the pointee or the pointer (or both):

```c
const int *p;       // p is mutable; *p is const-int (cannot modify pointee through p)
int *const p;       // p is const-pointer; *p is mutable
const int *const p; // both const
```

Read these right-to-left from the variable name. The `const int *` form is the canonical signature for read-only function parameters — `size_t strlen(const char *s)`.

## When to prefer `const` over [[CConstant|`#define`]]

- The value has a **specific type** that should be enforced at usage sites.
- You want the symbol visible to a **debugger**.
- You want the constant **scoped** (block-local, file-local) rather than file-global from the `#define` line.

## When [[CConstant|`#define`]] still wins

- The constant is used in [[SwitchStatement|`switch` case labels]] (a `const int` is not a [[CaseLabel|compile-time constant expression]] in standard C, though some compilers accept it as an extension).
- The constant is a [[CompositeMacro|composite token expansion]] — e.g., function-like macros `#define MAX(a, b) ((a) > (b) ? (a) : (b))`.
- The constant must work in array-size declarations at file scope: `int buf[N];` requires `N` be a [[CConstant|`#define`]] or [[CEnum|`enum`]] constant, not a `const int`.

## Connections

- [[dis-2-9-1-advanced-switch]] — source.
- [[CConstant]] — the `#define` alternative — preprocessor substitution.
- [[CEnum]] — the `enum` alternative — typed integer constants only.
- [[CompilationProcess]] — `const` is enforced by the compiler proper, not the preprocessor.
- [[LValue]] — `const` makes a variable a *non-modifiable* lvalue.
- [[CLanguage]] / [[DiveIntoSystems]].
