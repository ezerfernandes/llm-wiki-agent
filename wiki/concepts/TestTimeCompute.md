---
title: "Test-Time Compute"
type: concept
tags: [inference, sampling, llm, reasoning]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Test-Time Compute

The family of techniques that **generate multiple outputs per query** — trading inference compute for output quality. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Instead of generating only one response per query, you generate multiple responses to increase the chance of good responses."

Ch 2 uses *test-time compute* (the literature's term, despite *test* being a research-time word) for this whole family of inference-time-sampling-many-outputs strategies. The wiki's broader [[testtimescaling|test-time scaling]] page covers the same idea under a different name.

## Strategies named in Ch 2

| Strategy | Description |
|---|---|
| **[[bestofn|Best-of-N]]** | Sample N independent outputs, pick the best by some selector (RM, logprob, heuristic). |
| **[[beamsearch|Beam search]]** | Maintain k most-promising partial-sequence candidates at each decode step. |
| **[[selfconsistency|Self-consistency / SC@N]]** | Sample N times, return the most common answer (majority vote). |
| **Diversity tweaking** | Vary sampling variables across outputs to maximize candidate diversity. |
| **Verifier-guided selection** | Score candidates with a [[Verifier|verifier]] / [[RewardModel|reward model]], pick the highest-scoring. |

## How big a deal is test-time compute?

Per Ch 2, OpenAI's math-problem study (Cobbe et al. 2021) found:

> "The use of verifiers resulted in approximately the same performance boost as a **30× model size increase**. This means that a 100-million-parameter model that uses a verifier can perform on par with a 3-billion-parameter model that doesn't use a verifier."

[[googledeepmind|DeepMind]] (Snell et al. 2024) argues this generalizes: **scaling test-time compute can be more efficient than scaling parameters**.

## How far can it scale?

- **OpenAI (2021)**: performance peaks at ~400 samples; declines beyond (the model finds outputs that fool the verifier).
- **Stanford "Monkey Business"** (Brown et al. 2024): log-linear improvement up to 10,000 samples — much further than OpenAI's peak.
- Huyen's caveat: *"I don't believe anyone in production samples 400 or 10,000 different outputs for each input. The cost would be astronomical."*

## Selection methods

How to pick the best output among N candidates:
1. **Show the user multiple outputs** — let humans pick.
2. **Average logprob** — pick the highest-likelihood sequence; what OpenAI's `best_of` API does.
3. **Reward model / verifier** — pick highest-scoring; Stitch Fix and Grab use this approach.
4. **Heuristics** — shortest output, valid SQL, validates against a grammar, etc.
5. **Most common answer** — [[selfconsistency|self-consistency]] for exact-answer tasks (math, multiple choice).

## Latency hack

TIFIN (Kittipat Kampa, head of AI): generate multiple responses in parallel; **show the user the first response that completes and validates**. Test-time compute as a latency hedge for slow chain-of-thought queries.

## Connections
- [[testtimescaling]] — the same family under a different name; cross-link.
- [[bestofn]] / [[beamsearch]] / [[selfconsistency]] — the named strategies.
- [[Verifier]] / [[RewardModel]] — the selectors.
- [[Logprobs]] — the most basic selector.
- [[StructuredOutputs]] — the "keep generating until output is valid" instance.
- [[Hallucination]] / [[Inconsistency]] — what test-time compute partially mitigates.
- [[ai-engineering-ch02-foundation-models]] — primary source.
