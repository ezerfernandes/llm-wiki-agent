---
title: "Offline Replay Environment"
type: concept
tags: [test-time-scaling, search, evaluation, agentic-discovery]
sources: [2605.08083-autotts]
last_updated: 2026-05-15
---

# Offline Replay Environment

The affordability mechanism behind [[AutoTTS]]: pre-collect *all* LLM-generated reasoning trajectories and probe signals before any controller search begins, then evaluate candidate controllers deterministically against the stored data — **zero additional LLM calls** during search.

## Construction (from [[2605.08083-autotts]] §3.1)

For each problem $q\in\mathcal{Q}$ and base LLM $\pi$:
- Pre-sample $N=128$ independent reasoning trajectories at temperature 0.7.
- Segment each trajectory into fixed-length intervals of $\Delta=500$ tokens.
- Record branch prefixes $z_{i,1}, z_{i,2}, \ldots$ and intermediate probe answers $\omega_{i,1}, \omega_{i,2}, \ldots$
- Store everything offline.

## Evaluation Semantics

A `PROBE(i)` action at depth $k$ on branch $i$ becomes a *table lookup* of the pre-collected $\omega_{i,k}$ — zero generation cost. `CONTINUE(i)` advances $\ell_{t,i}\to\ell_{t,i}+1$ deterministically by reading the next pre-stored prefix. `BRANCH` instantiates a fresh pre-collected trajectory. Cost accounting still charges $\sum \ell_{t,i}$ tokens for fair comparison with handcrafted baselines.

This makes the entire $\beta$ sweep + multi-round controller-edit loop tractable: AutoTTS's five-round discovery runs in **160 minutes total** and costs **$39.9 in explorer-LLM API** — replay reuses the same trajectories for every candidate.

## Why It Matters

Without offline replay, every candidate controller would need to *invoke the base LLM* on every problem at every state — prohibitive at frontier-model scale. The offline-replay trick **moves all LLM costs upstream**, before the search begins; it is the same accounting trick that makes [[2604.25850-agentic-harness-engineering|Meta-Harness]] discovery cost-effective.

## Limitations

- The pre-collected trajectory pool *bounds* the policies the controller can express: it cannot ask the LLM for a question it would not have generated.
- Probe interval $\Delta$ is fixed at collection time; finer granularity requires re-collection.
- Generalization to non-replayable settings (e.g. tool-augmented agents whose actions affect external state) is non-trivial.

## Connections

- [[2605.08083-autotts]] — origin.
- [[AutoTTS]] — the framework this underlies.
- [[2602.03845-parallel-probe|Parallel-Probe]] — the data-collection protocol AutoTTS borrows ($N$, $\Delta$, temperature, probing format).
- [[2604.25850-agentic-harness-engineering|Meta-Harness]] — adjacent agentic-discovery framework also using replay-style evaluation.
- [[BetaParameterization]] — without offline replay, the $\beta$ sweep would be too expensive to be worth shrinking the search space.
