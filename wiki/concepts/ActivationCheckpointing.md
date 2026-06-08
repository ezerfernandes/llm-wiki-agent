---
title: "Activation Checkpointing"
type: concept
tags: [frameworks, memory, training, autodiff, mlsysbook]
sources: [mlsysbook-ch07-ml-frameworks, mlsysbook-ch08-model-training, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Activation Checkpointing

**Activation checkpointing** (also called gradient checkpointing) trades recomputation for memory during [[ReverseModeAutodiff|reverse-mode]] training. Rather than storing every forward activation until the backward pass consumes it, the framework stores only selected **checkpoints** and recomputes the intermediate activations on demand during backprop. With optimal $\sqrt{N_L}$ checkpoint placement (for an $N_L$-layer network), it reduces activation memory by **50–90%** at the cost of **20–33%** additional compute.

In [[IronLawOfMLSystems|iron-law]] terms it increases the $O$ term (recomputation) to reduce the $D_{\text{vol}}$ term (memory traffic) — the binding constraint, since reverse-mode AD's stored activations can consume 3–4× more memory than the model weights. It is one of the primary levers (alongside [[KernelFusion|operation fusion]] and [[MixedPrecisionTraining|mixed precision]]) that make training large models fit in accelerator memory.

> This concept is closely related to / largely synonymous with [[GradientCheckpointing]]; the mlsysbook chapter uses both terms.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the differentiation problem's memory management.
- [[GradientCheckpointing]] — synonymous term (Chen et al. 2016).
- [[ReverseModeAutodiff]] / [[Autograd]] — why activations must persist.
- [[GradientAccumulation]] / [[MixedPrecisionTraining]] / [[KernelFusion]] — complementary memory levers.
- [[MemoryWall]] — the constraint being attacked.
- [[mlsysbook-ch08-model-training]] — Ch 8 derives optimal placement ($k_{\text{optimal}}=\sqrt{N_L}$): GPT-2's 48 layers → ~7 checkpoints, **71% memory savings for ~33% extra compute**; *selective* checkpointing (attention yes, cheap FFN/LayerNorm no) reaches 60–80% at 20–25% overhead. See [[GradientCheckpointing]] (the synonym).
- [[GradientCheckpointing]] — synonymous concept (the name AI-Engineering/Hands-On-LLMs use).
- [[mlsysbook-ch10-model-compression]] — Ch 10 lists checkpointing as a **memory-optimization** design principle ($\mathcal{O}(A_{\text{total}})\to\mathcal{O}(\sqrt{A_{\text{total}}})$ peak memory) that enables training larger models within a fixed budget, which in turn gives more capacity for subsequent [[Pruning|pruning]] / [[KnowledgeDistillation|distillation]] to exploit.
