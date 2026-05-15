---
title: "Constitutional AI"
type: concept
tags: [alignment, safety, post-training]
sources: [2312.11805-gemini]
last_updated: 2026-05-10
---

# Constitutional AI

A post-training recipe (Bai et al., 2022, [[Anthropic]]) in which model responses to harm-inducing prompts are **revised by the model itself against an explicit written policy ("constitution")** before being used as SFT or preference-learning data. Replaces some human preference labeling with model-generated critique-and-revise loops grounded in the constitution.

## Reference in this wiki

[[2312.11805-gemini]] reports a "loosely inspired" variant: Google's content policies are injected as constitutions; the Gemini base model's strong zero-shot reasoning is used to revise candidate responses to harm-inducing queries; the revised responses become safety SFT data. This sits alongside conventional human-collected safety SFT.

## See also

- [[RLHF]] — the broader post-training context.
- [[LLM-as-Judge]] — a related "model evaluates model" pattern for evaluation rather than rewriting.
