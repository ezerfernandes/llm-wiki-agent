---
title: "ReAct"
type: concept
tags: [ml-method, prompting, agent, tool-use]
sources: [dspy-modules, dspy-programming-overview, dspy-tools]
last_updated: 2026-05-17
---

# ReAct

**ReAct** ([Yao et al. 2022](https://arxiv.org/abs/2210.03629) — *"ReAct: Synergizing Reasoning and Acting in Language Models"*) is the prompting pattern in which an LM interleaves **reasoning** steps (free-form thought) with **action** steps (tool calls or environment interactions), each action's observation feeding back into the next reasoning step. ReAct underpins most modern *agentic* LLM systems — it is the structural ancestor of every *"the LM thinks, calls a tool, observes the result, thinks again"* loop in the field.

Across the wiki, ReAct is referenced as a baseline tool-use foundation (alongside [[ChainOfThought|chain-of-thought]]) by [[2604.21590-agenticqwen|AgenticQwen]] and as the lineage behind contemporary agent harnesses ([[2604.25850-agentic-harness-engineering]]).

## DSPy implementation: `dspy.ReAct`

[[DSPy]] exposes ReAct as the built-in [[DSPyModules|Module]] `dspy.ReAct`: *"An agent that can use tools to implement the given signature"* ([[dspy-modules]]). The DSPy framing has three meaningfully distinct properties over the research-paper recipe:

1. **Generalized over any signature.** `dspy.ReAct('question -> answer: float', tools=[...])` is the same Module class that implements the *think-act-observe-think* loop for **any** user-declared [[DSPySignatures|Signature]]. The Signature is the **stable interface**; the tool list is the per-instance dial.

2. **Tools are plain Python callables.** The `tools=[...]` kwarg takes ordinary Python functions; their docstrings and type hints become the tool descriptions the LM sees. The page's canonical example:

   ```python
   def evaluate_math(expression: str) -> float:
       return dspy.PythonInterpreter({}).execute(expression)

   def search_wikipedia(query: str) -> str:
       results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3)
       return [x['text'] for x in results]

   react = dspy.ReAct("question -> answer: float",
                      tools=[evaluate_math, search_wikipedia])
   pred = react(question="What is 9362158 divided by the year of birth of "
                         "David Gregory of Kinnairdy castle?")
   print(pred.answer)   # 5761.328
   ```

3. **Tool-call slots are an automatic signature expansion.** Like [[ChainOfThought|`dspy.ChainOfThought`]] injects `reasoning`, `dspy.ReAct` injects the tool-call orchestration slots — the user does not declare them on the Signature. The user-facing Signature stays as the abstract task definition; the framework expands it under the hood with the *think-act-observe* scaffolding.

### Position in the DSPy module taxonomy

| Module | Strategy |
|---|---|
| [[DSPyPredict\|`dspy.Predict`]] | One LM call. |
| [[ChainOfThought\|`dspy.ChainOfThought`]] | Reasoning prose + answer. |
| [[DSPyProgramOfThought\|`dspy.ProgramOfThought`]] | Generate-and-execute code. |
| **`dspy.ReAct`** | **Think-act-observe loop over `tools=[...]`.** |
| [[DSPyRecursiveLanguageModel\|`dspy.RLM`]] | Recursive sub-LLM calls in a sandboxed REPL. |

The `dspy.ReAct` Module is one of the two equal-status entry points for the [[DSPyTools|Tools]] sub-system on [[dspy-tools|the DSPy Tools page]] (page 7 of 13 of the *Learn* documentation).

### Managed vs manual tool handling

[[dspy-tools|The Tools page]] (ingested 2026-05-17) sharpens the wiki's prior framing — in which `dspy.ReAct` was the canonical DSPy tool-use entry point — into a **paired** rubric. `dspy.ReAct` is the **fully-managed** path; **manual handling** via [[DSPyPredict|`dspy.Predict`]] with a Signature whose input includes `tools: list[dspy.Tool]` and whose output is `dspy.ToolCalls` is the equal-status alternative. The decision rubric the Tools page commits to:

| Choose `dspy.ReAct` when | Choose manual handling when |
|---|---|
| Automatic reasoning and tool selection are desired | Precise execution control is necessary |
| Tasks require multiple sequential tool calls | Custom error-handling logic is required |
| Built-in error recovery is beneficial | Latency minimization matters |
| Focus on tool implementation over orchestration is preferred | **Tools return no values (void functions)** |

The **void-return-tool** case is the most informative — `dspy.ReAct`'s think-act-observe loop feeds each observation back into the next reasoning step, so side-effect-only tools (logging, telemetry emission, fire-and-forget actions) don't fit the managed path and motivate the manual one. The page's prior framing — `dspy.ReAct` as the default-and-only tool entry point — is **incomplete**; manual handling is co-equal, not a fallback.

### `Prediction.trajectory`

`dspy.ReAct`'s return [[DSPyPrediction|`Prediction`]] carries an extra `trajectory` field — *"complete reasoning trajectory tracking"* — recording every reasoning step and every tool call made during the loop. This is the **introspection hook** that distinguishes managed handling from manual: the manual path has access to `response.outputs.tool_calls` directly (it owns the loop), but `dspy.ReAct`'s loop is internal — `trajectory` is how the user reconstructs what happened.

## Connections

- [[ChainOfThought|Chain-of-Thought]] — the closest sibling prompting pattern; ReAct extends CoT with action steps.
- [[2604.21590-agenticqwen|AgenticQwen]] — names CoT and ReAct as baseline tool-use foundations.
- [[2604.25850-agentic-harness-engineering|Agentic Harness Engineering]] — the contemporary critique of *"DSPy-style instruction tuning"*; ReAct is one of the prompting layers AHE counter-positions against.
- [[DSPy]] — framework whose `dspy.ReAct` Module is ReAct's typed, signature-parameterized form.
- [[DSPyModules]] — the parent abstraction.
- [[DSPyPredict]] — the minimal primitive `dspy.ReAct` is built on top of.
- [[DSPySignatures]] — the Signature `dspy.ReAct` honors at its outer interface.
- [[DSPyTools]] — the Tools sub-system `dspy.ReAct`'s `tools=[...]` kwarg routes through; `dspy.Tool` wraps each callable; the manual-handling counterpart uses `dspy.ToolCalls` as a Signature output type.
- [[dspy-tools]] — canonical source for the *managed vs manual* duality, the `dspy.Tool` / `dspy.ToolCalls` API surface, the per-Adapter native-function-calling kwarg, and the async-tool support (page 7 of 13).
- [[DSPyProgrammingModel]] — the *swap-modules-without-touching-signature* portability claim that lets `dspy.Predict` ↔ `dspy.ChainOfThought` ↔ `dspy.ReAct` be a constructor-name change.
- [[DSPyPrediction]] — the return object after the think-act-observe loop terminates.
- [[ColBERTv2]] — the retriever used in the page's ReAct example. Forward reference; named only.
