---
title: "Monte Carlo Simulation"
type: concept
tags: [statistics, simulation, parallel-computing, probability]
sources: [parproc-ch14-statistics-data-mining]
last_updated: 2026-05-17
---

# Monte Carlo Simulation

A computational technique that estimates probabilistic quantities — probabilities, expected values, integrals — by repeating random experiments many times and averaging results. Named for the Monte Carlo casino due to its reliance on randomness.

## General Structure

```
count = 0
for i = 1,...,n:
    simulate one random experiment
    if condition holds: count = count + 1
calculate approximate probability as count/n
```

The larger n is, the more accurate the approximation. The method applies whenever an analytical solution is intractable but simulation is feasible.

## Parallelization

At first glance, Monte Carlo is embarrassingly parallel: distribute the n iterations across p threads/processes, each running n/p trials and reporting a partial count. The manager averages the counts.

**Critical hazard: independent random number streams.** Each thread or process must use an independent random number sequence. Using C's `random()` naively is dangerous — some implementations return identical streams per thread, or correlated streams. This completely invalidates the independence assumption and produces incorrect results.

## Parallel Random Number Generation

Purpose-built parallel RNG libraries are required (§14.5, [[parproc-ch14-statistics-data-mining]]):

- **CURAND** — CUDA SDK parallel RNG; includes Mersenne Twister.
- **RngStream** — works with [[OpenMP]] and [[MPI]].
- **SPRNG** — aimed at MPI; also usable in shared-memory settings; **Rsprng** is an R interface.
- **OpenMP Mersenne Twister** — available at http://www.pgroup.com/lit/articles/insider/v2n2a4.htm.

## Connections

- [[ProbabilityDensityFunction]] — Monte Carlo can estimate integrals of densities.
- [[OpenMP]] — RngStream and OpenMP Mersenne Twister provide parallel RNG for shared memory.
- [[MPI]] — SPRNG and RngStream provide parallel RNG for message-passing.
- [[CUDA]] — CURAND provides GPU-parallel RNG.
- [[parproc-ch14-statistics-data-mining]] — primary source (§14.5).
