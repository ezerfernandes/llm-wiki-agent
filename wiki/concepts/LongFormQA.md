---
title: "LongFormQA"
type: concept
tags: [concept, benchmark, qa, citation, dspy]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-22
---

# LongFormQA

**LongFormQA** is one of four [[hotpotqa|HotPotQA]]-derived tasks evaluated in [[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. (2024)]]. Extends [[MultiHopQA]] with a long-form, citation-bearing answer requirement: the generated paragraph must include inline citations `[x]` to retrieved sources, and the text preceding each citation must be **faithful** to the cited passage.

## Pipeline

```python
class LongFormQAWithAssertions(dspy.Module):
    def forward(self, question):
        context = []
        for hop in range(2):
            query = self.generate_query(context=context, question=question).query
            context += self.retrieve(query).passages

        pred = self.generate_cited_paragraph(context=context, question=question)

        dspy.Suggest(citations_check(pred.paragraph),
                     "Every 1-2 sentences should have citations: 'text... [x].'")

        for line, citation in get_lines_and_citations(pred, context):
            dspy.Suggest(is_faithful(line, citation),
                         f"Your output should be based on the context: '{citation}'.")

        return pred
```

Two suggestions: (1) citation density (a [[DSPySuggest|`Suggest`]] checked by a Python regex); (2) per-line citation faithfulness (a [[DSPySuggest|`Suggest`]] whose check is itself a small DSPy program that asks the LM whether the line is supported by the citation).

The second suggestion is illustrative of [[LMAssertions]]' design: `constraint` is not restricted to a Python boolean — it can invoke another DSPy module, including one that calls the LM. *"The robust API design of Suggest allows the user to specify arbitrary expressions as conditional checks, such as an LM call."*

## Metrics

- **Citation Faithfulness** (intrinsic): per-line LM-judged check averaged across citations.
- **Citation Recall** (extrinsic): coverage of gold titles.
- **Citation Precision** (extrinsic): proportion of cited titles that match gold.
- **Has Answer** (extrinsic): does the paragraph include the gold answer?

## Headline results (Dev / Test)

| Strategy | Citation Faithfulness | Citation Recall | Citation Precision | Has Answer |
|---|---|---|---|---|
| Vanilla | 77.3 / 78.8 | 51.5 / 52.1 | 58.1 / 59.2 | 65.7 / 60.2 |
| Infer w/ Assert | 90.0 / 90.8 | **56.3 / 57.8** | 63.9 / 64.6 | 65.7 / **60.4** |
| Compile | 82.3 / 79.6 | 41.0 / 39.8 | 76.8 / 73.5 | 68.3 / 56.4 |
| Compile w/ Assert | 84.0 / 81.2 | 55.8 / 53.5 | 66.4 / 63.5 | 68.0 / 57.4 |
| **C+Infer w/ Assert** | **92.7 / 91.8** | 43.8 / 43.0 | **80.1 / 76.3** | **69.7** / 55.4 |

The Citation-Recall column shows the **conflicting-suggestions** failure mode in mild form — `C+Infer w/ Assert` is worse at recall than `Infer w/ Assert` alone, because compile-time bootstrapping skews toward Precision-passing examples at the cost of coverage.

## Related

- [[MultiHopQA]] — the underlying task this extends with citations.
- [[hotpotqa]] — source dataset.
- [[chainofthought]] — prompting module.
- [[DSPySuggest]] — used for both citation density and faithfulness.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the task formulation.
