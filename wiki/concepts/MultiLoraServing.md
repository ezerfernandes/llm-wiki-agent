---
title: "Multi-LoRA Serving"
type: concept
tags: [lora, peft, serving, inference, multi-tenancy]
sources: [ai-engineering-ch07-finetuning, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Multi-LoRA Serving

Serving **multiple [[lora|LoRA]]-finetuned models that share a single base model** by keeping the base weights `W` shared and routing requests to the appropriate per-tenant (A, B) adapter pair. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], this is one of LoRA's most under-discussed structural wins.

## The two serving options (Ch 7)

| Option | What's stored | Inference latency | When to use |
|---|---|---|---|
| **1. Pre-merge** | One full `W' = W + (α/r)·W_AB` per tenant | No overhead | One LoRA total |
| **2. Keep separate** | One shared `W` + many small `(A, B)` per tenant | Small overhead (A·B computed per request) | Many LoRAs sharing a base |

For **N customer LoRAs sharing a base**, option 2 is the dramatic storage winner.

## Worked example (Ch 7)

Setup: 100 customer LoRAs of Llama-2-13B; rank=8 applied to query + key matrices. Each (A, B) pair = 6.55 MB.

| | Option 1 (pre-merge) | Option 2 (shared base) |
|---|---|---|
| Total storage | 100 × 26 GB = **2.6 TB** | 26 GB + 100 × 6.55 MB ≈ **26.66 GB** |
| Storage ratio | — | **≈ 98× smaller** |

## Tenant-switching latency

Option 2 also wins on **per-request tenant switching**:
- Option 1: load a new 26 GB model from disk (seconds).
- Option 2: load a 6.55 MB adapter into GPU memory (milliseconds).

This makes per-tenant serving economically viable in ways that per-tenant full models aren't.

## How adapters get loaded efficiently

The optimization landscape includes:
- **Batching across tenants**: pack requests from multiple tenants into a single batch and apply the relevant adapter per request slice.
- **Adapter caching**: keep hot adapters in GPU memory; swap cold ones to CPU.
- **Tensor parallelism with adapter routing**: a tenant-aware extension of standard parallel serving.

The book's GitHub repo has a walkthrough of the LoRA-serving optimization stack.

## Real-world cases

- **[[Apple]] (2024)** — multiple LoRA adapters over a single 3B base model power different iPhone features. Combined with [[Quantization|3.5-bits-per-weight quantization]], the whole bundle fits on-device.
- **[[HuggingFace]] / [[AdapterHub]]** — community-shared adapter registries enable many tenants to use the same hosted base.
- **Per-customer SaaS finetunes** — the cost-effective way to ship "your own model" to many small customers.

## Connections

- [[lora|LoRA]] — the parent technique.
- [[QLoRA]] — quantized base extends this further.
- [[AdapterHub]] — community registry.
- [[Apple]] — on-device multi-LoRA case.
- [[FineTuning]] — parent operation.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 contextualizes multi-LoRA serving as the **routing-side counterpart** to [[PromptCaching|prompt caching]] in the service-level optimization stack. While prompt caching shares **prefix computation** across requests, multi-LoRA serving shares **base-model storage and compute** across tenants — they're the two main "share what's shareable across requests" wins at the service layer.

For [[AppleNeuralEngine|Apple Neural Engine]] deployments specifically, Ch 9 reinforces the Ch 7 narrative: multi-LoRA + aggressive [[Quantization|quantization]] (3.5 bits/weight average) is what makes "one foundation model serving many features" tractable on iPhone-class power and memory budgets.
