---
title: "GPU"
type: concept
tags: [hardware, deep-learning, gpu, infrastructure]
sources: [d2l-builders-guide, d2l-computational-performance, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# GPU (Graphics Processing Unit)

A massively-parallel coprocessor with thousands of compute cores and high-bandwidth on-board memory, optimized for the dense linear algebra (matrix-matrix multiplications, convolutions, elementwise nonlinearities) that dominates deep-learning workloads. The execution substrate for essentially all modern neural-network training and serving ([[d2l-builders-guide]] §`use-gpu.md`).

## Why deep learning runs on GPUs

[[d2l-builders-guide]]: "GPU performance has increased by a factor of 1000 every decade since 2000." A modern A100 / H100 GPU offers 10–100× the matmul throughput of a comparable CPU at similar cost, and 50–200× the memory bandwidth — the right ratios for training Transformers and CNNs whose inner loops are dominated by `Y = X @ W + b`.

## Device handles

In [[PyTorch]] every tensor and every module has a *device*:

```python
torch.device('cpu')          # entire CPU + main memory
torch.device('cuda')         # GPU 0 (shorthand for cuda:0)
torch.device('cuda:1')       # second GPU
torch.cuda.device_count()    # how many GPUs are visible
```

`cpu` represents *all* CPU cores and the entire main memory; `cuda:i` represents *one* specific GPU card and its (typically 16–80 GB) device memory. The D2L `try_gpu(i)` helper falls back to `cpu()` if GPU `i` is not available — the standard pattern for code that runs in both Colab-with-T4 and "I forgot to provision GPUs" environments.

## The cardinal rule: same-device operands

```python
X = torch.ones(2, 3, device='cuda:0')
Y = torch.ones(2, 3, device='cuda:1')
X + Y                         # RuntimeError
```

[[d2l-builders-guide]]: "If we sum two tensors, we need to make sure that both arguments live on the same device — otherwise the framework would not know where to store the result or even how to decide where to perform the computation." Move explicitly with `Y_on_0 = Y.cuda(0)` (or `Y.to('cuda:0')`); never implicit. Models follow the same rule: `net = net.to(device='cuda:0')` migrates all `nn.Parameter`s.

## Transfers are slow

> "People use GPUs to do machine learning because they expect them to be fast. But transferring variables between devices is slow: much slower than computation."

Practical consequences ([[d2l-builders-guide]] §Side Notes):

- **Many small ops worse than one big op** — kernel launch + transfer overhead dominates small computations.
- **`print(gpu_tensor)` copies to CPU** — silent transfer.
- **NumPy conversion copies to CPU** — same.
- **Logging loss-per-minibatch to CPU stalls all GPUs** — triggers Python's GIL on each transfer; "keep logs on the GPU and only move larger logs."

The whole point of [[FlashAttention]] / [[KernelFusion|kernel fusion]] is to minimize HBM ↔ SRAM traffic *within* a GPU; the analogous rule across devices is "batch transfers, do them rarely."

## See also

- [[d2l-builders-guide]] — §`use-gpu.md` canonical reference for the framework API.
- [[CUDA]] — NVIDIA's GPU programming platform; the substrate `cuda:i` refers to.
- [[NVIDIA]] — vendor of essentially all DL training GPUs (A100, H100, B200, …).
- [[gpumemoryhierarchy]] — bandwidth/size table for HBM / SRAM / DRAM.
- [[FlashAttention]] — canonical example of memory-aware GPU kernel design.
- [[KernelFusion]] — companion optimization.
- [[DistributedTraining]] — what happens when one GPU is not enough.
- [[PyTorchDDP]] — PyTorch's multi-GPU training API.
- [[Tensor]] — what lives on a GPU.
- [[NeuralNetworkModule]] — what `.to(device)` migrates.
