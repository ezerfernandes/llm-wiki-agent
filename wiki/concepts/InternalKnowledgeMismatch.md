---
title: "Internal Knowledge Mismatch"
type: concept
tags: [hallucination, llm, sft, failure-mode, alignment]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Internal Knowledge Mismatch

The **second of two hypotheses for why language models hallucinate** in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]. Originally argued by **[[LeoGao|Leo Gao]]**, an [[openai|OpenAI]] researcher, and echoed in **[[JohnSchulman|John Schulman]]'s** April 2023 UC Berkeley talk.

## The mechanism

During [[SupervisedFinetuning|SFT]], models are trained to mimic responses written by labelers. **If these responses use knowledge the labelers have but the model doesn't have, we're effectively teaching the model to hallucinate.**

> "If labelers can include the knowledge they use with each response they write so that the model knows that the responses aren't made up, we can perhaps teach the model to use only what it knows. However, this is impossible in practice." — Ch 2

The model is being trained to be confident on a distribution of questions it doesn't actually have the knowledge to answer correctly.

## Schulman's "models know what they know" claim

[[JohnSchulman|John Schulman]] (UC Berkeley 2023): **LLMs know if they know something** — a big claim in itself. If true, hallucinations can be reduced by forcing the model to answer based only on what it knows.

## Two proposed mitigations (Schulman 2023)

1. **Verification** — for each response, ask the model to retrieve the sources it bases the response on.
2. **Better reward function** — train the [[RewardModel|reward model]] to **punish making things up** more heavily. Currently the RM gets only comparisons (A > B) without an explanation of *why* A is better; a more discriminating loss could push the model toward calibrated confidence.

## The contested empirical record

Per Ch 2:

> "In that same talk, Schulman mentioned that OpenAI found that RLHF helps with reducing hallucinations. However, the InstructGPT paper shows that RLHF made hallucination worse [than SFT alone] (Ouyang et al., 2022)."

Internal contradiction in OpenAI's own reports. Even so, **labelers preferred the RLHF model over the SFT-alone model overall** — RLHF improved other aspects despite the hallucination regression.

## Complement to [[SelfDelusion|self-delusion]]

> "The self-delusion hypothesis focuses on how self-supervision causes hallucinations, whereas the mismatched internal knowledge hypothesis focuses on how supervision causes hallucinations." — Ch 2

The two hypotheses are complementary — both contribute to the overall phenomenon. Self-delusion is the *inference-time* mechanism (model conflates its outputs with facts); internal-knowledge mismatch is the *training-time* mechanism (model is trained to assert things it doesn't know).

## Mitigation via prompting

Some teams add prompts like *"Answer as truthfully as possible, and if you're unsure of the answer, say, 'Sorry, I don't know.'"* — assuming the model has accurate self-knowledge. Asking for **concise responses** also seems to help (fewer tokens → less opportunity to make things up).

## Connections
- [[Hallucination]] — parent phenomenon.
- [[SelfDelusion]] — complementary hypothesis.
- [[SupervisedFinetuning]] / [[BehaviorCloning]] — the training mechanic this hypothesis indicts.
- [[LeoGao]] / [[JohnSchulman]] — the researchers behind the hypothesis.
- [[RewardModel]] — what Schulman proposes to improve.
- [[ai-engineering-ch02-foundation-models]] — primary source.
