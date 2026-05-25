---
title: "Inconsistency"
type: concept
tags: [llm, sampling, failure-mode, evaluation]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Inconsistency

A failure mode of probabilistic LLM outputs: **the model gives different responses for the same or slightly different prompts**. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Inconsistency is when a model generates very different responses for the same or slightly different prompts."

## Two flavors

Ch 2 distinguishes:

| Flavor | Description | Mitigation difficulty |
|---|---|---|
| **Same input → different outputs** | Identical prompt run twice produces different responses. | Easier — cache, fix temperature/top-p/top-k/seed. |
| **Slightly different input → drastically different outputs** | Capitalizing a letter or rephrasing changes the output completely. | Harder — fixing sampling variables can't force consistency across different inputs. |

## Worked example (Ch 2 Fig 2-23)

Huyen tried ChatGPT to score essays. The same prompt gave **3/5 the first run, 5/5 the second**.

## Why it matters

> "Inconsistency can create a jarring user experience. In human-to-human communication, we expect a certain level of consistency. Imagine a person giving you a different name every time you see them."

A real-data point Huyen cites: in December 2023, reviewing **three months of customer-support requests** for an AI company she advised, **1/5 of all support tickets were about inconsistency** of AI models.

## Mitigations for same-input case

1. **Cache the answer** — same question → same cached answer next time.
2. **Fix sampling variables** — temperature, top-p, top-k.
3. **Fix the seed** — the random-number-generator's starting point.

## Mitigations for slightly-different-input case

- **Carefully crafted prompts** (Ch 5).
- **Memory systems** (Ch 6).
- *No deterministic mitigation exists — this is an open engineering problem.*

## The hardware caveat

Even with everything fixed, **100% consistency is not guaranteed**:

> "The hardware the model runs the output generation on can also impact the output, as different machines have different ways of executing the same instruction and can handle different ranges of numbers." — Ch 2

If you self-host, you have control. If you use OpenAI/Google APIs, you don't.

## Inconsistency vs Self-Consistency: same substrate, opposite stance

The wiki's existing [[selfconsistency]] page treats this same probabilistic substrate as a **resource** — sample N times and majority-vote. Ch 2's inconsistency framing treats it as a **failure mode** to mitigate. They're complementary engineering responses to the same underlying [[Sampling|sampling]] mechanism.

## Connections
- [[Hallucination]] — the other probabilistic failure mode.
- [[Temperature]] / [[Topk]] / [[Topp]] — sampling variables to fix.
- [[selfconsistency]] — the resource-stance of the same substrate.
- [[bestofn]] / [[TestTimeCompute]] — exploit inconsistency to find good outputs.
- [[Logprobs]] — useful for understanding model uncertainty.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[AutoregressiveLanguageModel]] — the architecture whose probabilistic nature creates inconsistency.
