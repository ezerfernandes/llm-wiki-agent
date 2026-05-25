---
title: "Data Synthesis"
type: concept
tags: [dataset-engineering, synthetic-data, llm]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Data Synthesis

**Generating data to mimic the properties of real data** — distinct from [[DataAugmentation|data augmentation]], which *derives* new data from real data. Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]]: "Data synthesis generates data to mimic the properties of real data. For example, you can simulate how a mouse moves through a web page to generate data for what bot movements would look like." Synthesized data isn't real; augmented data is.

In practice, [[ChipHuyen|Huyen]] notes the two terms are often used interchangeably "since the goal of both augmentation and synthesis is to automate data creation."

## Five reasons to synthesize (Ch 8)

1. **Increase data quantity** — rare events (weather extremes, accidents, deep-sea exploration), expensive-to-collect domains.
2. **Increase data coverage** — generate targeted adversarial / toxic / safety-edge-case data; balance class distributions.
3. **Increase data quality** — sometimes AI generates better data than humans (math problems beyond average expert difficulty; more-consistent preference ratings).
4. **Mitigate privacy concerns** — healthcare patient records, insurance claims, financial PII — synthesize instead of using real.
5. **Distill models** — required when training a student to imitate a teacher; the teacher's outputs *are* the training data.

## Three classes of technique (Ch 8 taxonomy)

| Class | Examples |
|---|---|
| **[[RuleBasedDataSynthesis\|Rule-based]]** | Templates ([[Faker]], transaction templates), grammar-driven generation, [[AlphaGeometry]]'s 100M Olympiad problems |
| **[[Simulation]]** | [[CARLA]], Waymo SimulationCity, Tesla SF simulation, [[OpenAIDota2\|OpenAI Dota 2 self-play]], robotics sim2real |
| **[[AIPoweredDataSynthesis\|AI-powered]]** | Paraphrasing, [[Backtranslation\|back-translation]], [[ReverseInstruction\|reverse instruction]], [[InstructionDataSynthesis]], [[Cosmopedia]], [[MetaMath]], [[StableToolBench]], [[UltraChat]] |

The third class is the chapter's main contribution — what becomes possible once LLMs can generate human-indistinguishable data at scale.

## Synthetic data verification

Without verification, synthetic data is worthless. Ch 8's verification toolkit:

- **Functional correctness** (code: run unit tests; math: check answers).
- **AI judges** — score 1-5 or good/bad; mitigate [[FirstPositionBias|first-position bias]] by swapping order.
- **Factual-consistency** detection (Ch 4's [[FactualConsistency]] machinery).
- **Heuristic filters** — length, repetition, keyword, source ([[SelfInstruct|Self-Instruct]]'s 4-filter recipe).
- **Anomaly detection** — outlier examples are often low quality.
- **AI content detectors** — if it's easy to distinguish real from synthetic, the synthetic isn't good enough.

## The four limits of AI-synthesized data (Ch 8)

1. **Quality control** — garbage in, garbage out.
2. **[[SuperficialImitation|Superficial imitation]]** — students mimic teacher style without inheriting capability; can force the student to hallucinate (Gudibande et al. 2023).
3. **[[ModelCollapse|Model collapse]]** — recursive training on synthetic data degrades models irreversibly (Shumailov et al. 2023); mixing with real data avoids it but no specific ratio is proven.
4. **Obscure [[DataLineage|data lineage]]** — AI-generated data hides copyright + contamination risk from the upstream model.

## Connections

- [[DataAugmentation]] — sibling technique (derives from real data).
- [[AIPoweredDataSynthesis]] — the AI-generation subclass.
- [[RuleBasedDataSynthesis]] / [[Simulation]] — the two traditional approaches.
- [[knowledgedistillation]] — the canonical use case requiring synthetic data.
- [[ModelCollapse]] / [[SuperficialImitation]] — the two main limits.
- [[DatasetEngineering]] — parent discipline.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
