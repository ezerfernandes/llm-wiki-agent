---
title: "Ring AllReduce"
type: concept
tags: [distributed-training, collective-ops, parallelism, multi-gpu]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Ring AllReduce

The bandwidth-optimal [[AllReduce]] algorithm: arrange $n$ devices in a ring, partition each device's gradient into $n$ chunks, then run two passes (**reduce-scatter** + **all-gather**) along the ring such that every link carries exactly one chunk at a time. Total time **does not grow with $n$** ([[d2l-computational-performance]] §`parameterserver`).

## Cost analysis

For a naive linear pass around $n$ nodes: each step sends the full gradient → time $O(n)$.

Ring trick: break the gradient into $n$ chunks of size $1/n$, start chunk $i$ from node $i$. In step $j$, each link transmits one chunk. After $n-1$ steps, every chunk has visited every node and been summed → total time

$$T = (n-1) \cdot \frac{G/n}{B} \approx \frac{G}{B}\qquad\text{(independent of $n$).}$$

> *"In other words, the time spent to aggregate gradients does not grow as we increase the size of the ring. This is quite an astonishing result."* — [[d2l-computational-performance]]

For 160 MB across 8× V100 over NVLink (~18 GB/s × 3 effective bidirectional rings):

$$T \approx \frac{2 \cdot 160\,\textrm{MB}}{3 \cdot 18\,\textrm{GB/s}} \approx 6\,\textrm{ms}$$

— better than the PCIe-based aggregation even at 8 GPUs.

## Topology awareness

D2L notes the [[NVLink]] connectivity of AWS p3.16xlarge / NVIDIA DGX-2 (8× V100) decomposes into one "double-bandwidth" ring (1-2-3-4-5-6-7-8-1) and one regular-bandwidth ring (1-4-6-3-5-8-2-7-1) — designing the protocol over both simultaneously is nontrivial but is what [[NCCL]] does.

## History

Introduced widely to deep learning by Baidu (2017) and popularized by [[Horovod]] (Uber, 2018) which made ring-allreduce ergonomic via MPI. [[NCCL]] 2.x absorbed ring + tree variants and is now the default backend for [[PyTorch]] DDP / [[TensorFlow]] / [[MXNet]] on NVIDIA hardware.

## Caveats

D2L tempers the hype: *"There is a common misconception that ring synchronization is fundamentally different from other synchronization algorithms. The only difference is that the synchronization path is somewhat more elaborate when compared with a simple tree."* In practice, gains over a well-implemented tree-allreduce on modern fabrics are modest; **the bigger win is topology-aware path selection**.

## See also
- [[AllReduce]] — the parent primitive.
- [[NVLink]] — the fabric that makes ring-allreduce shine.
- [[NCCL]] / [[Horovod]] — production implementations.
- [[DataParallelism]] — the consumer.
- [[d2l-computational-performance]] §`parameterserver`.
