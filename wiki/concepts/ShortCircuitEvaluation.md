---
title: "Short-Circuit Evaluation"
type: concept
tags: [c-language, operator, semantics]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# Short-Circuit Evaluation

**Short-circuit evaluation** is the rule that [[LogicalOperator|logical operators]] **stop evaluating their operands as soon as the result is known**. It is a property of the language's *evaluation strategy*, not of the algebra of logical operations.

Per [[dis-1-3-conditionals-loops|DiS Ch 1.3]]:

> "Logical operator evaluation stops evaluating a logical expression as soon as the result is known."

## In [[CLanguage|C]]

- **`A && B`** — `A` is evaluated first. If `A` is **false** (zero), `B` is **not evaluated**; the whole expression is `0`. If `A` is true, `B` is evaluated; the result is `B`'s truthiness as `0` or `1`.
- **`A || B`** — `A` is evaluated first. If `A` is **true** (nonzero), `B` is **not evaluated**; the whole expression is `1`. If `A` is false, `B` is evaluated.

## Why it matters

- **Guard idioms become safe.** `if (p != NULL && *p == 0)` cannot dereference a null pointer, because `*p` is skipped when `p == NULL`.
- **Side effects in the second operand may not run.** `if (init() && next())` calls `next()` only when `init()` returns nonzero — a feature for sequencing dependent calls, a footgun when the side effect was assumed unconditional.
- **Performance** — avoids unnecessary evaluation of expensive right operands when the left already settles the result.

## Equivalents in other languages

Most C-family languages (Python's `and`/`or`, JavaScript's `&&`/`||`, Java's `&&`/`||`) inherit short-circuit semantics. The non-short-circuiting bitwise siblings `&` / `|` always evaluate both operands.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[LogicalOperator]] — the operators whose semantics this concept defines.
- [[RelationalOperator]] — typically what `&&` / `||` combine.
- [[CBooleanExpression]] — the host expression form.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
