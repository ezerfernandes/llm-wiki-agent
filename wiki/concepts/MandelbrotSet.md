---
title: "Mandelbrot Set (computation)"
type: concept
tags: [parallel-computing, mathematics, fractal, load-balancing]
sources: [parproc-ch04-introduction-to-openmp, parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Mandelbrot Set

Set of complex numbers $c$ for which the iteration $z \leftarrow z^2 + c$ starting at $z_0 = 0$ remains bounded. The boundary is the famous fractal; per-pixel determination is iterative, with **early termination** for points clearly outside the set (`|z|^2 > 4`) and **many iterations** for points inside or near the boundary. See [[Mandelbrot]] for the general concept; this page focuses on the **computational pattern** that makes Mandelbrot the recurring [[LoadBalancing|load-balance]] case study in [[NormMatloff|Matloff]]'s book.

## The computation

```c
int inset(double complex c) {
    int iters;
    double complex z = c;
    for (iters = 0; iters < MAXITERS; iters++) {
        z = z * z + c;
        if (creal(z)*creal(z) + cimag(z)*cimag(z) > 4) return 0;
    }
    return 1;
}
```

Wrapped in a double loop over an `nptsside × nptsside` grid (`xv, yv = (x - side2) / side4` to map pixels to a complex plane), counting `inset()` returns of 1.

## Parallel pattern

[[parproc-ch04-introduction-to-openmp]] §4.4 wraps this in OpenMP with `#ifdef` switches over scheduling strategies:

```c
#ifdef STATIC
#pragma omp for reduction(+:count) schedule(static)
#elif defined DYNAMIC
#pragma omp for reduction(+:count) schedule(dynamic)
#elif defined GUIDED
#pragma omp for reduction(+:count) schedule(guided)
#endif
```

Plus an `RC` (random chunk) variant that uses `rpermute()` to shuffle row indices before assignment — the Ch2 randomized-static fix.

## Why Mandelbrot is the canonical load-balance failure

Per-pixel iteration count varies dramatically across the image — most "interior" points iterate the full `MAXITERS`, while exterior points bail out within tens of iterations. Worse, **the costs are spatially correlated**: the bulk of the Mandelbrot set lies left-of-center, so a naïve left/right split gives thread 0 most of the work and thread 1 most of the idle time.

[[parproc-ch02-recurring-performance-issues]] §2.4 timings on an 8000×8000 grid, two threads:

| schedule | time (s) |
|---|---|
| `static` (contiguous halves) | 47.8 |
| `dynamic` | 21.4 |
| `guided` | 29.6 |
| randomized static (RC) | 15.7 |

The randomized-static winner makes the per-chunk costs i.i.d. by construction; dynamic comes second by re-routing fast-finishing thread 1 to a slow-finishing thread 0's leftover rows; guided is intermediate; naïve static loses badly.

## Connections
- [[parproc-ch04-introduction-to-openmp]] — §4.4 OpenMP code.
- [[parproc-ch02-recurring-performance-issues]] — §2.4 timing argument.
- [[Mandelbrot]] — companion page on the mathematical object.
- [[ScheduleClause]] — the chapter's worked toggle.
- [[LoadBalancing]] — the pedagogical point.
- [[ReductionClause]] — `reduction(+:count)` for the `inset()` total.
- [[StaticTaskAssignment]] / [[DynamicTaskAssignment]] — the comparison axes.
- [[EmbarrassinglyParallel]] — Mandelbrot qualifies under both old and new meanings of the term.
