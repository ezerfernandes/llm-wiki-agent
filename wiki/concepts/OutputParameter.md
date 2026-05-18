---
title: "Output Parameter (C)"
type: concept
tags: [c-language, pointers, functions, parameter-passing, idiom]
sources: [dis-2-3-pointers-functions]
last_updated: 2026-05-17
---

# Output Parameter (C)

An **output parameter** in [[CLanguage|C]] is a [[FunctionParameter|function parameter]] whose purpose is to deliver a value *out* of the function back to the caller — the opposite of an input parameter, which carries a value *into* the function. Because [[CLanguage|C]] is strictly [[PassByValue|pass-by-value]] and every [[Function|function]] has only **one** [[ReturnStatement|`return`]] slot, an output parameter is implemented as a [[Pointer|pointer]] parameter: the caller passes the [[AddressOfOperator|address]] of a destination variable, the callee [[DereferenceOperator|dereferences]] the pointer and writes to that destination. Per [[dis-2-3-pointers-functions|DIS Ch 2.3]]: *"Pointer parameters provide a mechanism through which functions can modify argument values."*

The output-parameter idiom is the **named [[CLanguage|C]] convention** that operationalizes [[PassByPointer|pass-by-pointer]] for one specific purpose: producing values, not mutating existing data.

## Why output parameters exist

[[CLanguage|C]] [[Function|functions]] have a structural restriction: exactly one value flows out through [[ReturnStatement|`return`]]. Real-world functions frequently want to produce more — quotient *and* remainder, parsed value *and* success flag, located record *and* insertion point, computed result *and* error code. Output parameters are the [[CLanguage|C]] workaround:

| Function need | One return value? | Output parameter pattern |
|---|---|---|
| Integer division → quotient + remainder | No | `void divmod(int a, int b, int *q, int *r)` |
| String parse → value + status | No | `int parse_int(const char *s, int *out)` (returns status, writes value) |
| Lookup → record + found-flag | No | `int lookup(Key k, Record *out)` |
| Pure computation → one scalar | Yes | Use [[ReturnStatement|`return`]]; no output parameter needed |

The recipe is the [[dis-2-3-pointers-functions|Ch 2.3]] three-step:

1. **Declare** a [[Pointer|pointer]]-typed parameter — `int *out`.
2. **Caller** passes the [[AddressOfOperator|address]] of a destination — `parse_int("42", &n)`.
3. **Callee** [[DereferenceOperator|dereferences]] to write — `*out = parsed_value;`.

## The canonical worked example

The [[dis-2-3-pointers-functions|Ch 2.3]] `change_value` function — the simplest possible demonstration:

```c
int change_value(int *input) {
    int val = *input;       /* READ through pointer parameter */
    if (val < 100) {
        *input = 100;       /* WRITE through pointer parameter — output */
    } else {
        *input = val * 2;
    }
    return val;             /* primary return: original value */
}

int main(void) {
    int x = 30, y;
    y = change_value(&x);                  /* pass address of x */
    printf("x: %d y: %d\n", x, y);         /* x: 100 y: 30 */
}
```

The single call yields **two outputs**: `y` receives `30` through the [[ReturnStatement|`return`]] slot; `x` receives `100` through the pass-by-pointer back-channel. Both return paths are simultaneously usable from one function — this is what output parameters give you.

## Output parameter vs. in-place mutation

[[PassByPointer|Pass-by-pointer]] supports two distinct intents — output parameter and in-place mutation — and the same syntax serves both. The convention is *semantic*:

| Intent | Caller setup | Callee behavior | Example |
|---|---|---|---|
| **Output parameter** | Variable need not be initialized | Function *writes only*; doesn't read the destination first | `parse_int(s, &n)` — `n` need not be initialized |
| **In-place mutation** | Variable must be initialized to a meaningful value | Function reads, modifies, writes back | `increment(&counter)` — `counter` must hold valid count |

The `change_value` example mixes both: it reads `*input` (in-place style) and then writes to it (output style). Real code typically commits to one intent.

## Multiple return values

The natural extension of one output parameter is **several** — multiple pointer parameters give the function as many output slots as needed:

```c
void divmod(int a, int b, int *quot, int *rem) {
    *quot = a / b;
    *rem  = a % b;
}

int q, r;
divmod(17, 5, &q, &r);   /* q == 3, r == 2 */
```

Some authors call this *multiple return values* (the function logically returns two values, even though the [[ReturnStatement|`return`]] slot is unused or carries a status code). It is one of the *"five capabilities pointers unlock"* the [[dis-2-2-pointers|Ch 2.2]] page enumerates.

## Convention: error code in `return`, value through output parameter

A widespread [[CLanguage|C]] idiom — used by [[Scanf|`scanf`]], `strtol`, POSIX I/O, and most parsers — is to **reserve the [[ReturnStatement|`return`]] slot for an error/status code** and route the *interesting* value through an output parameter:

```c
/* Returns 0 on success, -1 on failure; writes parsed int to *out on success */
int parse_int(const char *s, int *out) {
    char *end;
    long v = strtol(s, &end, 10);
    if (*end != '\0' || v < INT_MIN || v > INT_MAX) {
        return -1;
    }
    *out = (int)v;
    return 0;
}

int n;
if (parse_int("42", &n) == 0) {
    /* use n safely */
}
```

This pattern composes cleanly with the [[ShortCircuitEvaluation|short-circuit]] `if (ok && *out > 0) { ... }` idiom — a structural alternative to languages that throw exceptions.

## Pre- and post-conditions

The output-parameter contract has obligations on **both sides**:

- **Caller obligations**: pass the [[AddressOfOperator|address]] of a destination variable of the matching type; the variable need not be initialized (the function will write to it on success).
- **Callee obligations**: write to `*out` on the documented success path; if the function may fail, document whether `*out` is touched on failure (best practice: leave untouched, so the caller's variable retains its prior value).
- **Both**: guard for [[NullPointer|`NULL`]] if the function's contract permits a missing output (`if (out != NULL) *out = value;` is the defensive form).

The [[NullPointer|`NULL`]] convention often serves as **"caller doesn't want this output"** — e.g. `divmod(17, 5, &q, NULL)` if the remainder is uninteresting; the callee then writes the quotient and skips the remainder write.

## Cross-walk

| Language | Mechanism | Note |
|---|---|---|
| [[CLanguage|C]] | Pointer parameter + `&x` at call | This page. |
| C++ | Reference parameter (`int& out`) or pointer parameter | References avoid the `&x`/`*p` syntax tax. |
| C# | `out` / `ref` parameter modifiers | Compiler-checked: `out` requires assignment before return. |
| Go | Multiple return values: `func divmod(a, b int) (int, int)` | First-class language feature — no pointer needed. |
| Rust | Return tuple `(i32, i32)` or `Result<T, E>` | Tuple destructuring + `?`-operator carries the same ergonomic load. |
| [[Python]] | Tuple return: `return q, r` | Same as Go conceptually. |

The [[CLanguage|C]] mechanism is the most verbose — but it composes with the [[Pointer|pointer]] toolkit and was the only option available before C++/Java/Rust normalized first-class multi-return.

## Distinction from in-place mutation, struct passing, and array passing

Output parameters share the [[PassByPointer|pass-by-pointer]] mechanism with three sibling idioms:

| Idiom | Intent | Read/write pattern |
|---|---|---|
| **Output parameter** | Produce a *new* value | Write-only on success |
| **In-place mutation** | Modify *existing* state | Read-then-write |
| **Efficient struct passing** | Avoid [[StructAssignment|wholesale copy]] | Read-only (often `const struct T *p`) |
| **Array-as-output** | Fill an array supplied by caller | Write-many (e.g. `void zero(int *a, int n)`) |

Same mechanism, different conventions. The output-parameter convention is the *write-only-on-success* slice of the [[PassByPointer|pass-by-pointer]] space.

## What this page doesn't cover

- **Pointer-to-pointer output parameters** (`int **`) — letting the callee *allocate and hand back* a fresh pointer to the caller (e.g. `int allocate_buffer(int **buf, size_t n)`). Deferred — needs [[DynamicMemoryAllocation|`malloc`]] from [[dis-2-2-pointers|Ch 2.2]]'s deferred Ch 2.4.
- **`const`-qualified pointer parameters** — the read-only-input promise that distinguishes input parameters from output parameters at the type level.

## Connections

- [[CLanguage]] — the language whose single-[[ReturnStatement|`return`]] restriction this idiom routes around.
- [[PassByPointer]] — the underlying mechanism; output parameters are a *use convention* on top of pass-by-pointer.
- [[PassByValue]] — the rule still in force; the *value* being passed is an [[CMemoryAddress|address]].
- [[Pointer]] — the parameter type.
- [[AddressOfOperator]] — produces the value the caller passes (`&n`).
- [[DereferenceOperator]] — accesses the caller's storage inside the callee (`*out = ...;`).
- [[FunctionParameter]] — the slot an output parameter fills.
- [[ReturnStatement]] — the *primary* return channel; output parameters supplement it.
- [[NullPointer]] — used as an "optional output" sentinel (`if (out != NULL) *out = value;`).
- [[CMemoryAddress]] — what an output parameter holds at the type level.
- [[Scanf]] — the [[StandardIOLibrary|`<stdio.h>`]] function whose `&num` argument was the corpus's first sighting of output-parameter syntax — Ch 2.3 finally formalizes the pattern.
- [[dis-2-3-pointers-functions]] — defining source; the [[DiveIntoSystems]] Ch 2.3 section that operationalizes the idiom.
- [[dis-2-2-pointers]] — Ch 2.2; lists output parameters as the first of [[Pointer|pointer]]s' five use cases.
- [[dis-1-4-functions]] — Ch 1.4; single-[[ReturnStatement|`return`]] [[PassByValue|pass-by-value]] [[Function|function]] model that output parameters route around.
- [[dis-1-5-arrays-strings]] — Ch 1.5; [[CArray|array]] parameters are output parameters by another name (array name decays to a [[Pointer|pointer]] to the first element).
- [[dis-1-2-input-output]] — Ch 1.2; [[Scanf|`scanf`]]'s `&num` argument prefigures the output-parameter pattern without yet naming it.
