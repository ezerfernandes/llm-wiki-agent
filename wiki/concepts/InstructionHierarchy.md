---
title: "Instruction Hierarchy"
type: concept
tags: [llm, safety, post-training, prompt-injection-defense, openai]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Instruction Hierarchy

**A post-training scheme that teaches an LLM to prioritize instructions from privileged sources (system prompt) over less-privileged ones (user prompt, tool output).** Introduced by [[WallaceEtAl2024|Wallace et al. 2024]] at [[openai|OpenAI]] in *"The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions."* Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the mechanistic reason [[SystemPrompt|system prompts]] outperform [[UserPrompt|user prompts]] for embedding application-developer behavior, and as a **structural defense against [[PromptInjection|prompt injection]]**.

> "The model might have been post-trained to pay more attention to the system prompt, as shared in the OpenAI paper 'The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions' (Wallace et al., 2024). Training a model to prioritize system prompts also helps mitigate prompt attacks." — Ch 5

## Why it matters

Without instruction hierarchy, a model sees system and user prompts as semantically equivalent strings — they're concatenated into one input. A user can therefore *override* application-developer rules just by saying *"Ignore the above and ..."* The instruction-hierarchy training scheme makes this override much harder:

- **System prompt** > **User prompt** > **Tool output** in privilege ordering.
- The model is trained on examples where the lower-privilege instruction *conflicts* with the higher-privilege one and the correct behavior is to follow the higher.

This is one of the cleanest model-level (rather than wrapper-level) defenses against [[PromptInjection|prompt injection]] and [[IndirectPromptInjection|indirect prompt injection]] — and it is necessary precisely because *"as models get better at following instructions, they also get better at following malicious instructions"* (Ch 5).

## Relation to other defenses

| Layer | Approach | Where the work happens |
|---|---|---|
| **Model** | Instruction hierarchy | Post-training |
| **Prompt** | "Write your system prompt assuming it will become public" | Authoring |
| **Wrapper** | Filters for suspicious patterns / PII | Application code |
| **External** | [[Guardrail\|Guardrails]] ([[LlamaGuard]], [[NeMoGuardrails]], [[GuardrailsAI]]) | Separate model/system |

Instruction hierarchy is **the only defense that scales with model intelligence** rather than against it — the other three become less effective as attackers get smarter, but instruction hierarchy gets *more* effective as the model gets better at recognizing privilege conflicts.

## The four priority levels (full enumeration)

The Ch 5 defenses-supplemental section makes the hierarchy fully explicit — there are **four** privilege levels, not two:

1. **System prompt** (highest)
2. **User prompt**
3. **Model outputs**
4. **Tool outputs** (lowest)

Placing tool outputs at the bottom is the load-bearing structural defense against [[IndirectPromptInjection|indirect prompt injection]] — the model is trained to treat instructions arriving via tool outputs (web pages, retrieved documents, emails) as the *lowest*-trust signal source, neutralizing many injection attacks at the model layer rather than relying on wrapper-level filtering.

## Quantitative result

> "They found that this improves safety results on all of their main evaluations, even increasing robustness by up to 63% while imposing minimal degradations on standard capabilities." — Ch 5 (paraphrasing [[WallaceEtAl2024]])

The ~63% robustness improvement with minimal capability loss is the headline empirical claim that makes instruction-hierarchy training a clear win — unlike many safety interventions, it does not trade off measurable capability.

## Pairs with borderline-request training

Instruction-hierarchy training must be accompanied by **[[BorderlineRequest|borderline-request]] training** — examples where the model learns *safe-helpful* responses to ambiguous queries (e.g., "how do I break into a locked room" → suggest a locksmith). Without this, instruction-hierarchy training inflates [[FalseRefusalRate|false refusal rate]] by teaching the model to refuse anything that *might* be malicious. The joint training target is **low [[ViolationRate|violation rate]] AND low [[FalseRefusalRate|false refusal rate]]**.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[WallaceEtAl2024]] — the OpenAI paper.
- [[openai|OpenAI]] — the lab that introduced it.
- [[SystemPrompt]] / [[UserPrompt]] — the top two sides of the hierarchy.
- [[PromptInjection]] / [[IndirectPromptInjection]] — the attacks it defends against (the latter via the tool-output-lowest rule).
- [[Jailbreak]] — the broader attack family.
- [[Guardrail]] — wrapper-layer alternative.
- [[BorderlineRequest]] / [[ViolationRate]] / [[FalseRefusalRate]] — the joint training targets and metrics.
- [[LLMRedTeaming]] — the discipline whose findings shape the training data.
