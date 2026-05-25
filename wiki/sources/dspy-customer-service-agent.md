---
title: "DSPy Tutorial — Building AI Agents (Customer Service Agent)"
type: source
tags: [dspy, tutorial, react, agent, tools, customer-service, pydantic]
date: 2026-05-22
source_file: raw/dspy-customer-service-agent.md
---

## Summary

The [[DSPy]] **Building AI Agents (Customer Service Agent)** tutorial ([dspy.ai/tutorials/customer_service_agent](https://dspy.ai/tutorials/customer_service_agent/)) is the canonical end-to-end receipt for **building a multi-tool [[react|ReAct]] agent over a typed domain in [[DSPy]]**. Where [[dspy-tools|the Tools page]] (page 7 of 13) defined the [[DSPyTools|`dspy.Tool`]] abstraction in isolation and [[dspy-modules|the Modules page]]'s [[react|`dspy.ReAct`]] entry sketched the managed think-act-observe loop, this tutorial supplies the **first whole-system worked example**: a seven-tool airline customer-service agent built over a five-class [[Pydantic]] domain model (`Date`, `UserProfile`, `Flight`, `Itinerary`, `Ticket`), driven by a two-field [[DSPySignatures|Signature]] (`user_request: str` → `process_result: str`), instantiated as `dspy.ReAct(SignatureClass, tools=[...])`, invoked with a natural-language request, and producing a [[DSPyPrediction|`Prediction`]] with `trajectory` + `reasoning` + `process_result` fields.

The tutorial is the **second wiki-corpus DSPy tutorial** (after [[dspy-conversation-history]]), and it slots one rung **above** conversation-history on the DSPy application stack: a single-agent multi-tool task with structured domain types, rather than a multi-turn chatbot over a flat history. It is **also** the first wiki-corpus page to show [[Pydantic]] models composing through every layer — [[DSPyTools|tool argument types]], tool return types, and (implicitly, since tools accept and return them) the LM-rendered argument-and-observation surface that the [[DSPyAdapters|Adapter]] serializes.

The tutorial's three load-bearing structural claims:

1. **Tools are just typed Python functions** — docstrings + type hints are sufficient; no `dspy.Tool(...)` wrapping required when the function is passed directly into `dspy.ReAct(..., tools=[...])`. The framework introspects the function metadata.
2. **A single Signature scopes the whole agent**, regardless of tool count — the seven-tool agent has a two-field Signature; tools are *not* declared on the Signature, they are passed as the `tools=` kwarg on `dspy.ReAct`. The Signature is the **stable interface** between the user and the agent; the tool list is the **action surface** the agent searches over.
3. **The agent returns three fields**: `trajectory` (full reasoning + tool-call + observation log), `reasoning` (final-decision explanation), and `process_result` (the Signature's declared output field). The first two are added by `dspy.ReAct`; only `process_result` was declared on the Signature.

## Key Claims

- **Tools as Python functions with docstrings + type hints are sufficient for [[react|`dspy.ReAct`]].** *"Each tool must include: descriptive docstrings explaining functionality; type hints for all arguments (enabling proper LM argument generation)"* — the function's name, docstring, and type hints together supply everything [[DSPyTools|`dspy.Tool`]] needs (`.name` from `__name__`, `.desc` from the docstring, `.args` from type hints). When passed directly to `dspy.ReAct(..., tools=[...])`, the framework wraps each callable in a `dspy.Tool` automatically.

- **[[Pydantic]] models compose as first-class tool argument and return types.** The seven tools take and return `Date`, `UserProfile`, `Flight`, `Itinerary`, `Ticket` Pydantic models — the LM generates structured arguments matching the schema, and observations are returned as the same structured objects. This is the [[DSPySignatures|Signatures]] page's five-tier type system (tier three: *pydantic models*) **operationalized at the tool layer**.

- **The agent Signature is independent of the tool list.** *"`class DSPyAirlineCustomerService(dspy.Signature): user_request: str = dspy.InputField(); process_result: str = dspy.OutputField(desc=...)`"* — two fields, no tool-related types. The tool list is the **`tools=` kwarg on the Module constructor**, not a Signature field. This is structurally important: the same Signature could host a different tool list (different agent), and the same tool list could host a different Signature (different task scoping over the same actions).

- **The Signature's docstring becomes the agent's task description.** *"You are an airline customer service agent that helps user book and manage flights. You are given a list of tools to handle user request, and you should decide the right tool to use."* — the [[DSPyAdapters|Adapter]] renders the docstring as the system instruction. The Signature class docstring is the **primary natural-language scoping** of the agent's role.

- **`OutputField(desc=...)` documents the expected output content.** *"Message that summarizes the process result, and the information users need, e.g., the confirmation_number if a new flight is booked."* — the `desc=` kwarg is the developer's hint to the LM about what the output should contain (without typing it formally as a structured field). The tutorial uses this to scope `process_result` as a user-facing natural-language summary that **must include the confirmation number** when a flight is booked.

- **The agent returns three fields**: `trajectory` (the full think-act-observe log), `reasoning` (the final-decision explanation), and `process_result` (the Signature's declared output). The first two are added by [[react|`dspy.ReAct`]] internally; only `process_result` was declared on the Signature. This is the structural signature of *"modules expand signatures under the hood"* from [[dspy-modules|the Modules page]] — `dspy.ReAct` adds `trajectory` + `reasoning` to whatever Signature the user supplies.

- **`dspy.inspect_history()` is the canonical debugging surface.** *"Use `dspy.inspect_history()` to examine LM interactions at each step, viewing prompts, tool calls, and responses"* — the same global-history-print function the [[dspy-conversation-history]] tutorial uses for the chatbot pattern. Cross-tutorial confirmation that `dspy.inspect_history()` is the **standard cross-DSPy-Module introspection hook**, not a feature of any one Module.

## Key Quotes

> *"This tutorial demonstrates creating an airline customer service agent using DSPy's ReAct module."* — frames the entire tutorial as a [[react|ReAct]]-specific receipt.

> *"ReAct stands for 'Reasoning and Acting', it provides task descriptions and tool lists to language models, allowing them to decide when to call tools for observations or generate final outputs."* — restates the canonical [[react|ReAct]] mechanism from [[Yao2022|Yao et al. 2022]] in DSPy-vocabulary terms. The two LM choices per loop iteration: call a tool, or emit the final output.

> *"Each tool must include: descriptive docstrings explaining functionality; type hints for all arguments (enabling proper LM argument generation)."* — load-bearing developer-discipline statement. Mirrors the [[dspy-tools|Tools page]]'s design-guidance rules.

> *"Define tools as Python functions with docstrings and type hints. Pass tools to `dspy.ReAct` with a signature defining the task. Invoke with input fields; the framework handles the reasoning-acting loop internally."* — three-step recipe summary at the end of the tutorial.

## Code Receipts

### Receipt 1 — Pydantic domain model

Five classes scope the airline-booking domain:

```python
class Date(BaseModel):
    year: int
    month: int
    day: int
    hour: int

class UserProfile(BaseModel):
    user_id: str
    name: str
    email: str

class Flight(BaseModel):
    flight_id: str
    date_time: Date
    origin: str
    destination: str
    duration: float
    price: float

class Itinerary(BaseModel):
    confirmation_number: str
    user_profile: UserProfile
    flight: Flight

class Ticket(BaseModel):
    user_request: str
    user_profile: UserProfile
```

Structural notes: (i) `Itinerary` composes `UserProfile` + `Flight` — nested Pydantic models work at any depth; (ii) `Flight` composes `Date` — same property; (iii) `Ticket` is the escalation type for `file_ticket`; the [[react|ReAct]] agent decides when to escalate based on which tool it picks.

### Receipt 2 — Two of seven tools

```python
def fetch_flight_info(date: Date, origin: str, destination: str):
    """Fetch flight information from origin to destination on the given date"""
    # Implementation details...

def book_flight(flight: Flight, user_profile: UserProfile):
    """Book a flight on behalf of the user."""
    # Implementation details...
```

Both tools take Pydantic-typed arguments; the LM must generate a `Date(year=..., month=..., day=..., hour=...)` instance to call `fetch_flight_info`, and a `Flight(...)` + `UserProfile(...)` pair to call `book_flight`. The [[DSPyAdapters|Adapter]] handles the serialization-and-parsing translation between LM-emitted JSON and the typed Python objects.

### Receipt 3 — Agent Signature

```python
class DSPyAirlineCustomerService(dspy.Signature):
    """You are an airline customer service agent that helps user
    book and manage flights. You are given a list of tools to handle
    user request, and you should decide the right tool to use."""

    user_request: str = dspy.InputField()
    process_result: str = dspy.OutputField(
        desc="Message that summarizes the process result, and the "
             "information users need, e.g., the confirmation_number "
             "if a new flight is booked."
    )
```

The Signature has **no tool fields** — the tools are passed separately to `dspy.ReAct`. The class docstring is the agent's system instruction; the `OutputField(desc=...)` hint scopes what `process_result` should contain.

### Receipt 4 — Agent instantiation + invocation

```python
agent = dspy.ReAct(
    DSPyAirlineCustomerService,
    tools=[
        fetch_flight_info,
        fetch_itinerary,
        pick_flight,
        book_flight,
        cancel_itinerary,
        get_user_info,
        file_ticket,
    ]
)

import os
os.environ["OPENAI_API_KEY"] = "{your openai key}"
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

result = agent(
    user_request="please help me book a flight from SFO to JFK on 09/01/2025, my name is Adam"
)
print(result)
```

The agent is invoked with a single natural-language `user_request`. The framework: (1) parses the docstring + tool list into the system prompt; (2) runs the think-act-observe loop internally; (3) returns a [[DSPyPrediction|`Prediction`]] with `trajectory` + `reasoning` + `process_result`.

## Connections

- **[[DSPy]]** — entity. The tutorial extends [[DSPy]] with the canonical multi-tool agent receipt.
- **[[react]]** — concept. The tutorial is a worked example of [[react|`dspy.ReAct`]]'s managed think-act-observe loop with seven tools. Direct application of the [[Yao2022|Yao et al. 2022]] [[react|ReAct]] pattern.
- **[[CustomerServiceAgent]]** — concept (newly minted). The general application pattern this tutorial instantiates — a single-agent multi-tool task over a structured domain with escalation to human support as the safety valve.
- **[[DSPyTools]]** — concept. Operationalizes the [[DSPyTools|`dspy.Tool`]] abstraction at scale (seven tools, multiple Pydantic argument types). Receipt for the *"just pass Python functions"* shortcut: `dspy.ReAct(..., tools=[fn1, fn2, ...])` auto-wraps each callable.
- **[[DSPySignatures]]** — concept. Demonstrates the tier-three (Pydantic models) type system at the tool-argument and tool-return layer. The two-field user-facing Signature is decoupled from the seven-tool action surface.
- **[[DSPyModules]]** — concept. [[react|`dspy.ReAct`]] is the canonical tool-using Module; the tutorial shows the *modules-expand-signatures-under-the-hood* mechanism — `dspy.ReAct` adds `trajectory` and `reasoning` to the user's two-field Signature.
- **[[DSPyPredict]]** — concept. The [[DSPyTools|manual-handling path]] alternative — instead of `dspy.ReAct`, the user could use `dspy.Predict` over a Signature whose input is `tools: list[dspy.Tool]` and output is `dspy.ToolCalls`, owning the loop themselves. This tutorial takes the **managed path**.
- **[[DSPyPrediction]]** — concept. The return type carries `trajectory` + `reasoning` + `process_result`. The `trajectory` is the [[react|ReAct]]-specific introspection hook.
- **[[DSPyAdapters]]** — concept. The Adapter handles the serialization of Pydantic argument types into LM-emitted JSON and the parsing of LM responses back into typed Python objects.
- **[[Pydantic]]** — entity (forward reference). The Python data-validation library underpinning the typed domain model. Tier three of the [[DSPySignatures|Signatures]] type system.
- **[[gpt-4o]]** — entity. The tutorial uses `openai/gpt-4o-mini` as the backbone LM, mirroring [[dspy-conversation-history]].
- **[[LiteLLM]]** — entity. `dspy.LM("openai/gpt-4o-mini")` routes through [[LiteLLM]] for provider-agnostic LM dispatch.
- **[[chainofthought]]** — concept. [[react|`dspy.ReAct`]]'s `reasoning` field is the per-iteration CoT thought; the final `reasoning` field on the [[DSPyPrediction|Prediction]] is the final-decision explanation.
- **[[Yao2022]]** — forward reference. The original [[react|ReAct]] paper Yao et al. 2022 that the [[react|`dspy.ReAct`]] Module implements.
- **[[LLMModuloFramework]]** — concept. The agent is **not** an [[LLMModuloFramework|LLM-Modulo]] system — there is no external sound critic verifying that a booked flight is consistent or that an itinerary modification is valid. The Module is the soft-critic path; sound critics for the airline domain would be **deterministic Python checks** (e.g., `assert flight.origin != flight.destination`, `assert flight.date_time > now()`) added either inside each tool or as [[DSPyAssert|`dspy.Assert`]] checks.
- **[[DSPyAssert]]** — concept. The natural extension surface: hard-constraint checks (`dspy.Assert(flight.date_time > now())`) inside `book_flight` would make the agent fail-fast on invalid bookings instead of silently producing them.
- **[[2604.25850-agentic-harness-engineering]]** — paper. Counter-positioning: the AHE paper argues that DSPy-style instruction tuning is **not** the load-bearing layer — tools + middleware + long-term memory are. This tutorial is the strongest concrete DSPy receipt of an **agent built primarily on tools** rather than on prompt optimization; the load-bearing artifact here is the seven-function tool list, not the two-field Signature.

## Contradictions

None with existing wiki content. The tutorial **complements** prior DSPy pages:

- The *"tools are Python functions with docstrings + type hints"* discipline mirrors [[dspy-tools|the Tools page]] design-guidance rules verbatim.
- The Signature-vs-tools decoupling is the structural form of [[DSPyProgrammingModel|the Programming Model's]] four-concerns separation (Signature = task interface; tools = action surface; Module = strategy; Adapter = wire format).
- The single-Signature multi-tool pattern is the canonical realization of [[DSPyModules|the Modules page]]'s ReAct entry: *"`dspy.ReAct` — adds Tool-call slots; `tools=[...]` kwarg"*.

## Scope Limits

The tutorial is deliberately demonstrative. **Out of scope** (the tutorial does not address):

- **Optimization** — no [[BootstrapFewShot]] / [[MIPROv2]] / [[GEPA]] receipt. The agent is hand-written; no metric, no training set, no optimizer run. The [[dspy-optimizers|Optimizers page]]'s worked receipt for [[react|ReAct]] + [[MIPROv2]] on HotPotQA (24% → 51%) is the optimization-pattern complement.
- **[[DSPyAssertions|LM Assertions]]** — no hard-constraint checks inside tools. A production airline agent would gate every booking with `dspy.Assert(...)` checks.
- **[[DSPyHistory|Conversation history]]** — single-turn agent; no `dspy.History` field. A multi-turn customer-service agent (e.g., disambiguating "which flight?" across turns) would compose this tutorial's pattern with the [[dspy-conversation-history|conversation-history pattern]].
- **Tool failure handling** — no retry / fallback / human-in-the-loop on tool errors. The `file_ticket` tool is the agent-level escalation; tool-level error handling is application policy.
- **Per-tool authorization / cost / latency budgets** — no rate limits, no per-user permissions, no cost accounting per tool call. [[DSPyLM|`dspy.LM.history`]] / `get_lm_usage()` give LM-level telemetry but not tool-level.
- **[[ModelContextProtocol|MCP]]** — local Python tool functions only, not [[ModelContextProtocol|MCP]]-server-sourced tools. The [[dspy-mcp]] tutorial would supply the MCP-tool variant of the same pattern.
- **Multi-agent coordination** — single-agent only, no [[CoSTORM|Co-STORM]]-style multi-expert collaborative discourse.

These scope limits are the natural extension surface for production deployment.

## Position in the DSPy Application Stack

The Customer Service Agent tutorial is the **second wiki-corpus DSPy tutorial** and the **first whole-system worked example of a multi-tool ReAct agent over a typed domain**. It slots one rung above [[dspy-conversation-history]] on the DSPy application stack:

| Rung | Pattern | Wiki anchor |
|---|---|---|
| 1. Single LM call | [[DSPyPredict|`dspy.Predict`]] | [[dspy-modules]] |
| 2. Single LM-program call | [[DSPyModules|`dspy.Module`]] subclass | [[dspy-modules]] |
| 3. Multi-turn conversation | [[DSPyHistory|`dspy.History`]] + Python loop | [[dspy-conversation-history]] |
| 4. **Single-agent multi-tool task** | **[[react|`dspy.ReAct`]] + typed tool list** | **this tutorial** |
| 5. Multi-agent collaborative discourse | Custom multi-Module orchestration | [[2408.15232-co-storm]] |
| 6. Long-horizon RL'd compound system | [[grpo|GRPO]] / [[GEPA]] over $\langle \Pi, \Theta \rangle$ | [[2407.10930-better-together]] / [[2507.19457-gepa]] |

Rung 4 is the **natural composition** of rungs 1–3 — a [[DSPyModules|Module]] (rung 2) with [[DSPyTools|tools]] (action surface) and optionally [[DSPyHistory|history]] (rung 3 composition) — and the **building block** for rung 5 — a Co-STORM expert agent would internally be a rung-4 single-agent multi-tool system before contributing to the cross-agent mind map.

The seven-tool airline domain is also the wiki's **first canonical receipt for a deployment-shaped LM agent** — every prior DSPy ingest scoped either toy benchmarks ([[hotpotqa|HotPotQA]] / [[GSM8K]] / [[Iris]] / [[Banking77]]) or research domains ([[2025-bionlp-archehr-qa-neural|clinical QA]] / [[2507.03152-medval|clinical text validation]] / [[CoSTORM|collaborative discourse]]). The customer-service-agent shape — natural-language request → tool selection → structured action → user-facing response with confirmation — is the **production-application shape** the corpus had been missing.
