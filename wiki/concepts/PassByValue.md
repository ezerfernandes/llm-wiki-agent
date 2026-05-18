---
title: "Pass-by-Value"
type: concept
tags: [c-language, functions, semantics, calling-convention]
sources: [dis-1-4-functions, dis-2-3-pointers-functions]
last_updated: 2026-05-17
---

# Pass-by-Value

**Pass-by-value** is the parameter-passing discipline used by [[CLanguage|C]]: at every [[FunctionCall|function call]], each [[FunctionParameter|parameter]] is *initialized to the value of the corresponding [[FunctionArgument|argument]]*. The parameter is, semantically, a fresh [[LocalVariable|local variable]] in the called function's [[StackFrame|stack frame]].

[[dis-2-3-pointers-functions|DIS Ch 2.3]] re-states the rule with surgical precision in the context of [[PassByPointer|pass-by-pointer]]: *"All arguments in C are passed by value and follow pass-by-value semantics: the parameter gets a copy of its argument value, and modifying the parameter's value does not change its argument's value."* The same rule applies when the value being copied is an [[CMemoryAddress|address]] — the [[Pointer|pointer]] parameter still receives a *copy*, and rewiring it (`p = &something_else;`) is local-only. What [[DereferenceOperator|dereference]] (`*p = value;`) reaches is the caller's storage only because the *copied address* still resolves there — the pass-by-value mechanism is not violated.

> "Arguments to C functions are **passed by value**: each function parameter is assigned the value of the corresponding argument passed to it in the function call by the caller." — [[dis-1-4-functions|DIS Ch 1.4]]

## The headline consequence

> "Any change to a parameter's value in the function (that is, assigning a parameter a new value in the function) is **not visible** to the caller." — [[dis-1-4-functions|DIS Ch 1.4]]

```c
void try_to_change(int n) {
    n = 42;       /* assigns the local copy */
}

int main(void) {
    int x = 5;
    try_to_change(x);
    /* x is still 5 */
}
```

The function received a *copy* of `x`'s value into its parameter `n`; assignments to `n` touch only the called function's [[StackFrame|frame]]. The caller's `x` is untouched.

## Why this matters

- **Predictability.** Function calls cannot silently mutate caller variables — the *only* effect of a call (absent globals / I/O) is its returned value.
- **Motivation for pointers.** True output-parameter semantics in [[CLanguage|C]] require explicit address passing — the caller passes `&x`, the callee dereferences. This is the central motivation for the *pointer* chapter that follows [[dis-1-4-functions|Ch 1.4]] in [[DiveIntoSystems]].
- **Contrast with reference-passing languages.** Java/Python *object* arguments behave like pass-by-value of a *reference*, so callee mutations to object fields *are* visible; C has no such layer — what you copy is exactly what the caller had.

## What's actually copied

For [[CPrimitiveType|primitive types]] it's the bit pattern. For aggregates (arrays, structs) the rules differ — arrays decay to pointers and structs are copied wholesale — but these are later-chapter topics; for Ch 1.4's `int` parameters, *the integer value* is what's copied.

## Connections

- [[dis-1-4-functions]] — introducing source (the *headline* rule of the chapter).
- [[dis-2-3-pointers-functions]] — the surgical re-statement of the rule for pass-by-pointer contexts (*"the parameter still gets the value of its argument, but it is passed the value of an address"*).
- [[PassByPointer]] — the [[CLanguage|C]] idiom that *upholds* pass-by-value while producing caller-visible mutation through [[DereferenceOperator|dereference]] of a copied [[CMemoryAddress|address]].
- [[OutputParameter]] — the named convention built on pass-by-pointer.
- [[Function]] / [[FunctionParameter]] / [[FunctionArgument]] — the participants.
- [[FunctionCall]] / [[StackFrame]] — where the copy lives.
- [[LocalVariable]] — what a parameter *behaves as* under pass-by-value.
- [[ReturnStatement]] — the only built-in way out (the other direction).
- [[CLanguage]] / [[DiveIntoSystems]].
- [[Python]] — contrast: object references are passed by value of the reference, so mutations to mutable objects *are* visible.
