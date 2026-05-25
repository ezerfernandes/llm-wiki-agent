---
title: "MedHELM"
type: concept
tags: [benchmark, leaderboard, medical-nlp, evaluation, stanford]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MedHELM

**Medical extension of the HELM (Holistic Evaluation of Language Models) leaderboard.** Stanford's effort to systematically benchmark medical LMs across a unified evaluation suite. Ref [73] in [[2507.03152-medval]].

## Role in MedVAL

[[2507.03152-medval]] uses MedHELM's published baseline numbers to choose **GPT-4o and GPT-4o Mini** for the [[MEDEC]] external-validation experiment in §3.6 — *"as their baseline performance is reported on the MedHELM leaderboard, enabling a fair, apples-to-apples comparison."* This inherits comparison rigor without re-running zero-shot baselines.

## Scope

Authors of MedVAL acknowledge (§5 Limitations) that **MedVAL-Bench's six tasks do not cover the full medical-LM evaluation spectrum** — broader benchmarks like MedHELM, MedS-Bench, HealthBench remain future targets. MedHELM is positioned as the **canonical broader-evaluation benchmark** beyond MedVAL-Bench's risk-graded scope.

## Connections

- [[2507.03152-medval]] — uses MedHELM-reported baselines for external comparison.
- [[stanforduniversity|Stanford]] — host institution.
- [[MedicalTextValidation]] / [[MedVALBench]] — narrower-scope sibling.
- [[MEDEC]] — listed benchmark used by MedVAL for OOD testing.
