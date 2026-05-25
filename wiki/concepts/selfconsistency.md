---
title: "Self-Consistency"
type: concept
tags: [ml-method, reasoning, inference, test-time-scaling]
sources: [2605.08083-autotts, 2025-bionlp-archehr-qa-neural, ai-engineering-ch02-foundation-models, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Self-Consistency

Sample $N$ independent chain-of-thought trajectories from a base model and return the **majority-voted** final answer (Wang et al., arXiv 2203.11171, 2022). Often referred to as **SC@N** (e.g. SC@64 = 64 samples).

The canonical [[parallelreasoning|parallel reasoning]] / [[bestofn|best-of-N]] baseline in the [[testtimescaling|TTS]] literature, and the "fixed full-budget corner" of the [[WidthDepthSearch|width–depth control space]] in [[2605.08083-autotts|AutoTTS]]. Used as the dominant handcrafted baseline in AutoTTS: at $\beta=0.5$ the discovered [[ConfidenceMomentumController|CMC]] reduces tokens by ~69.5% at matched accuracy.

A **Beta-majority confidence** variant — used as the underlying confidence signal in many adaptive TTS controllers including [[ConfidenceMomentumController|CMC]], IBC, SCR, DGCC — derives a smoother confidence estimate from the (top1, top2) vote-count pair than raw plurality.

## Applications in this wiki

- **[[2025-bionlp-archehr-qa-neural|ArchEHR-QA 2025 (Neural)]].** $R=5$ majority vote applied to Stage 1 (sentence-level evidence classification) of a two-stage [[MIPROv2]]-optimized clinical-QA pipeline; lifts evidence recall without sacrificing precision. Stochastic seeds at temperature 0.7, threshold $\tau = \lceil R/2 \rceil = 3$.

## Connections

- [[2605.08083-autotts]] — the AutoTTS paper's primary baseline.
- [[2025-bionlp-archehr-qa-neural]] — clinical-QA Stage-1 application.
- [[testtimescaling|Test-Time Scaling]] — parent concept.
- [[parallelreasoning|Parallel Reasoning]] — the width-axis pattern SC instantiates.
- [[bestofn|Best-of-N]] — SC = BoN + majority vote.
- [[chainofthought|Chain-of-Thought]] — the per-branch reasoning substrate.
- [[ConfidenceMomentumController|CMC]] — uses Beta-majority confidence over pool of SC-style branches.
- [[WidthDepthSearch]] — places SC@64 as the "fixed full-budget corner."

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

[[ChipHuyen|Chip Huyen]] frames self-consistency as **the majority-vote variant of [[bestofn|best-of-N]]** within the [[TestTimeCompute|test-time compute]] family:

> "Picking out the most common output among a set of outputs can be especially useful for tasks that expect exact answers. For example, given a math problem, the model can solve it multiple times and pick the most frequent answer as its final solution."

The most striking Ch-2 data point: **[[google|Google]] sampled 32 outputs per question** when evaluating [[gemini|Gemini]] on [[mmlu|MMLU]], voting majority — allowing Gemini Ultra to reach a higher score than single-output evaluation would have produced. This is the same self-consistency trick used as Gemini's reported headline MMLU number.

Per Ch 2's framing, self-consistency is the right choice when the task has **exact-answer ground truth** (math, multiple choice) — where majority voting reliably picks correct answers. For open-ended generation, [[Logprobs|logprob]]-based or [[Verifier|verifier]]-based selection is the alternative.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 frames self-consistency as the **natural response to temperature/top_p stochasticity**:

> *"Using the same prompt multiple times can lead to different results if we allow for a degree of creativity through parameters like temperature and top_p. As a result, the quality of the output might improve or degrade depending on the random selection of tokens. In other words, luck! To counteract this degree of randomness and improve the performance of generative models, self-consistency was introduced."* — Ch 6

### Natural pairing with chain-of-thought

> *"This method can further be improved by adding chain-of-thought prompting to improve its reasoning while only using the answer for the voting procedure."* — Ch 6

The pattern: sample $N$ reasoning chains with stochastic decoding (varied [[Temperature|temperature]] / [[Topp|top_p]]), extract the final answer from each chain, **majority-vote the answers** (not the chains). The reasoning chains differ but the final answers cluster.

### Cost — n times slower

> *"It does require a single question to be asked multiple times. As a result, although the method can improve performance, it becomes n times slower where n is the number of output samples."* — Ch 6

Ch 6's framing is **the practitioner cost axis** — Huyen Ch 2's framing is the **test-time-compute taxonomy axis**. Both are consistent extensions of [[selfconsistency]]; the cost framing is the one most directly visible to engineers integrating the technique.
