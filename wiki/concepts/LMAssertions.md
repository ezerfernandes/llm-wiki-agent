---
title: "LM Assertions"
type: concept
tags: [concept, dspy, assertions, self-refinement, constraints]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-22
---

# LM Assertions

**LM Assertions** are first-class programming constructs introduced in [[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. (2024)]] that let a [[DSPy]] developer express **arbitrary computational constraints** on the outputs of LM modules, with the framework enforcing them via retry-with-feedback at inference time and via assertion-aware demonstration bootstrapping at compile time.

Two variants:

| Construct | Severity | On persistent failure after $R$ retries |
|---|---|---|
| **[[DSPyAssert\|`dspy.Assert`]]** | Hard — non-negotiable | Raises `AssertionError`; halts pipeline |
| **[[DSPySuggest\|`dspy.Suggest`]]** | Soft — heuristic guidance | Logs `SuggestionError`; continues to next module |

## API

```python
dspy.Assert(constraint: bool, msg: Optional[str], backtrack: Optional[module])
dspy.Suggest(constraint: bool, msg: Optional[str], backtrack: Optional[module])
```

- `constraint` — boolean check (can itself invoke DSPy modules, so the check can be an LM call).
- `msg` — natural-language feedback string injected into the retry prompt.
- `backtrack` — module to retry (defaults to the most recently called module).

## Semantics

Big-step operational semantics over retry-counted states $\sigma_r$:

$$\sigma_r \vdash \text{Assert}(e,m) \to \sigma'_0 \quad \text{if } \text{eval}(\sigma,e) = \text{true}$$
$$\sigma_r \vdash \text{Assert}(e,m) \to \sigma_{r+1} \quad \text{if false and } r < R$$
$$\sigma_r \vdash \text{Assert}(e,m) \to \sigma^\perp \quad \text{if false and } r \geq R$$

`Suggest` is identical except the $r \geq R$ branch transitions to $\sigma''_0$ (warn, continue, reset retry count) rather than $\sigma^\perp$.

## What the LM sees on retry

When a constraint fails, the framework's `Retry` meta-module rewrites the failing module's prompt to include:

- `Context: ...` (original)
- `Question: ...` (original)
- `Past Query: <previous attempt w/ errors>` (the failing output)
- `Instruction: <assertion error message>` (the `msg` argument)

The LM is now *self-aware of its prior failure* and the rule it broke — this is the core mechanism of [[AssertionDrivenBacktracking|assertion-driven backtracking]].

## Compile-time uses

LM Assertions are not only a runtime construct. Wrapped around the **teacher** model inside [[BootstrapFewShotWithRandomSearch|`BootstrapFewShotWithRandomSearch`]], they enable two compile-time optimizations:

- **[[AssertionDrivenExampleBootstrapping|Assertion-driven example bootstrapping]]** — bootstrapped few-shot demonstrations are guaranteed to satisfy every assertion at every intermediate module, not only the final-answer metric.
- **[[CounterexampleBootstrapping|Counterexample bootstrapping]]** — failed-then-fixed traces become demonstrations, teaching the student model to avoid the same mistakes.

## Why not just call `assert`?

Python's built-in `assert` halts on failure. An LM can be *re-prompted* with the failure as feedback — so an assertion in an LM program should trigger a retry-with-feedback loop, not termination. The paper makes this the central design distinction:

> "[Our `Assert` construct] offers a sophisticated retry mechanism while supporting several new optimizations. On an `Assert` failing, the pipeline transitions to a special retry state, allowing it to reattempt a failing LM call while being aware of its previous attempts and the error message raised."

## Position vs related ideas

- **vs [[SelfVerification]].** LM Assertions deliberately do **not** ask the LM to verify itself — the constraint is a Python boolean (possibly invoking a DSPy program). This sidesteps the [[2402.01817-llm-modulo|LLM-Modulo (Kambhampati et al.)]] critique that LMs cannot self-verify; the check is external code.
- **vs model assertions (Kang et al. 2020).** Model assertions monitor ML model behavior in *training* — used for data collection and weak supervision. LM Assertions retry the *failing module* with its own past output, and are used for few-shot bootstrapping and self-refinement.
- **vs guardrails ([NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails), [LMQL](https://lmql.ai/)).** Guardrail systems sit around a single LM call. LM Assertions operate at the *pipeline* level (multi-module DSPy programs) and are integrated with the prompt optimizer, not as a post-hoc filter.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the introducing paper.
