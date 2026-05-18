---
title: "Global Variable (C)"
type: concept
tags: [c-language, variables, globals, scope, memory]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Global Variable (C)

A **global variable** in [[CLanguage|C]] is a variable [[VariableDeclaration|declared]] *outside* any function body. Per [[dis-2-1-scope-memory|DIS Ch 2.1]]:

> "Declaring a variable outside of any function body creates a **global variable**. Global variables remain permanently in scope and can be used by any code in the program."

Three load-bearing properties:

1. **Declared outside any function** — typically near the top of the source file, *after* `#include` directives and *before* any function definition.
2. **In [[GlobalScope|global scope]]** — every function in the program can read and write it by name; no parameter passing required.
3. **Lives in the [[DataSection|data section]]** — program-lifetime storage, allocated at load, never pushed onto a [[StackFrame|frame]] or [[Free|free]]d.

## Example

```c
#include <stdio.h>

int g_x = 0;                   /* global — outside any function */

void change_global(int val) {
    g_x = val;                 /* read by any function */
}

int max(int n1, int n2) {
    int val;                   /* this val is local, distinct from main's val */
    val = n1;
    if (n2 > n1) val = n2;
    if (g_x > val) val = g_x;  /* global g_x reachable here too */
    return val;
}

int main(void) {
    int val = 5;
    change_global(val);
    /* g_x is now 5 */
    return 0;
}
```

Three different `val` variables (in `main`, `change_global`, `max`) — but **one** `g_x`, shared across all three functions.

## Style: avoid them

Per [[dis-2-1-scope-memory|Ch 2.1]]: *"avoid programming with global variables whenever possible"* — code that uses only [[LocalVariable|locals]] is *"more modular, more general-purpose, and easier to debug."*

The standard alternatives the rest of Ch 2 supplies:

- **Pass values *into* functions** via [[FunctionParameter|parameters]] (pass-by-value from [[dis-1-4-functions|Ch 1.4]]).
- **Pass values *out of* functions** via [[ReturnStatement|return]] statements.
- **Mutate caller state via [[Pointer|pointers]]** (Ch 2.2) — the principal Ch 2 alternative to globals for cross-function communication.

## Initialization

A global declared with an initializer (`int g_x = 7;`) arrives at its initial value before [[MainFunction|`main`]] runs — the initial bytes come from the executable file's data segment. A global declared without an initializer (`int g_x;`) is **zero-initialized** by the OS via the BSS sub-region. Either way, the programmer never has to write code to initialize globals — unlike [[LocalVariable|locals]], which contain garbage until explicitly assigned.

## Lifetime ≠ scope (preview)

For globals, lifetime and scope are *both* the whole program. For [[LocalVariable|locals]] (without `static`), lifetime = scope = the function's frame on the [[ExecutionStack|stack]]. The decoupled case — *function scope but program lifetime* — is what `static` locals do; deferred to a later chapter.

## Connections

- [[dis-2-1-scope-memory]] — introducing source.
- [[GlobalScope]] — the scope class that governs them.
- [[VariableScope]] — the umbrella scope concept.
- [[DataSection]] — the memory region they live in.
- [[ProcessMemory]] — the four-region picture.
- [[LocalVariable]] — the contrasting class.
- [[FunctionParameter]] / [[ReturnStatement]] / [[Pointer]] — the *alternatives* to globals for cross-function communication.
- [[VariableDeclaration]] — the syntactic construct that creates one.
- [[CLanguage]] / [[DiveIntoSystems]].
