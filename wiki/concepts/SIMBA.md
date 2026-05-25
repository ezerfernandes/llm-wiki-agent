---
title: "SIMBA"
type: concept
tags: [dspy, prompt-optimization, optimizer, stochastic-search, self-reflective]
sources: [2603.19247-prompt-optimization-jailbreaking, dspy-tool-use-tutorial]
last_updated: 2026-05-24
---

# SIMBA

**SIMBA** is a [[DSPy]] prompt optimizer in the *Automatic Instruction Optimization* family alongside `COPRO`, [[MIPROv2]], and [[GEPA]]. It searches the instruction space using **stochastic mini-batch sampling combined with self-reflective rules** (see the optimizer table in [[GEPA]]).

## Mechanism (as described in the wiki's anchor pages)

- **Mini-batches.** Instead of evaluating proposals on the full training set per round, SIMBA scores on a random mini-batch — cheap, noisy, and exploratory.
- **Self-reflection.** Between rounds, the optimizer reflects on the prompt + minibatch traces to generate the next candidate, rather than relying on a Bayesian surrogate ([[MIPROv2]]) or hill-climbing (`COPRO`).
- **Result for red-teaming**: the high-variance + reflection combination explores more of the prompt space per unit compute, which is empirically the best property for adversarial search ([[2603.19247-prompt-optimization-jailbreaking]]).

## First wiki-corpus empirical anchor: red-teaming

[[2603.19247-prompt-optimization-jailbreaking|Shamsi, Chekuru, Guzman & Garg (2026)]] use SIMBA at batch=16 with up to 4 optimization steps to drive system-prompt search against four LLMs. **SIMBA wins on all four**, beating [[GEPA]] and [[MIPROv2]] on mean [[DangerScore|danger score]]:

| Model | Baseline | MIPROv2 | GEPA | **SIMBA** |
|---|---|---|---|---|
| Claude-4.5-Sonnet | 0.046 | 0.103 | 0.236 | **0.347** |
| LLaMA-4-Maverick | 0.215 | 0.581 | 0.469 | **0.623** |
| Qwen-3-8B | 0.090 | 0.746 | 0.477 | **0.792** |
| Gemini-2.5-Pro | 0.645 | 0.704 | 0.734 | **0.774** |

The Shamsi et al. ordering **SIMBA > GEPA > MIPROv2** is for *adversarial* search. The [[2507.19457-gepa|GEPA paper]]'s benign-task ordering is GEPA > MIPROv2; SIMBA isn't a target in that paper. So the two orderings live in different objective spaces and don't directly conflict.

## Why it beats MIPROv2 / GEPA on the danger objective

Hypotheses consistent with the paper:

- **Higher exploration variance.** MIPROv2's Bayesian surrogate concentrates probability on past high-reward regions; GEPA's reflective mutation refines locally. SIMBA's stochastic mini-batches keep proposing prompts further from any one mode — useful when the danger surface has multiple disconnected high-reward basins (different harm categories).
- **Aggressive exploitation under tight budgets.** With only 4 steps × batch=16 = 64 proposals, MIPROv2's surrogate has too little data to converge; GEPA's reflection chain has limited length. SIMBA's mini-batch / reflect / re-sample loop converts every batch into proposal pressure.
- **Less averaging across the seed pool.** Mini-batch sampling means an adversarial prompt that strongly elicits one harm category can survive even if it doesn't help on others — opposite of the helpful-task averaging objective.

## First runnable tutorial receipt — [[dspy-tool-use-tutorial|SIMBA on ToolHop]]

The wiki's **first executable `dspy.SIMBA(...)` invocation receipt** is [[dspy-tool-use-tutorial|the official DSPy Advanced Tool Use tutorial]] at `https://dspy.ai/tutorials/tool_use/`. Optimizes a **[[HandRolledReAct|hand-rolled ReAct]] agent** (single `dspy.ChainOfThought` Signature in a `max_steps=5` for-loop) on the [[ToolHop]] benchmark with [[GPT4o|GPT-4o]] (`temperature=0.7`) student.

Headline trace:

| | |
|---|---|
| Program | `Agent(dspy.Module)` — `dspy.ChainOfThought('question, trajectory, functions -> next_selected_fn, args: dict[str, Any]', instructions=...)` driving a 5-step manual loop with a synthetic `finish(answer)` terminal tool |
| Optimizer | `dspy.SIMBA(metric=metric, max_steps=12, max_demos=10)` invoked as `simba.compile(agent, trainset=trainset, seed=6793115)` |
| LM | `openai/gpt-4o`, `temperature=0.7` (single LM for both student and SIMBA's internal reflection) |
| Metric | `pred == gold` after lowercasing + `rstrip(".0")` + `replace(",", "")` |
| Tool sandbox | [[func_timeout|`@func_set_timeout(10)`]] + try/except → `{"return_value": ..., "errors": ...}` |
| Train / Dev / Test | 100 / 300 / 595 ([[ToolHop]]) |
| Baseline | 35.0% dev accuracy |
| Optimized | **60.7% dev accuracy** |
| **Lift** | **+25.7 absolute / +71% relative** |

**First-of-kind features this tutorial adds to the wiki's SIMBA receipt corpus:**

1. **First disclosure of `dspy.SIMBA(...)` constructor kwargs**: `metric`, `max_steps`, `max_demos`. Prior [[2603.19247-prompt-optimization-jailbreaking|Shamsi et al.]] receipt described the algorithm but did not show the Python invocation.
2. **First disclosure of `simba.compile(student, trainset, seed=int)` invocation surface** — including the **explicit `seed` parameter** (`seed=6793115`), a reproducibility surface no prior DSPy optimizer receipt in the wiki had documented.
3. **First benign-task SIMBA receipt with before/after accuracy numbers** — prior receipt was adversarial ([[DangerScore|danger]] on jailbreaks; no benign accuracy).
4. **First SIMBA × [[GPT4o|GPT-4o]]** receipt. Prior models: Claude 4.5 Sonnet, LLaMA 4 Maverick, Qwen 3-8B, Gemini 2.5-Pro.
5. **First SIMBA-on-tool-use** receipt. Prior task: system-prompt jailbreak elicitation.
6. **First SIMBA + [[HandRolledReAct|hand-rolled ReAct]]** combination — confirms SIMBA composes with custom `dspy.Module` agents without API changes.

**Symmetric coverage**: the wiki now has SIMBA receipts on both *adversarial* objectives (max [[DangerScore|danger]]; Shamsi et al.) and *benign* objectives (max accuracy; this tutorial). The pattern that explains both: SIMBA's **high-exploration variance** helps when the reward surface has multiple disconnected high-reward basins, whether those basins are "different harm categories" or "different formatting conventions for short-answer outputs".

## Connections

- [[2603.19247-prompt-optimization-jailbreaking]] — primary wiki source for the adversarial-objective receipt.
- [[dspy-tool-use-tutorial]] — first executable receipt; benign-objective accuracy lift on [[ToolHop]] with [[GPT4o|GPT-4o]] + [[HandRolledReAct|hand-rolled ReAct]].
- [[DSPy]] — host framework.
- [[GEPA]] — sibling optimizer; comparison row in the same Automatic Instruction Optimization family table.
- [[MIPROv2]] — sibling Bayesian optimizer; SIMBA beats it on every Shamsi et al. cell.
- [[AdversarialPromptSearch]] — the search paradigm SIMBA tops in this paper.
- [[DangerScore]] — reward signal used.
- [[BootstrapFewShotWithRandomSearch]] — the older stochastic-search optimizer in the DSPy catalog; SIMBA generalizes its randomization with self-reflection.
