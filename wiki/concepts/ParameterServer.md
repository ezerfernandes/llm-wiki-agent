---
title: "Parameter Server"
type: concept
tags: [distributed-training, parallelism, infrastructure, deep-learning]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Parameter Server

A distributed-training architecture where **workers** compute gradients and **parameter servers** store/aggregate the shared parameter tensors. Workers `push` gradients to servers; servers aggregate (typically sum), apply the optimizer update, and workers `pull` the updated parameters ([[d2l-computational-performance]] §`parameterserver`).

## History

Introduced by [Smola & Narayanamurthy 2010] for distributed latent-variable models. Push/pull semantics formalized by Ahmed et al. 2012; the full system + open-source library by [Li, Andersen, Park et al. 2014] (the canonical paper). Inspired MXNet's KVStore, TensorFlow's `tf.distribute.ParameterServerStrategy`, and PyTorch's `torch.distributed.rpc` PS modules.

## API: key–value store with custom update

Parameters are indexed by key $i$ (one key per layer / tensor); gradients are *commutative reductions*:

$$\mathbf{g}_i = \sum_{k \in \textrm{workers}} \sum_{j \in \textrm{GPUs}} \mathbf{g}_{ijk}.$$

The interface is intentionally tiny:

- **`push(key, value)`** — worker sends gradient to PS; PS aggregates (sum / weighted average).
- **`pull(key, value)`** — worker retrieves the aggregated parameter from PS.

This abstraction lives in the same family as Dynamo (Amazon 2007) and distributed key–value stores generally.

## Scaling math

D2L's argument:

- One PS bottleneck: $m$ workers all push their gradients to a single server with finite bandwidth → time $\mathcal{O}(m)$.
- Shard parameters across $n$ servers: each server handles $\mathcal{O}(1/n)$ of the parameters → total time $\mathcal{O}(m/n)$.
- **Match $m = n$ (same machines act as workers *and* PSes) → constant scaling regardless of cluster size.**

This is the underlying argument for the 2014 PS design and remains the foundation of [[DistributedTraining|distributed training]] at scale.

## When to prefer PS vs AllReduce

| | Parameter Server | [[AllReduce]] / [[RingAllReduce]] |
|---|---|---|
| Network topology | Hub-and-spoke (servers in the middle) | Symmetric ring / tree |
| Failure tolerance | Easy (replace a PS shard) | Harder (all peers must restart) |
| Heterogeneous workers | Natural (slow workers don't block) | Synchronous by default |
| Asynchronous updates | Native (workers push when ready) | Requires careful design |
| Modern LLM training | Less common | Default (NCCL ring) |

For 2026 dense-LLM training, AllReduce dominates because workers are homogeneous and synchronous SGD generalizes better. PS still matters in **recommender systems** (sparse embeddings sharded across servers — billions of features, each worker only touches a slice) and **federated / asynchronous** settings.

## See also
- [[AllReduce]] / [[RingAllReduce]] — the symmetric alternative.
- [[DataParallelism]] — the training strategy a PS coordinates.
- [[KeyValueStore]] — the abstraction.
- [[DistributedTraining]] — parent concept.
- [[d2l-computational-performance]] §`parameterserver`.
