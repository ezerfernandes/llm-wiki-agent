---
title: "Thrust"
type: concept
tags: [gpu, cuda, library, c-plus-plus, openmp, template-library, stl, tbb]
sources: [parproc-ch05-cuda-gpu-programming, parproc-ch06-thrust-programming]
last_updated: 2026-05-17
---

# Thrust

A high-level C++ template library for [[NVIDIA]] [[CUDA]] that provides STL-style parallel algorithms on GPU and multicore-CPU containers. Thrust *"uses the C++ STL library as a model, and Thrust is indeed a C++ template library. It includes various data manipulation routines, such as for sorting and prefix scan operations"* ([[parproc-ch06-thrust-programming]] §6 intro). The headline distinguishing feature: the **same Thrust source compiles to any of three back ends** — [[CUDA]] (GPU), [[OpenMP]] (multicore CPU), or Intel TBB (often faster than OpenMP) — selected by a compile-time macro.

## Position in the CUDA wrapper-library stack

| Library | Domain | Backends |
|---|---|---|
| [[CUBLAS]] | BLAS / linear algebra | CUDA only |
| [[CUFFT]] | Fast Fourier Transform | CUDA only |
| **Thrust** | STL-style parallel algorithms | CUDA + [[OpenMP]] + Intel TBB |

The cross-backend property is what makes Thrust distinctive: code written against Thrust can run on a GPU server, a CPU workstation, or in a unit-test environment without device access, by toggling the backend at compile time.

## Back-end selection (Ch6 §6.1)

| Back end | Compile command |
|---|---|
| **CUDA** | `nvcc x.cu` — no special link flags needed since CUDA 4.0 ships with Thrust |
| **OpenMP** | `g++ -fopenmp -lgomp -DTHRUST_DEVICE_BACKEND=THRUST_DEVICE_BACKEND_OMP -I/path/to/thrust x.cpp` |
| **TBB** | analogous to OpenMP with `THRUST_DEVICE_BACKEND_TBB` |

Newer Thrust uses `THRUST_DEVICE_SYSTEM` / `THRUST_DEVICE_SYSTEM_OMP` (the C-wrapper example in §6.3 uses this form). `OMP_NUM_THREADS` controls thread count under the OpenMP back end. **Critical caveat** ([[parproc-ch06-thrust-programming]] §6.1.2 footnote): *"Threads will not be set up if you use host arrays/vectors"* — only `thrust::device_vector` triggers parallelism, even when "device" is the CPU under the OpenMP back end.

## API surface (from [[parproc-ch06-thrust-programming]])

### Containers

- `thrust::host_vector<T>` — STL-vector-like container in host memory.
- `thrust::device_vector<T>` — same in "device" memory (GPU under CUDA back end; host memory under OpenMP back end). Assignment between them (`device_vector<int> dv = hv;`) does the host↔device copy implicitly, replacing manual `cudaMalloc` / `cudaMemcpy` plumbing.

### Algorithms (the STL-style core)

| Function | Role |
|---|---|
| `thrust::sort(begin, end)` | parallel sort |
| `thrust::reduce(begin, end, init, op)` | parallel fold |
| `thrust::transform(begin, end, out, F)` *(1-input)* | parallel map |
| `thrust::transform(begin1, end1, begin2, out, F)` *(2-input)* | parallel pairwise map |
| `thrust::for_each(begin, end, F)` | parallel side-effecting apply, no output |
| `thrust::generate(begin, end, F)` | fill via a 0-arg function (or functor) |
| `thrust::sequence(begin, end, init)` | fill with `init, init+1, init+2, ...` |
| `thrust::copy(begin, end, out)` | parallel copy |
| `thrust::copy_if(begin, end, out, pred)` | filter (4-arg form) |
| `thrust::copy_if(begin, end, stencil_begin, out, pred)` | filter-with-stencil (5-arg form) |
| `thrust::unique(begin, end)` | remove **consecutive** duplicates (sort first if you want set-uniqueness) |
| `thrust::scatter(src_begin, src_end, map, dst)` | permutation: `dst[map[i]] = src[i]` |
| `thrust::gather(map_begin, map_end, src, dst)` | permutation: `dst[i] = src[map[i]]` |
| `thrust::inclusive_scan(begin, end, out)` | [[PrefixScan|prefix scan]] (inclusive); default `+`, override with op |
| `thrust::exclusive_scan(begin, end, out)` | prefix scan (exclusive) |
| `thrust::count(...)` / `thrust::min_element(...)` / ... | STL parallel-equivalents |

### [[Functor|Functors]] — stateful callables

The canonical Thrust user-extension mechanism. *"A functor is a C++ mechanism to produce a callable function, largely similar in goal to using a pointer to a function. [...] Since structs and classes can have member variables, we can store needed data in them, and that is what distinguishes functors from function pointers — we can save state."* ([[parproc-ch06-thrust-programming]] §6.2). Typical shape:

```cpp
struct ismultk {
    const int increm;
    ismultk(int _increm) : increm(_increm) {}
    __device__
    bool operator()(const int i) {
        return i != 0 && (i % increm) == 0;
    }
};
// ... thrust::copy_if(dx.begin(), dx.end(), seq.begin(), out.begin(), ismultk(k));
```

The parentheses in `ismultk(k)` *construct* an instance whose `operator()` is then invoked per element. By contrast, `thrust::generate(hv.begin(), hv.end(), rand16)` passes a plain function pointer (no parens) because `rand16` is an ordinary function. Functors used with `make_transform_iterator` must inherit from `thrust::unary_function<In, Out>` — *"It won't work without this!"*

### [[FancyIterator|Fancy iterators]] — memory-traffic and overhead savers ([[parproc-ch06-thrust-programming]] §6.8)

*"Since each Thrust call invokes considerable overhead, Thrust offers some special iterators to reduce memory access time and memory space requirements."*

| Iterator | Header | Role |
|---|---|---|
| **[[CountingIterator]]** | `<thrust/iterator/counting_iterator.h>` | virtual `0,1,2,...` without materializing an array (replaces `sequence()`) |
| **[[TransformIterator]]** | `<thrust/iterator/transform_iterator.h>` | applies a functor lazily; implements **fusion** of `transform()` into a consuming algorithm |
| **[[ZipIterator]]** | `<thrust/iterator/zip_iterator.h>` | co-iterates parallel arrays as tuples |
| **[[DiscardIterator]]** | `<thrust/iterator/discard_iterator.h>` | output `/dev/null` — for `transform()` calls whose work is side-effecting |
| **[[PermutationIterator]]** | `<thrust/iterator/permutation_iterator.h>` | virtual `gather` via an index map |

**Fusion via `make_transform_iterator`** is the chapter's centerpiece. Instead of:

```cpp
thrust::transform(seq.begin(), seq.end(), dmap.begin(), F);
thrust::scatter(src.begin(), src.end(), dmap.begin(), dst.begin());
```

write:

```cpp
thrust::scatter(src.begin(), src.end(),
    thrust::make_transform_iterator(seq.begin(), F),
    dst.begin());
```

— *"Don't apply F to `seq` yet. Instead, perform that operation as you go along, and feed each result directly into `scatter()`."* Saves *n* memory reads, *n* memory writes, and the kernel-launch overhead of the eliminated `transform()` call.

**Gotcha**: counting iterators work with `gather()` (which takes `(begin, end)` for the map) but **not with `scatter()`** (which takes only `begin` for the map) — *"the compiler encounters problems with determining where the end of the counting sequence is."*

### Thrust ↔ CUDA interop ([[parproc-ch06-thrust-programming]] §6.5)

Two casts at the API boundary:

```cpp
// Thrust → CUDA: extract raw int* from device_vector
int *wd = thrust::raw_pointer_cast(&w[0]);

// CUDA → Thrust: wrap cudaMalloc'd int* for Thrust algorithms
int *dz; cudaMalloc(&dz, 100*sizeof(int));
thrust::device_ptr<int> tz(dz);
int k = thrust::reduce(tz, tz+100, (int)0, thrust::plus<int>());
```

Rule of thumb: **Thrust owns its containers' memory; CUDA owns raw pointers; cast at the boundary.** A common pattern is to extract a raw pointer in a functor's constructor (capturing the iterator passed in) so the `operator()` can use ordinary `wd[i]` array subscripting instead of Thrust iterator arithmetic.

### Plain-C wrapper ([[parproc-ch06-thrust-programming]] §6.3)

```cpp
extern "C" void tsort(int *x, int *nx);
void tsort(int *x, int *nx) {
    int n = *nx;
    thrust::device_vector<int> dx(x, x+n);
    thrust::sort(dx.begin(), dx.end());
    thrust::copy(dx.begin(), dx.end(), x);
}
```

Compile with `nvcc -c` (CUDA) or `g++ ... -DTHRUST_DEVICE_SYSTEM=THRUST_DEVICE_SYSTEM_OMP` (OpenMP); link from R / Fortran / plain C via `extern "C"`. The *same `.cu` file* targets either back end depending on the host-compiler invocation.

## Synchronicity ([[parproc-ch06-thrust-programming]] §6.12.1)

> *"Thrust calls are in fact CUDA kernel calls, and thus entail some latency. Other than the `transform()`-family functions, the calls are all synchronous."*

**Inverted vs raw CUDA.** Raw CUDA kernel launches are always asynchronous; Thrust algorithm calls are **synchronous by default** with only the `transform()`-family async. Programmers porting raw CUDA → Thrust must remember the flip; programmers porting Thrust → raw CUDA must insert explicit `cudaThreadSynchronize()` calls.

## Lack of a parallel loop primitive

A surprising absence from Ch6: *"`sequence()` simply generates an array consisting of 0,1,2,...,n-1. Note that this is typically used because Thrust has no direct parallel loop facilities."* ([[parproc-ch06-thrust-programming]] §6.4). The canonical idiom for "do this work for `i = 0..n-1` in parallel" is:

```cpp
thrust::device_vector<int> seq(n);
thrust::sequence(seq.begin(), seq.end(), 0);
thrust::transform(seq.begin(), seq.end(), out.begin(), F_that_uses_i);
// or, using a counting iterator to skip the materialization:
thrust::counting_iterator<int> seqb(0);
thrust::transform(seqb, seqb+n, out.begin(), F_that_uses_i);
// or, when the functor side-effects:
thrust::for_each(seqb, seqb+n, F_that_uses_i);
```

`for_each` is the closest direct analog to `#pragma omp parallel for`, used in [[parproc-ch06-thrust-programming]] §6.9's faster matrix-transpose implementation.

## Performance — the §6.9 surprise

Fancy iterators are **not unconditionally faster**. [[parproc-ch06-thrust-programming]] §6.9 head-to-head times two matrix-transpose implementations:

- **Code 1**: Matloff's hand-rolled `thrust::for_each` over a counting-iterator range with a functor that uses `raw_pointer_cast`-extracted `int*` for ordinary array subscripting.
- **Code 2**: Thrust's distribution-example implementation, using `thrust::gather` + `make_transform_iterator` + counting iterators — the full fusion stack.

| device | matrix | Code 1 (s) | Code 2 (s) |
|---|---|---|---|
| GeForce 9800 GTX | 10000² | 3.67 | 3.75 |
| Tesla C2050 | 10000² | 3.43 | 3.50 |
| OpenMP 2 threads | 6000² | **9.57** | **23.01** |
| OpenMP 4 threads | 6000² | 5.17 | 10.62 |
| OpenMP 8 threads | 6000² | 3.01 | 7.42 |
| OpenMP 16 threads | 6000² | 1.99 | 3.35 |

The simpler `for_each`-plus-pointer-functor wins everywhere — slightly on CUDA, **2-2.4× on OpenMP**. The chapter doesn't fully explain why, but the implication is the fancy-iterator machinery (`thrust::unary_function` base, `make_transform_iterator` wrapping, counting-iterator end-deduction) pays a per-element overhead that exceeds the memory-traffic savings, especially when the consuming algorithm and the predicate functor are simple enough to be near-bandwidth-bound on their own.

## Error-message UX ([[parproc-ch06-thrust-programming]] §6.13)

Two failure modes:

- `terminate called after throwing an instance of 'std::bad_alloc' / what(): std::bad_alloc` — *"may mean that Thrust wasn't able to allocate your large array on the GPU."*
- Forgetting `.begin()` on a Thrust container, or missing an `#include`, produces *"a very long megillah as an error message, a highly uninformative one. Keep this in mind if you get a 30-line compiler error."* Standard heavy-C++-template-library hazard.

## Caveats (inherited from §5.18, reinforced in Ch6)

- **Kernel-launch overhead per call** — *"each Thrust call invokes considerable overhead"* ([[parproc-ch06-thrust-programming]] §6.8). Batch where possible; use fancy-iterator fusion to combine pipeline stages.
- **Optimized but not optimal** — handwritten CUDA can beat Thrust in specialized cases. §6.9 shows even hand-tuned-within-Thrust beats Thrust's own example code.
- **C++** — unlike [[CUBLAS]] / [[CUFFT]] (callable from C), Thrust requires C++ host code. The `extern "C"` wrapper pattern (§6.3) is the workaround for C/Fortran/R callers.
- **No parallel loop primitive** — emulate via `sequence` + `transform` or via counting iterators.

## See also

- [[CUDA]] — the primary backend.
- [[OpenMP]] — the alternate backend; the cross-target story is Thrust's distinguishing feature.
- [[CUBLAS]] / [[CUFFT]] — sibling NVIDIA libraries (CUDA-only).
- [[Functor]] — the stateful-callable mechanism Thrust uses pervasively.
- [[FancyIterator]] — umbrella for [[CountingIterator]] / [[TransformIterator]] / [[ZipIterator]] / [[DiscardIterator]] / [[PermutationIterator]].
- [[ScatterOperation]] / [[GatherOperation]] — Thrust's permutation primitives.
- [[PrefixScan]] — Thrust's `inclusive_scan` / `exclusive_scan`.
- [[STLForGPU]] — the design pattern Thrust embodies.
- [[parproc-ch05-cuda-gpu-programming]] — §5.18.2 (introduction-by-deferral).
- [[parproc-ch06-thrust-programming]] — the full chapter.
