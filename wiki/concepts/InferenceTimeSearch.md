---
title: "Inference-Time Search"
type: concept
tags: [inference, code-generation, prompt-optimization, gepa]
sources: [2507.19457-gepa, 2605.08083-autotts]
last_updated: 2026-05-22
---

# Inference-Time Search

A use of a prompt optimizer where the *target tasks themselves* serve as the training set — the optimizer "overfits" them by iteratively proposing better solutions per problem. The trained artifact is the *set of solutions*, not a generalizable prompt.

## In GEPA ([[2507.19457-gepa]])

The paper demonstrates this on two code-generation benchmarks:

### NPUEval ([[XDNA2|AMD XDNA2 NPU]] kernels)

Pass the set of kernel-generation tasks as both $D_{train}$ and $D_{pareto}$ to GEPA. Use Sequential10 (an agent that iteratively refines kernels up to 10 times based on compiler-error feedback) as $\Phi$. The [[FeedbackFunction|feedback function]] $\mu_f$ uses **RAG-augmented retrieval of architecture documentation** triggered by compiler errors — when a rollout fails with an error like *"vector lane mismatch"*, $\mu_f$ retrieves the relevant section of the XDNA2 ISA manual and includes it in the feedback text. GEPA then evolves the system prompt to internalize architectural best-practices.

Result: **30.52% mean vector utilization** (GPT-4o) vs:
- Sequential10 alone: **4.25%**
- Sequential10 + RAG: 16.33%
- Sequential10 + RAG + MIPROv2: 19.03%
- Sequential10 with a *single* GEPA-evolved prompt (no RAG at inference time): **26.85%**

The standalone-prompt result is the key: GEPA can compress the architecture knowledge from many RAG retrievals into one declarative system prompt that no longer needs RAG.

### KernelBench (NVIDIA V100 CUDA)

35 tasks from the representative subset. GEPA + GPT-4o pushes $fast_1$ (kernel beats PyTorch-eager) from ~0% to **>20%**. $fast_{0.5}$ (kernel runs at ≥0.5× PyTorch-eager) reaches ~50%.

## Distinguishing from training-time optimization

| Property | Training-time optimization | Inference-time search |
|---|---|---|
| Train/test split | $D_{train}$ disjoint from $D_{test}$ | $D_{train} = D_{test}$ |
| Returned artifact | one prompt generalizing across tasks | a set of solutions, one per task |
| Use case | deploy the prompt for new tasks of same type | solve a fixed, known task set as well as possible |
| Sample efficiency claim | per-rollout learning that *transfers* | per-rollout learning on *this exact problem* |

## Position in the search-controller literature

GEPA's inference-time use overlaps with [[2605.08083-autotts|AutoTTS]]'s test-time-scaling search and [[ConfidenceMomentumController|CMC]]'s width-depth control — both discover better solution procedures by iterating on tasks. GEPA differs by maintaining a candidate pool of full *system prompts* on a Pareto frontier rather than per-step controller parameters. The two are largely complementary.

## Connections
- [[2507.19457-gepa]] — canonical source for the framing.
- [[GEPA]] — the optimizer.
- [[FeedbackFunction]] — RAG-augmented $\mu_f$ is what makes inference-time search effective on code tasks.
- [[NPUEval]] — AMD XDNA2 NPU benchmark.
- [[KernelBench]] — NVIDIA CUDA benchmark.
- [[XDNA2]] — target architecture.
- [[2605.08083-autotts|AutoTTS]] — complementary search-controller-discovery framework.
- [[testtimescaling|Test-Time Scaling]] — broader category.
