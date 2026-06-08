---
title: "SearchStrategy (Hypothesis)"
type: concept
tags: [testing, python, hypothesis, property-based-testing, typing]
sources: [hypothesis-howto-type-strategies]
last_updated: 2026-06-05
---

# SearchStrategy (Hypothesis)

In [[Hypothesis]], **`SearchStrategy[T]`** is the type of a *strategy* — the core abstraction that describes a space of input values and produces concrete examples from it during [[PropertyBasedTesting|property-based testing]]. Every strategy is generic over `T`, the type of the example it generates: `st.integers()` is a `SearchStrategy[int]`, `st.lists(st.integers())` is a `SearchStrategy[list[int]]`. A strategy is what you pass to `@given` (and what `draw(...)` consumes inside a `@composite`); the engine samples many examples from it and, on failure, shrinks the offending example to a minimal reproducer.

## Strategy vs. function-returning-a-strategy
A subtle but load-bearing distinction (per [[hypothesis-howto-type-strategies]]):
- The *factory* `st.integers` has type `Callable[..., SearchStrategy[int]]` — calling it builds a strategy.
- The *value* `st.integers()` has type `SearchStrategy[int]` — the strategy itself.

This matters when writing [[TypeHints|type hints]]: a helper that *returns* a strategy is annotated `-> SearchStrategy[T]`.

```python
from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

# returns a strategy for "normal" numbers
def numbers() -> SearchStrategy[int | float]:
    return st.integers() | st.floats(allow_nan=False, allow_infinity=False)
```

## Type hints with `@composite`
A strategy defined with the `@composite` decorator is annotated with the type of the value it `return`s — **not** `SearchStrategy`. The decorator adapts the inner function (which takes a `draw` callable) into a strategy, so the user writes the generated type directly:

```python
@st.composite
def ordered_pairs(draw) -> tuple[int, int]:
    n1 = draw(st.integers())
    n2 = draw(st.integers(min_value=n1))
    return (n1, n2)
```

Here `ordered_pairs` is itself usable as a `SearchStrategy[tuple[int, int]]`, even though the annotation is `tuple[int, int]`.

## Covariance
`SearchStrategy` is **covariant** in its type parameter: if `B < A` (B is a subtype of A) then `SearchStrategy[B] < SearchStrategy[A]`. For example `st.from_type(Dog)` is a subtype of `st.from_type(Animal)`. Practically, a strategy for a more specific type can be supplied wherever a strategy for a supertype is expected — the static checker treats it as valid.

## Inspecting strategy types
Because Hypothesis ships hints for all strategies, a type checker can `reveal_type` them:

```python
from hypothesis import strategies as st

reveal_type(st.integers())            # SearchStrategy[int]
reveal_type(st.lists(st.integers()))  # SearchStrategy[list[int]]
```

## Connections
- [[Hypothesis]] — the library that defines `SearchStrategy` and exposes it via `hypothesis.strategies`.
- [[PropertyBasedTesting]] — strategies define the input *domain* the engine samples and shrinks over.
- [[TypeHints]] — annotating strategy-returning functions as `SearchStrategy[T]` applies PEP 484 hints.
- [[StaticallyTyped|static type checking]] — `reveal_type`, the `Callable[..., SearchStrategy[int]]` factory type, and covariance are all checker-level concepts.
- [[Pytest]] — strategies are consumed by `@given` tests that run as ordinary pytest tests.
- [[Python]] — examples use `int | float` unions and built-in generics like `list[int]`.

## Sources
- [[hypothesis-howto-type-strategies]] — how-to on writing type hints for strategies (basic hints, `@composite`, covariance).
