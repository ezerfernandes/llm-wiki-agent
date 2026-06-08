---
title: "Metaprogramming"
type: concept
tags: [metaprogramming, compile-time, generics, reflection, language-design]
sources: [zig-in-depth-overview, zig-why-zig-vs-rust-d-cpp]
last_updated: 2026-06-07
---

# Metaprogramming

Metaprogramming is writing code that generates, inspects, or transforms other code — enabling generics, reflection, and code specialization. Languages implement it in different ways: C with a textual preprocessor and macros, C++ with templates, Rust with a macro system, and [[Zig]] with compile-time code execution.

## Zig's approach: comptime

Per [[zig-in-depth-overview]], [[Zig]] deliberately has **no preprocessor and no macros**. Instead, all metaprogramming is done in ordinary Zig code that runs at compile time via [[Comptime|comptime]], preserving the [[NoHiddenControlFlow]] principle. The two pillars are:

- **Generics as type-returning functions** — since types are compile-time values, a generic is just a `fn(comptime T: type) type`.
- **Reflection** — `@typeInfo` and `@typeName` let code inspect struct fields and types at compile time.

A frequently cited consequence is that Zig's formatted printing is implemented entirely in Zig (using reflection), whereas C hard-codes `printf` checks into the compiler and Rust hard-codes its format macro into the compiler. [[zig-why-zig-vs-rust-d-cpp]] uses this same `format!` example to argue that macro-free metaprogramming need not sacrifice power: "Even Rust has macros with special cases like `format!`, which is implemented in the compiler itself. Meanwhile in Zig, the equivalent function is implemented in the standard library with no special case code in the compiler." The broader claim is that the macro-heavy approaches of C++, Rust, and D add language surface that distracts from the application itself, where Zig's comptime keeps metaprogramming inside the ordinary language.

## Connections

- [[Comptime]] — Zig's concrete metaprogramming mechanism.
- [[Zig]] — the language using comptime for metaprogramming.
- [[NoHiddenControlFlow]] — comptime keeps metaprogramming free of hidden control flow.
- [[RustLanguage]] — contrasted (macros) approach to metaprogramming.
- [[RustMacro]] — Rust's macro system, including the compiler-baked `format!` Zig contrasts against.
- [[zig-in-depth-overview]] — source for the comparison across languages.
- [[zig-why-zig-vs-rust-d-cpp]] — source for the simplicity argument against macro-heavy languages.
