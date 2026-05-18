---
title: "Function Definition (C)"
type: concept
tags: [c-language, functions]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Function Definition (C)

A **function definition** in [[CLanguage|C]] is the full header *plus* body of a [[Function|function]] — the artifact that supplies the executable code the [[CCompiler|compiler]] eventually emits.

```c
<return type> <name>(<parameter list>) {
    <body>
}
```

Contrast with a [[FunctionPrototype|prototype]], which supplies only the header (terminated by a `;` rather than a body).

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

The header declares the [[ReturnType|return type]] (`int`), the function name (`max`), and the [[FunctionParameter|parameter list]] (`int n1, int n2`). The body opens a new [[FunctionScope|scope]] in which the parameters and any [[LocalVariable|local variables]] (`int result;`) live; a [[ReturnStatement|`return`]] statement yields a value of the declared return type back to the [[FunctionCall|caller]].

## Placement rule

In [[CLanguage|C]], a function must be either *defined* or [[FunctionPrototype|prototyped]] before any call site. If you put every definition above its caller, you can skip prototypes — but the [[dis-1-4-functions|Ch 1.4]] idiom is to **prototype at the top, define below**, so [[MainFunction|`main`]] can sit near the top and read top-down.

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] — the umbrella concept.
- [[FunctionPrototype]] — the header-only counterpart.
- [[FunctionParameter]] / [[ReturnType]] / [[ReturnStatement]] — the header and exit pieces.
- [[LocalVariable]] / [[FunctionScope]] — what lives inside the body.
- [[CLanguage]] / [[DiveIntoSystems]].
