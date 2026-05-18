---
title: "Python for Data Analysis 3E — Ch.2: Python Language Basics, IPython, and Jupyter Notebooks"
type: source
tags: [book, python, ipython, jupyter, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/python-basics.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/python-basics.html
chapter: 2
---

## Summary
Self-contained tour of the Python language features needed for the rest of the book and a primer on the [[IPython]] shell + [[Jupyter]] notebook. Covers the interpreter model, IPython tab-completion / introspection / `%run` / `%pdb`, then language semantics (indentation-significant blocks, everything-is-an-object, dynamic typing, mutable vs immutable, duck typing), scalar types, and control flow.

## Key Claims
- **IPython** adds tab completion, object introspection (`?` and `??`), magic commands (`%run`, `%paste`, `%timeit`, `%debug`, `%pdb`), and shell integration on top of the standard interpreter.
- **Jupyter notebook** stores everything (code + Markdown + outputs) in a `.ipynb` JSON file; kernel architecture supports 40+ languages, Python kernel powered by IPython.
- **Language semantics** — indentation-significant blocks (PEP-8: 4 spaces); single colon; everything is an [[PythonObject|object]]; comments via `#`; functions / methods called the same way; variables are references / aliases not values; [[DynamicTyping]] with [[DuckTyping]] (`isinstance`, `hasattr`); imports of `.py` modules; `is` vs `==`; mutable (list / dict / ndarray) vs immutable (string / tuple).
- **Scalar types** — `None`, `str` (immutable), `bytes`, `float`, `bool`, `int` (arbitrary precision), `datetime`. String formatting via `.format()` and f-strings.
- **Control flow** — `if`/`elif`/`else`, `for`, `while`, `pass`, `range`, ternary `x if cond else y`.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[IPython]] — chapter introduces and Appendix B extends.
- [[Jupyter]] — notebook environment used by all chapter notebooks.
- [[PythonLanguage]] — base language for everything downstream.
- [[pydata-python-builtin]] — chapter 3 continues with built-in data structures.

## Contradictions
- None.
