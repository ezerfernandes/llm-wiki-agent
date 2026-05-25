---
title: "Assertion-Driven Backtracking"
type: concept
tags: [concept, dspy, assertions, self-refinement, backtracking]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-22
---

# Assertion-Driven Backtracking

**Assertion-driven backtracking** is the inference-time control-flow mechanism that powers [[LMAssertions|LM Assertions]] ([[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. 2024]]). When a [[DSPyAssert|`dspy.Assert`]] or [[DSPySuggest|`dspy.Suggest`]] constraint fails, the DSPy pipeline dynamically alters its control flow: instead of advancing to the next module, it re-invokes the **failing module** with its prior output and the user-supplied error message injected into the prompt, giving the LM a chance to self-correct against the constraint.

## Mechanism

Implemented via a lightweight auxiliary meta-module **`Retry`** that wraps any DSPy module and stores the history of failed predictions. On a constraint failure:

1. The pipeline transitions to a special **retry state** $\sigma_{r+1}$, incrementing retry count $r$.
2. The `Retry` wrapper rewrites the failing module's prompt to include the failed prediction and the constraint's error message $m$ as additional fields:
   - `Past Query: <previous attempt w/ errors>`
   - `Instruction: <assertion error message>`
3. The failing module re-runs with this enriched context — the LM is *self-aware of its prior failure* and the rule it broke.
4. If the retry passes the constraint, the pipeline resumes normal flow. Otherwise, repeat up to $R$ times.
5. After $R$ retries: [[DSPyAssert|`Assert`]] raises `AssertionError` and halts; [[DSPySuggest|`Suggest`]] logs `SuggestionError` and continues.

## Worked example (from paper Figure 1, MultiHopQA)

```python
class MultiHopQAWithAssertions(dspy.Module):
    def forward(self, question):
        context, queries = [], [question]
        for hop in range(2):
            query = self.generate_query(context=context, question=question).query

            dspy.Suggest(len(query) < 100,
                "Query should be less than 100 characters")

            dspy.Suggest(is_query_distinct(query, queries),
                f"Query should be distinct from {queries}")

            context += self.retrieve(query).passages
            queries.append(query)

        return self.generate_answer(context=context, question=question)
```

If the second-hop `generate_query` produces a query that violates `is_query_distinct`, the pipeline backtracks to `generate_query` and re-runs it with the failed query + the "Query should be distinct from..." instruction. The retrieved-context-and-answer flow continues with the corrected query.

## Why "backtracking" rather than "self-refinement"?

The paper uses both terms but emphasizes the *control-flow* aspect. Unlike chain-of-thought self-refinement (Madaan et al. 2023) which is a single in-prompt monologue, assertion-driven backtracking actually re-invokes the failing module as a *separate LM call* with a rewritten prompt — the pipeline graph is dynamically rewired. This is closer to a programming-language exception-handler with retry semantics than to a self-reflection prompt.

## Headline gains attributable to backtracking alone

From `Vanilla` → `Infer w/ Assert` (inference-time backtracking, no compile-time changes):

- **MultiHopQA Suggestions Passed**: 66.3 → 89.7 dev (+23.4).
- **LongFormQA Citation Recall**: 51.5 → 56.3 (+4.8).
- **QuizGen Correct JSON**: 41.7 → 100 (+58.3) — backtracking alone reaches a hard format constraint.
- **TweetGen No "#"**: 21.3 → 71.7 (+50.4).

The QuizGen Correct-JSON gain is particularly striking: a format constraint that prompt engineering alone struggled to enforce becomes trivially enforceable once the LM gets a single retry with the failure message.

## Related

- [[LMAssertions]] — the construct family.
- [[DSPyAssert]] / [[DSPySuggest]] — the two assertion variants.
- [[AssertionDrivenExampleBootstrapping]] — the compile-time use of this same mechanism on the teacher model.
- [[CounterexampleBootstrapping]] — captures backtracking traces as demonstrations.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the introducing paper.
