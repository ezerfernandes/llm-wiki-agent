---
title: "ParProcBook Ch6: Introduction to Thrust Programming"
type: source
tags: [textbook, parallel-computing, thrust, cuda, openmp, stl]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch6: Introduction to Thrust Programming

Chapter 6 (book pp. 157–180, PDF pp. 177–200) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. A twenty-four-page applied tour of [[Thrust]] — the **C++ STL-modeled template library** that ships with [[CUDA]] and compiles the **same source** against a CUDA back end (GPU), an [[OpenMP]] back end (multicore CPU), or an Intel TBB back end (often faster than OpenMP). Chapter 5 (§5.18.2) only flagged Thrust's existence; Ch6 is the full treatment. Structured around eight worked examples — counting distinct values in an array, a plain-C wrapper around `thrust::sort`, percentile calculation with `copy_if`, doubling every k-th element via Thrust↔CUDA pointer-cast interop, scatter/gather permutation, matrix transpose (twice — once with [[ScatterOperation|`scatter()`]], once with [[FancyIterator|fancy iterators]] and `gather()`), an adjacency-matrix transformation with [[CountingIterator|counting iterators]] and a [[DiscardIterator|discard iterator]], and a prefix-scan one-liner — that build up Thrust's API surface and demonstrate the **functor + iterator** programming model the library inherits from the C++ STL.

## Summary

Ch6 frames [[Thrust]] as *"in the spirit of [[CUBLAS]] and other packages, [...] another package to ease CUDA programming"* — but with a critical distinguishing feature: Thrust is **back-end-portable**. The library *"uses the C++ STL library as a model"* and *"is indeed a C++ template library"*, so the abstraction that lets STL algorithms work on any container also lets Thrust algorithms target any of three parallel substrates without source changes.

**§6.1 Compiling Thrust Code.** Thrust ships with CUDA ≥ 4.0, so the CUDA path is just `nvcc` with no special link flags. The OpenMP path uses ordinary `g++` plus three additions: `-fopenmp -lgomp` (the [[OpenMP]] runtime), `-DTHRUST_DEVICE_BACKEND=THRUST_DEVICE_BACKEND_OMP` (the back-end selector), and `-I/path/to/thrust` (the Thrust include tree). *"The result is real OpenMP code"* — *"the threads set up by Thrust will be OpenMP threads on the CPU rather than CUDA threads on the GPU."* `OMP_NUM_THREADS` controls thread count as in any OpenMP program. A footnote warns: *"threads will not be set up if you use host arrays/vectors"* — only `device_vector` triggers parallelism even with the OpenMP back end. A third back end, **Intel TBB**, is also available and *"often produces faster code than OpenMP"*.

**§6.2 Counting Unique Values in an Array.** The chapter's introductory example, organized as three Thrust-native phases: (a) sort the array, (b) compute element-wise differences against a one-position shift to mark transitions, (c) count the marks. The first version uses `thrust::host_vector<int> hv(1000)`, populates it with `thrust::generate(hv.begin(), hv.end(), rand16)` (where `rand16()` is an ordinary C function — *"rand16() is an ordinary function, not a functor, so we just write its name here, thus passing a pointer to the function"*), copies to device with `thrust::device_vector<int> dv = hv`, sorts in place via `thrust::sort(dv.begin(), dv.end())`, allocates a length-(n−1) difference vector, and calls

```cpp
thrust::transform(dv.begin(), dv.end()-1, dv.begin()+1, diffs.begin(), finddiff());
```

where `finddiff` is a **[[Functor|functor]]** — a C++ struct with an `__device__ int operator()(const int& x, const int& y) { return x==y ? 0 : 1; }`. The count of distinct values is then `thrust::reduce(diffs.begin(), diffs.end(), (int)0, thrust::plus<int>()) + 1`. A shorter rewrite uses `thrust::unique(dv.begin(), dv.end())` directly — returning an iterator one past the unique-prefix end, which subtracted from `dv.begin()` gives the distinct count. The chapter is explicit that `unique()` *"only removes consecutive duplicates, so the preliminary sort is still needed."*

**Functor explained.** *"A functor is a C++ mechanism to produce a callable function, largely similar in goal to using a pointer to a function. In the context above, we are turning a C++ struct into a callable function, and we can do so with classes too. Since structs and classes can have member variables, we can store needed data in them, and that is what distinguishes functors from function pointers — we can save state."* This **stateful-callable** property is what makes functors the right tool for parameterized parallel operations (the `ismultk` functor in §6.4 carries `k` as a member, the `transidx` functor in §6.7.1 carries matrix dimensions).

**Iterator semantics.** `dv.begin()` and `dv.end()` return values *"formally called iterators, and work in a manner similar to pointers"* — type `thrust::device_vector<int>::iterator` here. `end()` returns *one past the end*, matching STL convention. The transform call's first three iterators specify the input ranges (`begin, end-1, begin+1` — the original and shifted-by-one views over `dv`); the fourth is the output start; the fifth is the functor instance (note the parentheses — `finddiff()` constructs an instance and *returns a pointer to it*).

**§6.3 A Plain-C Wrapper for Thrust sort().** Thrust requires C++ host code, but C/Fortran/R callers can be served by a thin `extern "C"` wrapper:

```cpp
extern "C" void tsort(int *x, int *nx);
void tsort(int *x, int *nx) {
    int n = *nx;
    thrust::device_vector<int> dx(x, x+n);
    thrust::sort(dx.begin(), dx.end());
    thrust::copy(dx.begin(), dx.end(), x);
}
```

Compile the wrapper with `nvcc -c SortForC.cu`, then link with `gcc Main.c S*.o -L/usr/local/cuda/lib -lcudart` (or for the OpenMP back end, `g++ -mcmodel=medium -fopenmp -lgomp -DTHRUST_DEVICE_SYSTEM=THRUST_DEVICE_SYSTEM_OMP ...`). The example showcases the back-end-toggling property concretely: *the same `.cu` file* produces CUDA output under `nvcc` and OpenMP output under `g++` with the right `-D` flag.

**§6.4 Calculating Percentiles in an Array (`copy_if`).** *"One of the most useful types of Thrust operations is that provided by conditional functions. For instance, `copy_if()` acts as a filter, copying from an array only those elements that satisfy some predicate."* The worked program copies every k-th element (after sorting), giving the `i·k/n · 100` percentiles. The functor here — `ismultk` — has a **member variable** `const int increm`, initialized via constructor `ismultk(int _increm): increm(_increm) {}`, and an `operator()(const int i) { return i != 0 && (i % increm) == 0; }`. To produce the indices `0, 1, 2, ..., n-1` against which `ismultk` is applied, the chapter calls `thrust::sequence(seq.begin(), seq.end(), 0)`, noting **a key observation about Thrust's lack of explicit loop control**:

> *"The `sequence()` function simply generates an array consisting of 0,1,2,...,n-1. Note that **this is typically used because Thrust has no direct parallel loop facilities**."*

`copy_if` signature: `copy_if(a.begin(), a.end(), b.begin(), c.begin(), callable_struct(args))` — *"the 'copy' part referring to the vector a, and the 'if' part referring to b. So, the call is saying copy the parts of a that satisfy the conditions specified by b and the callable struct, and place the results in c."* The chapter dwells on functor-as-state — *"`incrim` acts as a 'global' variable to all the actions of the operator"* — and on the equivalence of `ismultk(incr)` to *"creating a function, after which we pass a pointer to that function to `thrust::copy_if()`."*

**§6.5 Mixing Thrust and CUDA Code.** Two interop functions bridge between Thrust's typed iterators and CUDA's raw `int*`:

- `thrust::raw_pointer_cast(&w[0])` — extract a CUDA-style device pointer from a Thrust `device_vector` so it can be used in handwritten CUDA kernels or with `wd[i] = 2 * wd[i]` array subscripting inside a functor.
- `thrust::device_ptr<int> tz(dz)` — wrap a raw `cudaMalloc`-returned `int*` so Thrust algorithms (`thrust::reduce(tz, tz+100, ...)`) can operate on it.

The asymmetry — one cast per direction — exposes the rule: **Thrust owns its containers' memory; CUDA owns raw pointers; cast at the boundary.**

**§6.6 Doubling Every k-th Element (functor-with-iterator).** Extends §6.4: instead of filtering into an output, mutate the input in place. The `ismultk` functor here takes a `thrust::device_vector<int>::iterator _w` in its constructor, immediately calls `wd = thrust::raw_pointer_cast(&w[0])` to extract a raw `int*` member, and inside `operator()` does ordinary C subscripting: `if (i != 0 && (i % increm) == 0) wd[i] = 2 * wd[i]`. The structural trick exposed here:

> *"One of the functor's arguments is an iterator, rather than a simple type like int. This is really just like passing an array pointer to an ordinary C function. [...] The point of converting to the raw array here was to enable the use of ordinary array subscripting, rather than Thrust iterators."*

Note also: *"Our call to `copy_if()` doesn't actually do any copying. We are exploiting the 'if' in 'copy if,' not the 'copy.'"* — `copy_if`'s output is unused; its iteration is the side-effecting work.

**§6.7 Scatter and Gather Operations.** Two complementary permutation primitives, parameterized by a *map* vector `m`:

- **[[ScatterOperation|`scatter(src.begin(), src.end(), m.begin(), dst.begin())`]]** — *"the original `x[0]` should now be at position 3, the original `x[1]` now at position 2, etc."* — `dst[m[i]] = src[i]`.
- **[[GatherOperation|`gather(m.begin(), m.end(), src.begin(), dst.begin())`]]** — *"the original `x[3]` should now be at position 0, etc."* — `dst[i] = src[m[i]]`.

The chapter justifies keeping both: *"one might be copying between two vectors of different sizes. Say for instance the source vector is larger than the destination one. Then only some elements from the source will be copied, so a scatter operation won't work, as it would require all source elements to be mapped. Thus a gather is useful. The opposite would be true if the destination vector is larger."*

**§6.7.1 Matrix Transpose (via `scatter`).** Stored in row-major one-dimensional layout. The `transidx` functor takes `nr` (rows) and `nc` (cols) as members, and for input index `i` computes `r = i/nc`, `c = i%nc`, then `out_idx = c*nr + r` — i.e. position of the transposed element. Construct the map via `thrust::transform(seq.begin(), seq.end(), dmap.begin(), transidx(nrow, ncol))`, then `thrust::scatter(dmat.begin(), dmat.end(), dmap.begin(), ddst.begin())`. *"Not much new here in terms of Thrust, just more complexity."* Performance caveat: *"the performance of this algorithm with a GPU backend would likely be better if matrix tiling were used (Section 11.2)."*

**§6.8 Advanced ("Fancy") Iterators.** Thrust's [[FancyIterator|fancy iterators]] save *"memory access time and memory space requirements"* by virtualizing intermediate arrays. *"Since each Thrust call invokes considerable overhead, Thrust offers some special iterators."* Four families:

- **[[CountingIterator|Counting iterators]]** — *"play the same role as `thrust::sequence()`, but without actually setting up an array, thus avoiding the memory issues."* `thrust::counting_iterator<int> seqb(0); auto seqe = seqb + n;` — virtual `0, 1, 2, ..., n-1`.
- **[[TransformIterator|Transform iterators]]** — *"if your code first calls `thrust::transform()` and then makes another Thrust call on the result, you can combine them, which the Thrust people call **fusion**."* Built via `thrust::make_transform_iterator(seq.begin(), transidx(nrow, ncol))` — produces an iterator that *applies `transidx` on-the-fly* as the consuming algorithm reads, saving *n* reads and *n* writes to the intermediate map array.
- **[[ZipIterator|Zip iterators]]** — *"essentially 'zip' together two arrays (picture two halves of a zipper lining up parallel to each other as you zip up a coat). This is often useful when one needs to retain information on the position of an element within its array."*
- **[[DiscardIterator|Discard iterators]]** — *"sometimes we call `transform()` but don't need its output. Discard iterators then act in a manner similar to `/dev/null`."*

**§6.8.1 Matrix Transpose Again (with fusion).** Same problem as §6.7.1, but the `transidx` map is **never materialized** — `thrust::scatter(dmat.begin(), dmat.end(), make_transform_iterator(seq.begin(), transidx(nrow, ncol)), ddst.begin())` feeds each computed map-index directly into `scatter`. *"That word **direct** is the salient one here; it means we save n memory reads and n memory writes. Moreover, we save the overhead of the kernel call, if our backend is CUDA."* A footnote: *"We are still writing to temporary storage, but that will probably be in registers (since we don't create the entire map at once), thus fast to access."* A required syntactic wrinkle for transform-iterator-compatible functors: *the struct must inherit from `thrust::unary_function<int, int>`* — *"It won't work without this!"* Also: counting iterators don't work directly with `scatter()` (*"the compiler encounters problems with determining where the end of the counting sequence is"*) but **do** work with `gather()` since *"the former specifies a beginning and an end for the map array."*

**§6.9 A Timing Comparison.** A direct head-to-head: **Code 1** is Matloff's own matrix transpose using `thrust::for_each` (a parallel "do this functor on every element in this range, no output required") with a `copyelt2xp` functor that holds `int *m1, *mxp1` raw pointers extracted via `raw_pointer_cast` and writes `mxp1[c*nrow+r] = m1[r*ncol+c]`. **Code 2** is the **Thrust distribution's own example**, using `thrust::gather` plus `thrust::make_transform_iterator` over `thrust::counting_iterator` — the full fancy-iterator fusion stack. Results on a 10000×10000 matrix:

| device | Code 1 (s) | Code 2 (s) |
|---|---|---|
| GeForce 9800 GTX | 3.67 | 3.75 |
| Tesla C2050 | 3.43 | 3.50 |

And on a multicore-CPU OpenMP back end with a 6000×6000 matrix:

| # threads | Code 1 (s) | Code 2 (s) |
|---|---|---|
| 2 | 9.57 | 23.01 |
| 4 | 5.17 | 10.62 |
| 8 | 3.01 | 7.42 |
| 16 | 1.99 | 3.35 |

The surprising headline: *"the simpler code, i.e. Code 1, is actually a little faster than Code 2 in the case of a CUDA backend, and a lot faster in the OpenMP case."* Fancy iterators are **not unconditionally faster** — `for_each` plus a stateful raw-pointer functor wins. This contradicts the §6.8 motivation paragraph's prima facie expectation; the chapter doesn't explain why but the implication is **the OpenMP back end pays more overhead for fancy-iterator machinery than for plain pointer loops**.

**§6.10 Transforming an Adjacency Matrix (using counting + discard iterators).** Same Ch4 §4.13 / Ch5 §5.13 problem — convert a 0/1 adjacency matrix to a 2-column edge list — now in Thrust. Two stages: (1) find linear indices of all 1s via `thrust::copy_if(seqb, seqe, dx.begin(), ones.begin(), thrust::identity<int>())` where `seqb, seqe` are **counting iterators** over `0..nrc` and the predicate is `thrust::identity<int>()` (returns the input value, so 1 means "copy", 0 means "skip"); (2) for each 1-position `i`, write the pair `(i/nc, i%nc)` into the output via `thrust::transform(ones.begin(), newend, seq2b, thrust::make_discard_iterator(), makerow(newmat.begin(), nc))`. The `makerow` functor extracts a raw pointer from the output `device_vector` iterator in its constructor and uses `operator()(const int i, const int j)` to write *as a side effect* — *"the construction of the output matrix, `newmat`, is actually done as a side effect of calling `makerow()`. For this reason, we've set our third parameter to `thrust::make_discard_iterator()`. Since we never use the output from `transform()` itself, and it thus would be wasteful — of both memory space and memory bandwidth — to store that output in a real array."* The chapter is explicit about why this is two stages: *"we don't know the size of the output matrix in advance; counting the 1s separately gives us that information. Without that, we'd either have to make the output matrix too large initially and then shrink it, or continually expand it as we go through the computation. The latter would probably result in a major slowdown, as memory allocation takes time."*

**§6.11 Prefix Scan.** A one-liner: `thrust::inclusive_scan(hx.begin(), hx.end(), hx.begin())` — in-place, default `+` operation. *"Thrust includes functions for prefix scan (see Chapter 10)."* Both inclusive and exclusive variants exist; this section is short because the algorithmic theory is deferred to Ch10, but its presence here is the chapter's demonstration that the **[[PrefixScan|prefix-scan]] primitive** is one of Thrust's headline operations.

**§6.12 More on Thrust as CUDA Backend.**

- **§6.12.1 Synchronicity.** *"Thrust calls are in fact CUDA kernel calls, and thus entail some latency. Other than the `transform()`-family functions, the calls are all synchronous."* The transform family is async (returns control to the host before the kernel completes); everything else blocks on completion. This is the **inverted default** vs raw CUDA (where kernel launches are always async); programmers porting from CUDA must remember the flip.

**§6.13 Error Messages.** Two failure modes worth recognizing:
- `terminate called after throwing an instance of 'std::bad_alloc' / what(): std::bad_alloc` *"may mean that Thrust wasn't able to allocate your large array on the GPU."*
- Forgetting `.begin()` on a Thrust container (e.g. `thrust::copy_if(hx.begin(), hx.end(), seq, out, ismultk(...))` instead of `seq.begin()`) — *"would have been fine [for a non-Thrust array] but not for a Thrust array."* The compiler emits *"a very long megillah as an error message, a highly uninformative one. Keep this in mind if you get a 30-line compiler error."* Forgetting `#include` files produces the same template-deduction-failure mess.

**§6.14 Other Examples of Thrust Code in This Book.** One forward pointer: *"an application of Thrust's prefix-scan functionality is presented in Section 10.6."*

## Key Claims

- **[[Thrust]] is a C++ template library modeled on the STL.** *"It uses the C++ STL library as a model, and Thrust is indeed a C++ template library. It includes various data manipulation routines, such as for sorting and prefix scan operations."* (§6 intro, p. 157). The STL inheritance — `host_vector` / `device_vector` containers, iterators with `begin()`/`end()`, generic algorithms (`sort`, `transform`, `reduce`, `copy_if`, `unique`, `scatter`, `gather`, `inclusive_scan`), function objects (functors) — is the chapter's organizing API metaphor.
- **Three back ends: CUDA, OpenMP, Intel TBB.** *"In addition to the CUDA back end, for running on the GPU, one can also choose OpenMP as the back end. The latter choice allows the high-level expressive power of Thrust to be used on multicore machines. A third choice is Intel's TBB language, which often produces faster code than OpenMP."* (§6.1, p. 157). The back end is **chosen at compile time** via `-DTHRUST_DEVICE_BACKEND` (or, in newer Thrust, `THRUST_DEVICE_SYSTEM`); the same source code re-compiles to a different target.
- **CUDA compilation needs no special flags.** *"If your CUDA version is at least 4.0, then Thrust is included, which will be assumed here. In that case, you compile Thrust code with nvcc, no special link commands needed."* (§6.1.1, p. 157).
- **OpenMP compilation needs three additions.** `-fopenmp -lgomp` for the OpenMP runtime; `-DTHRUST_DEVICE_BACKEND=THRUST_DEVICE_BACKEND_OMP` for the back-end selector; `-I/path/to/thrust` for the include tree. *"The result is real OpenMP code. Everywhere you set up a Thrust vector, you'll be using OpenMP, i.e. the threads set up by Thrust will be OpenMP threads on the CPU rather than CUDA threads on the GPU."* (§6.1.2, p. 158). `OMP_NUM_THREADS` controls threading as usual.
- **Host vectors don't parallelize.** *"Threads will not be set up if you use host arrays/vectors."* (§6.1.2 footnote, p. 158). Parallelism is bound to `device_vector` (which, under the OpenMP back end, lives in **host memory** but triggers thread teams for algorithms that operate on it). This is non-obvious — under OpenMP-back-end Thrust, "device" is the CPU but you still use `device_vector`.
- **A [[Functor|functor]] is a stateful callable.** *"A functor is a C++ mechanism to produce a callable function, largely similar in goal to using a pointer to a function. [...] Since structs and classes can have member variables, we can store needed data in them, and that is what distinguishes functors from function pointers — we can save state."* (§6.2, p. 160). Functor-with-state is the canonical way to parameterize a parallel operation in Thrust.
- **Functor-creating syntax has parentheses.** `thrust::transform(..., finddiff())` calls the **constructor** of `finddiff`, producing an instance whose `operator()` will be invoked per element. By contrast, `thrust::generate(..., rand16)` passes a function pointer (no parens), because `rand16` is a plain function, not a functor. *"Note the parentheses in 'finddiff().' This is basically a constructor, creating an instance of a `finddiff` object and returning a pointer to it. By contrast, in the code `thrust::generate(hv.begin(), hv.end(), rand16);` `rand16()` is an ordinary function, not a functor, so we just write its name here."* (§6.2, p. 160).
- **Thrust has no parallel loop primitive — `sequence()` substitutes.** *"`sequence()` simply generates an array consisting of 0,1,2,...,n-1. Note that this is typically used because Thrust has no direct parallel loop facilities."* (§6.4, p. 164). The canonical idiom is: `thrust::sequence(seq.begin(), seq.end(), 0)`, then `thrust::transform`/`copy_if` over `seq` with a functor that uses the index.
- **`copy_if`'s 5-argument form is filter-with-stencil.** Signature `copy_if(a.begin(), a.end(), b.begin(), c.begin(), pred)` — *"copy the parts of a that satisfy the conditions specified by b and the callable struct, and place the results in c."* (§6.4, p. 164). The 4-argument form (`copy_if(a.begin(), a.end(), c.begin(), pred)`) uses elements of `a` itself as the predicate input.
- **`unique()` only removes consecutive duplicates.** *"That function only removes consecutive duplicates, so the preliminary sort is still needed."* (§6.2, p. 161). A trap for users coming from set-style "unique" semantics.
- **Two casts bridge Thrust and CUDA.** `thrust::raw_pointer_cast(&w[0])` extracts a raw `int*` from a Thrust device container for use with hand-written CUDA kernels or array subscripting. `thrust::device_ptr<int> tz(dz)` wraps a raw `cudaMalloc`-allocated `int*` for use with Thrust algorithms. (§6.5, p. 165). Thrust **owns its memory**; CUDA owns raw pointers; cast at the boundary.
- **[[ScatterOperation|`scatter`]] writes `dst[m[i]] = src[i]`; [[GatherOperation|`gather`]] writes `dst[i] = src[m[i]]`.** Both take a *map* vector. Both are present because scatter requires every source element to be placed (so destination must be ≥ source size) and gather requires every destination element to be sourced (so destination drives the loop). (§6.7, p. 167–169).
- **Counting iterators virtualize `sequence()`'s output.** `thrust::counting_iterator<int> seqb(0); auto seqe = seqb + n;` — *"play the same role as `thrust::sequence()`, but without actually setting up an array, thus avoiding the memory issues."* (§6.8, p. 170).
- **Transform iterators implement fusion.** `thrust::make_transform_iterator(seq.begin(), F)` produces an iterator that applies `F` lazily. Used inside a consuming algorithm (e.g. `scatter`, `gather`), this *"saves n memory reads and n memory writes. Moreover, we save the overhead of the kernel call, if our backend is CUDA."* (§6.8.1, p. 172). **Required syntactic constraint**: the functor must inherit from `thrust::unary_function<In, Out>`. *"It won't work without this!"*
- **Counting iterators work with `gather()` but not `scatter()`.** *"The compiler encounters problems with determining where the end of the counting sequence is [in `scatter()`]. [...] `gather()` instead of `scatter()`. Since the former specifies a beginning and an end for the map array, counting iterators work fine."* (§6.8.1, p. 172).
- **Zip iterators co-iterate parallel arrays.** *"Essentially 'zip' together two arrays [...] This is often useful when one needs to retain information on the position of an element within its array."* (§6.8, p. 170).
- **Discard iterators are `/dev/null`.** *"Sometimes we call `transform()` but don't need its output. Discard iterators then act in a manner similar to `/dev/null`."* (§6.8, p. 170). Used when the work is in the functor's side effects.
- **Fancy iterators are not unconditionally faster.** The §6.9 timing table shows a hand-rolled `for_each`-plus-raw-pointer-functor (Code 1) beating the fancy-iterator gather/transform-iterator/counting-iterator stack (Code 2) — slightly on CUDA backends (3.67 vs 3.75 s on a 10000² matrix on the GeForce 9800 GTX), substantially on OpenMP (9.57 vs 23.01 s on a 6000² matrix at 2 threads — 2.4×). *"The simpler code, i.e. Code 1, is actually a little faster than Code 2 in the case of a CUDA backend, and a lot faster in the OpenMP case."* (§6.9, p. 176).
- **Thrust calls are CUDA kernel calls.** *"Thrust calls are in fact CUDA kernel calls, and thus entail some latency."* (§6.12.1, p. 179). Every Thrust operation pays the per-launch overhead Ch5 §5.18 warned about.
- **The `transform()` family is async; everything else is sync.** *"Other than the `transform()`-family functions, the calls are all synchronous."* (§6.12.1, p. 179). Inverted from raw-CUDA convention; common source of correctness bugs when porting CUDA → Thrust.
- **`std::bad_alloc` usually means "couldn't fit on the GPU".** *"A message like 'terminate called after throwing an instance of std::bad_alloc' [...] may mean that Thrust wasn't able to allocate your large array on the GPU."* (§6.13, p. 179).
- **Compiler errors are template-deduction megillahs.** *"The compiler gives us a very long megillah as an error message, a highly uninformative one. Keep this in mind if you get a 30-line compiler error. The same thing happens if we forget to state the proper 'include' files."* (§6.13, p. 180). The same hazard exists in any heavy C++ template library; Thrust just inherits it.

## Key Quotes

> *"In the spirit of CUBLAS and other packages, the CUDA people have brought in another package to ease CUDA programming, Thrust. It uses the C++ STL library as a model, and Thrust is indeed a C++ template library. It includes various data manipulation routines, such as for sorting and prefix scan operations."* — §6 intro, p. 157. Thrust's STL inheritance is established in the chapter's first paragraph.

> *"Thrust allows the programmer a choice of back ends, i.e. platforms on which the executable code will run. In addition to the CUDA back end, for running on the GPU, one can also choose OpenMP as the back end. [...] A third choice is Intel's TBB language, which often produces faster code than OpenMP."* — §6.1, p. 157. The back-end portability statement.

> *"A functor is a C++ mechanism to produce a callable function, largely similar in goal to using a pointer to a function. [...] Since structs and classes can have member variables, we can store needed data in them, and that is what distinguishes functors from function pointers — we can save state."* — §6.2, p. 160. The functor definition.

> *"`sequence()` simply generates an array consisting of 0,1,2,...,n-1. Note that this is typically used because Thrust has no direct parallel loop facilities."* — §6.4, p. 164. A surprising absence — no `parallel_for`-style primitive — that drives the `sequence`/`counting_iterator` idioms.

> *"You might think that, having one of the scatter/gather operations available might make the other redundant, but it's handy to have both, because one might be copying between two vectors of different sizes."* — §6.7, p. 169. Why scatter and gather both exist.

> *"Since each Thrust call invokes considerable overhead, Thrust offers some special iterators to reduce memory access time and memory space requirements."* — §6.8, p. 170. The fancy-iterator motivation in one sentence.

> *"Essentially our use of `make_transform_iterator()` is telling Thrust, 'Don't apply `transidx()` to `seq` yet. Instead, perform that operation as you go along, and feed each result of `transidx()` directly into `scatter()`.' That word **direct** is the salient one here; it means we save n memory reads and n memory writes. Moreover, we save the overhead of the kernel call, if our backend is CUDA."* — §6.8.1, p. 172. The fusion-as-streaming framing.

> *"It turns out, though, that — good news! — the simpler code, i.e. Code 1, is actually a little faster than Code 2 in the case of a CUDA backend, and a lot faster in the OpenMP case."* — §6.9, p. 176. The counter-intuitive timing-comparison headline.

> *"Thrust calls are in fact CUDA kernel calls, and thus entail some latency. Other than the `transform()`-family functions, the calls are all synchronous."* — §6.12.1, p. 179. The synchronicity rule.

> *"The compiler gives us a very long megillah as an error message, a highly uninformative one. Keep this in mind if you get a 30-line compiler error."* — §6.13, p. 180. The template-deduction-error UX warning.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[parproc-ch01-intro-parallel-processing]] — Ch1's survey listed [[OpenMP]] as the *"de facto standard for shared-memory programming"* on multicore; Ch6 lets the **same Thrust source code** target both [[CUDA]] (GPU) and [[OpenMP]] (multicore) back ends. The cross-substrate property folds Ch1's shared-memory / GPU / message-passing trichotomy into a single API surface for the first two.
- [[parproc-ch02-recurring-performance-issues]] — Ch2's [[Latency]] / overhead vocabulary recurs explicitly in *"each Thrust call invokes considerable overhead"* and *"Thrust calls are in fact CUDA kernel calls"*; the **fancy-iterator fusion** of §6.8 is a Thrust-specific instance of Ch2's latency-hiding-by-fusion theme.
- [[parproc-ch03-shared-memory-parallelism]] — Ch3's shared-memory hardware substrate is the OpenMP back end's deployment target; the §6.9 timing comparison's OpenMP runs are Ch3's hardware in action.
- [[parproc-ch04-introduction-to-openmp]] — Ch4's [[OpenMP]] pragma model is *what Thrust compiles to* under the `THRUST_DEVICE_BACKEND_OMP` switch. `OMP_NUM_THREADS` is the explicit lever from Ch4.
- [[parproc-ch05-cuda-gpu-programming]] — Ch5 §5.18.2 introduced [[Thrust]] but deferred full treatment to Ch6 (*"So I've put my coverage of Thrust in a separate chapter"*). Ch6 cashes the deferral. Ch5's [[CUBLAS]] / [[CUFFT]] are positioned as siblings to Thrust in the CUDA wrapper-library family; the **per-kernel-call overhead** warning from §5.18 is re-stated at §6.12.1.
- [[Thrust]] — substantially expanded by this ingest with the full API surface (`host_vector`/`device_vector`, `sort`, `transform`, `reduce`, `copy_if`, `unique`, `scatter`, `gather`, `inclusive_scan`, `sequence`, `for_each`, `generate`, `raw_pointer_cast`, `device_ptr`), back-end selection mechanics, fancy iterators, sync semantics, and error-message UX.
- [[CUDA]] — Thrust is one of three CUDA wrapper libraries (Ch5 §5.18). Thrust↔CUDA interop via `raw_pointer_cast` and `device_ptr` is the new content for the [[CUDA]] page from this chapter.
- [[OpenMP]] — Thrust's second back end. Same source compiles to OpenMP threads via the `-DTHRUST_DEVICE_BACKEND=THRUST_DEVICE_BACKEND_OMP` macro plus `-fopenmp -lgomp`. **`OMP_NUM_THREADS`** is the runtime knob.
- [[CUBLAS]] / [[CUFFT]] — sibling CUDA-only wrapper libraries; Ch6 implicitly contrasts Thrust's back-end portability with their CUDA-only nature.
- [[NVIDIA]] — vendor of CUDA + Thrust.
- [[STLForGPU]] — new concept page; the design pattern Thrust embodies (STL algorithms + STL iterators + STL function objects, transplanted to parallel substrates).
- [[Functor]] — new concept page; the C++ "callable struct/class with state" idiom Thrust uses pervasively.
- [[FancyIterator]] — new concept page; Thrust's umbrella term for counting / transform / zip / discard / permutation iterators.
- [[CountingIterator]] — new concept page; virtual `0..n-1` iterator that doesn't materialize an array.
- [[TransformIterator]] — new concept page; lazy-evaluation iterator implementing **fusion** of `transform()` with a consuming algorithm.
- [[PermutationIterator]] — new concept page; iterator that gathers via an index map (not in Ch6's worked examples but listed in the Thrust feature surface).
- [[ZipIterator]] — new concept page; iterator that co-iterates parallel arrays as tuples.
- [[DiscardIterator]] — new concept page; `/dev/null` output iterator for side-effecting `transform` calls.
- [[PrefixScan]] — new concept page; `inclusive_scan` / `exclusive_scan` parallel scan primitive deferred theoretically to Ch10 but exposed in Thrust as a one-line API.
- [[ScatterOperation]] — new concept page; Thrust's `scatter(src, src_end, map, dst)` permutation primitive (`dst[map[i]] = src[i]`). Distinct from the [[ScatterGather|scatter/gather manager-worker pattern]] of Ch1 — same word, different abstraction level.
- [[GatherOperation]] — new concept page; Thrust's `gather(map, map_end, src, dst)` permutation primitive (`dst[i] = src[map[i]]`).
- [[ParallelComputing]] — overarching domain.
- [[SharedMemoryArchitecture]] — substrate for the OpenMP back end.

## Contradictions

- **No contradictions with prior wiki content.** Ch6 deepens rather than overrides Ch5's brief Thrust treatment. The earlier [[Thrust]] page's *"Thrust spans CUDA and OpenMP"* / *"each call involves a CUDA kernel call"* / *"handwritten CUDA can beat Thrust in specialized cases"* claims are all confirmed and operationalized here.
- **Internal contradiction between §6.8's motivation and §6.9's results.** §6.8 motivates fancy iterators as memory-access-and-overhead savers (*"saves n memory reads and n memory writes"*). §6.9's measurements show a non-fancy `for_each` + raw-pointer functor beats the fancy-iterator fused stack on both CUDA (slightly) and OpenMP (substantially). The chapter does not reconcile the two — readers must infer that **the fancy-iterator machinery's own overhead can exceed the memory-traffic savings it provides**, especially under the OpenMP back end. This is a tension within Ch6, not with prior chapters.
- **Naming clash with Ch1 [[ScatterGather]].** Ch1's *scatter/gather* refers to the manager-worker pattern (one node parcels work, workers compute, manager aggregates). Ch6's `thrust::scatter` / `thrust::gather` refer to *permutation operations on a single device's memory*. The wiki disambiguates by giving the Thrust primitives their own pages ([[ScatterOperation]] / [[GatherOperation]]) and leaving [[ScatterGather]] for the manager-worker pattern. The chapter doesn't acknowledge the clash but readers crossing from Ch1 should note the distinct meanings.
- **Tesla-baseline timing numbers (§6.9).** The 9800 GTX and Tesla C2050 GPUs are pre-Fermi / Fermi-era; OpenMP timings are on an unnamed multi-core machine *"with many more cores than the 16 we tried."* Modern hardware would shift absolute numbers significantly but the *qualitative* result (simpler code wins) is the takeaway the chapter highlights, and that is plausibly architecture-independent.
- **Async transform vs Ch5's "kernels are always async".** Ch5 §5.3 stated all CUDA kernel launches are non-blocking. Ch6 §6.12.1 says Thrust calls are *"all synchronous"* **except the `transform()` family**. The Thrust runtime adds an implicit `cudaThreadSynchronize` (or equivalent) after most algorithm calls, inverting raw-CUDA's default. This is *not* a contradiction — it's a wrapper-library convention layered over the raw-CUDA primitive — but porting CUDA → Thrust code must account for the flip.
