---
title: "GDB `x` (Examine Memory)"
type: concept
tags: [debugging, gdb, memory-inspection, c-language, low-level]
sources: [dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB `x` (Examine Memory)

The [[GDB]] **raw-memory inspection** primitive — *examine* `n` units of memory at a given address, formatted as the user requests. The escape hatch when [[GdbPrint|`print`]]'s type awareness is wrong, absent, or in the way: `x` reads bytes by address and renders them in whatever shape the user specifies.

## Syntax

```text
x/nfu address
```

Three modifiers control what `x` shows:

| Modifier | Role | Values |
|---|---|---|
| `n` | **repeat count** — how many units to display | integer (`1` if omitted) |
| `f` | **format** — how to render each unit | `d` decimal / `u` unsigned / `x` hex / `o` octal / `t` binary / `c` char / `s` null-terminated string / `i` instruction / `f` float / `a` address |
| `u` | **unit size** — bytes per unit | `b` byte / `h` halfword (2 B) / `w` word (4 B) / `g` giant (8 B) |

[[dis-3-2-gdb-commands|Ch 3.2]] worked examples:

| Command | Effect |
|---|---|
| `x/d ptr` | Print one decimal int at `ptr`. |
| `x/4c s1` | Show first 4 characters of string `s1`. |
| `x/s s1` | Display as null-terminated string. |
| `x/8d s1` | Show 8 ASCII byte values as decimal. |
| `x/16xb ptr` | Hex-dump 16 bytes starting at `ptr`. |
| `x/4wd &arr[0]` | 4 decimal words from the start of `arr`. |
| `x/i $pc` | Disassemble the instruction at the current program counter. |

## Address-of vs. value

`x` takes an **address**, not a variable name. Equivalent forms:

```text
x/d ptr             # ptr already holds an address
x/d &x              # take address of x
x/d 0x7fffffffe1c0  # literal address
```

Bare `x x_variable_name` treats the *value* of `x_variable_name` as the address — usually not what you want for non-pointer variables.

## When to reach for `x` over `print`

- **No type information** — debugging stripped binaries / raw memory regions / [[CoreFile|core dumps]] without symbols.
- **`void *` or wrong type** — when [[GdbPrint|`print`]] would print as the wrong type and you want byte-level truth.
- **[[Pointer|Pointer]] traversal** — walking a [[LinkedList|linked list]] or [[CArray|array]] via address arithmetic.
- **Instruction-level debugging** — `x/10i $pc` shows the next 10 machine instructions, the disassembly view.
- **Register-pointed memory** — `x/wx $rsp` shows the top of the [[ExecutionStack|stack]].

## Repeating

After the first `x/nfu addr`, bare `x` re-uses the same `n` / `f` / `u` and advances the address — letting you scroll through a memory region one screen at a time.

## Connections

- [[dis-3-2-gdb-commands]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool.
- [[GdbPrint]] — the typed sibling; `x` is the byte-level fallback.
- [[GdbInfo]] — `info registers` complements `x` for CPU-state inspection.
- [[Pointer]] / [[CMemoryAddress]] — what `x`'s address argument is.
- [[CArray]] / [[CString]] / [[NullTerminator]] — `x/s` and `x/Nc` show C-string layout directly.
- [[ProcessMemory]] / [[StackSection]] / [[HeapSection]] — the memory regions `x` reads from.
- [[Objdump]] — the offline disassembler; `x/i $pc` is the live equivalent.
