---
title: "Tensor Parallelism"
type: concept
tags: [inference, training, parallelism, gpu, llm-engineering]
sources: [leh-ch08-inference-optimization, leh-ch10-inference-pipeline-deployment, ai-engineering-ch09-inference-optimization, mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

## Definition
**Tensor parallelism (TP)** is a model-parallelism strategy that shards individual weight matrices within a layer across multiple GPUs — typically column-wise for one matrix and row-wise for the next so the inter-layer all-reduce is implicit — allowing a model too large for one GPU to be served while each GPU only computes a fraction of each layer's matmul. Megatron-LM (Shoeybi et al. 2019) is the canonical reference.

## In LLM Engineer's Handbook
[[leh-ch08-inference-optimization]] is the deep technical treatment. The chapter explains that attention heads and MLP blocks parallelize cleanly under TP — making it the preferred inference-time parallelism for LLMs. TP requires high-speed interconnects ([[NVLink]] or [[Infiniband]]) because the per-layer all-reduce dominates latency on slower fabrics. The chapter contrasts TP with [[DataParallelism|data parallelism]] (replicate model, shard data — only works if the model fits on one GPU) and [[PipelineParallelism|pipeline parallelism]] (slice layers across GPUs, micro-batching to fill bubbles), and notes the three are orthogonal and composable: typical large-scale serving uses PP across stages with TP within a stage. All three production inference engines — TGI, vLLM, TensorRT-LLM — support TP. [[leh-ch10-inference-pipeline-deployment]] cites TP as one of the headline TGI features enabling LLM Twin's SageMaker deployment.

## Key details
- Shards weight matrices column- or row-wise within a single layer.
- Uses [[AllReduce]] as the collective for partial-output reconciliation.
- Sequence parallelism (Megatron-LM, 2019) generalizes TP to LayerNorm and Dropout activations.
- Requires NVLink / Infiniband-class interconnects for good throughput.
- Composes with PP and DP — large frontier serving uses PP across stages, TP within stages, DP for replication.
- Preferred over DP at inference whenever the model is too large for one GPU.

## Connections
- [[ModelParallelism]] — parent concept; TP is one of three flavors (DP, PP, TP).
- [[DataParallelism]] / [[PipelineParallelism]] — sibling parallelism strategies.
- [[AllReduce]] — collective TP relies on.
- [[NVLink]] / [[Infiniband]] — high-speed interconnects TP requires.
- [[TextGenerationInference]] / [[vLLM]] / [[TensorRTLLM]] — engines implementing TP.
- [[InferenceOptimization]] — the broader technique family.
- [[GPU]] — hardware substrate.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 names tensor parallelism (a.k.a. **intra-operator parallelism**) as the **most common model-parallelism approach for inference**:

> *"The most common approach for inference is tensor parallelism, also known as intra-operator parallelism. Inference involves a sequence of operators on multidimensional tensors, such as matrix multiplication. In this approach, tensors involved in an operator are partitioned across multiple devices, effectively breaking up this operator into smaller pieces to be executed in parallel, thus speeding up the computation."*

### Two benefits

> *"Tensor parallelism provides two benefits. First, it makes it possible to serve large models that don't fit on single machines. Second, it reduces latency. The latency benefit, however, might be reduced due to extra communication overhead."* — Ch 9

This dual benefit — capacity AND latency — is what makes tensor parallelism the **#2 most impactful technique** in Ch 9's closing prescription (after [[Quantization]]):

> *"Across various use cases, the most impactful techniques are typically quantization, tensor parallelism (which both reduces latency and enables serving larger models), replica parallelism, and attention mechanism optimization."*

### vs [[PipelineParallelism|Pipeline parallelism]]

Pipeline parallelism *increases* per-request latency due to inter-stage communication, so it's typically avoided for strict-latency inference (preferred for training throughput). Tensor parallelism *reduces* per-request latency (when interconnects are fast enough), which is why it's the inference favorite.

### Composes with replica parallelism

TP shares model weights across GPUs in a node; [[ReplicaParallelism|replica parallelism]] adds copies across nodes. Together they form the foundation of modern multi-GPU LLM serving.

## From [[mlsysbook-ch08-model-training|mlsysbook Ch 8 (Model Training)]]

Ch 8 describes TP as the **finest-grained** parallelism: rather than assigning whole layers to devices, it splits individual operations — e.g. column-wise sharding the FFN weight matrix $W$ in $Y=XW$ so each GPU computes part of the output, then gathering. Megatron-LM used this to train models with hundreds of billions of parameters by distributing individual attention heads and FFN blocks. Because TP communicates frequently, it belongs *within a node* (high-bandwidth [[NVLink]]) in the hybrid stack; pipeline parallelism goes across nodes and data parallelism across racks.

- [[mlsysbook-ch08-model-training]] — TP as intra-layer operation splitting; Megatron-LM at hundreds of billions of params; placement within the NVLink-bandwidth tier.
- [[MegatronLM]] — the canonical tensor-parallel training system.
