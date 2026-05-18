---
title: "Functor (Thrust / C++)"
type: concept
tags: [c-plus-plus, thrust, callable, stateful, parallel-computing]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Functor (Thrust / C++)

A **functor** is a C++ struct (or class) with an overloaded `operator()` — i.e. a *callable object*. In the context of [[Thrust]] and the C++ STL, functors are the canonical way to pass user code to a generic parallel algorithm.

> *"A functor is a C++ mechanism to produce a callable function, largely similar in goal to using a pointer to a function. [...] Since structs and classes can have member variables, we can store needed data in them, and that is what distinguishes functors from function pointers — we can save state."* ([[parproc-ch06-thrust-programming]] §6.2)

The **stateful-callable** property is the entire point. A function pointer can only carry its code; a functor can also carry **member variables** — parameters, captured iterators, raw pointers, dimensions. This makes functors the natural mechanism for parameterized parallel operations.

## Canonical shape

```cpp
struct ismultk {
    const int increm;                    // member: stored state
    ismultk(int _increm) : increm(_increm) {}   // constructor
    __device__
    bool operator()(const int i) {       // the callable interface
        return i != 0 && (i % increm) == 0;
    }
};
```

- The struct **carries `increm`** as a member.
- The constructor initializes the member from its arg.
- `operator()` defines what the functor *does* when called.
- `__device__` marks it as callable from device code under the [[CUDA]] back end (omitted under OpenMP).

## Invocation pattern

```cpp
thrust::copy_if(dx.begin(), dx.end(), seq.begin(), out.begin(), ismultk(k));
//                                                                ^^^^^^^^
//                                          parens construct an instance
```

The `ismultk(k)` expression *constructs an instance* whose `operator()` Thrust will then invoke per element. Each call to `operator()` accesses the same `increm` member — *"`incrim` acts as a 'global' variable to all the actions of the operator"* ([[parproc-ch06-thrust-programming]] §6.4).

By contrast, [[parproc-ch06-thrust-programming]] §6.2's `thrust::generate(hv.begin(), hv.end(), rand16)` passes a **function pointer**, not a functor — note the **lack of parentheses**. `rand16` is just an ordinary stateless C function.

## Functor with iterator state ([[parproc-ch06-thrust-programming]] §6.6)

A functor can carry a Thrust iterator and immediately extract a raw pointer:

```cpp
struct ismultk {
    const int increm;
    thrust::device_vector<int>::iterator w;
    int *wd;
    ismultk(thrust::device_vector<int>::iterator _w, int _increm):
        w(_w), increm(_increm) {
            wd = thrust::raw_pointer_cast(&w[0]);
        }
    __device__
    bool operator()(const int i) {
        if (i != 0 && (i % increm) == 0) wd[i] = 2 * wd[i];
    }
};
```

This lets `operator()` use **ordinary C array subscripting** (`wd[i]`) instead of Thrust iterator arithmetic. *"This is really just like passing an array pointer to an ordinary C function. [...] The point of converting to the raw array here was to enable the use of ordinary array subscripting, rather than Thrust iterators."*

## Inheriting from `thrust::unary_function`

Functors used inside `thrust::make_transform_iterator` *must* inherit from `thrust::unary_function<In, Out>`:

```cpp
struct transidx : public thrust::unary_function<int, int> {
    const int nr, nc;
    __host__ __device__
    transidx(int _nr, int _nc) : nr(_nr), nc(_nc) {}
    __host__ __device__
    int operator()(int i) {
        int r = i / nc; int c = i % nc;
        return c * nr + r;
    }
};
```

*"It won't work without this!"* ([[parproc-ch06-thrust-programming]] §6.8.1). The base class supplies the typedefs (`argument_type`, `result_type`) Thrust's iterator-trait machinery needs to deduce the iterator's value type at compile time. A 2-argument variant (`thrust::binary_function<In1, In2, Out>`) is used for functors passed to `transform()` with two input ranges.

## Why functors instead of lambdas?

Thrust pre-dates C++11 device-side lambdas. Modern CUDA does support `[] __device__` lambdas, but functors remain the documented Thrust idiom and have one strict advantage: the **stored state** is reusable across multiple algorithm invocations.

## See also

- [[Thrust]] — primary user of the functor pattern.
- [[FancyIterator]] / [[TransformIterator]] — require `thrust::unary_function`-derived functors.
- [[parproc-ch06-thrust-programming]] — §6.2 (definition), §6.4 (with state), §6.6 (with iterator state), §6.8.1 (with `unary_function` base).
