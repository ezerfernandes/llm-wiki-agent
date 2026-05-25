---
title: "ORPO (Odds Ratio Preference Optimization)"
type: concept
tags: [preference-alignment, fine-tuning, sft, dpo, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# ORPO — Odds Ratio Preference Optimization

**ORPO** (Hong, Lee & Thorne 2024, arXiv:2403.07691) — *"Monolithic preference optimization without reference model."* A preference-alignment method that **collapses the two-pass [[SupervisedFinetuning|SFT]] + [[DPO]] pipeline into a single training process**, eliminating the need for a separate SFT stage *and* the reference model that DPO requires.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] introduces ORPO at the end of the preference-tuning section as the **forward-looking simplification** of the SFT-then-DPO pipeline the chapter just walked:

> *"Since the release of DPO, new methods of aligning preferences have been developed. Of note is Odds Ratio Preference Optimization (ORPO), a process that combines SFT and DPO into a single training process. It removes the need to perform two separate training loops, further simplifying the training process while allowing for the use of QLoRA."*
> — Ch 12

The implied advantage chain:

| Pipeline | Loops | Reference model | Reward model | QLoRA-compatible |
|---|---|---|---|---|
| [[rlhf|RLHF]] (SFT → RM → PPO) | 3 | — | yes | partial |
| SFT → [[DPO]] | 2 | yes | no | yes |
| **ORPO** | **1** | **no** | **no** | **yes** |

## How ORPO differs from DPO (concept-level)

- **DPO** needs a frozen reference model (typically the SFT checkpoint) to compute log-probability shifts on chosen vs rejected.
- **ORPO** uses an **odds-ratio penalty term** added to the standard SFT cross-entropy loss — there's no separate reference model, just a single training objective that combines the chosen-prediction loss with a penalty on rejected-prediction likelihood.

## Position in the preference-alignment family

| Method | Year | Citation in Ch 12 |
|---|---|---|
| [[PPO]] | 2017 | Schulman et al., arXiv:1707.06347 |
| [[DPO]] | 2023 | Rafailov et al., arXiv:2305.18290 |
| **ORPO** | 2024 | Hong, Lee & Thorne, arXiv:2403.07691 |

Each successor simplifies the prior method: DPO removed the reward model and the RL loop; ORPO removes the separate SFT stage and the reference model.

## Connections

- [[DPO]] — the immediate predecessor ORPO simplifies.
- [[PPO]] / [[rlhf]] — earlier preference-alignment methods.
- [[SupervisedFinetuning]] — what ORPO folds into the same loss.
- [[PreferenceFinetuning]] — the parent regime.
- [[QLoRA]] — ORPO is QLoRA-compatible, preserving the memory advantages.
- [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]] — Huyen's broader preference-finetuning framing.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
