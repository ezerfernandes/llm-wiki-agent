---
title: "Synthetic Data"
type: concept
tags: [concept]
sources: [2604.28181-synthetic-computers-at-scale, ai-engineering-ch08-dataset-engineering, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Synthetic Data

Machine-generated training data, often used when real trajectories are private/expensive. Ge et al. argue the next frontier is synthesizing not just tasks but the surrounding context (filesystem + artifacts + history).

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

[[ChipHuyen|Huyen]] in Ch 8 expands the wiki's coverage of synthetic data into a full taxonomy:

### Five reasons to synthesize

1. **Increase data quantity** — rare events (extreme weather, accidents, deep-sea), private domains.
2. **Increase data coverage** — adversarial / toxic / safety edge cases; class imbalance.
3. **Increase data quality** — sometimes AI beats humans (complex math problems, consistent preference ratings, tool-use traces).
4. **Mitigate privacy concerns** — healthcare, insurance, finance.
5. **[[knowledgedistillation|Distill models]]** — the use case that *requires* synthetic data.

### Three classes of technique

- **[[RuleBasedDataSynthesis|Rule-based]]** — templates ([[Faker]]) + grammar-driven generators; [[AlphaGeometry]]'s 100M procedural Olympiad examples.
- **[[Simulation]]** — virtual environments ([[CARLA]], Waymo SimulationCity, [[Tesla|Tesla]] SF sim, [[OpenAIDota2]] self-play).
- **[[AIPoweredDataSynthesis|AI-powered]]** — paraphrasing, [[Backtranslation|back-translation]], [[ReverseInstruction|reverse instruction]], [[InstructionDataSynthesis]], [[Cosmopedia]], [[MetaMath]], [[UltraChat]], [[StableToolBench]], [[Nemotron4]].

### Four limits

1. **Quality control** — garbage in, garbage out.
2. **[[SuperficialImitation|Superficial imitation]]** — students mimic style without inheriting capability, can be forced to hallucinate (Gudibande et al. 2023).
3. **[[ModelCollapse|Model collapse]]** — recursive synthetic-data training degrades models irreversibly (Shumailov et al. 2023); avoided by mixing with real data.
4. **Obscure [[DataLineage|data lineage]]** — hides upstream copyright + contamination risk.

### Counter-intuitive findings

- AI-synthesized data sometimes **exceeds** human data quality (math difficulty, preference consistency, tool-use efficiency — Ch 8 / Llama 3 team).
- **Reverse-direction distillation works**: [[Nemotron4|Nemotron-4-340B]] (student) exceeded Mixtral-8x7B (teacher) using teacher-generated synthetic data — disproving the "teacher ≥ student" framing.
- **Verifiability drives usage**: coding is the dominant synthetic-data domain because it's functionally verifiable (Llama 3's 2.7M synthetic coding examples).

## In ML systems (mlsysbook)

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) treats [[SyntheticDataGeneration|synthetic generation]] as an acquisition channel that *changes the scaling constraint* (human labor → validation burden), valuable for rare-event coverage and augmentation (AutoAugment, RandAugment, SpecAugment). Its fallacy-flag echoes the limits above: synthetic data **augments but cannot replace** real collection — a KWS model trained purely on synthesized speech fails on unmodeled accents/noises.

## Connections
- [[SyntheticDataGeneration]] — the mlsysbook acquisition-channel page.
- [[DataAugmentation]] — the augmentation subset.
- [[mlsysbook-ch04-data-engineering]] — source.
