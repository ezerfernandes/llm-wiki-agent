---
title: "ParProcBook Ch10: The Parallel Prefix Problem"
type: source
tags: [textbook, parallel-computing, prefix-scan, openmp, thrust]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch10: The Parallel Prefix Problem

Chapter 10 (book pp. 223–234, PDF pp. 243–254) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. The chapter centralises the [[PrefixScan]] (parallel prefix) primitive: defines inclusive vs exclusive scan over any associative operator, presents the [[HillisSteeleScan|Hillis-Steele]] data-parallel algorithm, covers the blocked reduction strategy for the general n > p case, catalogues platform implementations ([[MPI]], TBB, [[Thrust]]), and works three applications — parallel prefix summing in [[OpenMP]], [[RunLengthEncoding|run-length decompression]] in both [[OpenMP]] and [[Thrust]], and [[MovingAverage|moving average]] via Thrust's `exclusive_scan` + `transform` — closing with C++11 [[LambdaFunction]] syntax as a cleaner functor alternative.

## Summary

§10.1 motivates the chapter through a permutations example: applying a sequence of permutation matrices via matrix multiplication fits the scan definition with $\otimes$ = matrix multiplication and non-scalar elements, establishing that the operator need not be commutative. §10.2 presents the [[HillisSteeleScan|Hillis-Steele]] data-parallel algorithm for n = p threads in $\log_2 n$ rounds (step 1 combines elements 1 apart, step 2 elements 2 apart, step 3 elements 4 apart), with the auxiliary **red/black** double-buffer technique to avoid read-after-write hazards; extends to the n > p case via a blocked three-phase approach (serial scan per block → parallel scan of block sums → add block-sum offsets back). §10.3 notes that `MPI_Scan()`, Intel TBB, Thrust (`thrust::inclusive_scan` / `thrust::exclusive_scan`), and CUDPP each provide the primitive natively. §10.4 codes the blocked approach in [[OpenMP]]; §10.5 uses `parprfsum` to decompress [[RunLengthEncoding|run-length-coded]] data — prefix-summing run counts gives starting offsets for each run. §10.6 re-implements the placement step in [[Thrust]] using `copy_if` + `thrust::sequence` + `thrust::inclusive_scan` to extract even-indexed elements then scan their counts. §10.7 implements [[MovingAverage]] as `exclusive_scan` of the input → subtract shifted cumulative sums and divide by window width — a concise prefix-based derivation; §10.7.3 replaces the `minus_and_divide` functor struct with a C++11 [[LambdaFunction]] captured by value.

## Key Claims

- **Prefix scan / parallel prefix are the same operation.** *"An operation that arises in a variety of parallel algorithms is that of prefix (or scan)."* (p. 223). Given $(x_0, ..., x_{n-1})$ and associative $\otimes$, the output is $(s_0, ..., s_{n-1})$ where $s_i = x_0 \otimes x_1 \otimes \cdots \otimes x_i$. This is the **inclusive** variant; the **exclusive** variant shifts by one position and sets $s_0$ to the identity.
- **Elements can be non-scalar and the operator need not be commutative.** §10.1's permutation example represents each permutation as a matrix and uses matrix multiplication as $\otimes$. *"The elements might be nonscalars"* and *"the associative operator need not be commutative."* (p. 224). This generalises scan well beyond prefix sums.
- **The Hillis-Steele algorithm runs in $\log_2 n$ steps with n threads.** §10.2's data-parallel algorithm processes distances 1, 2, 4, ... in successive steps; all n updates at each step run in parallel. For n not a power of 2, the step count is $\lfloor \log_2 n \rfloor$. (p. 225–226).
- **Hillis-Steele requires an auxiliary array to avoid read-before-write hazards.** Because each step reads and writes the same logical array, a **red/black** double-buffer must alternate between two physical arrays across odd and even steps. (p. 226, footnote 1).
- **Hillis-Steele has O(n log n) total work vs O(n) for sequential scan.** More threads become idle in each successive step; load balancing is poor and synchronisation at each step adds overhead. (p. 226).
- **The blocked n > p strategy restores O(n) work for prefix sums.** The three phases — (1) each of p threads serially scans its contiguous chunk; (2) p–1 rightmost elements form array G, which is scanned in parallel; (3) each thread i > 0 adds G[i–1] to every element of its chunk — run in O(n/p + log p) time. (p. 226, pseudocode lines 1–7).
- **The blocked approach is the standard production strategy.** *"The standard approach is that taken in Section 5.11"* — the same blocked plan introduced for CUDA in Ch5 is reused here for OpenMP. (p. 226).
- **MPI, TBB, Thrust, and CUDPP all provide native prefix scan.** `MPI_Scan()` supports max/min/sum/product/etc.; Intel TBB includes a scan; Thrust exposes `thrust::inclusive_scan()` and `thrust::exclusive_scan()`; CUDPP contains CUDA functions for sorting and other operations based on parallel scan. (p. 227).
- **Run-length decompression maps onto prefix scan naturally.** Compressed data alternates run-counts and run-values. An exclusive prefix sum of the run-counts gives the starting offset of each run in the output array; per-run fill can then proceed in parallel. (§10.5, p. 228).
- **Thrust's `copy_if` + `sequence` + `inclusive_scan` implements the placement step.** The even-indexed elements of the compressed array are the run-counts; `copy_if` with an `iseven` predicate extracts them; `inclusive_scan` converts them to end-positions from which start-positions are derived. (§10.6, pp. 229–230).
- **Moving average reduces to two prefix sums and a subtract-divide.** Given input $x_1, ..., x_n$ and window width $w$, compute exclusive cumulative sums $c_i$; then $a_i = (c_i - c_{i-w}) / w$. Only one `exclusive_scan` call and one `transform` call are needed. (§10.7.2, p. 232, eq. 10.22).
- **C++11 lambda functions eliminate functor boilerplate in Thrust.** The `minus_and_divide` struct with `operator()` can be replaced inline by `[=](double& a, double& b){ return (a-b)/wa; }`. The `[=]` capture-by-value bracket makes outer variables (here `wa`) accessible inside the lambda without passing them as arguments. (§10.7.3, pp. 232–234).
- **Lambda capture modes: `=` for by-value, `&` for by-reference.** If mutation of the captured variable is needed, `&` is used instead of `=`. (p. 234).

## Key Quotes

> *"An operation that arises in a variety of parallel algorithms is that of prefix (or scan)."* — p. 223. Positions prefix scan as a general parallel primitive.

> *"The elements might be nonscalars [and] the associative operator need not be commutative."* — p. 224. Generalises beyond prefix sums to, e.g., permutation-matrix composition.

> *"There will be $\log_2 n$ steps, or if n is not a power of 2, the number of steps is $\lfloor \log_2 n \rfloor$."* — p. 226. The depth cost of the Hillis-Steele algorithm.

> *"As time goes on, more and more threads are idle. Thus load balancing is poor."* — p. 226. The key algorithmic weakness of Hillis-Steele for the n = p case.

> *"The Thrust library for CUDA or OpenMP includes functions `thrust::inclusive_scan()` and `thrust::exclusive_scan()`."* — p. 227. Native platform support.

> *"All this is so much clearer and cleaner than using a functor!"* — p. 234. Matloff's endorsement of C++11 lambdas over struct-based functors for Thrust usage.

## Connections

- [[NormMatloff]] — author; Rth package (§10.7.1) is his own R–Thrust interface.
- [[UCDavis]] — author's institution.
- [[PrefixScan]] — chapter subject; substantially expanded with Hillis-Steele algorithm, blocked strategy, complexity analysis, applications, and platform support.
- [[HillisSteeleScan]] — §10.2's data-parallel $\log_2 n$-round algorithm; new concept page created.
- [[BlellochScan]] — the up-sweep/down-sweep work-efficient algorithm; not explicitly named in Ch10 but the blocked strategy relates to it; referenced in expanded [[PrefixScan]] page.
- [[RunLengthEncoding]] — §10.5–10.6 application; new concept page created.
- [[MovingAverage]] — §10.7 application; new concept page created.
- [[LambdaFunction]] — §10.7.3 C++11 feature; new concept page created.
- [[OpenMP]] — §10.4 and §10.5 implementation platform.
- [[Thrust]] — §10.6 and §10.7 implementation platform; `inclusive_scan`, `exclusive_scan`, `copy_if`, `transform`, `sequence`.
- [[Block]] — the blocked n > p decomposition strategy; each thread owns one contiguous block.
- [[Warp]] — GPU context; idle threads in later Hillis-Steele rounds cause warp divergence.
- [[parproc-ch05-cuda-gpu-programming]] — §5.11 introduced the blocked prefix-sum approach in CUDA; Ch10 §10.2 adopts the same three-phase strategy for multicore.
- [[parproc-ch06-thrust-programming]] — §6.11 introduced Thrust's scan API; Ch10 §10.6–10.7 provide the deferred application examples forward-referenced by Ch6.
- [[parproc-ch09-mapreduce-computation]] — prior chapter; no direct connection to prefix scan.

## Contradictions

- **No outright contradictions with prior wiki content.** Ch10 completes the deferred examples Ch5 (§5.11) and Ch6 (§6.11, §6.14) promised, consistently extending the existing [[PrefixScan]] page.
- **Hillis-Steele is O(n log n) work, not O(n).** The existing [[PrefixScan]] page stated *"$O(\log n)$-depth parallel algorithm"* (correct for depth/span) but did not call out total work being O(n log n) vs sequential O(n). Ch10 explicitly notes poor load balancing and idle threads. The expansion of [[PrefixScan]] adds this nuance.
- **The chapter does not use the name "Blelloch."** The work-efficient two-pass (up-sweep/down-sweep) algorithm is the standard counterpoint to Hillis-Steele in the literature, but Ch10 presents only the blocked serial-then-parallel strategy for n > p, not a pure O(n) work algorithm. The [[BlellochScan]] page is created for completeness but is not directly derived from Ch10 text.
