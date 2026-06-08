---
title: "Equivalent Mutant"
type: concept
tags: [testing, mutation-testing, undecidability, statistics, software-engineering]
sources: [fuzzingbook-08-mutation-analysis]
last_updated: 2026-06-06
---

# Equivalent Mutant

An **equivalent mutant** is a [[Mutant|mutant]] that is *semantically identical* to the original program despite a syntactic difference — it produces the same output on every input, so **no test can ever kill it**. Equivalent mutants are the central practical problem of [[MutationAnalysis|mutation analysis]]: they sit permanently in the "surviving" bucket, depressing the [[MutationScore|mutation score]] with no signal about test quality. Deciding whether a mutant is equivalent is **undecidable** in general (it reduces to program equivalence), so the equivalent count must be *estimated*, not computed.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] illustrates with `new_gcd()`: deleting an inconsequential `a, b = a, b` assignment (replacing it with `pass`) yields a mutant indistinguishable from the original — an equivalent mutant. The chapter stresses the resulting ambiguity: with a measured score of 70%, anywhere from 0–30% of mutants might be equivalent, so the *achievable* score is unknown. It offers two estimation strategies:

- **Statistical sampling** — randomly sample surviving mutants for manual inspection; the binomial sample size is `n ≥ p̂(1−p̂)(Z_{α/2}/Δ)²` (≈ 9604 mutants for ±1% at 95% confidence; only ≈ 96 for ±10%).
- **Chao's estimator** — `Ŝ_Chao1 = S(n) + f₁²/(2f₂)` (using singletons `f₁` and doubletons `f₂` from the full test×mutant kill matrix) estimates the true number of killable mutants; `M − Ŝ_Chao1` gives the count of **immortal** mutants. Immortality is oracle-relative (a weak error-only oracle leaves more immortals than a strong differential oracle); with a sufficiently strong oracle, immortal ≈ equivalent. The full derivation is in [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]].

## Connections
- [[Mutant]] — equivalent mutants are a subset that can never be killed.
- [[MutationScore]] — equivalent mutants distort it; the achievable score is unknown without estimating them.
- [[MutationAnalysis]] — the technique whose chief limitation this is.
- [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] — Chao's estimator and species-discovery theory.
- [[TestOracle]] — immortality is relative to oracle strength.

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
