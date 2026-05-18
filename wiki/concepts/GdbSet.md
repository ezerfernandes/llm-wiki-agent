---
title: "GDB `set` (Live Variable Mutation)"
type: concept
tags: [debugging, gdb, debugging-primitive, mutation]
sources: [dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB `set` (Live Variable Mutation)

The [[GDB]] command that **rewrites a variable in the running debuggee without recompiling**. Where [[GdbPrint|`print`]] *reads* state and [[GdbDisplay|`display`]] *watches* state, `set` *writes* state — the debugger's mutation primitive.

## Syntax

```text
set var <name> = <expr>
set <name> = <expr>          # often works without the literal "var" keyword
```

[[dis-3-2-gdb-commands|Ch 3.2]] example: `set x = 123 * y` — overwrites `x` in the current [[StackFrame|frame]] with the value of `123 * y`. The right-hand side is evaluated in the same scope as [[GdbPrint|`print`]] — so locals, parameters, globals, struct fields, and arbitrary C expressions all work.

## What you can `set`

- **Locals**: `set i = 0` — rewind a loop counter.
- **Parameters**: `set argc = 3` — pretend a different argument count.
- **Globals**: `set errno = 0` — clear an error state.
- **Struct fields**: `set s.x = 42` / `set p->x = 42`.
- **Array elements**: `set arr[3] = 99`.
- **Memory at an address**: `set *(int *)0x7fffffffe1c0 = 0xdeadbeef`.
- **Registers**: `set $rax = 0` — directly write a CPU register (architecture-specific).

## The two `set` namespaces

GDB overloads `set` for both **debuggee mutation** (above) and **debugger configuration** (`set pagination off`, `set print elements 200`, `set logging on`). The disambiguator is the `var` keyword:

- `set var x = 5` — definitely debuggee mutation.
- `set pagination off` — definitely debugger config.
- `set x = 5` — ambiguous; GDB usually picks debuggee mutation if `x` is a known variable.

## Use cases

- **Patch-around-the-bug** — when you've identified a bug but don't want to recompile, `set` past the bad assignment and let execution continue.
- **Recovery from input errors** — `set name = "alice"` after [[Scanf|`scanf`]] failed to read it correctly.
- **What-if exploration** — try a different value and see what downstream code does.
- **Manual loop unrolling for debugging** — `set i = 1000` to skip to a specific iteration without `condition`/`ignore`.

## Caveats

- Mutations are **session-only** — the executable on disk is unchanged.
- Mutations can violate invariants the [[CCompiler|compiler]] assumed (especially under [[CompilerOptimization|optimization]] — caches in registers may not see the write).
- `set` over [[ConstQualifier|`const`]] memory is undefined; on systems where `const` data sits in read-only pages, it may segfault.

## Connections

- [[dis-3-2-gdb-commands]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool.
- [[GdbPrint]] / [[GdbDisplay]] / [[GdbExamineMemory]] — sibling inspection commands; `set` is the *write* slice, they are the *read* slice.
- [[VariableScope]] — what determines variable resolution.
- [[CompilerOptimization]] — the orthogonal axis that can defeat `set` (register-cached values).
- [[Pointer]] / [[DereferenceOperator]] — what `set *(type *)addr = expr` exercises.
