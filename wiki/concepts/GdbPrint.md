---
title: "GDB `print` (`p`)"
type: concept
tags: [debugging, gdb, c-language, debugging-primitive, expression-evaluation]
sources: [dis-3-1-gdb, dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB `print` (`p`)

The [[GDB]] command that **evaluates an expression in the debuggee's current scope and prints the result**. The workhorse inspection primitive: every variable read, every pointer dereference, every arithmetic check goes through `print`. [[dis-3-1-gdb|DIS Ch 3.1]] introduces it as the *"display variable value"* command; [[dis-3-2-gdb-commands|Ch 3.2]] fans out the format-specifier surface.

## Forms

| Form | Behavior |
|---|---|
| `print expr` / `p expr` | Print `expr` in the default format for its inferred type. |
| `print/x expr` | Print as **hexadecimal** (`print/x 123` → `0x7b`). |
| `print/t expr` | Print as **binary** (`print/t 123` → `1111011`). |
| `print/c expr` | Print as **ASCII character** (`print/c 99` → `'c'`). |
| `print/d expr` | Print as **signed decimal**. |
| `print/u expr` | Print as **unsigned decimal**. |
| `print/o expr` | Print as **octal**. |
| `print/f expr` | Print as **floating-point**. |
| `print *(type *)addr` | **Typed dereference** of a raw address — `print *(int *)0x8ff4bc10` reads 4 bytes at the address as an `int`. |

The format specifier sticks for **one command only** — subsequent bare `print` calls revert to default formatting.

## Scope resolution

`print var` resolves `var` in the **current frame's [[VariableScope|scope]]** — so after [[GdbBacktrace|`frame N`]] switches frames, the same `print x` reads frame `N`'s `x`. This is what makes [[GdbBacktrace|`bt` + `frame N` + `print`]] the canonical *"what did the caller think it was passing me?"* recipe.

## What you can `print`

- **Local variables** (`p i`, `p name`).
- **Function parameters** (`p argc`, `p argv[0]`).
- **Globals** (`p errno`).
- **Struct fields** (`p s.x`, `p s->x`, `p (*p).field`).
- **Array elements** (`p arr[3]`, `p arr[0]@10` — the `@N` artificial-array syntax shows 10 elements).
- **Arbitrary C expressions** (`p i + j * 2`, `p strlen(s)` — yes, GDB will **call functions** in the debuggee).
- **Typed memory at an address** (`p *(struct studentT *)0x7fffffffe1c0`).

## Function calls from `print`

`print func(arg1, arg2)` actually invokes the function inside the running debuggee. Useful for inspecting helper functions, **dangerous** if the function has side effects (mutates state, writes files, allocates memory) — those persist after the print completes.

## Related commands

- [[GdbDisplay|`display`]] — auto-print at every pause (instead of once-per-command).
- [[GdbExamineMemory|`x/nfu`]] — print raw bytes at an address without type interpretation (escape hatch when `print`'s type-awareness is wrong or absent).
- [[GdbWhatis|`whatis expr`]] — report the *type* of `expr` without evaluating it.

## Connections

- [[dis-3-1-gdb]] — introducing source ([[GDB]] workflow narrative).
- [[dis-3-2-gdb-commands]] — the command reference that adds the format-specifier surface.
- [[GDB]] / [[Debugger]] — the host tool.
- [[Breakpoint]] / [[StepDebug]] — the halt mechanisms that make `print` interesting.
- [[GdbBacktrace]] — frame switching that changes which scope `print` resolves in.
- [[GdbDisplay]] / [[GdbExamineMemory]] / [[GdbInfo]] / [[GdbWhatis]] — sibling inspection commands.
- [[VariableScope]] — what determines variable resolution.
- [[StackFrame]] / [[LocalVariable]] / [[FunctionParameter]] — the per-frame state `print` reads.
- [[Pointer]] / [[DereferenceOperator]] — the C semantics `print *p` exposes.
