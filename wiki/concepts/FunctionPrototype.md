---
title: "Function Prototype (C)"
type: concept
tags: [c-language, functions, declarations]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Function Prototype (C)

A **function prototype** (also called a **declaration**) is a header-only statement of a [[Function|function]]'s signature — its name, [[ReturnType|return type]], and [[FunctionParameter|parameter list]] — *without* a body. Per [[dis-1-4-functions|DIS Ch 1.4]]:

> "A function declaration or prototype specifies the function's name, its return type, and its parameter list (the number and types of all the parameters)."

```c
int  max(int n1, int n2);
void print_table(int start, int stop);
```

A prototype ends in a `;` rather than a `{ ... }` block.

## Why C needs them

The [[CCompiler|C compiler]] processes a file in essentially one pass. By the time it sees a [[FunctionCall|call site]], it must already know that function's signature in order to type-check the call and arrange arguments per the calling convention. The available options are:

1. Put each [[FunctionDefinition|definition]] *physically above* any caller (works for small programs).
2. Put **prototypes at the top of the file** (above [[MainFunction|`main`]]) and place full [[FunctionDefinition|definitions]] below — the [[dis-1-4-functions|Ch 1.4]] standard idiom.
3. `#include` prototypes from a [[HeaderFile|header file]] — the multi-file generalization the [[StandardIOLibrary|`<stdio.h>`]]-style libraries use.

Option 2 is what [[dis-1-4-functions|Ch 1.4]] introduces; the same pattern, at file scale, is what makes [[HeaderFile|header files]] work.

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] / [[FunctionDefinition]] — prototype is the header-only counterpart of a full definition.
- [[FunctionParameter]] / [[ReturnType]] — the typed pieces a prototype carries.
- [[FunctionCall]] — what the prototype enables: calling before defining.
- [[HeaderFile]] / [[PreprocessorDirective]] — the multi-file generalization of this same pattern.
- [[MainFunction]] — typically sits *between* the top-of-file prototypes and the definitions below.
- [[CCompiler]] — the consumer that needs the signature at the call site.
- [[CLanguage]] / [[DiveIntoSystems]].
