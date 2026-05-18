---
title: "Lambda Function"
type: concept
tags: [c++, programming-languages, functional-programming, thrust, r]
sources: [parproc-ch10-parallel-prefix-problem]
last_updated: 2026-05-17
---

# Lambda Function

An **anonymous function** — a function defined inline at the point of use, without a named declaration. Available in C++ since C++11 and natively in R (as unnamed `function(...)` expressions).

## C++11 Lambda Syntax

```cpp
[capture](params) -> return_type { body }
```

- **`[capture]`**: the capture clause — specifies which outer variables are accessible inside the lambda.
  - `[=]` — capture all used outer variables **by value** (read only; a copy is made).
  - `[&]` — capture all used outer variables **by reference** (allows mutation of the outer variable).
  - `[x, &y]` — capture `x` by value and `y` by reference.
- **`(params)`**: ordinary function parameters.
- **`-> return_type`**: optional explicit return type (often inferred).
- **`{ body }`**: function body.

### Example from Ch10 (moving average)

```cpp
// Functor version (verbose):
struct minus_and_divide : public thrust::binary_function<double,double,double> {
    double w;
    minus_and_divide(double w) : w(w) {}
    __host__ __device__
    double operator()(const double& a, const double& b) const
    { return (a - b) / w; }
};

// Lambda version (concise, C++11):
[=](double& a, double& b) { return (a-b)/wa; }
```

Both are passed as the last argument to `thrust::transform()`. The lambda captures `wa` (the window width) by value via `[=]`, making it accessible inside the body without passing it explicitly.

> *"All this is so much cleaner and cleaner than using a functor!"* — [[NormMatloff]], [[parproc-ch10-parallel-prefix-problem]] §10.7.3, p. 234.

## Capture semantics

The **captured variable** (`wa` in the example) is a local variable of the enclosing function. It is "captured" — made available inside the lambda — without being passed as an argument. This mirrors R's lexical scoping (anonymous functions in R automatically access enclosing-frame variables).

Using `[=]` creates a **by-value copy** at the moment the lambda object is constructed, so later changes to `wa` in the outer scope do not affect the lambda. Use `[&]` if the lambda needs to read the current value or mutate the outer variable.

## Compilation

Requires `g++ -std=c++11` (or later: `-std=c++14`, `-std=c++17`). Older compilers without C++11 support require the explicit functor struct approach.

## Relevance to Thrust and TBB

[[Thrust]] and Intel TBB accept lambdas wherever they previously required functor structs (objects with `operator()`). The `__host__ __device__` qualifiers needed for CUDA back-end functors are not required for OpenMP/TBB back-end lambdas.

## See also

- [[Thrust]] — primary context in the parproc corpus.
- [[MovingAverage]] — the worked example where the lambda replaces `minus_and_divide`.
- [[parproc-ch10-parallel-prefix-problem]] — §10.7.3 (full explanation and code).
