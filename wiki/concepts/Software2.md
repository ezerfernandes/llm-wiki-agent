---
title: "Software 2.0"
type: concept
tags: [paradigm, ml-systems, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Software 2.0

[[AndrejKarpathy|Andrej Karpathy]]'s 2017 reframing of the shift from rule-based to data-driven computing, central to the opening of Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]). The "programmer" no longer writes the logic; they **curate the dataset that the optimization process uses to write the logic.**

| Feature | Software 1.0 (Traditional) | Software 2.0 (Machine Learning) |
|---|---|---|
| Source Code | C++, Python, Java | Training Data + Labels |
| Compiler | GCC, LLVM | Training loop ([[StochasticGradientDescent|SGD]]) |
| Logic | Explicit (hand-coded) | Implicit (learned) |
| Failure Mode | Loud (crash, exception) | [[SilentDegradation|Silent (metric degradation)]] |
| Debugging | Trace execution path | Inspect data distribution |

The "compiler" analogy is approximate: unlike a deterministic compiler, training is *stochastic* and may produce different "executables" from the same "source code."

## The "data as code" invariant

The dataset is source code, the training pipeline is the compiler, and [[ModelWeights|model weights]] are the binary executable. Consequences: debugging moves *upstream* from code to data; version control must track *datasets*, not just commits; testing must validate *data distributions*, not just code paths. A structural **verification invariant** remains — finite test sets cannot cover vast continuous input spaces (a $224\times224$ RGB image has $256^{150{,}528}$ configurations), forcing reliance on production monitoring over predeployment proof.

## Connections

- [[AndrejKarpathy]] — originator.
- [[MachineLearningSystems]] — the systems this paradigm describes.
- [[SilentDegradation]] / [[DistributionShift]] — the Software-2.0 failure mode.
- [[StochasticGradientDescent]] / [[ModelWeights]] — the "compiler" and "executable."
- [[DataEngineering]] — the discipline that owns the new "source code."
- [[mlsysbook-ch01-introduction]] — source.
