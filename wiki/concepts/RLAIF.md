---
title: "RLAIF"
type: concept
tags: [post-training, alignment, llm, preference-finetuning]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# RLAIF

**Reinforcement Learning from AI Feedback** — a [[PreferenceFinetuning|preference-finetuning]] technique that replaces human labelers with an **AI labeler** in the comparison-data-collection step. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], RLAIF is one of three named preference-finetuning techniques (alongside [[rlhf|RLHF]] and [[DPO|DPO]]) and is *"potentially used by [[anthropic|Claude]]."*

## How it differs from RLHF

In standard [[rlhf|RLHF]]:
- Human labelers compare candidate responses and select the preferred one.
- A reward model is trained on this human-collected comparison data.
- The foundation model is then optimized against the reward model.

In RLAIF, **the human labeling step is replaced by an AI labeler** — typically a strong existing model judging candidate responses against some specification or constitution. This is the same idea as Anthropic's **[[constitutionalai]]** approach (which uses model-generated critiques rooted in an explicit policy "constitution").

## Why use RLAIF

- **Cost.** Human comparison labeling at $3.50/sample (Llama 2 author Thomas Scialom, cited in Ch 2) is expensive at scale.
- **Speed.** AI labeling is essentially instantaneous and consistent.
- **Scalability.** Generating 100K AI-judged comparisons is feasible; 100K human-judged comparisons typically isn't.

## Trade-offs

- **The AI labeler's biases become the model's preferences.** If the AI judge is itself biased or wrong, RLAIF propagates that.
- **Risk of [[RewardHacking|reward hacking]] is amplified** when both judge and trainee share architecture.

## Position in the wiki

RLAIF is the **least-detailed** of the three techniques Ch 2 names — Huyen flags it as a likely-Claude approach without claiming definitive knowledge. The wiki's [[rlhf]] page already mentions [[constitutionalai]] as the canonical example of model-generated preferences feeding back into RLHF; RLAIF is the more general name for that pattern.

## Connections
- [[PreferenceFinetuning]] — parent stage.
- [[rlhf]] — the human-labeled counterpart.
- [[DPO]] — the third named technique in Ch 2.
- [[RewardModel]] — the artifact RLAIF still trains, just with AI-generated labels.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[LLMAsAJudge]] — closely related general pattern (LM judging LM output).
