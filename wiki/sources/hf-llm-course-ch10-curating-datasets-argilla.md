---
title: "HuggingFace LLM Course — Ch 10: Curate high-quality datasets with Argilla"
type: source
tags: [hf-llm-course, course, argilla, data-annotation, data-curation, rlhf]
date: 2026-05-23
source_file: raw/hf-llm-course/ch10-curating-datasets-argilla.md
---

## Summary

Chapter 10 of the HuggingFace LLM Course is a hands-on introduction to [[Argilla]], an open-source data annotation and curation platform now stewarded by Hugging Face. The chapter argues that high-quality training data — not just more data — is the lever that determines model quality, and walks through the end-to-end workflow for turning a raw Hub dataset (`SetFit/ag_news`) into a curated, human-reviewed dataset suitable for text classification and named entity recognition. It covers deploying an Argilla instance on [[HuggingFaceSpaces]], connecting via the Python SDK, declaring an annotation schema with `rg.Settings` (fields + questions), uploading records with field mappings for pre-annotation, distributing work across annotators with configurable minimum-response thresholds, writing [[AnnotationGuidelines]], and finally exporting the annotated dataset back to the Hugging Face Hub as either filtered records or a fully round-trippable Argilla dataset.

## Key Claims

- High-quality, task-specific data is the dominant factor in model performance; generic Hub datasets often don't fit a specific use case and must be curated. ([[DataQuality]], [[DataCuration]])
- Argilla turns unstructured data into structured, labeled data and supports gathering human feedback for LLMs and multi-modal models — including [[RLHF]]-style preference data.
- The easiest deployment path is the official Argilla Space template on [[HuggingFaceSpaces]]; enabling **Persistent storage** is required to survive Space pauses/restarts.
- Three credentials are needed to drive Argilla programmatically: an API URL (the Space's Direct URL, `https://..hf.space`), an API key from "My Settings," and an HF access token with write permissions for private Spaces.
- An Argilla dataset is configured via `rg.Settings`, which composes **fields** (data shown to annotators, e.g. `TextField`) and **questions** (annotation tasks, e.g. `LabelQuestion`, `SpanQuestion`).
- `LabelQuestion` models text classification; `SpanQuestion` models token-level NER over a named field — labels (`PERSON`, `ORG`, `LOC`, `EVENT`) are declared up front.
- Records are uploaded with `dataset.records.log(data, mapping=...)`, and column→question mappings turn existing dataset labels into **pre-annotations**, accelerating review. (See [[PreAnnotation]] / [[ActiveLearning]] adjacent concepts.)
- Logging is asynchronous: annotators can start working in the UI while records are still being ingested.
- Writing explicit [[AnnotationGuidelines]] is best practice, especially for teams — they align annotators on label semantics and resolve edge-case conflicts.
- The **minimum submitted responses** setting controls task distribution: 1 = single-annotator (fast), >1 = multiple annotators per record (enables [[InterAnnotatorAgreement]] analysis); the value must be ≤ total annotators.
- Records in Argilla flow through statuses (`submitted`, `draft`, `discarded`); a record reaches `completed` only when the minimum-response threshold is met, and a completed record can carry multiple responses with mixed statuses.
- When Argilla is deployed on a HF Space, team members can authenticate via Hugging Face OAuth — no manual user provisioning required.
- Annotated data is exported back to the Hub two ways: `filtered_records.to_datasets().push_to_hub(...)` (just rows) or `dataset.to_hub(repo_id=...)` (rows + Argilla settings, fully round-trippable via `rg.Dataset.from_hub`).
- This round-trippable export makes Argilla datasets a portable, sharable artifact — others can re-open the dataset in their own Argilla instance with one line of code.
- Chapter positions Argilla as the bridge between Chapter 5 (building datasets with [[Datasets]]) and Chapter 6 (fine-tuning) — i.e., curation sits between raw data and model training.

## Key Quotes

> "The key to training models that perform well is to have high-quality data." — section 1

> "With Argilla you can: turn unstructured data into structured data ... curate a dataset to go from a low-quality dataset to a high-quality dataset ... gather human feedback for LLMs and multi-modal models ... invite experts to collaborate with you in Argilla, or crowdsource annotations!" — section 1

> "You may want to enable **Persistent storage** so the data isn't lost if the Space is paused or restarted." — section 2, deployment warning

> "In our mapping, we've specified that the `label_text` column in the dataset should be mapped to the question with the name `label`. In this way, we'll use the existing labels in the dataset as pre-annotations so we can annotate faster." — section 3, on pre-annotation

> "Sometimes, you want to have more than one submitted response per record, for example, if you want to analyze the inter-annotator agreement in your task." — section 4, multi-annotator workflow

> "Records with `completed` status ... could have more than one response and ... each response can have any status from `submitted`, `draft` or `discarded`." — section 5, status model

## Code & Patterns

**Connecting to an Argilla instance:**
```python
import argilla as rg

HF_TOKEN = "..."  # only for private spaces
client = rg.Argilla(
    api_url="...",
    api_key="...",
    headers={"Authorization": f"Bearer {HF_TOKEN}"},
)
client.me  # sanity check
```

**Declaring a dataset schema (`rg.Settings` — fields + questions):**
```python
settings = rg.Settings(
    fields=[rg.TextField(name="text")],
    questions=[
        rg.LabelQuestion(
            name="label", title="Classify the text:",
            labels=data.unique("label_text"),
        ),
        rg.SpanQuestion(
            name="entities",
            title="Highlight all the entities in the text:",
            labels=["PERSON", "ORG", "LOC", "EVENT"],
            field="text",
        ),
    ],
)
```
The docs note additional advanced settings, namely **metadata** and **vectors** (for semantic-similarity search over records), beyond fields/questions.

**Creating the dataset and logging records with a column→question mapping (pre-annotation):**
```python
dataset = rg.Dataset(name="ag_news", settings=settings)
dataset.create()
dataset.records.log(data, mapping={"label_text": "label"})
```

**Multi-annotator / task distribution:** configured in the dataset settings page in the UI via the "minimum submitted responses" knob — drives the [[InterAnnotatorAgreement]] workflow.

**Filtering records by status with `rg.Query` / `rg.Filter`:**
```python
status_filter = rg.Query(filter=rg.Filter([("status", "==", "completed")]))
filtered_records = dataset.records(status_filter)
```

**Exporting to the Hub (two flavors):**
```python
# (a) records only -> a plain HF Dataset
filtered_records.to_datasets().push_to_hub("argilla/ag_news_annotated")

# (b) full Argilla dataset incl. settings (round-trippable)
dataset.to_hub(repo_id="argilla/ag_news_annotated")

# Re-import on another Argilla instance:
dataset = rg.Dataset.from_hub(repo_id="argilla/ag_news_annotated")
```

**Worked example dataset:** `SetFit/ag_news` (news classification), repurposed to two tasks simultaneously — topic classification (`LabelQuestion`) and NER (`SpanQuestion`).

> Note: this chapter uses the modern `rg.Dataset` / `rg.Settings` API (Argilla 2.x). Earlier Argilla used a `FeedbackDataset` abstraction; the new API generalizes it via `rg.Settings(fields=..., questions=..., metadata=..., vectors=...)`.

## Connections

- [[Argilla]] — the platform this chapter teaches; open-source data annotation tool, part of the Hugging Face ecosystem.
- [[HuggingFaceSpaces]] — recommended deployment target via the official Argilla Space template.
- [[HuggingFaceHub]] — source of raw datasets and destination for curated, exported datasets.
- [[Datasets]] — the 🤗 Datasets library; `load_dataset` feeds records into Argilla and `push_to_hub` exports them.
- [[DataCuration]] — the central activity of the chapter: going from low- to high-quality data.
- [[DataAnnotation]] — the human-in-the-loop labeling step.
- [[DataQuality]] — the motivating quality property the curation pipeline targets.
- [[AnnotationGuidelines]] — explicit written rules that align annotators on label semantics.
- [[InterAnnotatorAgreement]] — measurable via Argilla's multi-response distribution setting.
- [[PreAnnotation]] — using existing labels (via field mapping) as suggestions to speed review.
- [[TextClassification]] — modeled as `rg.LabelQuestion`.
- [[NamedEntityRecognition]] / [[TokenClassification]] — modeled as `rg.SpanQuestion` over a named field.
- [[RLHF]] / [[HumanFeedback]] — Argilla is positioned as a tool to gather preference/feedback data for LLMs.
- [[FineTuning]] — the downstream consumer of curated datasets (Ch. 6 of the same course).
- [[distilabel]] — Argilla's sibling synthetic-data library (not covered explicitly here, but part of the same ecosystem).
- [[HFLLMCourse]] — sibling chapter pages (Ch 5 datasets, Ch 6 fine-tuning).

## Contradictions

- None observed against existing wiki content. The chapter is a tooling tutorial; its claim that "high-quality data is the key to good models" aligns with the [[ScalingLaws]] / [[DataQuality]] threads already in the wiki rather than contradicting them. If older wiki pages reference Argilla's `FeedbackDataset` API, note that this chapter uses the newer unified `rg.Settings` API — a versioning shift, not a contradiction.
