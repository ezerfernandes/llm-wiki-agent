---
title: "static (file-scope linkage in C)"
type: concept
tags: [c-language, linkage, scope, libraries]
sources: [dis-2-9-6-writing-libraries]
last_updated: 2026-05-17
---

# `static` (File-Scope Linkage)

The [[CLanguage|C]] keyword `static`, when applied to a function or global variable at **file scope** (outside any function body), gives that name [[InternalLinkage|internal linkage]] — the symbol is visible only within its own translation unit and is invisible to the [[Linker|linker]] when resolving cross-`.o` references.

Per [[dis-2-9-6-writing-libraries|DIS Ch 2.9.6]], `static` is the library-author's tool for **hiding helper functions** that exist only to support the library's exported API:

```c
// mylib.c

static int internal_helper(int x) {  // not visible to library users
    return x * 2;
}

float bigger(float y, float z) {     // exported (no static)
    return (y > z) ? y : z;
}
```

The `static int internal_helper` symbol does **not** appear in `mylib.o`'s exported symbol table, so a user program that accidentally writes `int internal_helper(int);` and tries to call it will fail at the link stage with [[UndefinedReferenceError|*"undefined reference to `internal_helper`"*]].

## Two unrelated meanings of `static`

`static` is one of [[CLanguage|C]]'s most overloaded keywords. The other meaning lives **inside** a function:

```c
int counter(void) {
    static int n = 0;  // persists across calls; initialized once
    return ++n;
}
```

Here `static` upgrades a [[LocalVariable|local]] from [[StackSection|stack-allocated]] / [[AutomaticStorage|automatic]] to [[DataSection|data-segment]] / [[StaticStorage|static-storage] duration — the variable persists across calls but retains [[BlockScope|block scope]] for visibility. This is **not** the linkage meaning, just a coincident keyword reuse.

## Linkage taxonomy (the three modes)

| Storage class at file scope | Linkage | Visible to | Used for |
|---|---|---|---|
| `extern` (or default) | **external** | All translation units that share the linker invocation | Exported library API; cross-`.o` calls. |
| `static` | **internal** | Only the defining `.c` file | Library-internal helpers; file-private globals. |
| (inside a function) | **none** | Only the defining scope | Local variables. |

## Why library authors use it

Without `static`, every function in `mylib.c` becomes part of `libmylib.a`/`libmylib.so`'s **public surface area** — users can call it, name collisions can occur (if a user defines their own `internal_helper`, the linker may pick the wrong one), and the library's [[ABI|ABI]] grows uncontrollably. `static` is the [[CLanguage|C]]'s **only** access-control mechanism (no `private` / `public` keywords); using it liberally is good library hygiene.

## Connections

- [[dis-2-9-6-writing-libraries]] — introducing source.
- [[CLanguage]] — the language.
- [[Linker]] — what `static` hides symbols from.
- [[HeaderFile]] — `static` functions are **not** declared in headers (they have no external presence).
- [[CSourceFile]] — `static` lives in the `.c` file alongside the function body.
- [[CLibrary]] — `static` is the library-author's encapsulation tool.
- [[UndefinedReferenceError]] — the error a user gets if they try to call a `static` function from outside.
- [[InternalLinkage]] / [[ExternalLinkage]] — the formal linkage taxonomy.
- [[GlobalVariable]] — `static` at file scope makes a global file-private.
