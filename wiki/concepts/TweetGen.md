---
title: "TweetGen"
type: concept
tags: [concept, benchmark, tweet-generation, dspy]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-22
---

# TweetGen

**TweetGen** is one of four [[hotpotqa|HotPotQA]]-derived tasks evaluated in [[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. (2024)]]. The task: given a HotPotQA question + answer, retrieve supporting context and generate a **tweet** (≤280 chars, no hashtags, engaging, faithful to context) that effectively answers the question.

## Pipeline (paper Figure 5)

```python
class TweetGenerationWithAssertions(dspy.Module):
    def forward(self, question, answer):
        context = []
        generate_query = [dspy.ChainOfThought("context, question -> query") for _ in range(2)]
        retrieve = dspy.Retrieve(k=3)
        for hop in range(2):
            query = generate_query[hop](context=context, question=question).query
            passages = retrieve(query).passages
            context = deduplicate(context + passages)

        generated_tweet = self.generate_tweet(question=question, context=context).tweet

        dspy.Suggest(has_no_hashtags(generated_tweet),
                     "Please revise the tweet to remove hashtag phrases following it.")
        dspy.Suggest(is_within_length_limit(generated_tweet, 280),
                     "Please ensure the tweet is within 280 characters.")
        dspy.Suggest(has_correct_answer(generated_tweet, answer),
                     "The tweet does not include the correct answer to the question. Please revise accordingly.")
        # engaging — LM-judged via a sub-DSPy program
        engaging_assessment = dspy.Predict("context, assessed_text, assessment_question -> assessment_answer")(
            context=context, assessed_text=generated_tweet,
            assessment_question="Does the assessed text make for a self-contained, engaging tweet?")
        dspy.Suggest(is_assessment_yes(engaging_assessment.assessment_answer),
                     "The text is not engaging enough. Please revise to make it more captivating.")
        # faithful — LM-judged
        faithful_assessment = dspy.Predict("context, assessed_text, assessment_question -> assessment_answer")(
            context=context, assessed_text=generated_tweet,
            assessment_question="Is the assessed text grounded in the context?")
        dspy.Suggest(is_assessment_yes(faithful_assessment.assessment_answer),
                     "The text contains unfaithful elements or significant facts not in the context.")

        return dspy.Prediction(generated_tweet=generated_tweet, context=context)
```

Five [[DSPySuggest|`Suggest`]] statements — three deterministic Python checks (hashtags, length, answer inclusion) and two LM-judged checks (engagement, faithfulness).

## Metrics

- **No "#"** (intrinsic, deterministic) — no hashtags.
- **Has Answer** (intrinsic) — correct answer mentioned.
- **Concise** (intrinsic) — within 280 chars.
- **Engaging** (intrinsic, LM-judged) — engagement assessment.
- **Faithful** (intrinsic, LM-judged) — grounding in retrieved context.
- **Quality** (extrinsic, composite) — average of intrinsic, gated on Concise + Has-Answer.

## Headline results (Dev / Test)

| Strategy | No "#" | Has Answer | Concise | Engaging | Faithful | Quality |
|---|---|---|---|---|---|---|
| Vanilla | 21.3 / 19.8 | 52.3 / 46.0 | 99.7 / 99.6 | 29.3 / 32.2 | **78.3 / 79.0** | 34.7 / 30.5 |
| Infer w/ Assert | 71.7 / 67.6 | 48.7 / 41.0 | 98.3 / 96.6 | 37.0 / 36.4 | 67.7 / 70.4 | 38.3 / 30.6 |
| Compile | **100 / 100** | 51.0 / 44.2 | **100 / 100** | 1.0 / 2.0 | 63.0 / 65.6 | 37.8 / 32.8 |
| Compile w/ Assert | 96.3 / 95.0 | 55.0 / 48.8 | 97.9 / 98.6 | 74.0 / 73.0 | 75.0 / 74.8 | 48.5 / 42.9 |
| **C+Infer w/ Assert** | 98.0 / 96.2 | **56.0 / 49.2** | 96.7 / 97.2 | **90.7 / 85.0** | 68.3 / 68.0 | **51.4 / 45.0** |

## Conflicting-suggestions case study

TweetGen is the paper's exhibit for the **[[DSPySuggest|conflicting-suggestions]]** failure mode:

- `Compile` (no assertions) — *engaging* collapses to **1.0%/2.0%** even though hashtags and conciseness are perfect. The compile bootstrap produces formulaic on-spec but boring tweets.
- `Infer w/ Assert` — no significant Quality gain over Vanilla. Sequentially defined suggestions on the same output (no-hashtag, length, answer, engaging, faithful) compete during self-refinement.

The paper's Appendix D shows two examples where `Compile w/ Assert` passes the No-"#" constraint at the cost of engaging, while `C+Infer w/ Assert` passes engaging at the cost of No-"#" — illustrating that LM Assertion *design* (deciding which to enforce and in what order) is itself a learnable skill.

## Related

- [[hotpotqa]] — source dataset.
- [[chainofthought]] — prompting module.
- [[DSPySuggest]] — used for all five constraints.
- [[MultiHopQA]] / [[LongFormQA]] / [[QuizGen]] — sibling tasks.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the task formulation.
