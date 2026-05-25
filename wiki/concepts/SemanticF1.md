---
title: "SemanticF1"
type: concept
tags: [dspy, metric, llm-as-judge, rag, evaluation]
sources: [dspy-rag-tutorial, dspy-optimizers, 2406.11695-mipro]
last_updated: 2026-05-22
---

# SemanticF1

**`dspy.evaluate.SemanticF1`** is a [[DSPyMetrics|DSPy metric]] that scores a generated response against a gold-standard answer by **decomposing both into atomic claims and computing the F1 over claim coverage** — recall (which gold claims appear in the response) and precision (which response claims appear in the gold). Implemented as an [[llmasjudge|LLM-as-judge]] DSPy program, not as a surface-text metric.

## Why it's not [[F1Score|surface F1]]

Conventional [[F1Score|F1]] over tokens or n-grams penalizes paraphrase and rewards lexical overlap; on long-form QA — where the gold answer and a correct system answer often share **no** content words — surface F1 collapses to noise. SemanticF1 sidesteps this by:

1. Prompting an LLM to decompose the gold answer into atomic factual claims.
2. Prompting the LLM (again) to decompose the system response into atomic claims.
3. Prompting the LLM to grade overlap — which gold claims are covered by the response (**recall**) and which response claims are supported by the gold (**precision**).
4. Returning the harmonic mean.

The whole metric is **itself a DSPy program** (a small composition of [[DSPyPredict|`dspy.Predict`]] / [[chainofthought|`dspy.ChainOfThought`]] calls over a typed [[DSPySignatures|`class Assess(dspy.Signature)`]] rubric — the canonical [[dspy-metrics|AI-feedback metric pattern]] from page 11 of the *Learn* corpus) — so it is **recursively optimizable** ([[DSPyEvaluation|Step 4]] of the four-step evaluation loop).

## Canonical usage

```python
from dspy.evaluate import SemanticF1

metric = SemanticF1()
score = metric(example, prediction)   # float in [0, 1]

# As an optimizer's reward:
tp = dspy.MIPROv2(metric=SemanticF1(), auto="medium", num_threads=24)
optimized = tp.compile(program, trainset=trainset)

# As a parallel dev-set harness:
evaluator = dspy.Evaluate(devset=dev, metric=SemanticF1(), num_threads=24, display_progress=True)
evaluator(program)
```

## Worked receipts in the wiki

| Program / dataset | Baseline | RAG | +MIPROv2 | Source |
|---|---|---|---|---|
| RAG-QA Arena Tech (~1K) | 42% | 55.5% | **61.1%** | [[dspy-rag-tutorial]] |
| StackExchange subset | — | 53% | **61%** | [[dspy-optimizers]] Receipt 2 / [[MIPROv2]] |

Both runs use `auto="medium"`, `max_bootstrapped_demos=2`, `max_labeled_demos=2`, and converge on **~61% SemanticF1 as the post-optimization ceiling** for a single-hop CoT-based RAG on gpt-4o-mini — a remarkably consistent envelope across two unrelated benchmarks.

## Position relative to other evaluation metrics

| Metric | Lexical / Semantic | Reference-based? | Wiki anchor |
|---|---|---|---|
| Exact match / [[F1Score]] (token) | Lexical | Yes | [[F1Score]] |
| [[bleu|BLEU]] / [[ROUGE]] | Lexical n-gram | Yes | [[bleu]] / [[ROUGE]] |
| [[BERTScore]] | Semantic (embedding) | Yes | [[BERTScore]] |
| [[AlignScore]] | Semantic (NLI) | Yes (claim-grounding) | [[AlignScore]] |
| **SemanticF1** | **Semantic (LLM-judged claim coverage)** | **Yes** | **this page** |
| [[GREEN]] / [[VeriFact]] / [[MedVAL]] | Semantic (clinical-LLM-judged) | Mixed | [[2507.03152-medval]] |

SemanticF1 is the **reference-based [[llmasjudge|LLM-as-judge]] metric** of the DSPy ecosystem — sibling to the **reference-free** [[MedVAL]] family on the clinical side. The reference dependency is what lets it ship with a 1K-example public dataset like [[RAGQAArenaTech]]; reference-free metrics like [[MedVAL]] require physician-graded validation instead.

## Connections

- [[dspy-rag-tutorial]] — canonical worked source: 42% / 55.5% / 61.1% on [[RAGQAArenaTech]].
- [[MIPROv2]] — the optimizer that consumes SemanticF1 as its reward signal in the canonical RAG receipts.
- [[dspy-metrics]] — the [[DSPyMetrics|metric contract]] page that defines the AI-feedback pattern SemanticF1 instantiates.
- [[DSPyMetrics]] — the canonical concept; SemanticF1 is one of the two named built-in metric families (alongside the simpler `answer_exact_match` / `answer_passage_match`).
- [[llmasjudge|LLM-as-judge]] — the general pattern; SemanticF1 is DSPy's typed-Signature operationalization of it for reference-based long-form QA.
- [[F1Score]] — the lexical sibling; SemanticF1 is structurally the same harmonic-mean-of-precision-recall, applied at the **claim** level rather than the **token** level.
- [[DSPyEvaluate]] — the parallel dev-set harness SemanticF1 commonly lives inside.
- [[DSPyEvaluation]] — the four-step loop SemanticF1 instantiates Steps 2 + 4 of (define metric; optimize metric).
- [[rag|RAG]] — the application class SemanticF1 is most commonly used to evaluate.
- [[RAGQAArenaTech]] — the dataset SemanticF1 is benchmarked against in [[dspy-rag-tutorial]].
- [[BERTScore]] / [[AlignScore]] / [[ROUGE]] / [[bleu|BLEU]] — sibling reference-based metrics; SemanticF1 is the **LLM-judged claim-coverage** variant.
- [[MedVAL]] — the **reference-free** clinical sibling; both are LLM-judged metrics but MedVAL grades risk against the input note rather than a reference answer.
- [[2604.14585-prompt-optimization-coin-flip]] — supplies the caveat that LLM-judge metric gains are model-specific and may not transfer; the +6-point SemanticF1 lift in [[dspy-rag-tutorial]] is above the paper's 2-pt headroom threshold.
