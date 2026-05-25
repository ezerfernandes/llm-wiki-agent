---
title: "HumanEval"
type: concept
tags: [benchmark, code-generation, python, evaluation]
sources: [ai-engineering-ch03-evaluation-methodology, ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# HumanEval

**HumanEval** ([[openai|OpenAI]], Chen et al. 2021) is a Python code-generation benchmark of hand-written programming problems, each paired with a function signature, docstring, body, and a battery of unit tests. Models are scored by [[PassAtK|`pass@k`]] over the unit tests — pure [[FunctionalCorrectness|functional correctness]].

## Format (Ch 3 example)

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer
    to each other than given threshold. """
```

Plus a corresponding `check(candidate)` function with multiple `assert` test cases — each `assert` is one test case in the [[PassAtK|`pass@k`]] computation.

## Why HumanEval matters in Ch 3

Ch 3 uses HumanEval to make **two methodological points**:

1. **HumanEval is the archetype of automatable functional-correctness eval**: Python interpreter + unit tests = no human grader needed.
2. **HumanEval is where the [[bleu|BLEU]] / functional-correctness decoupling was first shown**: *"on HumanEval, a code generation benchmark, OpenAI found that BLEU scores for incorrect and correct solutions were similar."* (Chen et al. 2021). Optimizing BLEU does not optimize functional correctness.

## Position

Sibling to [[MBPP]] ([[google|Google]]'s Mostly Basic Python Problems). Together they are the dominant *"can this model code?"* benchmarks for foundation models, both built on the [[ExecutionAccuracy|execution-accuracy]] paradigm.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[FunctionalCorrectness]] / [[ExecutionAccuracy]] / [[PassAtK]] — the eval paradigm.
- [[MBPP]] — sibling Python-codegen benchmark.
- [[Spider]] / [[BIRDSQL]] / [[WikiSQL]] — text-to-SQL siblings using the same paradigm.
- [[bleu|BLEU]] — the surface metric decoupled from HumanEval functional correctness (Chen et al. 2021).
- [[openai|OpenAI]] — author.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 adds three context points:

1. **Excluded from leaderboards on cost grounds.** *"Hugging Face opted out of HumanEval due to its large compute requirements — you need to generate a lot of completions."* HumanEval is conspicuously absent from the [[OpenLLMLeaderboard|Open LLM Leaderboard]] for this reason.
2. **Used in the example evaluation criteria table** (Ch 4 Table 4-3): a fictional application's hard requirement is *pass@1 > 90% on HumanEval*, ideal *> 95%*. Illustrates how to use a public benchmark inside a [[CustomLeaderboard|custom evaluation rubric]].
3. **Anchors the [[DomainSpecificCapability|domain-specific capability]] bucket.** Together with [[MBPP]], it's the canonical *"can this model code?"* test in the Ch 4 four-bucket taxonomy.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names HumanEval (Chen et al. 2021) in **Table 12-1** as one of six canonical public benchmarks for evaluating generative LLMs (alongside [[MMLU]], [[GLUE]], [[GSM8K]], [[HellaSwag]], [[TruthfulQA]]). Description: *"164 programming problems."* HumanEval anchors Ch 12's framing of generative-eval as task-heterogeneous — *"a generative model's ability to solve mathematical questions does not guarantee success in solving coding questions."*
