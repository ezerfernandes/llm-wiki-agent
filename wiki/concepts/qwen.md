---
title: "Qwen"
type: concept
tags: [llm, alibaba, qwen]
sources: [2605.12357-delta-mem, 2507.19457-gepa, 2507.03152-medval, 2603.19247-prompt-optimization-jailbreaking, dspy-rl-multihop-tutorial]
last_updated: 2026-05-24
---

# Qwen

Alibaba's open-weights LLM family. Qwen3 is the third generation, with sizes from 4B through 14B (Instruct + Base flavors); Qwen2.5 is the second-generation line that the smaller (sub-2B) Instruct checkpoints come from.

Appearances in this wiki's corpus:
- **Qwen3-4B-Instruct / Qwen3-8B / Qwen-Next** — backbones in [[2605.12357-delta-mem|δ-mem]] (online associative memory).
- **Qwen3 8B** — primary evaluation model in [[2507.19457-gepa|GEPA]] (ICLR 2026). GEPA's headline RL-vs-reflection comparison is run against [[grpo|GRPO]] fine-tuning of Qwen3 8B (with LoRA) on six benchmarks.
- **Qwen3-4B (dense)** — base model for **[[MedVAL4B|MedVAL-4B]]** in [[2507.03152-medval|Aali et al. (MedVAL, 2026)]]; QLoRA fine-tuned to F1 = 0.527 on [[MedVALBench]] (overall) — **highest open-source result** in the benchmark and **beats baselines of MedGemma-27B (0.482), Llama-3.3-70B (0.480), Gemini 2.0 Flash (0.515)**. Demonstrates that a 4B open student fine-tuned with [[QLoRA]] on a single A6000 can outclass much larger / domain-pretrained / proprietary baselines for clinical text validation.
- **Qwen2.5 Math** — see [[Qwen25Math]].
- **Qwen2.5-1.5B-Instruct** — student model in [[dspy-rl-multihop-tutorial|the DSPy `rl_multihop` tutorial]]. **Wiki's smallest open-weights DSPy student** (below the prior 3B floor set by [[Llama|Llama-3.2-3B-Instruct]] in [[dspy-tutorial-rag-as-agent]]). 18 hours of online [[grpo|GRPO]] / [[DAPO]] via [[ArborGRPO]] lifts [[HoVer]]-3-hop devset recall from 61.8% → 66.2% with rank-8 LoRA on seven projection matrices. The 1.5B scale is the regime [[ArborGRPO|the tutorial authors]] explicitly call out as the value proposition of online RL — *"a solid start for online RL over arbitrary LM programs for tiny LMs"* — small enough that prompt-only optimization plausibly hits a capability ceiling.
- **Qwen-3 8B** — *target* (not backbone) in [[2603.19247-prompt-optimization-jailbreaking|Shamsi et al. (Algoverse, 2026)]] adaptive red-teaming. **Most vulnerable of the four target models**: baseline danger 0.090 → MIPROv2 0.746 → GEPA 0.477 → **SIMBA 0.792** (8.8× rise). Open-weights deployability cuts both ways — making Qwen-3 the most accessible target for adversarial system-prompt search.

The Qwen-Next retention design supplies the per-dimension forget-gate inspiration for δ-mem's gated delta-rule update.

In [[2507.19457-gepa|GEPA]]'s **cross-model generalization** experiment, prompts optimized on Qwen3-8B and evaluated on the much larger / different-family GPT-4.1 Mini *without modification* still achieve +9.00 aggregate improvement over baseline, outperforming baselines that optimized directly on GPT-4.1 Mini — evidence that **Qwen3-8B is a useful "cheap proxy" for prompt-evolution targeted at a more expensive model**.

## Connections
- [[2605.12357-delta-mem]] / [[2507.19457-gepa]] / [[2507.03152-medval]] — papers that use Qwen3 as base/eval models.
- [[alibaba]] — the developing org.
- [[grpo|GRPO]] — the RL fine-tuning approach against which GEPA's prompt-only adaptation of Qwen3 is benchmarked.
- [[MedVAL4B]] — the Qwen3-4B-based clinical text validator distilled by [[MedVAL]].
- [[QLoRA]] — the PEFT method [[MedVAL4B]] uses to fine-tune Qwen3-4B on consumer GPUs.
- [[lora|LoRA]] — the PEFT method [[ArborGRPO]] uses to fine-tune Qwen2.5-1.5B-Instruct via online GRPO.
- [[ArborGRPO]] / [[dspy-rl-multihop-tutorial]] — the wiki's first explicit `Qwen/Qwen2.5-1.5B-Instruct` receipt as a DSPy student model.
- [[ResearchHop]] — the multi-hop retrieval program Qwen2.5-1.5B-Instruct serves as student for.
