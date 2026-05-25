---
title: "Execution Accuracy"
type: concept
tags: [evaluation, code-generation, methodology]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Execution Accuracy

The code-specific flavor of [[FunctionalCorrectness|functional correctness]]: *"Functional correctness in coding is sometimes execution accuracy"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]). The generated code is fed into an interpreter (or compiler), executed against test cases, and the output is compared to the expected result.

## Worked example from Ch 3

Given the prompt *"write a Python function `gcd(num1, num2)` to find the greatest common denominator,"* execution accuracy:

1. Generates the candidate function.
2. Executes it on test pairs (e.g., `(15, 20)`).
3. Compares output to the expected result (`5`).
4. Marks the function correct iff all test cases pass.

## Used by

- [[HumanEval]] — OpenAI's Python benchmark.
- [[MBPP]] — Google's Mostly Basic Python Problems.
- [[Spider]] — Yu et al. 2018, text-to-SQL.
- [[BIRDSQL]] — Li et al. 2023, large-scale text-to-SQL.
- [[WikiSQL]] — Zhong et al. 2017, earlier text-to-SQL benchmark.

All of these report results via the [[PassAtK|`pass@k`]] family of metrics.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[FunctionalCorrectness]] — parent concept.
- [[PassAtK]] — the aggregation metric.
- [[HumanEval]] / [[MBPP]] / [[Spider]] / [[BIRDSQL]] / [[WikiSQL]] — benchmarks.
