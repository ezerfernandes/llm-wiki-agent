---
title: "Zero-Shot Chain-of-Thought"
type: concept
tags: [reasoning, prompting, chain-of-thought, llm]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Zero-Shot Chain-of-Thought

**Eliciting step-by-step reasoning without providing any few-shot example chains, simply by appending a trigger phrase to the prompt.** Kojima et al. 2022, *"Large Language Models Are Zero-Shot Reasoners"*. Named in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]] as the **example-free variant** of [[chainofthought|chain-of-thought]] (CoT):

> *"Instead of providing examples, we can simply ask the generative model to provide the reasoning (zero-shot chain-of-thought). There are many different forms that work but a common and effective method is to use the phrase 'Let's think step-by-step.'"* — Ch 6

## The canonical trigger

```
Let's think step-by-step.
```

Appended to the prompt — usually at the end. Ch 6's worked example on the cafeteria-apples problem produces the step-by-step solution that arrives at *9 apples*:

> *Step 1: Start with the initial number of apples, which is 23.*
> *Step 2: Subtract the number of apples used to make lunch, which is 20. So, 23 - 20 = 3 apples remaining.*
> *Step 3: Add the number of apples bought, which is 6. So, 3 + 6 = 9 apples.*

## Alternative triggers

Ch 6 names two alternative triggers (citing Yang et al. 2023 *"Large Language Models as Optimizers"*):
- **"Take a deep breath and think step-by-step."**
- **"Let's work through this problem step-by-step."**

The chapter's framing: *"although the prompt 'Let's think step by step' can improve the output, you are not constrained by this exact formulation."* — the operative mechanism is **prompting the model to spend tokens on a reasoning trace before committing to the answer**, not the specific trigger phrase.

## Position in the CoT variant catalog

[[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]] catalogs four CoT variants:
- **Zero-shot CoT** — *"Think step by step before arriving at an answer."* (this page)
- **Zero-shot CoT with rationale** — *"Explain your rationale before giving an answer."*
- **Zero-shot CoT with explicit steps** — *"Follow these steps to find an answer: 1. ... 2. ... 3. ..."*
- **One-shot CoT** — one example of question + steps + answer.

Ch 6's *"Let's think step-by-step"* trigger is the canonical zero-shot CoT form; the alternative triggers are equivalent operating points within this row.

## When zero-shot CoT works (and when it doesn't)

Per Ch 6's compute-justification framing of CoT generally: *"each additional token in this reasoning process allows the LLM to stabilize its output"* — zero-shot CoT works because reasoning tokens are produced *before* the final-answer tokens, allowing the model to consume its own intermediate output as conditioning context. The technique succeeds primarily on **arithmetic / commonsense / symbolic-reasoning** tasks where step-by-step decomposition naturally maps to the problem. For open-ended generation or tasks lacking sequential decomposition, the trigger has less effect.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[chainofthought|Chain-of-Thought]] — parent concept; zero-shot CoT is a variant.
- [[InContextLearning]] — broader paradigm; zero-shot CoT is in-context-learning with zero examples + reasoning trigger.
- [[ZeroShotLearning]] — sibling zero-example variant for non-reasoning tasks.
- [[selfconsistency]] — pairs naturally with zero-shot CoT: sample N reasoning chains, majority-vote the answers.
- [[TreeOfThoughts]] — multi-path elaboration of the same intuition.
- [[ai-engineering-ch05-prompt-engineering]] — Huyen Ch 5's variant catalog.
- [[hands-on-llm-ch06-prompt-engineering]] — Alammar & Grootendorst Ch 6's framing.
- [[System1And2]] — the Kahneman framing zero-shot CoT operationalizes.
