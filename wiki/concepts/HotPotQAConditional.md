---
title: "HotPotQA Conditional"
type: concept
tags: [benchmark, qa, multi-hop, conditional-rules, mipro]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# HotPotQA Conditional

A variant of [[hotpotqa|HotPotQA]] introduced by the [[2406.11695-mipro|MIPRO paper (Opsahl-Ong et al. 2024)]] specifically to test the hypothesis that **instruction optimization beats demo optimization when the task has conditional rules not easily expressible via a few examples**.

## The conditional rule

The original [[hotpotqa|HotPotQA]] answer format is plain string. In **HotPotQA Conditional**, the expected answer format **depends on the entity type of the answer**:

- If the answer is a **person** → format one way.
- If the answer is a **date** → format another way.
- If the answer is a **place** → format yet another way.
- Custom metric scores the response against the entity-type-conditional format.

These rules are difficult to convey through a small number of few-shot examples because the rules are *categorical* (entity-type-keyed) and a 4–8-example demo set will not span enough entity types to expose the categorical structure.

## Why it exists in the benchmark

The MIPRO paper uses HotPotQA Conditional to **decisively separate instruction-only from demo-only optimization**:

- Demo-only baselines plateau because the few-shot examples can't articulate the rule.
- Instruction-only optimizers (Module-Level OPRO, 0-Shot MIPRO) lift performance because the proposer LM can write the rules in natural language.
- Joint [[MIPROv2|MIPRO]] is strongest overall.

This is the paper's **Lesson 3** evidence: *"Instruction optimization is most important for tasks with conditional rules that are (i) not immediately obvious to the LM and (ii) not expressible via a limited number of few-shot examples."*

## Results (Table 2)

| Optimizer | Train | Dev | Test |
|---|---|---|---|
| N/A baseline | 13.8 | 10.5 | 6 |
| 0-Shot MIPRO | 22.6 | 20.3 | 14.6 |
| **MIPRO** | **28.4** | **28.1** | **23.3** |

MIPRO lifts the baseline from 6% to **23.3% on test** — a ~17-point absolute gain, the largest relative gain in the entire benchmark.

## Connections

- [[2406.11695-mipro]] — the canonical source.
- [[hotpotqa|HotPotQA]] — the parent benchmark.
- [[DSPyOptimizerBenchmark]] — the seven-task benchmark this variant belongs to.
- [[MIPROv2|MIPRO]] — the optimizer whose value-proposition is most clearly demonstrated here.
- Conditional rules — the failure mode demos-only optimization hits.
- [[IrisTypo]] — sibling "instructions-matter-most" benchmark, but for a different reason (correcting a misspelled seed prompt).
