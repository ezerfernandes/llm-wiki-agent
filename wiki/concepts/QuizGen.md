---
title: "QuizGen"
type: concept
tags: [concept, benchmark, qa, json, dspy]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-22
---

# QuizGen

**QuizGen** is one of four [[hotpotqa|HotPotQA]]-derived tasks evaluated in [[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. (2024)]]. The task: given a HotPotQA question-answer pair and a target number of choices, generate a multiple-choice quiz question in JSON format with one correct answer and plausible distractor choices.

## Pipeline

```python
class QuizChoiceGenerationWithAssertions(dspy.Module):
    def forward(self, question, answer):
        choice_string = self.generate_choices(
            question=question,
            correct_answer=answer,
            number_of_choices=number_of_choices
        ).answer_choices

        dspy.Suggest(format_checker(choice_string),
            "The format of the answer choices should be in JSON format. Please revise accordingly.")

        dspy.Suggest(is_correct_answer_included(answer, choice_string),
            "The answer choices do not include the correct answer to the question. Please revise accordingly.")

        plausibility_assessment = dspy.Predict(...)(...)
        dspy.Suggest(is_plausibility_yes(plausibility_assessment.answer_choices),
            "The answer choices are not plausible distractors or are too easily identifiable as incorrect. Please revise to provide more challenging and plausible distractors.")

        return dspy.Prediction(choices=choice_string)
```

Three suggestions: JSON format / correct-answer inclusion / distractor plausibility.

## Metrics

- **Correct JSON** (intrinsic): valid JSON format.
- **Has Answer** (intrinsic): correct answer is among the choices.
- **Citation Precision** (intrinsic): legacy column — not the primary signal here.
- **Validity** (extrinsic, composite): average of intrinsic metrics, gated on both Correct-JSON and Has-Answer being satisfied (otherwise score = 0).

## Headline results (Dev / Test)

| Strategy | Correct JSON | Has Answer | Citation Precision | Validity |
|---|---|---|---|---|
| Vanilla | 41.7 / 37.6 | 40.3 / 34.8 | 63.7 / 60.4 | 36.9 / 30.5 |
| Infer w/ Assert | **100** / 98.8 | 86.3 / 76.6 | 73.0 / 67.0 | 80.2 / 70.5 |
| Compile | **100** / **100** | 96.3 / 92.8 | 68.3 / 63.8 | 86.1 / 81.7 |
| Compile w/ Assert | **100** / 99.8 | **95.0** / 91.6 | 70.0 / 62.4 | 85.1 / 80.5 |
| **C+Infer w/ Assert** | **100** / **100** | 96.3 / **94.6** | **82.7 / 75.4** | **91.0 / 87.2** |

QuizGen produces the paper's headline result: **JSON-format validity from 37.6% baseline → 100% with assertion-driven backtracking**, and composite validity from 30.5% → 87.2%. This is also the task that most clearly demonstrates assertion-driven backtracking's effectiveness on hard structural constraints — the LM consistently produces well-formed JSON once it's given a single retry with a clear error message.

## Primitive-instruction stress test (paper Appendix C)

With minimal instructions ("Generate answer choices for the specified question"), the `Vanilla` baseline drops to **1.3% / 2.8%** Correct JSON and **1.2 / 2.3** Validity — but `C+Infer w/ Assert` still reaches **100% / 100%** Correct JSON and **85.8 / 81.1** Validity. *"Model pipelines with LM Assertions and assertion-driven optimizations are less sensitive to instructions, requiring less effort on manual prompt tuning."*

## Related

- [[hotpotqa]] — source dataset.
- [[chainofthought]] — prompting module.
- [[DSPySuggest]] — used for format / inclusion / plausibility checks.
- [[MultiHopQA]] / [[LongFormQA]] / [[TweetGen]] — sibling tasks.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the task formulation.
