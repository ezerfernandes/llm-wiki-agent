---
title: "Verbosity Bias"
type: concept
tags: [evaluation, bias, llm-as-judge]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Verbosity Bias

**Verbosity bias** is the tendency of AI judges to *"favor lengthier answers, regardless of their quality"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]).

## Empirical evidence

Ch 3 cites two studies:

1. **Wu & Aji (2023)** found that *"both GPT-4 and Claude-1 prefer longer responses (~100 words) with factual errors over shorter, correct responses (~50 words)."* The bias is **strong enough to override factual correctness** at typical length ratios.

2. **Saito et al. (2023)** studied verbosity bias for creative tasks: *"when the length difference is large enough (e.g., one response is twice as long as the other), the judge almost always prefers the longer one."*

## The "stronger models are less biased" finding

Per Ch 3, both Zheng et al. (2023) and Saito et al. (2023) found that *"GPT-4 is less prone to this bias than GPT-3.5, suggesting that this bias might go away as models become stronger."*

This is one of the chapter's more optimistic data points about AI-as-judge: the biases are real but appear to attenuate with model capability.

## The human counterpart

Saito et al. found *"humans tend to favor longer responses too, but to a much lesser extent."* So verbosity bias is **present in both AI and human judges, with AI exhibiting it more strongly** — making it a place where AI judges and humans agree directionally but disagree on magnitude.

## Implications

- **Don't use verbosity-prone judges to grade conciseness**: an AI judge will likely score the longer response higher even if conciseness is explicitly in the rubric.
- **Strip length asymmetry where possible**: pair candidates of similar length, or normalize for length before scoring.
- **Be careful with reward models**: a verbosity-biased reward model in [[rlhf|RLHF]] will push the policy toward longer outputs — a well-documented failure mode of RLHF deployments.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[LLMAsAJudge]] — the parent paradigm.
- [[SelfBiasJudge]] / [[FirstPositionBias]] — sibling AI-judge biases.
- [[RecencyBias]] — the human counterpart bias for position.
- [[rlhf|RLHF]] — the alignment method whose reward model can inherit verbosity bias.
- [[EvaluationCriteriaAmbiguity]] — sibling AI-judge failure mode.
