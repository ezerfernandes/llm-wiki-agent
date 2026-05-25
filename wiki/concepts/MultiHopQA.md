---
title: "MultiHopQA"
type: concept
tags: [concept, benchmark, qa, multi-hop, dspy]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-22
---

# MultiHopQA

**MultiHopQA** is the [[hotpotqa|HotPotQA]]-derived multi-hop question-answering task used in the DSPy literature ([[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. 2024]]). The LM pipeline performs a series of inferential steps (multi-hop) before answering a question, utilizing a retriever to gather relevant context.

Pipeline (canonical 2-hop variant):

```
question
  ─► generate_query (hop 0) ─► retrieve ─► passages
                                            │
  ─► generate_query (hop 1, sees passages) ─► retrieve ─► passages
                                                            │
                                                          generate_answer
```

Each `generate_query` is a [[chainofthought|ChainOfThought]] module; retrieval uses [[ColBERTv2]] over the 2017 Wikipedia abstracts dump.

## Use in [[2312.13382-dspy-assertions|DSPy Assertions]]

Two suggestions illustrate the construct:

1. `dspy.Suggest(len(query) < 100, "Query should be less than 100 characters")` — efficiency hint.
2. `dspy.Suggest(is_query_distinct(query, queries), f"Query should be distinct from {queries}")` — diversity hint, prevents the multi-hop pipeline from emitting redundant queries.

**Headline result**: introducing just these two soft constraints improves retrieval recall by **6.5–7.9%** and answer-correctness by **3.4–14.4%** on the [[hotpotqa|HotPotQA]] dataset.

### Full result table (Dev / Test)

| Strategy | Suggestions Passed | Retrieval Recall | Answer Correctness |
|---|---|---|---|
| Vanilla | 66.3 / 66.2 | 35.0 / 36.6 | 45.7 / 41.6 |
| Infer w/ Assert | 89.7 / 88.0 | 39.3 / 39.0 | 47.3 / 43.0 |
| Compile | 71.3 / 63.4 | 37.0 / 40.2 | 43.7 / 40.4 |
| Compile w/ Assert | 78.3 / 71.6 | 44.3 / 42.2 | 52.7 / **46.2** |
| **C+Infer w/ Assert** | **95.7 / 91.6** | **46.0 / 43.4** | **53.3** / 45.4 |

## Distinction from [[hotpotqa|HotPotQA]] itself

[[hotpotqa|HotPotQA]] is the underlying *dataset* (Yang et al. 2018). MultiHopQA in the DSPy Assertions paper is the *task formulation* — a particular DSPy pipeline architecture (2-hop CoT + retrieval) operating on HotPotQA. The terminology distinction matters: [[2407.10930-better-together|BetterTogether]]'s 3-module HotPotQA pipeline and [[2406.11695-mipro|MIPRO]]'s 2-module pipeline are different MultiHopQA-style task formulations over the same underlying dataset.

## Related

- [[hotpotqa]] — the underlying dataset.
- [[LongFormQA]] — extends MultiHopQA with citation requirements.
- [[QuizGen]] — derives quiz questions from HotPotQA.
- [[TweetGen]] — generates tweets answering HotPotQA questions.
- [[chainofthought]] — prompting module used.
- [[ColBERTv2]] — retrieval backend.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the task formulation.
