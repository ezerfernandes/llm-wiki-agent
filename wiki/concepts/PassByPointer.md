---
title: "Pass-by-Pointer (C)"
type: concept
tags: [c-language, pointers, functions, parameter-passing]
sources: [dis-2-2-pointers, dis-2-3-pointers-functions]
last_updated: 2026-05-17
---

# Pass-by-Pointer (C)

**Pass-by-pointer** is the [[CLanguage|C]] idiom for letting a [[Function|function]] mutate its caller's storage: the caller passes the **[[CMemoryAddress|address]]** of a variable (via [[AddressOfOperator|`&`]]), and the callee writes through that address (via [[DereferenceOperator|`*`]]). Per [[dis-2-2-pointers|DIS Ch 2.2]], this is the first of the five use cases pointers enable: *"implement functions whose parameters can modify values in the caller's stack frame."* [[dis-2-3-pointers-functions|DIS Ch 2.3]] then operationalizes the idiom as the entire subject of its section, distilling it to a three-step recipe ([[PointerDeclaration|pointer-typed parameter]] → [[AddressOfOperator|`&`]]-of-variable at call site → [[DereferenceOperator|`*`]]-deref in body) and walking a complete worked example.

It is the workaround [[dis-1-4-functions|Ch 1.4]] could not yet supply — and the resolution of the [[PassByValue|pass-by-value]] vs. [[PassByReference|pass-by-reference]] tension introduced by [[dis-1-5-arrays-strings|Ch 1.5]].

## The pattern

```c
/* output parameter via pass-by-pointer */
void set_to_42(int *out) {
    *out = 42;          /* writes through the pointer to caller's storage */
}

int main(void) {
    int x = 0;
    set_to_42(&x);      /* pass x's ADDRESS */
    /* x is now 42 */
    return 0;
}
```

The mechanism: the *pointer* `&x` is passed by value (per [[dis-1-4-functions|Ch 1.4]]'s blanket rule, still intact), but because the pointer value addresses the caller's storage, [[DereferenceOperator|dereferencing]] it inside the callee reaches and may mutate the caller's variable.

## Reconciling the Ch 1.4 / Ch 1.5 tension

| Chapter | Rule | Resolution in Ch 2.2 |
|---|---|---|
| [[dis-1-4-functions|Ch 1.4]] | *"C is pass-by-value"* | Still true — but the value passed can be a pointer |
| [[dis-1-5-arrays-strings|Ch 1.5]] | *"Arrays pass by reference"* | Arrays decay to a pointer to their first element; the **pointer** is passed by value |
| [[dis-2-2-pointers|Ch 2.2]] | Pass-by-pointer | Explicit version: pass `&x`, deref `*p` inside callee |

The pithy summary: **C is always pass-by-value; pass-by-reference is just pass-by-value of a pointer.**

## Ch 2.3's worked example: `change_value`

[[dis-2-3-pointers-functions|Ch 2.3]] supplies the canonical worked example — the simplest function that exercises both return channels at once:

```c
int change_value(int *input) {
    int val = *input;            /* READ through pointer parameter */
    if (val < 100) {
        *input = 100;            /* WRITE through pointer parameter */
    } else {
        *input = val * 2;
    }
    return val;                  /* primary return: original value */
}

int main(void) {
    int x = 30, y;
    y = change_value(&x);              /* pass address of x */
    printf("x: %d y: %d\n", x, y);     /* x: 100 y: 30 */
}
```

The output `x: 100 y: 30` makes the **two output channels** simultaneously visible: `y` receives the original `30` via the [[ReturnStatement|`return`]] slot; `x` receives the new `100` via the pass-by-pointer back-channel. The chapter's [[StackFrame|stack-frame]] diagram (Figure 1) shows `change_value`'s frame containing the local `input` *holding the [[CMemoryAddress|address]] of `main`'s `x`* — the arrow that crosses frames is what makes pass-by-pointer work.

The Ch 2.3 precision-restatement of the rule: *"In the pass-by-pointer pattern, the parameter still gets the value of its argument, but it is passed the value of an address. … by dereferencing a pointer parameter, the function can change the contents of memory that both the parameter and its argument refer to."* The pass-by-pointer mechanism *upholds* [[PassByValue|pass-by-value]] — the pointer is what's copied — and caller-visible mutation is the *consequence* of dereferencing the copied [[CMemoryAddress|address]].

## Three idiomatic uses

1. **Output parameters / multiple returns.** A [[Function|function]] returns at most one value via [[ReturnStatement|`return`]]; pointer parameters provide *additional* output slots:
   ```c
   void divmod(int a, int b, int *quot, int *rem) {
       *quot = a / b;
       *rem  = a % b;
   }
   ```

2. **In-place mutation of caller's variable.** The canonical `swap`:
   ```c
   void swap(int *a, int *b) {
       int tmp = *a;
       *a = *b;
       *b = tmp;
   }
   /* call: swap(&x, &y); */
   ```

3. **Efficient large-struct passing.** Pass one [[CMemoryAddress|address]] instead of [[StructAssignment|copying]] a 76-byte [[CStruct|struct]] per [[dis-1-6-structs|Ch 1.6]]:
   ```c
   void print_student(struct studentT *s) {
       printf("%s, age %d\n", s->name, s->age);
   }
   /* call: print_student(&alice); */
   ```
   Bonus: the callee can read *or* mutate; if read-only intent matters, add `const`: `const struct studentT *s`.

## Safety obligations

The caller and callee share the [[Pointer|pointer]] safety contract:

- **Caller:** must pass a valid address — `&x` of a live variable, or a freshly [[Malloc|`malloc`]]'d block, or [[NullPointer|`NULL`]] (if the callee documents NULL-handling).
- **Callee:** must check for [[NullPointer|`NULL`]] before [[DereferenceOperator|dereferencing]] (defensive), or document that NULL is not accepted (preconditioned).

The defensive callee:

```c
void set_to_42(int *out) {
    if (out != NULL) {
        *out = 42;
    }
}
```

## Pass-by-pointer vs. return value

When does the chapter recommend pass-by-pointer over [[ReturnStatement|return value]]?

| Situation | Use |
|---|---|
| Function produces one small value | [[ReturnStatement|`return`]] |
| Function produces a large [[CStruct|struct]] | Pointer parameter (avoid copy) |
| Function produces *multiple* values | Pointer parameters for the extras |
| Function mutates an existing object | Pointer parameter |
| Function may fail / produce no value | Return a [[Pointer|pointer]] that may be [[NullPointer|`NULL`]] |

## What this page doesn't cover (yet)

- **Pointer arithmetic in pass-by-pointer** (e.g. iterating an array parameter) — deferred to Ch 2.3.
- **Pointer-to-pointer parameters** (`int **`) — for letting the callee reassign a caller-side pointer (e.g. `void allocate(int **p)`).
- **`const`-qualified pointer parameters** — the read-only-promise version.

## Connections

- [[CLanguage]] — the language.
- [[Pointer]] — the value type passed.
- [[AddressOfOperator]] — produces the value to pass.
- [[DereferenceOperator]] — accesses the caller's storage inside the callee.
- [[PassByValue]] — the rule pass-by-pointer respects (the *pointer* is what's passed by value).
- [[PassByReference]] — what pass-by-pointer simulates at the semantic level.
- [[FunctionParameter]] — the slot a pointer parameter fills.
- [[NullPointer]] — the *no-address* value a defensive callee must guard against.
- [[CStruct]] — the canonical *pass-pointer-not-copy* use case.
- [[StructAssignment]] — the [[dis-1-6-structs|Ch 1.6]] mechanism pass-by-pointer avoids.
- [[ArrowOperator]] — the readable struct-member access through a pointer parameter.
- [[OutputParameter]] — the named convention specialization: pass-by-pointer used purely to deliver an additional return value.
- [[dis-2-2-pointers]] — defining source; introduces pass-by-pointer as one of five [[Pointer|pointer]] use cases.
- [[dis-2-3-pointers-functions]] — operationalizing source; takes pass-by-pointer as the entire subject of its section with the worked `change_value` example.
- [[dis-1-4-functions]] — the [[PassByValue|pass-by-value]] rule pass-by-pointer accommodates.
- [[dis-1-5-arrays-strings]] — the [[PassByReference|pass-by-reference]] story pass-by-pointer explains.
- [[dis-1-6-structs]] — the [[StructAssignment|whole-record copy]] cost pass-by-pointer side-steps.
