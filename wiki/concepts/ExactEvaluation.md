---
title: "Exact Evaluation"
type: concept
tags: [evaluation, methodology, ai-engineering]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Exact Evaluation

**Exact evaluation** produces *"judgment without ambiguity"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]). It's the counterpart to **subjective evaluation** (where the result depends on the grader — e.g., essay grading or [[LLMAsAJudge|AI-as-judge]]).

## Two branches

Ch 3 partitions exact evaluation into two families:

1. **[[FunctionalCorrectness|Functional correctness]]** — does the system actually perform its intended function? Measurable for code (execute the generated code, check outputs — [[ExecutionAccuracy]] / [[PassAtK]]), game bots (Tetris score), and other tasks with measurable objectives.

2. **[[SimilarityMeasurement|Similarity to reference data]]** — score generated outputs against curated references. Three sub-flavors:
   - **[[ExactMatch|Exact match]]** — binary: does the output match a reference exactly (or contain it)?
   - **[[LexicalSimilarity|Lexical similarity]]** — surface-overlap metrics ([[bleu|BLEU]], [[ROUGE]], [[METEOR]], [[TER]], [[CIDEr]], [[EditDistance|edit distance]] / [[FuzzyMatching|fuzzy matching]], [[NGramSimilarity|n-gram similarity]]).
   - **[[SemanticSimilarity|Semantic similarity]]** — embedding-space similarity ([[BERTScore]], [[MoverScore]]). *"While I put semantic similarity in the exact evaluation category, it can be considered subjective, as different embedding algorithms can produce different embeddings. However, given two embeddings, the similarity score between them is computed exactly."*

## Why this distinction matters

Ch 3 contrasts exact evaluation with [[LLMAsAJudge|AI-as-judge]] (subjective by construction) to motivate the trade-off:

| Property | Exact evaluation | AI-as-judge |
|---|---|---|
| Score depends on grader | No | Yes (model + prompt) |
| Reference data required | Yes (except functional correctness) | No |
| Flexibility across criteria | Limited | High |
| Reproducibility | High | Lower (probabilistic) |
| Cost | Low (often) | Higher (API calls) |

*"Despite the ease of use and flexibility of the AI as a judge approach, hand-designed similarity measurements are still widely used in the industry for their exact nature."*

## Scope in Ch 3

Ch 3's exact-evaluation section focuses on **open-ended responses** (arbitrary text generation), not close-ended (classification). The chapter explicitly punts close-ended evaluation as *"already well understood."*

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[Evaluation]] — parent concept.
- [[FunctionalCorrectness]] / [[SimilarityMeasurement]] — the two branches.
- [[ExactMatch]] / [[LexicalSimilarity]] / [[SemanticSimilarity]] — three sub-flavors of similarity.
- [[LLMAsAJudge]] — the subjective counterpart.
- [[ComparativeEvaluation]] — the orthogonal ranking-based approach.
- [[ReferenceData]] — what reference-based exact methods consume.
