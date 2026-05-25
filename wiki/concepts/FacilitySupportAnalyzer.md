---
title: "Facility Support Analyzer"
type: concept
tags: [dataset, classification, benchmark, enterprise, structured-extraction, multi-label, meta, llama-prompt-ops, gepa]
sources: [dspy-tutorial-gepa-facility-support-analyzer]
last_updated: 2026-05-24
---

# Facility Support Analyzer

**Facility Support Analyzer** is an enterprise structured-information-extraction dataset released by [[meta|Meta]] under the `llama-prompt-ops` repository (`meta-llama/llama-prompt-ops/use-cases/facility-support-analyzer/dataset.json`). Each of the **200 examples** is a fictional facility-maintenance email addressed to *ProCare Facility Solutions* paired with three gold labels per email:

1. **Urgency** — `Literal['low', 'medium', 'high']` (single-label, 3-way).
2. **Sentiment** — `Literal['positive', 'neutral', 'negative']` (single-label, 3-way).
3. **Categories** — `List[Literal[...]]` over a fixed 10-label vocabulary (multi-label).

## The 10-label categories vocabulary

```
emergency_repair_services
routine_maintenance_requests
quality_and_safety_concerns
specialized_cleaning_services
general_inquiries
sustainability_and_environmental_practices
training_and_support_requests
cleaning_services_scheduling
customer_feedback_and_complaints
facility_management_issues
```

Each example's `answer` field is a JSON string containing a `categories` object mapping each of the 10 labels to a boolean (`true` if applicable, `false` otherwise), plus `urgency` and `sentiment` string fields.

## Canonical task framing

> *"Given an email or message sent in an enterprise setting related to facility maintenance or support requests, the goal is to extract its urgency, assess the sentiment, and identify all relevant service request categories."*

This is the **three-task structured-extraction shape** the dataset canonicalizes — a multi-output classifier whose loss can be decomposed predictor-by-predictor, which makes it a natural fit for [[GEPA|`dspy.GEPA`]]'s **per-predictor [[FeedbackFunction|textual feedback]]** channel.

## Canonical receipt in the wiki

[[dspy-tutorial-gepa-facility-support-analyzer|The official DSPy GEPA tutorial]] uses this dataset to demonstrate **GEPA on a three-`ChainOfThought`-predictor program** with `pred_name`-routed feedback. Splits and headline numbers:

| Slot | Value |
|---|---|
| Total examples | 200 |
| Train / Val / Test | 66 / 66 / 68 (shuffled with `random.Random(0)`) |
| Student LM | [[GPT|GPT-4.1 nano]] |
| Baseline | 75.4% (51.30/68) |
| GEPA `auto="light"` | **87.0% (59.17/68)** |
| Lift | **+11.6 absolute points** |

Tutorial closing line: *"GEPA was able to optimize GPT-4.1 nano's performance from 75% score to 87% in the auto='light' setting."*

## Scoring shape

The tutorial's evaluation metric averages three sub-scores:

- **Urgency**: exact-match (0 or 1).
- **Sentiment**: exact-match (0 or 1).
- **Categories**: per-label match/mismatch accuracy — `(len(correctly_included) + len(correctly_excluded)) / 10`, where `correctly_included` are gold-true labels predicted true and `correctly_excluded` are gold-false labels predicted false.

Final metric = `(score_urgency + score_sentiment + score_categories) / 3`.

The **same comparison logic** is re-projected as textual feedback in `metric_with_feedback` — see [[FeedbackFunction|the FeedbackFunction page]] for the `pred_name`-routed pattern.

## Why this dataset matters for the wiki

- **First non-paper-benchmark GEPA receipt.** The [[2507.19457-gepa|GEPA paper]] benchmarks on six datasets (HotpotQA / IFBench / HoVer / PUPA / AIME-2025 / LiveBench-Math); Facility Support Analyzer is **not** one of them. This tutorial extends GEPA's documented operating envelope to **enterprise structured extraction** outside the paper's evaluation grid.
- **First multi-Signature classification benchmark in the wiki's DSPy corpus.** Sibling Programming-stage tutorials with multi-Signature pipelines ([[dspy-email-extraction-tutorial]], [[dspy-llms-txt-generation-tutorial]]) do not benchmark and do not optimize; this tutorial is the **first multi-Signature receipt with both a quantitative baseline and an optimizer-driven lift**.
- **Canonical test bed for `pred_name`-routed feedback.** The three-predictor decomposition is shallow enough to be reproducible and rich enough to exercise [[FeedbackFunction|multi-predictor textual supervision]].

## Connections

### Canonical tutorial
- [[dspy-tutorial-gepa-facility-support-analyzer]] — the runnable tutorial that uses this dataset.

### Methodological neighbors
- [[GEPA]] — the optimizer the tutorial applies. The Facility Support Analyzer receipt is the wiki's third runnable GEPA trace.
- [[FeedbackFunction]] — the per-predictor textual feedback channel the tutorial exercises via `pred_name`-routed branching.
- [[chainofthought|`dspy.ChainOfThought`]] — the base module composed three times in the program.
- [[Classification]] — the broader activity. **First wiki receipt of GEPA-on-classification.**

### Publisher
- [[meta|Meta]] — dataset publisher. Released under the `llama-prompt-ops` repository alongside other prompt-optimization use cases.

### Adjacent enterprise-extraction tutorials
- [[dspy-email-extraction-tutorial]] — 4-Signature email-triage pipeline (no optimizer, no benchmark). Structurally adjacent to Facility Support Analyzer but Programming-stage-only.
- [[dspy-entity-extraction-tutorial]] — entity extraction (CoNLL-2003). Single-Signature optimized with MIPROv2.
