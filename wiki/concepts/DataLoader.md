---
title: "DataLoader"
type: concept
tags: [training, pytorch]
sources: [d2l-linear-regression]
last_updated: 2026-05-16
---

# DataLoader

A [[PyTorch]] (and similar in [[TensorFlow|TF]] / [[JAX]]) abstraction that wraps a [[Dataset]] with batching, shuffling, parallel workers, and prefetching. Decouples data IO from model compute, keeping GPUs fed during [[Backpropagation]] and underpinning [[DistributedTraining]] sampling. Yields the minibatches consumed by [[MinibatchSGD|minibatch SGD]].

[[d2l-linear-regression]] §3.3 contrasts a hand-rolled Python generator (educational, but inefficient — loads all data in memory, lots of random access) against the framework `DataLoader` (`torch.utils.data.DataLoader` / `tf.data.Dataset` / `gluon.data.DataLoader`), which the chapter recommends in production: "the built-in iterators implemented in a deep learning framework are considerably more efficient and they can deal with sources such as data stored in files, data received via a stream, and data generated or processed on the fly."

## Connections

- [[d2l-linear-regression]] — §3.3 canonical reference (synthetic-regression-data section).
- [[DataModule]] — D2L's higher-level wrapper.
- [[MinibatchSGD]] — consumer of the minibatches.
- [[Dataset]] — the underlying data source.
