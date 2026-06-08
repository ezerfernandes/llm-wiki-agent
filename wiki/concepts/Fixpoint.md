---
title: "Fixpoint"
type: concept
tags: [algorithm-design, parsing, iteration, functional-programming, fuzzing, python]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Fixpoint

A **fixpoint** (fixed point) of a function `f` is an element `x` of its domain that the function maps to itself: `f(x) == x`. Many algorithms compute a result by **iterating a step function until it stops changing** — repeatedly applying `f` to its own output until two successive results are equal. That converged value is a fixpoint, and "iterate to a fixpoint" is a standard pattern for closure/least-fixed-point computations (e.g. nullability, reachability, dataflow analyses). The chapter's example: `1` is a fixpoint of square root because `sqrt(1) == 1`.

## The Fuzzing Book's `fixpoint`
[[fuzzingbook-12-parser|Ch 12]] mints a reusable `fixpoint(f)` decorator that wraps a step function and re-applies it until its (string-serialized) output stabilizes:

```python
def fixpoint(f):
    def helper(arg):
        while True:
            sarg = str(arg)
            arg_ = f(arg)
            if str(arg_) == sarg:
                return arg
            arg = arg_
    return helper
```

(It compares via `str()` rather than hashing because the argument is an unhashable `set` with a stable string form.) The chapter applies it two ways:

- **`my_sqrt(x)`** — rewrites the Newton-iteration square root from Ch 1 as a fixpoint of `(approx + x/approx)/2`.
- **`nullable(grammar)`** — computes the set of **nullable** nonterminals (those that can derive the empty string) by iterating: start from `{ε}`, and on each pass add any nonterminal with a fully-nullable expansion, until the set stops growing. This nullable set is the key input to the **Aycock epsilon fix** that lets the [[EarleyParser|Earley parser]] handle epsilon rules.

## Connections
- [[EarleyParser]] — uses `fixpoint` to compute the `nullable` set for the epsilon fix.
- [[DynamicProgramming]] — fixpoint iteration is the closure-computation cousin of tabulated DP.
- [[ContextFreeGrammar]] — nullability is a per-nonterminal property of a CFG.
- [[fuzzingbook-12-parser]] — the chapter that mints the `fixpoint` decorator.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
