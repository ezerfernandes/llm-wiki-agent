---
title: "Data Quality"
type: concept
tags: [data, evaluation]
sources: [ai-engineering-ch08-dataset-engineering, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Data Quality

The fitness of data for its intended use, measured along axes like completeness, accuracy, consistency, timeliness, and uniqueness. Bad data dominates model failures; tools like [[GreatExpectations|Great Expectations]] and [[ConfidentLearning]] enforce constraints, and [[DataObservability]] catches regressions.

## Mechanical vs semantic quality (mlsysbook Ch 4)

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) distinguishes two dimensions: **mechanical** quality (the *Container* — is `age` an integer? deterministic yes/no) and **semantic** quality (the *Content* — is the `age` distribution shifting? probabilistic). A dataset can be mechanically perfect (no nulls, correct types) yet semantically broken (all users suddenly 25 from a default-value change). The self-driving-car LiDAR labels misaligned by 10–20 cm passed every [[SchemaValidation|schema check]] for 3 months because each record was structurally valid — only **statistical** monitoring caught it. Robust systems validate both, with synchronous schema checks (microseconds) plus asynchronous statistical validation ([[KolmogorovSmirnovTest|K-S test]], [[PopulationStabilityIndex|PSI]]) on 1–10% sampled traffic. **Data quality as code** ([[GreatExpectations|Great Expectations]] / Pandera / Pydantic) catches ~60% of issues before training.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

### Six characteristics (Ch 8 finetuning-specific definition)

[[ChipHuyen|Huyen]] defines high-quality finetuning data along six axes — narrower than the broader IBM (completeness, uniqueness, validity, timeliness, accuracy, consistency, fitness-for-purpose) or Wikipedia frameworks, and explicitly tuned to *finetuning* rather than general data quality:

1. **Relevant** — examples should match the task. A 19th-century legal dataset is irrelevant for a 21st-century legal QA model, but highly relevant for a "legal system in 19th century" task.
2. **Aligned with task requirements** — if the task needs factual consistency, annotations should be factually correct; if creative, creative; if a score plus justification, both; if concise, concise.
3. **Consistent** — annotations should agree across examples and annotators. Inconsistency confuses models.
4. **Correctly formatted** — match the model's expected format; remove HTML tags, trailing whitespace, inconsistent casing/numbers.
5. **Sufficiently unique** — duplicates introduce biases and contamination; the word "sufficiently" allows for use-case-specific duplication tolerance.
6. **Compliant** — respects laws and internal policies (no PII, copyright violations, sensitive data).

### Why this differs from general data quality

> "While I love writing, one of the things I absolutely do not enjoy is trying to condense everyone's opinions into one single definition." — Ch 8 footnote

Huyen's six-axis definition is intentionally narrower than IBM's seven-axis (completeness, uniqueness, validity, timeliness, accuracy, consistency, fitness-for-purpose) and Wikipedia's broader twelve-plus axes (adding accessibility, comparability, credibility, flexibility, plausibility). The focus on finetuning sharpens the axes.

### Quality beats quantity

The chapter's most-quoted empirical claim: **small high-quality datasets outperform large noisy ones**.

| Source | Evidence |
|---|---|
| [[LIMA]] (Zhou et al. 2023) | 1K curated → 65B Llama tied/beat GPT-4 in 43% of comparisons |
| [[YiModel\|Yi]] (Young et al. 2024) | 10K curated > hundreds of thousands of noisy |
| [[Llama|Llama 3]] (Dubey et al. 2024) | Human data is more error-prone than AI-assisted annotation for nuanced safety policies |

### "Aligned" vs "accurate"

> "I used 'aligned' instead of 'accurate' or 'correct' because, depending on the task, an accurate or correct response might not be what a user wants."

A user asking for *brainstorming* doesn't want the *most accurate* answer — they want creative variety. "Aligned with task requirements" captures the user-intent dimension that "accurate" doesn't.
