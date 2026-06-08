---
title: "Write type hints for strategies (Hypothesis how-to)"
type: source
tags: [testing, python, hypothesis, property-based-testing, typing, how-to]
date: 2026-06-05
source_file: raw/hypothesis/how-to/hypothesis-howto-type-strategies.md
---

## Summary
A short [[Hypothesis]] how-to guide explaining how to write [[TypeHints|type hints]] for [[PropertyBasedTesting|property-based testing]] strategies. Its core lesson is that every strategy has type [[SearchStrategy]]`[T]`, parametrized by the type `T` of the example it generates — so a function returning a strategy is annotated `-> SearchStrategy[T]`, while a strategy *value* is itself a `SearchStrategy[T]`. The guide covers three points: basic annotations for strategy-returning functions, the special rule that `@composite` strategies are annotated with the *generated* return type (not `SearchStrategy`), and the fact that `SearchStrategy` is **covariant** in its type parameter.

## Key Claims
- Hypothesis ships type hints for all of its strategies and for all functions that return a strategy, so `reveal_type(st.integers())` shows `SearchStrategy[int]` and `reveal_type(st.lists(st.integers()))` shows `SearchStrategy[list[int]]`.
- [[SearchStrategy]] is *the* type of a strategy, generic over the type of the example it generates; you annotate your own strategy-returning helpers as `-> SearchStrategy[T]`.
- There is a load-bearing distinction between a strategy and a function that returns one: `st.integers` has type `Callable[..., SearchStrategy[int]]`, whereas the *result* `st.integers()` has type `SearchStrategy[int]`.
- For strategies built with the `@composite` decorator, the type hint should be the type of the value the function `return`s (e.g. `tuple[int, int]`), **not** `SearchStrategy[...]` — because `@composite` wraps the function so that the value it produces is the example, and the decorator adapts the signature.
- `SearchStrategy` is **covariant** in its parameter: if `B` is a subtype of `A` (`B < A`), then `SearchStrategy[B] < SearchStrategy[A]`. So `st.from_type(Dog)` is a subtype of `st.from_type(Animal)`, and a more-specific strategy can be used where a strategy for a supertype is expected.

## Key Quotes
> "`SearchStrategy` is the type of a strategy. It is parametrized by the type of the example it generates." — defining the core abstraction

> "`integers()` is a function which returns a strategy, and that strategy has type `SearchStrategy[int]`. The function `st.integers` therefore has type `Callable[..., SearchStrategy[int]]`, while the value `s = st.integers()` has type `SearchStrategy[int]`." — function-vs-strategy distinction

> "When writing type hints for strategies defined with `@composite`, use the type of the returned value (not `SearchStrategy`)" — the `@composite` annotation rule

> "`SearchStrategy` is covariant, meaning that if `B < A` then `SearchStrategy[B] < SearchStrategy[A]`. In other words, the strategy `st.from_type(Dog)` is a subtype of the strategy `st.from_type(Animal)`." — covariance

## Code Receipt

`reveal_type` shows the inferred strategy types (mypy / type-checker output in comments):
```python
from hypothesis import strategies as st

reveal_type(st.integers())
# SearchStrategy[int]

reveal_type(st.lists(st.integers()))
# SearchStrategy[list[int]]
```

Annotating a strategy-returning helper with `SearchStrategy[T]`:
```python
from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

# returns a strategy for "normal" numbers
def numbers() -> SearchStrategy[int | float]:
    return st.integers() | st.floats(allow_nan=False, allow_infinity=False)
```

A `@composite` strategy: annotate with the *generated* value's type, not `SearchStrategy`:
```python
@st.composite
def ordered_pairs(draw) -> tuple[int, int]:
    n1 = draw(st.integers())
    n2 = draw(st.integers(min_value=n1))
    return (n1, n2)
```

## Connections
- [[Hypothesis]] — the library whose public types this guide documents.
- [[SearchStrategy]] — the central generic type the guide is about.
- [[PropertyBasedTesting]] — the paradigm strategies serve; strategies define the input domain.
- [[TypeHints]] — the Python (PEP 484) annotation feature being applied to strategies.
- [[StaticallyTyped|static type checking]] — `reveal_type` and `Callable[..., SearchStrategy[int]]` are checker-facing; covariance is a static-typing concept.
- [[Python]] — uses `int | float` union syntax (PEP 604) and built-in generic `list[int]`.

## Contradictions
- None. This guide is consistent with the rest of the [[Hypothesis]] cluster; it complements (does not conflict with) the domain/distribution and health-check how-tos.
