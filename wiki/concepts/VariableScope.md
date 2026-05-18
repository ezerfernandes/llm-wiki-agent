---
title: "Variable Scope (C)"
type: concept
tags: [c-language, scope, semantics, variables]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Variable Scope (C)

A variable's **scope** is the set of program code in which the variable's name has meaning. Per [[dis-2-1-scope-memory|DIS Ch 2.1]]:

> "A variable's **scope** defines when its name has meaning. In other words, scope defines the set of program code blocks in which a variable is bound to (associated with) a program memory location."

This is the corpus's **first formal definition of scope**. [[dis-1-4-functions|Ch 1.4]] used the term [[FunctionScope|function scope]] *operationally* (only the top [[StackFrame|frame]] is "in scope"); Ch 2.1 supplies the underlying language-level definition that [[FunctionScope]] and [[GlobalScope]] are both instances of.

## The two scope classes Ch 2.1 introduces

| Scope class | Where declared | Where in memory | Lifetime |
|---|---|---|---|
| **[[GlobalScope]]** | Outside any function body | [[DataSection]] | Program lifetime |
| **[[FunctionScope]]** (local + parameters) | Inside a function body | [[StackSection]] (per [[StackFrame|frame]]) | Per call |

Ch 2.1 stops here — it does **not** discuss [[BlockScope|block scope]] (the C scope rule that `{ }` blocks create scopes too), [[FileScope|file scope]] (the `static`-at-global-level case), or function-prototype scope. Those are deferred to later sections.

## Scope vs. lifetime

[[dis-2-1-scope-memory|Ch 2.1]] treats scope and lifetime as **coupled** in the two cases it introduces:

- A [[GlobalVariable|global]] has [[GlobalScope|global scope]] (any code can name it) **and** program lifetime (its [[DataSection|data-section]] storage is allocated at load and persists to exit).
- A [[LocalVariable|local]] has [[FunctionScope|function scope]] (only its enclosing function can name it) **and** call lifetime (its [[StackFrame|frame]] is pushed on call, popped on return).

These two attributes can be *decoupled* — that's exactly what `static` does (function scope, program lifetime) — but Ch 2.1 deliberately defers that complication.

## Same name, different scopes

The chapter's worked example declares `int val` in **three** different functions (`main`, `change_global`, `max`). All three are *different variables* — same identifier, different bindings, different storage. This is the operational consequence of [[FunctionScope|function scope]]: names are scoped to the function, so name collisions across functions are not collisions at all.

## Connections

- [[dis-2-1-scope-memory]] — introducing source (and the first formal scope definition).
- [[dis-1-4-functions]] — Ch 1.4; introduced [[FunctionScope|function scope]] operationally.
- [[GlobalScope]] — the scope class for [[GlobalVariable|globals]].
- [[FunctionScope]] — the scope class for [[LocalVariable|locals]] and [[FunctionParameter|parameters]].
- [[GlobalVariable]] / [[LocalVariable]] / [[FunctionParameter]] — what scope governs.
- [[VariableDeclaration]] — declaration is what *creates* a binding in a scope.
- [[ProcessMemory]] — the *where in memory* that scope ties to.
- [[CLanguage]] / [[DiveIntoSystems]].
