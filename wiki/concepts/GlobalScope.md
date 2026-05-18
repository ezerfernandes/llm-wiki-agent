---
title: "Global Scope (C)"
type: concept
tags: [c-language, scope, globals, semantics]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Global Scope (C)

**Global scope** is the [[VariableScope|scope]] class for [[GlobalVariable|global variables]] in [[CLanguage|C]] — variables [[VariableDeclaration|declared]] *outside* any function body. Per [[dis-2-1-scope-memory|DIS Ch 2.1]]:

> "Global variables remain permanently in scope and can be used by any code in the program."

Two load-bearing properties: **(1) any function can name the variable** (no parameter passing required) and **(2) the binding never goes out of scope** for the program's lifetime.

## Implementation

A globally-scoped variable lives in the [[DataSection|data section]] of [[ProcessMemory|program memory]]. The compiler emits a single fixed address; every reference to the name across the whole compilation unit resolves to that one address. There is no per-call allocation, no frame, no push/pop — just one slot for one variable, alive from load to exit.

## Contrast with function scope

| Property | [[GlobalScope]] | [[FunctionScope]] |
|---|---|---|
| **Where declared** | Outside any function | Inside a function |
| **Where in memory** | [[DataSection]] | [[StackSection]] / per-[[StackFrame|frame]] |
| **Reachable from** | Any function | Only the enclosing function |
| **Lifetime** | Program lifetime | Call lifetime |
| **Recursion-friendly** | No — single slot | Yes — fresh slot per call |

## Why Ch 2.1 introduces it carefully

The chapter pairs the definition with a **style rule** — *"avoid programming with global variables whenever possible"* — and immediately explains why: globals make cross-function communication implicit, defeating modularity and making bugs hard to localize. The chapter's worked `g_x` example exists to *demonstrate* global scope, not to *recommend* its use; the next chapter section's [[Pointer|pointers]] and [[ReturnStatement|return values]] supply the *alternatives*.

## Connections

- [[dis-2-1-scope-memory]] — introducing source.
- [[VariableScope]] — the umbrella scope concept.
- [[FunctionScope]] — the contrasting scope class.
- [[GlobalVariable]] — the variable class governed by this scope.
- [[DataSection]] — the memory region that backs global-scope storage.
- [[ProcessMemory]] — the four-region picture.
- [[CLanguage]] / [[DiveIntoSystems]].
