---
title: "Type Hints"
type: concept
tags: [python, devex, typing]
sources: [madewithml-styling, hypothesis-howto-type-strategies]
last_updated: 2026-06-05
---

# Type Hints

[[Python]] annotations (PEP 484) declaring expected types for variables and function signatures. Improve IDE help, enable [[StaticallyTyped|static checkers]] like mypy, and surface naturally in [[Mkdocstrings]] documentation.

## In Hypothesis
[[Hypothesis]] ships type hints for all of its strategies and strategy factories. A strategy value has type [[SearchStrategy]]`[T]`, so a function returning one is annotated `-> SearchStrategy[T]`; a `@composite` strategy is instead annotated with the type of the value it returns. See [[hypothesis-howto-type-strategies]].
