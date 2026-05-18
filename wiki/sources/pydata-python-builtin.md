---
title: "Python for Data Analysis 3E — Ch.3: Built-In Data Structures, Functions, and Files"
type: source
tags: [book, python, datastructures, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/python-builtin.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/python-builtin.html
chapter: 3
---

## Summary
Workhorse Python primitives used throughout the rest of the book: built-in sequence types (tuple, list, dict, set), comprehensions, functions (scope, multiple returns, first-class function objects, [[LambdaFunctions|lambda]], [[Generators|generators]], generator expressions, `itertools`), exception handling, and file I/O including bytes/unicode semantics.

## Key Claims
- **Tuple** — fixed-length immutable sequence; unpacking via `a, b, c = tup` and `a, b, *rest = values`; common return value when a function returns multiple things.
- **List** — variable-length mutable sequence; `append`/`insert`/`pop`/`remove`/`extend`; concatenation by `+`/`extend`; binary insertion via `bisect`; slicing with `[start:stop:step]` and negative indexes.
- **Dictionary** (hash map) — `{}` literal; `get(key, default)`/`pop`/`update`/`setdefault`; `collections.defaultdict`; keys must be hashable (tuples allowed; lists not).
- **Set** — unordered collection of unique elements; standard set algebra (`&`, `|`, `-`, `^`); `add`/`remove`/`update`.
- **Comprehensions** — list `[x for x in seq if cond]`, dict, set, and generator (`(x for x in seq)`); nested comprehensions; preferred over loop-then-append.
- **Functions** — first-class objects (can be passed/returned); positional + keyword args; `*args` / `**kwargs`; closures and `global`/`nonlocal`; lambdas (anonymous one-expression functions, useful with `sort(key=...)`/`map`/`filter`); generators with `yield` for lazy evaluation; `itertools` recipes (`groupby`, `combinations`, `permutations`, `product`, `chain`).
- **Exception handling** — `try`/`except`/`else`/`finally`; catch multiple exception types via tuple; raise / re-raise.
- **Files** — `open(path, mode)`; modes (`r`, `w`, `a`, `x`, `r+`, plus binary `b`); always close (prefer `with` block); `read`/`readlines`/`write`/`writelines`/`seek`/`tell`; text vs binary mode and `encoding=` for unicode.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[PythonLanguage]] — foundation continued from chapter 2.
- [[Generators]] — lazy iteration pattern.
- [[LambdaFunctions]] — anonymous functions used with sorting / mapping.
- [[pydata-numpy-basics]] — chapter 4 next.

## Contradictions
- None.
