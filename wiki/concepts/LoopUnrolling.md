---
title: "Loop Unrolling"
type: concept
tags: [compilers, optimization, gpu, cuda, performance]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Loop Unrolling

A classical compiler optimization that **replicates the body of a loop k times** to reduce branch overhead and enable downstream optimizations (instruction prefetching, register allocation). An n-iteration loop unrolled by factor k becomes ⌈n/k⌉ iterations, each doing k copies of the original body ([[parproc-ch05-cuda-gpu-programming]] §5.15).

> *"Loop unrolling is an old technique used on uniprocessor machines to achieve speedup due to branch elimination and the like. Branches make it difficult to do instruction or data prefetching, so eliminating them may speed things up."*

## Example

```c
for (i = 0; i < 2; i++) {
    sum  += x[i];
    sum2 += x[i] * x[i];
}
```

unrolled (k=2):

```c
sum  += x[1];
sum2 += x[1] * x[1];
sum  += x[2];
sum2 += x[2] * x[2];
```

## CUDA-specific benefit: register allocation

On NVIDIA GPUs, loop unrolling has an additional payoff beyond branch elimination: *"if `x` is local to this function, then unrolling will allow the compiler to store it in a register, which could be a great performance enhancer."* ([[parproc-ch05-cuda-gpu-programming]] §5.15).

The reason is that arrays with **variable indices** cannot be allocated to GPU registers (registers are not hardware-indexable). After unrolling, every array access has a **compile-time constant** index — the compiler can place each element in a distinct register.

## `#pragma unroll`

CUDA's nvcc accepts:

```c
#pragma unroll k
for (...) { ... }
```

- `k = 1` instructs the compiler **not** to unroll.
- `k > 1` suggests a k-fold unroll.
- Without the pragma, the compiler unrolls heuristically.

## When unrolling helps

- **Hot inner loops** dominated by branch overhead.
- **Small constant trip counts** known at compile time.
- **Tiny per-iteration bodies** where the branch is a large fraction of total cost.
- **GPU loops with array locals** that could become registers.

## When unrolling hurts

- **Large iteration bodies** — unrolling causes instruction-cache pressure.
- **Already-cheap loops** — modern branch predictors handle most loop branches at zero cost.
- **Variable trip count** — unrolling generates a "main + cleanup" structure that may not be worth the cost.

## See also

- [[CUDA]] — where `#pragma unroll` lives.
- [[KernelLaunch]] / [[Block]] — context where small inner loops dominate.
- [[ShortVectors]] — the packed-vector alternative path to bandwidth.
- [[parproc-ch05-cuda-gpu-programming]] — §5.15.
