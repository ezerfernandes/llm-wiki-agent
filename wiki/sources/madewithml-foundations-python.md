---
title: "Made With ML — Python for Machine Learning"
type: source
tags: [foundations, made-with-ml, python, programming, course]
date: 2026-05-15
source_file: raw/madewithml/foundations-python.md
---

## Summary
Tour of Python's core language features framed for an ML practitioner: variables and primitive types (int, float, str, bool); the four foundational data structures with their mutability/ordering/uniqueness trade-offs (list, tuple, set, dict); indexing and slicing; control flow (if, for, while); list comprehensions; functions with default and keyword arguments; classes with `__init__`, magic methods, inheritance, and methods; and decorators (including @-syntax, callback patterns, and stacking decorators). The lesson is presented as a tight, runnable notebook with short snippets and "Show answer" quizzes, intended as the prerequisite for the [[NumPy]], [[pandas]], and [[PyTorch]] lessons that follow.

## Key Claims
- The four primary collection types have crisp trade-offs: list (mutable, ordered, indexable, non-unique), tuple (immutable, ordered, indexable, non-unique), set (mutable, unordered, non-indexable, unique), dict (mutable, unordered, non-indexable, unique keys).
- Native Python dicts have been insertion-ordered since Python 3.7+; `OrderedDict` is mostly only needed for explicit re-ordering semantics now.
- Type awareness matters: `"5" + "3"` is `"53"`, not `8` — silently coercing between numeric and string types is a frequent ML data-pipeline bug.
- Classes encode behavior + state together; magic methods (`__str__`, `__add__`, etc.) hook into Python's syntax for printable, addable, iterable objects.
- Decorators are functions that wrap other functions; they compose top-down (the outermost `@decorator` runs last), making them ideal for orthogonal concerns like timing, caching, logging, or framework registration (e.g. `@app.get(...)` in FastAPI).
- List comprehensions `[f(x) for x in xs if pred(x)]` are the canonical Pythonic replacement for short imperative loops that build collections.

## Key Quotes
> "We should always know what types of variables we're dealing with so we can do the right operations with them."

> "After Python 3.7+, native dictionaries are insertion ordered."

> "Variables are containers for holding data and they're defined by a name and value."

## Connections
- [[GokuMohandas]] — author.
- [[MadeWithML]] — parent course.
- [[Python]] — the language itself.
- [[NumPy]] — successor lesson; builds on Python lists by introducing typed N-dim arrays.
- [[pandas]] — successor lesson; builds on Python dicts by introducing labeled tabular data.
- [[PyTorch]] — successor lesson; uses Python classes to define `nn.Module`s.
- [[ListComprehension]] — idiomatic transformation pattern.
- [[Decorator]] — language feature used throughout the ML/serving ecosystem.
- [[Class]] — OOP construct used to define models and services.

## Contradictions
None — pure language primer.
