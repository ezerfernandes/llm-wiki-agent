---
title: "Model Collapse"
type: concept
tags: [synthetic-data, training, llm-failure-mode, data-selection, mlsysbook]
sources: [ai-engineering-ch08-dataset-engineering, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Model Collapse

**Irreversible degradation of model performance from recursive training on AI-generated data.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], the phenomenon was named by Shumailov et al. (2023) in *"The Curse of Recursion: Training on Generated Data Makes Models Forget"*, and demonstrated for Variational Autoencoders, Gaussian Mixture Models, and LLMs. Later restated by the same authors in *"AI Models Collapse When Trained on Recursively Generated Data"* (Nature, July 2024).

## Mechanism

AI models are more likely to generate **probable events** than improbable ones. Over multiple iterations:

- Probable events become **over-represented**.
- Improbable events become **under-represented**.

The model forgets rare events; the distribution narrows; over enough iterations the model collapses to a sharp mode.

## Where collapse can occur

Both **pre-training and post-training** are vulnerable per Shumailov et al. — the phenomenon isn't restricted to a particular training phase.

## Is it inevitable?

[[ChipHuyen|Huyen]] surveys the open literature:

| Claim | Source |
|---|---|
| Inevitable if dataset is entirely synthetic | Shumailov et al. 2023 (original framing) |
| **Avoided by mixing synthetic with real data** | Gerstgrasser et al. 2024 ("Is Model Collapse Inevitable?"), Bertrand et al. 2023, Dohmatob et al. 2024 |
| **No paper recommends a specific mixing ratio** | open question |

## Counter-examples — large synthetic data, no observed collapse

- **Common 7B Language Models Already Possess Strong Math Capabilities** (Li et al. 2024) — synthetic math data scales to ~1M examples with **no saturation** for finetuning Llama 2-7B on math.
- **[[Nemotron4|Nemotron-4 340B-Instruct]]** — 98% synthetic data in instruction + preference finetuning; no collapse in one iteration.

Caveat: both were **single-iteration** experiments, not the recursive setup that triggers collapse.

## Bias amplification (related phenomenon)

> *"Data Feedback Loops: Model-driven Amplification of Dataset Biases"* (Taori & Hashimoto 2023): when models are trained on datasets that include previous model outputs, existing biases can be amplified.

Counter-finding: the *more faithful* the model's outputs to the original training distribution, the *more stable* the feedback loop. The mechanism is the same as model collapse but the failure mode is bias amplification rather than capability loss.

## Practical advice from Ch 8

- Mix synthetic with real (no specific ratio recommended).
- Verify synthetic data quality (functional correctness or AI judges).
- Track [[DataLineage|data lineage]] — recursive contamination is hard to detect after-the-fact.
- Limit recursion depth.

## In [[mlsysbook-ch09-data-selection|Machine Learning Systems Ch 9]]

Reddi Ch 9 cites Shumailov et al. 2024 with a concrete degradation curve: generative models systematically underrepresent tail distributions, so recursive training compresses the tails each generation — **original diversity can drop below 50% by generation 5**. This is the chapter's central caution against pure synthetic training and a key reason its optimal mixes are 50–80% synthetic + 20–50% real (alongside the [[DomainGap|domain gap]]).

## Connections

- [[SuperficialImitation]] — sibling limit on AI-generated data; about teacher → student knowledge transfer.
- [[DataSynthesis]] / [[AIPoweredDataSynthesis]] / [[SyntheticDataGeneration]] — the practice that risks collapse.
- [[DomainGap]] — the second failure mode of synthetic-only training in Ch 9.
- [[DataLineage]] — the tracking discipline that detects recursive contamination.
- [[Hallucination]] — the failure mode collapsed models often exhibit.
- [[ai-engineering-ch08-dataset-engineering]] / [[mlsysbook-ch09-data-selection]] — sources.
