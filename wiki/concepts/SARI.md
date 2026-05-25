---
title: "SARI"
type: concept
tags: [evaluation, metric, simplification, machine-translation]
sources: [2025-bionlp-archehr-qa-neural]
last_updated: 2026-05-22
---

# SARI

**System output Against References and against the Input** — text-simplification evaluation metric (Xu, Napoles, Pavlick, Chen & Callison-Burch, TACL 4:401–415, 2016). Rewards systems for **adding / keeping / deleting** the right tokens relative to multiple references **and the input** — captures the *transformation* operation rather than just output similarity. Originally for sentence simplification; reused in summarization / paraphrase / QA evaluation.

Used as the **simplification-aware** component of the relevance reward in [[2025-bionlp-archehr-qa-neural|ArchEHR-QA 2025 (Neural)]]. The Neural team's submission scored **73.1** on SARI — best in the leaderboard — reflecting that MIPROv2-optimized prompts produce more aggressive paraphrastic simplification than BLEU-overlap-tuned competitors.

## Connections
- [[bleu|BLEU]] / [[ROUGE]] / [[BERTScore]] / [[AlignScore]] / [[MEDCON]] — sibling generation metrics.
- [[2025-bionlp-archehr-qa-neural]] — application.
