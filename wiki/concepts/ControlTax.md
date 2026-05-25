---
title: "Control Tax"
type: concept
tags: [ai-control, backdoor-generation, dataset-pipeline, ukaisi]
sources: [dspy-tutorial-gepa-trusted-monitor]
last_updated: 2026-05-24
---

# Control Tax

**ControlTax** is the backdoor-generation pipeline used by [[ControlArena|`control_arena`]] to produce the [[APPSBenchmark|APPS]] **backdoor split**: paired (honest_code, attack_code, backdoor_input) triples a strong LLM generates by inserting plausible backdoors into known-correct competitive-programming solutions. Named via the `backdoor_source="control_tax"` kwarg in `control_arena.settings.apps.apps_setting.get_dataset(...)`.

## Why a generation pipeline

A [[TrustedMonitor|trusted monitor]] cannot be evaluated against **naturally-occurring backdoors** — there aren't enough of them, and they're not labeled. The [[AIControl|AI Control]] research program needs a **synthetic but plausible** backdoor source to evaluate monitor protocols at scale.

ControlTax solves this by prompting a strong LLM (the "attacker") to:
1. Read a known-correct APPS solution.
2. Insert a minimal modification that **passes the original test cases** but produces a different output on at least one **attacker-chosen trigger input**.
3. Return both the modified code and the trigger.

The result is a dataset of `~6,300+` synthetic-but-realistic backdoor attempts the trusted monitor must catch.

## The naming

The name "Control Tax" likely riffs on **alignment tax** — the cost of safety constraints on capability. ControlTax measures the *capability* cost (in monitor accuracy, deployment latency, false-positive rate) of running an AI-control protocol vs. trusting the strong model directly.

## Adversarial completeness

ControlTax is a **white-box adversarial dataset** in the sense that the attacker model is given everything it needs to construct successful backdoors (the original solution, the test suite, freedom in choosing the trigger). This makes it a **strong defense benchmark** — a trusted monitor that beats ControlTax-generated backdoors generalizes to weaker, real-world backdoor attempts.

## Tutorial usage

[[dspy-tutorial-gepa-trusted-monitor]] selects ControlTax explicitly:

```python
samples = get_dataset(
    has_backdoor_solution=True,
    backdoor_source="control_tax",
)
```

The trusted monitor (GPT-4.1 Nano) trained against ControlTax-generated backdoors reaches **0.81 comparative-pair accuracy** under [[GEPA]] optimization (baseline 0.69; final pareto-front 0.95).

## Connections

- [[APPSBenchmark]] — the host dataset.
- [[ControlArena]] — the library exposing ControlTax via `backdoor_source` kwarg.
- [[CodeBackdoor]] — the threat-model artifact ControlTax produces.
- [[TrustedMonitor]] — the defender evaluated against ControlTax-generated backdoors.
- [[AIControl]] — the parent safety paradigm.
- [[UKAISI]] — likely originator of the pipeline (`control_arena` is theirs).
- [[dspy-tutorial-gepa-trusted-monitor]] — first DSPy receipt against ControlTax-generated data.
- [[AlignmentTax]] — etymological inspiration; the conceptual cousin (cost of safety).
- [[2312.06942-ai-control]] — paper framing the threat model ControlTax instantiates (forward reference; not yet ingested).
