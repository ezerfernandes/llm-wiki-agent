---
title: "Moving Average"
type: concept
tags: [statistics, time-series, parallel-computing, prefix-scan, thrust]
sources: [parproc-ch10-parallel-prefix-problem]
last_updated: 2026-05-17
---

# Moving Average

A sliding-window summary statistic: given a sequence $x_1, ..., x_n$ and window width $w$, the moving average at position $i$ ($i = w, ..., n$) is:

$$a_i = \frac{x_{i-w+1} + \cdots + x_i}{w}$$

It answers the question "What has the recent trend been?" at time $i$. Widely used in financial time-series, signal processing, and sensor data smoothing.

## Parallel computation via prefix scan

The sum in the numerator equals the difference of two [[PrefixScan|exclusive cumulative sums]] ([[parproc-ch10-parallel-prefix-problem]] §10.7.2):

$$x_{i-w+1} + \cdots + x_i = c_i - c_{i-w}$$

where $c_i$ is the exclusive cumulative sum of the input. Therefore:

1. Compute $c_i$ = `thrust::exclusive_scan(dx)`.
2. Compute $a_i = (c_i - c_{i-w}) / w$ for all $i$ simultaneously via `thrust::transform`.

Only one scan call and one transform call are needed — $O(n/p + \log p)$ parallel time.

## Thrust implementation (R via Rth, §10.7.1–10.7.2)

```cpp
// csums: exclusive scan of dx (device vector of input)
thrust::exclusive_scan(dx.begin(), dx.end(), csums.begin());
csums[xas] = xa[xas-1] + csums[xas-1];  // extend by one past the end

// compute moving averages: (c_i - c_{i-w}) / w for all valid i
thrust::transform(csums.begin() + wa, csums.end(),
                  csums.begin(),
                  xb.begin(),
                  minus_and_divide(double(wa)));
```

The `minus_and_divide` functor (or C++11 lambda equivalent) computes `(a - b) / w`.

### Lambda version (§10.7.3)

```cpp
thrust::transform(csums.begin() + wa, csums.end(),
                  csums.begin(), xb.begin(),
                  [=](double& a, double& b) { return (a-b)/wa; });
```

The `[=]` capture clause makes `wa` available inside the lambda by value without passing it as a function argument.

## Platform

The Rth package ([[parproc-ch10-parallel-prefix-problem]] §10.7.1) is [[NormMatloff]]'s R interface to [[Thrust]], exposing `rthma()` for parallel moving average. Rth supports OpenMP, TBB, and CUDA back ends via compile-time `RTH_OMP` / `RTH_TBB` flags.

## See also

- [[PrefixScan]] — the primitive; exclusive scan computes cumulative sums.
- [[Thrust]] — `exclusive_scan`, `transform`.
- [[LambdaFunction]] — C++11 syntax used in §10.7.3 to replace the functor struct.
- [[parproc-ch10-parallel-prefix-problem]] — §10.7 (full derivation and code).
