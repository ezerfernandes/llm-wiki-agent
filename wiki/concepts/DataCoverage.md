---
title: "Data Coverage"
type: concept
tags: [dataset-engineering, data-curation, diversity]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Data Coverage

The dimension of dataset design that measures **whether your training data reflects the range of problems your model will be asked to solve**. Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], coverage is one of the three orthogonal axes of data design alongside [[DataQuality|quality]] and [[DataQuantity|quantity]] — the "right mix of ingredients" in [[ChipHuyen|Huyen]]'s cooking analogy. Many practitioners use [[DataDiversity|"data diversity"]] interchangeably with coverage; Huyen treats them as synonyms.

## Why coverage matters

Real users have a wide range of problems and express those problems in widely varying ways. If your finetuning data captures one slice (e.g., short, well-formatted instructions in English) but real users send another (e.g., long instructions with typos in 12 languages), the model will fail on real traffic regardless of quality or quantity. Coverage is the dimension that ties training data to **deployment distribution**.

## Per-application diversity axes (Ch 8)

| Application | Critical axes |
|---|---|
| French-to-English translation | topic, length, speaking style (not language pairs — fixed) |
| Multilingual chatbot | linguistic + cultural diversity |
| Coding assistant | programming-language diversity |
| Customer support | typo robustness, formality range, intent distribution |
| General assistant | task type, topic, format, length |

## Llama 3 data-mix table (per training phase)

[[Llama|Llama 3]]'s public data-mix is the chapter's canonical reference:

| Domain | Pre-training | SFT | Preference FT |
|---|---|---|---|
| General knowledge (English) | 50% | 82.0% | 52.7% |
| Math and reasoning | 25% | 5.9% | 21.2% |
| Coding | 17% | 6.9% | 14.9% |
| Multilingual | 8% | 5.2% | 3.0% |
| Exam-like | — | — | 8.1% |
| Long context | — | — | 0.1% |

Pre-training over-represents math + code (~42% combined) far above the internet's natural distribution because **annealing the model on high-quality code and math data boosts reasoning benchmarks** — a finding that justifies the heavy mix.

## Coverage saturates

Chung et al. (2022) — *Scaling Instruction-Finetuned Language Models* — found:

| Finetuning task count | Performance |
|---|---|
| 9 → 282 | **Large gains** |
| 282 → 1,836 | Marginal (positive but plateau) |

So coverage matters until it plateaus; once you cover the user's task distribution, additional task variety has diminishing returns.

## Coverage can hurt

[[DataAdditionDilemma|*The Data Addition Dilemma*]] (Shen et al. 2024) demonstrated that adding more **heterogeneous** data can hurt performance — coverage isn't strictly monotonic if the added data doesn't match the target distribution. The cure is **distribution-aligned diversity**, not random diversity.

## Connections

- [[DatasetEngineering]] — parent discipline.
- [[DataQuality]] / [[DataQuantity]] — the other two design axes.
- [[DataDiversity]] — synonym; some practitioners use this term instead.
- [[DataMix]] — operationalizes coverage at the domain-token level.
- [[DataAdditionDilemma]] — the "more isn't always better" counter-result.
- [[Llama|Llama 3]] — the chapter's canonical case study.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
