---
title: "HarmfulQA"
type: concept
tags: [benchmark, jailbreak, llm-safety, adversarial, red-teaming]
sources: [2603.19247-prompt-optimization-jailbreaking]
last_updated: 2026-05-22
---

# HarmfulQA

**HarmfulQA** is an adversarial role-playing prompt benchmark for evaluating LLM safety boundaries. Released by **DeCLaRe Lab (2023)** — referenced as `DeCLaRe Lab, 2023` in [[2603.19247-prompt-optimization-jailbreaking]].

## Purpose

A static collection of harmful or role-play-framed user queries used to **stress-test refusal behavior**. Paired typically with a judge or classifier that scores whether the model's response constitutes a safety failure.

## How it's used in this wiki

[[2603.19247-prompt-optimization-jailbreaking]] uses HarmfulQA as one of **two seed pools** (the other is [[JailbreakBench]]) for adaptive prompt search:

- **150 prompts** evenly drawn from HarmfulQA + JailbreakBench.
- Treated as a **distribution of seed queries** $\mathcal{X}$ — not as a static benchmark — so that the optimizer searches the *system-prompt* space $\mathcal{S}$ that maximizes expected [[DangerScore|danger]] across the seed pool.
- The paper's framing: *"we treat HarmfulQA and JailbreakBench as distributions of seed queries, while adaptive optimizers search for instructions maximizing judged danger."* This re-purposes a static benchmark into the *input distribution* of an adaptive attack.

## Why the recast matters

The paper's headline empirical claim — that static safety benchmarks substantially underestimate residual risk — hinges on this reframing. A *single* fixed pass over HarmfulQA with the default system prompt produces a small fraction of failures (the baseline column of Table 1). Iterative search over system prompts using the *same* HarmfulQA queries as seeds drives that failure rate up by **5–9× on open-weights models** and **2–7× on proprietary models**. The conclusion is methodological: any safety evaluation that does not include adaptive search across the system-prompt surface understates risk.

## Related benchmarks

- [[JailbreakBench]] — sibling benchmark used jointly in [[2603.19247-prompt-optimization-jailbreaking]].
- [[CodeAttack]] — code-reframing attack family (single attack vector, not a benchmark pool).

## Connections

- [[2603.19247-prompt-optimization-jailbreaking]] — primary source in this wiki.
- [[Jailbreak]] — broader phenomenon.
- [[redteaming|Red Teaming]] — evaluation methodology HarmfulQA was originally designed to support.
- [[AdversarialPromptSearch]] — when HarmfulQA is used as a *seed pool* (this paper's mode) rather than a *static benchmark*.
- [[DangerScore]] — judge metric scored over HarmfulQA queries.
