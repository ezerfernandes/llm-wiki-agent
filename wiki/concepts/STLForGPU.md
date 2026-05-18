---
title: "STL for GPU"
type: concept
tags: [c-plus-plus, thrust, gpu, stl, library-design, design-pattern]
sources: [parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# STL for GPU

The design pattern [[Thrust]] embodies: **transplant the C++ Standard Template Library (STL) idioms — containers, iterators, generic algorithms, function objects — onto parallel substrates** so the same source compiles to either a GPU back end ([[CUDA]]), a multicore CPU back end ([[OpenMP]] or TBB), or a serial reference back end.

> *"It uses the C++ STL library as a model, and Thrust is indeed a C++ template library. It includes various data manipulation routines, such as for sorting and prefix scan operations."* ([[parproc-ch06-thrust-programming]] §6 intro)

## The four STL pillars and their Thrust counterparts

| STL concept | STL form | Thrust form |
|---|---|---|
| **Containers** | `std::vector<T>`, `std::list<T>` | `thrust::host_vector<T>`, `thrust::device_vector<T>` |
| **Iterators** | `vec.begin()`, `vec.end()` (random-access, bidirectional, etc.) | `device_vector<T>::iterator`, plus [[FancyIterator|fancy iterators]] |
| **Algorithms** | `std::sort`, `std::transform`, `std::accumulate`, `std::copy_if` | `thrust::sort`, `thrust::transform`, `thrust::reduce`, `thrust::copy_if` |
| **Function objects** | `std::plus<int>`, lambdas, callable structs | `thrust::plus<int>`, [[Functor|callable structs with `__device__ operator()`]] |

The mapping is **deliberate and near-mechanical**: Thrust users with STL experience can read and write Thrust code with minimal new vocabulary. The price is a hard requirement on **C++ host code** (unlike [[CUBLAS]] / [[CUFFT]], which are callable from C).

## What the abstraction buys

- **Source portability across substrates.** Same `.cu` file compiles to CUDA under `nvcc` or to OpenMP under `g++ -fopenmp -DTHRUST_DEVICE_BACKEND=THRUST_DEVICE_BACKEND_OMP`. The host-device transfer plumbing (`cudaMalloc`/`cudaMemcpy`) is hidden behind container assignment (`device_vector<int> dv = hv`).
- **Reuse of STL pedagogy.** A 2002-era textbook on the STL teaches you most of Thrust's surface area.
- **Composable parallel operations.** Algorithms compose via iterators: the output range of one is the input range of the next. [[FancyIterator|Fancy iterators]] extend this to **lazy fusion** — `make_transform_iterator` inserts an on-the-fly map step into any consuming algorithm without an intermediate array.

## What the abstraction costs

- **C++ template error messages.** *"The compiler gives us a very long megillah as an error message, a highly uninformative one. Keep this in mind if you get a 30-line compiler error."* ([[parproc-ch06-thrust-programming]] §6.13). Forgetting `.begin()` on a container or missing an `#include` produces deduction-failure cascades.
- **Per-call kernel overhead.** Each algorithm invocation is a [[CUDA]] kernel launch under the CUDA back end — *"each Thrust call invokes considerable overhead"* ([[parproc-ch06-thrust-programming]] §6.8). Fancy-iterator fusion is the documented mitigation.
- **No parallel loop primitive.** *"Thrust has no direct parallel loop facilities"* ([[parproc-ch06-thrust-programming]] §6.4). The idiomatic substitute is `thrust::for_each` over a counting-iterator range — close to but not identical to STL's `std::for_each`.
- **Hand-tuned code can beat the library.** The §6.9 timing comparison shows a `for_each` + raw-pointer-functor matrix transpose beating Thrust's distribution-example fancy-iterator implementation by ~2× on OpenMP.

## Sibling pattern — `std::execution` policies (C++17+)

The C++17 parallel STL (`std::execution::par`, `std::execution::par_unseq`) adopts a similar shape — pass an execution policy to a standard algorithm and the implementation chooses a parallel strategy. Thrust pre-dates this standardization by a decade and uses the **container-tagging** approach (host vs device) instead of policy-tagging. Modern CUDA additionally supports the C++17 parallel STL via NVIDIA's libcu++ / nvc++ implementations — partially closing the gap between Thrust and standard parallel C++.

## See also

- [[Thrust]] — the canonical implementation.
- [[Functor]] — Thrust's per-element customization point.
- [[FancyIterator]] — Thrust's lazy-iterator family.
- [[CUDA]] / [[OpenMP]] — the back ends Thrust targets.
- [[parproc-ch06-thrust-programming]] — §6 intro (STL framing), §6.13 (template-error UX).
