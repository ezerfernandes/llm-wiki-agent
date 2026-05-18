---
title: "return Statement (C)"
type: concept
tags: [c-language, functions, control-flow]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# return Statement (C)

The **`return` statement** ends the current [[Function|function]]'s execution and yields a value of the function's [[ReturnType|declared return type]] back to its [[FunctionCall|caller]].

```c
return <expression>;   /* for non-void functions */
return;                /* for void functions */
```

Encountering `return` (or falling off the end of a [[VoidType|`void`]] function) pops the current [[StackFrame|stack frame]] from the [[ExecutionStack|execution stack]] and resumes the caller's frame — the *pop* half of the call/return discipline.

## Example from [[dis-1-4-functions|DIS Ch 1.4]]

```c
int max(int n1, int n2) {
    int result;

    result = n1;
    if (n2 > n1) {
        result = n2;
    }

    return result;
}
```

The `return result;` yields the `int` value held in [[LocalVariable|local variable]] `result` to the caller, which received it as e.g. `larger = max(x, y);`.

## In `void` functions

A `void` function may omit `return` entirely (control simply falls off the closing `}`) or write a bare `return;` for an early exit:

```c
void print_table(int start, int stop) {
    if (start > stop) return;  /* early exit */
    /* ... */
}
```

## In [[MainFunction|`main`]]

`return 0;` from [[MainFunction|`main`]] becomes the process's [[ExitStatus|exit status]] — the canonical *"ran to completion"* signal to the [[OperatingSystem|OS]].

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] / [[ReturnType]] / [[VoidType]] — what return yields and from what.
- [[FunctionCall]] / [[StackFrame]] / [[ExecutionStack]] — `return` pops the frame.
- [[MainFunction]] / [[ExitStatus]] — the `return 0;`-becomes-exit-status special case.
- [[ControlFlow]] — `return` is a non-local jump out of the current function.
- [[CLanguage]] / [[DiveIntoSystems]].
