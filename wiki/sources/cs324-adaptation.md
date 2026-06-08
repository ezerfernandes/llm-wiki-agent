---
title: "CS324 — Adaptation"
type: source
tags: [cs324, llm, course-lecture, adaptation]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/adaptation/
---

## Summary
This Stanford CS324 lecture surveys how to adapt task-agnostic pre-trained language models to specific downstream tasks that differ from pre-training in formatting, topic, or temporal scope. It frames adaptation as optimizing parameters γ on a task loss and walks through three method families — [[Probing]], [[FineTuning]], and [[LightweightFineTuning]] (parameter-efficient methods such as [[PromptTuning]], [[PrefixTuning]], and [[Adapters]]). The central trade-off is expressivity versus storage cost, with lightweight methods optimizing under 1% of parameters while approaching full fine-tuning quality and improving out-of-distribution robustness.

## Key Claims
- Downstream tasks diverge from pre-training in three ways: **formatting** (e.g., [[NaturalLanguageInference]] takes two sentences and produces a binary output, unlike next-token or MASK prediction), **topic shift** (e.g., medical records), and **temporal shift** (new or non-public knowledge, e.g., [[GPT-3]] was trained before Biden became President).
- Adaptation is formalized as `γ_adapt = argmin_{γ ∈ Γ} (1/n) Σ ℓ_task(γ, θ_LM, x_i, y_i)`, where θ_LM are pre-trained LM parameters, γ are the optimized parameters from family Γ, and ℓ_task is the task loss.
- [[Probing]] freezes the LM encoder and trains a lightweight prediction head (linear or shallow feedforward) on top; it suits encoder-only models like [[BERT]] but extends to decoder-only models (Liu et al., 2021).
- Fixed-length sequence representations for probing come from the **CLS token** ([[BERT]] / Devlin et al., 2018) or by **averaging** over the L token embeddings.
- [[FineTuning]] initializes from θ_LM and optimizes all parameters plus task heads — more expressive than probing but expensive, requiring a full model copy per task.
- [[FLAN]] and [[T0]] fine-tune across many tasks under a unified prompt format to improve zero-shot generalization to unseen tasks.
- [[InstructGPT]] aligns [[GPT-3]] in three stages: supervised fine-tuning on human demonstrations, preference data collection (sampling k outputs per instruction), and reinforcement learning ([[RLHF]]) against a human-preference reward.
- InstructGPT results: a 1.3B InstructGPT model's outputs are preferred to 175B [[GPT-3]] 85% of the time (71% vs. few-shot GPT-3); it hallucinates 21% vs. 41% on closed-domain QA/summarization; produces 25% fewer toxic outputs when asked to be respectful; but shows no meaningful bias improvement on Winogender and CrowS-Pairs.
- [[LightweightFineTuning]] (parameter-efficient fine-tuning) optimizes **<1%** of parameters while freezing the rest, trading a little in-distribution quality for huge storage savings.
- [[PromptTuning]] (Lester et al., 2021, for [[T5]]) prepends k learnable continuous token embeddings to the input with the model frozen; it becomes more competitive with full fine-tuning as model scale increases, and initialization (random vocab, class-label embeddings, or pure random) matters.
- [[PrefixTuning]] (Li and Liang, 2021, for BART and [[GPT-2]]) concatenates learnable key/value matrices `P_key, P_value ∈ ℝ^{d×k}` at every attention layer: `K_prefix=[P_key,K]`, `V_prefix=[P_value,V]`; an all-layer variant (P-Tuning v2, He et al., 2022) helps both classification and generation.
- [[Adapters]] (Houlsby et al., 2019) insert frozen-Transformer bottleneck layers computing `Adapter(x) = x + W_up σ(W_down x)` with W_down ∈ ℝ^{r×d}, W_up ∈ ℝ^{d×r} and bottleneck dim r, adding <1% of parameters. Other lightweight methods include [[LoRA]] and [[BitFit]].
- Lightweight methods improve out-of-distribution robustness: prompt tuning improves F1 on out-of-domain MRQA 2019 after SQuAD training; prefix tuning improves ROUGE-L on XSUM when trained/tested on disparate news categories; full fine-tuning still slightly wins in-distribution.
- Prefix tuning enables personalized deployment: store N user-specific prefixes and prepend the right one per example in a minibatch over one shared frozen backbone.

## Key Quotes
> "A 1.3B InstructGPT model produces outputs that are preferred to 175B GPT-3 85% of the time, and 71% when using few-shot prompts." — InstructGPT alignment results

> "On closed-domain QA/summarization, InstructGPT hallucinates information 21% of the time vs 41% in GPT-3." — fine-tuning for instruction alignment

> "During both pre-training and fine-tuning, we prepend a special token called CLS to the prompt. We use the embedding vector corresponding to the CLS token as the 'sequence-level' embedding." — probing, CLS token representation [Devlin et al., 2018]

> "the downstream task requires new knowledge that is unavailable during pre-training because 1) the knowledge is new (e.g., GPT3 was trained before Biden became President), 2) the knowledge for the downstream task is not publicly available." — temporal shift

## Connections
- [[StanfordCS324]] — this is one lecture in the Winter 2022 "Large Language Models" course.
- [[Probing]] — frozen-encoder method with a trained prediction head; one of the three adaptation families.
- [[FineTuning]] — full-parameter adaptation; the high-expressivity, high-storage baseline.
- [[LightweightFineTuning]] — parameter-efficient family optimizing <1% of parameters.
- [[PromptTuning]] — lightweight method (Lester et al., 2021) developed for [[T5]].
- [[PrefixTuning]] — lightweight method (Li and Liang, 2021) for BART/[[GPT-2]], adding key/value prefixes at every layer.
- [[Adapters]] — Houlsby et al. (2019) bottleneck-layer lightweight method.
- [[LoRA]] — low-rank adaptation, mentioned as a lightweight method.
- [[BitFit]] — bias-only fine-tuning, mentioned as a lightweight method.
- [[InContextLearning]] — the prompting-based alternative to parameter updates this lecture's soft-prompt methods relate to.
- [[InstructGPT]] — fine-tuning + [[RLHF]] application aligning [[GPT-3]].
- [[FLAN]] / [[T0]] — instruction/multi-task fine-tuning for zero-shot generalization.
- [[BERT]] — canonical encoder-only model and source of the CLS-token probing approach.
- [[GPT-3]] — model adapted by InstructGPT; example of temporal-shift limitations.
- [[NaturalLanguageInference]] — running example task illustrating formatting divergence.

## Contradictions
- None identified.
