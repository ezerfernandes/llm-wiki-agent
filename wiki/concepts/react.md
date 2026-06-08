---
title: "ReAct"
type: concept
tags: [ml-method, prompting, agent, tool-use]
sources: [dspy-modules, dspy-programming-overview, dspy-tools, dspy-customer-service-agent, dspy-tutorial-rag-as-agent, dspy-yahoo-finance-react-tutorial, dspy-mem0-react-tutorial, ai-engineering-ch06-rag-agents, hands-on-llm-ch07-advanced-text-generation, dspy-tool-use-tutorial, agentic-design-patterns-ch06-planning, agentic-design-patterns-ch17-reasoning, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
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

The [[dspy-customer-service-agent|Customer Service Agent tutorial]] confirms that the [[DSPyPrediction|`Prediction`]] returned by `dspy.ReAct` actually carries **three** fields when invoked: `trajectory` (the full think-act-observe log), `reasoning` (the final-decision explanation, the same field [[ChainOfThought|`dspy.ChainOfThought`]] adds), and whatever output field the user declared on the Signature (`process_result` in the tutorial). Both `trajectory` and `reasoning` are added by `dspy.ReAct`'s under-the-hood signature expansion — the user never declares them.

## Reference receipt: the seven-tool customer-service agent

The [[dspy-customer-service-agent|Customer Service Agent tutorial]] is the wiki's canonical **end-to-end production-shaped receipt** for `dspy.ReAct` — a multi-tool agent over a typed [[Pydantic]] domain. Where the [[dspy-modules|Modules page]]'s two-tool calculator-plus-Wikipedia example demonstrates the *mechanism*, this tutorial demonstrates the *application shape* — seven tools (lookup / mutation / escalation), a five-class Pydantic domain (`Date`, `UserProfile`, `Flight`, `Itinerary`, `Ticket`), and a two-field user-facing Signature whose docstring scopes the agent's role:

```python
class DSPyAirlineCustomerService(dspy.Signature):
    """You are an airline customer service agent that helps user
    book and manage flights. You are given a list of tools to handle
    user request, and you should decide the right tool to use."""
    user_request: str = dspy.InputField()
    process_result: str = dspy.OutputField(desc="...")

agent = dspy.ReAct(DSPyAirlineCustomerService, tools=[
    fetch_flight_info, fetch_itinerary, pick_flight,
    book_flight, cancel_itinerary, get_user_info, file_ticket,
])

result = agent(user_request="please help me book a flight from SFO to JFK ...")
# result has .trajectory, .reasoning, .process_result
```

Three structural properties this receipt makes explicit, beyond what the Modules-page calculator example showed:

- **The Signature is independent of the tool list.** Two fields scope the user-facing interface; seven tools scope the action surface. The same Signature could host a different tool list (different agent over the same task framing); the same tools could host a different Signature (different task framing over the same actions).
- **[[Pydantic]] models compose at any depth in tool arguments and returns.** The `Itinerary` type contains a `UserProfile` and a `Flight`; the `Flight` contains a `Date`. The LM generates structured arguments matching the schema, and observations are returned as the same structured objects.
- **Escalation is a tool.** The `file_ticket` tool is the agent's safety valve when no other tool can resolve the request — the [[react|ReAct]]-pattern realization of the [[LLMModuloFramework|LLM-Modulo]] external-critic principle. Every production customer-service ReAct agent needs at least one such escalation surface.

See [[CustomerServiceAgent]] for the general application pattern this receipt instantiates.

## Hand-rolled alternative — when to escape `dspy.ReAct`

The [[dspy-tool-use-tutorial|DSPy tool-use tutorial]] is the wiki's **first receipt of a [[HandRolledReAct|hand-rolled ReAct]]** in a DSPy program — a manual `for` loop over a single `dspy.ChainOfThought` Signature, with the agent's `forward()` method managing trajectory state and tool selection directly. The pattern bypasses `dspy.ReAct` and instead emits `(next_selected_fn, args: dict[str, Any])` per step from one ChainOfThought, calls the chosen tool via the agent's own dispatch logic, appends to `trajectory`, and breaks when the model selects a synthetic `finish(answer)` terminal tool.

Four conditions under which the hand-rolled pattern is preferable to `dspy.ReAct`:

1. **Tool sets vary per example.** [[ToolHop]] ships a different `functions` dict per datapoint; tools are a runtime input, not a constructor kwarg. `dspy.ReAct(signature, tools=[...])` binds tools at construction.
2. **Termination needs custom logic.** A synthetic `finish(answer: str)` tool gives the model explicit control over when to stop, distinct from `dspy.ReAct`'s built-in termination.
3. **Tool metadata schema needs author control.** The hand-rolled pattern exposes tools to the LM as a `dict[str, Any]` Signature field; the author decides what metadata to include. `dspy.ReAct` uses `dspy.Tool`'s internal format.
4. **Untrusted tool code requires sandbox-aware invocation.** [[func_timeout|`func_timeout`]] wrapping, exception-to-`{return_value, errors}` dict mapping, side-effect tracking are easier at the loop level.

The hand-rolled pattern composes with any DSPy optimizer because the agent is still a regular `dspy.Module`. The tool-use tutorial achieves **35.0% → 60.7%** dev accuracy lift on [[ToolHop]] by composing hand-rolled ReAct with [[SIMBA|`dspy.SIMBA(max_steps=12, max_demos=10)`]] — confirming that the manual pattern is **not** a downgrade from framework convenience but a flexibility trade.

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
- [[dspy-customer-service-agent]] — canonical end-to-end production-shaped `dspy.ReAct` receipt: seven-tool airline customer-service agent over a five-class Pydantic domain. Confirms the three-field [[DSPyPrediction|`Prediction`]] return shape (`trajectory` + `reasoning` + user-declared output) and demonstrates the Signature-vs-tool-list decoupling at scale.
- [[HandRolledReAct]] — manual `dspy.ChainOfThought` + trajectory-loop alternative; canonical receipt: [[dspy-tool-use-tutorial]] on [[ToolHop]] with [[SIMBA]] (35.0% → 60.7%).
- [[dspy-tool-use-tutorial]] — first wiki hand-rolled ReAct + [[SIMBA]] receipt; bypasses `dspy.ReAct` for runtime-varying per-example tool sets and synthetic `finish(answer)` terminal-tool control.
- [[dspy-tutorial-rag-as-agent]] — canonical end-to-end **optimized** `dspy.ReAct` receipt: two-tool Wikipedia multi-hop retrieval agent over [[HoVer]] (three-hop subset). **First wiki receipt with `max_iters=20`** (long loops for three-hop reasoning) and **first wiki receipt that pairs `dspy.ReAct` with [[MIPROv2]] under teacher/student model decoupling** ([[OpenAI|GPT-4o]] teacher + [[Llama|Llama-3.2-3B]] student). Headline result: **8% → 41.67% top5_recall (5×)** from prompt optimization alone, no weight tuning.
- [[dspy-yahoo-finance-react-tutorial]] — **third agent-shaped DSPy tutorial** and the **first wiki receipt of `dspy.Tool.from_langchain(...)`** — a three-tool `dspy.ReAct` financial-analysis agent mixing a [[LangChain]] community tool (`YahooFinanceNewsTool`) with two plain-callable [[yfinance]] wrappers. `max_iters=6`, one-line string Signature (`"financial_query -> analysis_response"`), no optimizer, no metric. Documents `allow_tool_async_sync_conversion=True` set process-wide via `dspy.configure(...)` rather than per-block `dspy.context(...)`. Also the **first DSPy tutorial whose sample output reveals partial tool failure** (news fetch fails; agent reasons from price data alone) — a concrete *error-as-observation* receipt.
- [[CustomerServiceAgent]] — the general application pattern the tutorial receipt instantiates.
- [[Pydantic]] — first-class type provider for ReAct tool arguments and returns (forward reference).

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] cites ReAct (Yao et al. 2022) as the canonical **interleaving-of-reasoning-and-action** pattern that *"has become a common pattern for agents."* The Ch 6 framing is broader than the DSPy-specific framing already in this page — Yao et al. used *"reasoning"* to encompass both **planning** and **reflection**:

> *"At each step, the agent is asked to explain its thinking (planning), take actions, then analyze observations (reflection), until the task is considered finished by the agent."*

The canonical output format (which DSPy abstracts away as `trajectory`):

```
Thought 1: …
Act 1: …
Observation 1: …
… [continue until reflection determines the task is finished] …
Thought N: …
Act N: Finish [Response to query]
```

**Worked benchmark example**: Ch 6's ReAct illustration runs on [[hotpotqa|HotpotQA]] (Yang et al. 2018) — the multi-hop QA benchmark that anchors most of the wiki's DSPy retrieval receipts.

**Cost / latency trade-off** Huyen flags:

> *"Compared to plan generation, reflection is relatively easy to implement and can bring surprisingly good performance improvement. The downside of this approach is latency and cost. Thoughts, observations, and sometimes actions can take a lot of tokens to generate, which increases cost and user-perceived latency, especially for tasks with many intermediate steps. To nudge their agents to follow the format, both ReAct and Reflexion authors used plenty of examples in their prompts. This increases the cost of computing input tokens and reduces the context space available for other information."*

The chapter pairs ReAct with [[reflexion|Reflexion]] (Shinn et al. 2023) as the two canonical reflection mechanisms, and notes the [[ActorCriticAgent|actor-critic]] (Konda & Tsitsiklis 1999) RL ancestry in a footnote.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 of *Hands-On LLMs* is the **wiki's first runnable LangChain-native ReAct receipt**, complementing the existing [[DSPy]]-native receipts on this page. Ch 7's framing of ReAct:

> *"The driving force of many agent-based systems is the use of a framework called Reasoning and Acting (ReAct). ReAct merges these two concepts and allows reasoning to affect acting and actions to affect reasoning. ... the LLM is asked to create a 'thought' about the input prompt. Then, based on the thought, an 'action' is triggered. ... Finally, after the results of the 'action' are returned to the LLM it 'observes' the output."* — Ch 7

### The LangChain-native ReAct receipt

```python
from langchain.agents import AgentExecutor, create_react_agent
agent = create_react_agent(openai_llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
agent_executor.invoke({"input": "What is the current price of a MacBook Pro in USD? ..."})
```

Tools: a [[DuckDuckGoSearchResults|DuckDuckGo search]] wrapper + [[LLMMathTool|llm-math]] calculator. The agent runs two ReAct cycles (search → calculate) and produces *"$2,249.00 ... approximately 1911.65 EUR"* via [[ChatGPT|GPT-3.5-turbo]] (Phi-3-mini is **insufficient** for the agent role — the chapter's honest acknowledgment of the [[CompoundErrorAccumulation|capability cliff]]).

### DSPy-native vs LangChain-native ReAct

| Framework | Constructor | Trajectory access | I/O typing |
|---|---|---|---|
| **[[DSPy]]** | `dspy.ReAct(Signature, tools=[...])` | `pred.trajectory` field | Signature-typed |
| **[[LangChain]]** | `create_react_agent(llm, tools, prompt) + AgentExecutor` | `verbose=True` prints inline | Free-form text |

Same underlying Yao et al. 2022 scaffold; different ergonomics. The wiki now has both. See [[LangChainAgent]] for the LangChain-side receipt details and [[ShunyuYao]] for the paper author.

## Planning vs ReAct (Agentic Design Patterns, Ch 6)

[[agentic-design-patterns-ch06-planning|Chapter 6 of *Agentic Design Patterns*]] (Gulli) distinguishes the [[Planning]] pattern from the per-step think-act-observe loop ReAct embodies. ReAct decomposes *implicitly and step-by-step* (each Thought re-decides the next action given the last Observation); explicit Planning generates a coherent multi-step plan *up front* — decomposing the goal into sub-goals (see [[TaskDecomposition]]) — and may revise it via dynamic re-planning. The two compose: the chapter's [[DeepResearch|Deep Research]] exemplar is described in its Key Takeaways as a system that "reflects, plans, and executes," i.e. an explicit-planning layer wrapping a ReAct-style search-and-analyze loop, with [[Reflection]] driving knowledge-gap detection between iterations. The chapter's decision rule for when to add an explicit planner over a bare reactive ReAct agent: *"does the 'how' need to be discovered, or is it already known?"* — if known, a fixed workflow beats a planning agent.

## ReAct in the Reasoning Techniques chapter (Gulli, Ch 17)

[[agentic-design-patterns-ch17-reasoning|Chapter 17 of *Agentic Design Patterns*]] makes ReAct the **pivotal technique** of the [[ReasoningTechniques|Reasoning Techniques]] pattern — *"the pivotal leap to fully agentic systems… which empowers an agent to move beyond thinking and start acting by using external tools."* Gulli's framing of the loop is the canonical Thought → Action → Observation cycle (Fig. 3 shows ReAct querying a Public KB and Private KB), where the agent *"reasons about which actions to take… then acts by executing a tool or function call,"* and each observation feeds the next thought. Two chapter-specific points worth recording:

- **The interleaving frequency is tunable per task.** *"For knowledge-intensive reasoning tasks like fact-checking, thoughts are typically interleaved with every action… for decision-making tasks that require many actions, such as navigating a simulated environment, thoughts may be used more sparingly, allowing the agent to decide when thinking is necessary."* — i.e. the thought/action ratio is a design dial, not a fixed structure.
- **ReAct as the *core operational loop* of agents.** The chapter's Key Takeaways state ReAct *"provides agents with their core operational loop,"* establishing the thought-action-observation cycle as the foundation that the [[ScalingInferenceLaw|Scaling Inference Law]] (more thinking time) and multi-agent [[ChainOfDebates|debate]] frameworks build on top of. The chapter pairs ReAct with [[DeepResearch|Deep Research]] as the production-scale realization of this loop.

The book's [[agentic-design-patterns-appendix-a-prompting|Appendix A]] reprises ReAct at the prompt level as an "Action and Interaction Technique" — *"combines Chain of Thought-style reasoning with the ability to perform actions using tools in an interleaved manner"* — with the canonical four-step loop (Thought → Action → Observation → repeat until Final Answer) and an illustrative trace (*"What is the capital of France and its current population?"* → two `Search(...)` actions → Final Answer).
