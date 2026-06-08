---
title: "No Hidden Control Flow (Zig Design Philosophy)"
type: concept
tags: [zig, language-design, philosophy, readability, control-flow]
sources: [zig-in-depth-overview, zig-why-zig-vs-rust-d-cpp]
last_updated: 2026-06-07
---

# No Hidden Control Flow

"No hidden control flow" is the central design principle of the [[Zig]] language. Per [[zig-in-depth-overview]], Zig is deliberately a small, simple language — its entire syntax is specified by a 580-line PEG grammar file — so that programmers "focus on debugging your application rather than debugging your programming language knowledge."

## The three "no hidden" guarantees

Zig promises **no hidden control flow, no hidden memory allocations, no preprocessor, and no macros**. The slogan is: *if Zig code doesn't look like it's jumping away to call a function, then it isn't.* Given

```zig
var a = b + c.d;
foo();
bar();
```

it is guaranteed that this calls only `foo()` then `bar()` — without needing to know the type of anything. The overview contrasts this with features in other languages that hide control flow:

- **D** has `@property` functions — methods invoked with field-access syntax — so `c.d` could secretly call a function.
- **C++, D, and [[RustLanguage|Rust]]** have operator overloading, so `+` could call a function.
- **C++, D, and Go** have throw/catch exceptions, so `foo()` could throw and prevent `bar()` from running.

In Zig, all control flow is managed exclusively with language keywords and function calls, which the project frames as promoting maintainability and readability. The dedicated rationale essay [[zig-why-zig-vs-rust-d-cpp]] states the purpose plainly — *"The purpose of this design decision is to improve readability"* — and uses the same `var a = b + c.d; foo(); bar();` example, noting the guarantee holds *"without needing to know the types of anything."* It also concedes the natural limit: even in Zig, `foo()` could deadlock and prevent `bar()` from being called, but that is possible in any Turing-complete language.

## Related "no hidden" consequences

- **No hidden allocations** — any function (including in the standard library) that needs to allocate takes an explicit allocator parameter. See [[ZigAllocator]].
- **No preprocessor / no macros** — metaprogramming is done with ordinary compile-time code instead. See [[Comptime]]. Notably, Zig's formatted printing is implemented entirely in Zig via reflection, rather than being hard-coded into the compiler as C's `printf` checks and Rust's format macro are.
- **No exceptions** — errors are ordinary values that propagate through visible keywords. See [[ErrorUnion]].

## Connections

- [[Zig]] — the language built around this philosophy.
- [[Comptime]] — replaces the preprocessor/macros while keeping control flow visible.
- [[ZigAllocator]] — the mechanism behind "no hidden allocations."
- [[ErrorUnion]] — visible, value-based error propagation instead of exceptions.
- [[RustLanguage]] — contrasted for operator overloading.
- [[zig-in-depth-overview]] — source for this principle.
- [[zig-why-zig-vs-rust-d-cpp]] — rationale essay leading with this argument and the readability purpose.
