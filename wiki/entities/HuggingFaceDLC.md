---
title: "Hugging Face Deep Learning Container"
type: entity
tags: [product, hugging-face, container, model-serving, aws]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Hugging Face Deep Learning Containers (DLCs) are pre-built Docker images bundling Hugging Face's `transformers`, `datasets`, and `tokenizers` libraries together with a serving engine — most importantly **Text Generation Inference (TGI)** for LLM workloads. They are published as ECR images that SageMaker can pull directly.

## In LLM Engineer's Handbook
Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) selects the HF DLC as the base image for the LLM Twin's SageMaker endpoint; the image is resolved via `get_huggingface_llm_image_uri("huggingface", version=None)` and passed to `HuggingFaceModel(...)`. The DLC ships TGI's tensor parallelism, flash-attention-optimized transformer kernels, `bitsandbytes` quantization integration, continuous batching, `safetensors` fast loading, and SSE token streaming — collapsing what would otherwise be a complex serving-stack assembly into a single Docker image.

## Connections
- [[HuggingFace]] — publisher.
- [[TextGenerationInference]] — serving engine inside the DLC.
- [[AmazonSageMaker]] — destination platform that pulls the DLC.
- [[AmazonECR]] — registry that hosts the DLC images.
- [[Docker]] — image format.
- [[Bitsandbytes]] — quantization library bundled in.
- [[Safetensors]] — fast tensor format used inside.
