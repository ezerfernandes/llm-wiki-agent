---
title: "Chain-of-Thought"
type: concept
tags: [ml-method, prompting]
sources: [2512.04388-conductor, 2604.21590-agenticqwen, dspy-modules, dspy-signatures, dspy-programming-overview, ai-engineering-ch05-prompt-engineering, ai-engineering-ch08-dataset-engineering, hands-on-llm-ch06-prompt-engineering, dspy-entity-extraction-tutorial, dspy-ai-text-game-tutorial, dspy-sample-code-generation-tutorial, dspy-email-extraction-tutorial, dspy-tutorial-program-of-thought, agentic-design-patterns-ch17-reasoning, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Chain-of-Thought

CoT prompting (Wei et al., 2022) elicits step-by-step intermediate reasoning before a final answer. In this corpus it shows up as the substrate the [[2512.04388-conductor|Conductor]] parses workflow lists from, and as a baseline tool-use foundation cited by [[2604.21590-agenticqwen|AgenticQwen]] alongside ReAct.

## DSPy implementation: `dspy.ChainOfThought`

In [[DSPy]], CoT is exposed as the **built-in [[DSPyModules|Module]]** `dspy.ChainOfThought` — *"Teaches the LM to think step-by-step before committing to the signature's response"* ([[dspy-modules]]). It is one of the seven built-in Modules and the one [[dspy-programming-overview|the Programming Overview]] recommends as the *"start simple"* default for any new task.

Three properties make the DSPy framing meaningfully distinct from CoT-as-a-prompt-template:

1. **Generalized over any signature.** `dspy.ChainOfThought('question -> answer')`, `dspy.ChainOfThought('document -> summary')`, and `dspy.ChainOfThought('claim, notes -> query')` are the *same Module class* applied to three different [[DSPySignatures|Signatures]]. There is no per-task CoT prompt to engineer — the framework derives the prompt from the Signature.

2. **Expands the signature with a `reasoning` field.** *"The `dspy.ChainOfThought` module will generally inject a `reasoning` before the output field(s) of your signature"* ([[dspy-modules]]). A user-declared `'question -> answer'` becomes `'question -> reasoning, answer'` on the wire; the returned `dspy.Prediction(...)` exposes **both** `.reasoning` and `.answer`. The user never declared `reasoning` — this is the canonical instance of [[DSPySignatures|the *modules-expand-signatures* mechanism]].

3. **Swap-in upgrade over [[DSPyPredict|`dspy.Predict`]].** *"In many cases, simply swapping `dspy.ChainOfThought` in place of `dspy.Predict` improves quality."* The swap is the constructor name only; the Signature, the LM, the Adapter, the Optimizer all stay the same. This is the operational form of [[DSPyProgrammingModel|the Programming Model's]] *"swap one module for another without modifying the signature"* portability claim at the *prompting-strategy* axis.

### Canonical usage

```python
question = "What's something great about the ColBERT retrieval model?"

classify = dspy.ChainOfThought('question -> answer', temperature=0.7)
response = classify(question=question)
print(response.reasoning)   # injected by the Module
print(response.answer)      # declared by the user
```

### Position in the DSPy module taxonomy

| Module | Signature expansion |
|---|---|
| [[DSPyPredict\|`dspy.Predict`]] | None — identity. |
| **`dspy.ChainOfThought`** | **Adds a `reasoning` field before the output.** |
| [[DSPyProgramOfThought\|`dspy.ProgramOfThought`]] | Code-and-execution slots. |
| [[react\|`dspy.ReAct`]] | Tool-call slots. |
| [[DSPyMultiChainComparison\|`dspy.MultiChainComparison`]] | Runs N `ChainOfThought` and adds a comparison Predict. |

`dspy.ChainOfThought` is the **base case** for two of the more elaborate Modules: `dspy.MultiChainComparison` runs N of them and aggregates; the [[SelfConsistency|self-consistency]] pattern in research papers maps to running N `ChainOfThought` calls and calling [[DSPyMajority|`dspy.majority`]] on the result.

### Where CoT loses to ProgramOfThought (wiki-corpus printed failure case)

[[dspy-tutorial-program-of-thought|The ProgramOfThought tutorial]] supplies the wiki's **canonical printed CoT-failure receipt**: `dspy.ChainOfThought(BasicGenerateAnswer)` on `"Compute 12! / sum of prime numbers between 1 and 30."` reasons correctly through `12! = 479,001,600` and prime-sum `= 129` but **fails the final division** — returns `'3,710,009'` instead of the correct `3,713,190.697...`. Swapping to [[DSPyProgramOfThought|`dspy.ProgramOfThought`]] — *constructor name only, same Signature, same LM* — recovers the correct float. **Concrete demonstration that CoT's prose-arithmetic step is unreliable when the answer requires precise numerical computation**; the [[DSPyProgrammingModel|swap-without-modifying-the-signature]] portability claim becomes operational here.

## Connections
- [[react|ReAct]]
- [[grpo|GRPO]]
- [[2512.04388-conductor]]
- [[2604.21590-agenticqwen]]
- [[DSPy]] — framework whose `dspy.ChainOfThought` Module is CoT's typed, signature-parameterized form.
- [[DSPyModules]] — the parent abstraction.
- [[DSPyPredict]] — the minimal primitive `dspy.ChainOfThought` is built on top of.
- [[DSPySignatures]] — the Signature the Module honors and expands.
- [[DSPyProgrammingModel]] — names `dspy.ChainOfThought` as the *start simple, then grow* default starting point.
- [[DSPyMultiChainComparison]] — sibling Module that runs N CoT calls + comparison.
- [[DSPyMajority]] — function-style aggregator commonly paired with N `ChainOfThought` samples (research-paper *self-consistency*).
- [[DSPyPrediction]] — the return object carrying both the `reasoning` slot and the user-declared output.
- [[SelfConsistency]] — N-CoT + majority-vote pattern. Forward reference; stub.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 names CoT as one of two **"give the model time to think"** [[PromptEngineering|prompt-engineering]] techniques (alongside [[SelfCritique|self-critique]]).

> "CoT means explicitly asking the model to think step by step, nudging it toward a more systematic approach to problem solving. CoT is among the first prompting techniques that work well across models."

Ch 5 traces CoT to Wei et al. 2022 (*"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"*), almost a year before ChatGPT.

**Key Ch 5 data point**: *"LinkedIn found that CoT also reduces models' hallucinations."* — connecting CoT to [[Hallucination|hallucination]] mitigation rather than just accuracy improvement.

**Ch 5's four CoT variants** (Table 5-4):
- **Zero-shot CoT**: *"Think step by step before arriving at an answer."*
- **Zero-shot CoT with rationale**: *"Explain your rationale before giving an answer."*
- **Zero-shot CoT with explicit steps**: *"Follow these steps to find an answer: 1. ... 2. ... 3. ..."*
- **One-shot CoT**: include one example of question + steps + answer.

**Trade-off**: CoT increases user-perceived latency — *"a model might perform multiple intermediate steps before the user can see the first output token."* If the steps are model-chosen rather than developer-fixed, the chain length can grow unboundedly.

Ch 5 also positions CoT alongside [[PromptDecomposition|prompt decomposition]] as a *"give the model time to think"* lever — the difference being that CoT keeps the reasoning inside one model call (more tokens) while decomposition spreads it across multiple calls (more API calls).

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 extends the CoT story to **training data**: to teach a model to reason step-by-step, the SFT data should include step-by-step responses. Per Chun et al. (2024):

> "Incorporating step-by-step responses in the finetuning data greatly enhances the performance of models of various sizes on CoT tasks, with **accuracy nearly doubling** for certain tasks."

### The cost

CoT demonstration data is **harder to produce than answer-only data** — explaining how to solve a math problem step-by-step is much more challenging than just giving the final answer. As a result, **CoT datasets are less common than other instruction datasets**.

### Worked examples from Chun et al. (cited in Ch 8)

| Without CoT | With CoT |
|---|---|
| Q: Boiling point of Nitrogen? A: -320.4F | Q: Cafeteria had 23 apples, used 20, bought 6 more — how many? A: "23 originally. Used 20 to make lunch. So 23 - 20 = 3. Bought 6 more, so 3 + 6 = 9." |

The headline insight: **CoT prompting and CoT training data are complementary** — better training data makes CoT prompting more effective; CoT prompting only fully works if the model has seen step-by-step responses in training.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 frames CoT through the **[[System1And2|System 1 vs System 2]]** lens:

> *"If we could give a generative model the ability to mimic a form of self-reflection, we would essentially be emulating the system 2 way of thinking, which tends to produce more thoughtful responses than system 1 thinking."* — Ch 6

This is a **constructive operationalization** of System 2 reasoning that sits in soft tension with [[2402.01817-llm-modulo|Kambhampati et al.'s critique]] that LLM "reasoning" is empty without external verifiers. Both positions are documented on [[System1And2]].

### The cafeteria-apples canonical example

Ch 6 walks the **canonical few-shot CoT example** from Wei et al. 2022:

```python
cot_prompt = [
    {"role": "user", "content": "Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?"},
    {"role": "assistant", "content": "Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11."},
    {"role": "user", "content": "The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?"}
]
```

The model produces the reasoning chain *"23 - 20 = 3 apples left. Then they bought 6 more apples, so they now have 3 + 6 = 9 apples. The answer is 9."*

### Two-way framing — with examples or zero-shot trigger

| Form | How it works |
|---|---|
| **Few-shot CoT** | Provide one or more `(question, reasoning + answer)` example pairs in the prompt. Wei et al. 2022. |
| **[[ZeroShotCoT\|Zero-shot CoT]]** | Append *"Let's think step-by-step"* (or alternative triggers). Kojima et al. 2022. |

Alternative zero-shot triggers Ch 6 names (citing Yang et al. 2023): *"Take a deep breath and think step-by-step"* / *"Let's work through this problem step-by-step."*

### The compute-justification framing

Ch 6's mechanistic explanation for why CoT improves outputs:

> *"Adding this reasoning step allows the model to distribute more compute over the reasoning process. Instead of calculating the entire solution based on a few tokens, each additional token in this reasoning process allows the LLM to stabilize its output."* — Ch 6

This is the **token-budget argument** for CoT — the model can use intermediate reasoning tokens as conditioning context for the final answer. The argument is consistent with [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]]'s framing of CoT as a *"give the model time to think"* lever and with [[parallelreasoning|parallel reasoning]] / [[testtimescaling|test-time scaling]] literature that takes inference-time compute as a first-class resource.

### Position alongside Huyen Ch 5's variant catalog

Huyen Ch 5's four variants (zero-shot CoT, zero-shot CoT with rationale, zero-shot CoT with explicit steps, one-shot CoT) are **fully consistent** with Ch 6's two-way framing — Ch 6's *"Let's think step-by-step"* is the canonical zero-shot CoT trigger; the alternative triggers are equivalent operating points; Ch 6's few-shot CoT subsumes Huyen's one-shot CoT row.

## Agentic Design Patterns (Gulli, Ch 17) perspective

[[agentic-design-patterns-ch17-reasoning|Chapter 17 of *Agentic Design Patterns*]] opens its [[ReasoningTechniques|Reasoning Techniques]] survey with CoT, framing it as the agent's **internal monologue** — *"a cornerstone technique for enabling advanced reasoning capabilities in contemporary LLMs."* Gulli's emphasis is on the **agentic value of transparency**: by breaking a complex problem into manageable sub-problems explicitly, CoT lets autonomous agents *"perform more reliable and auditable actions in complex environments."* In the chapter's arc, CoT is the base layer (the internal plan) that [[TreeOfThoughts|ToT]] branches, [[Reflection|self-correction]] critiques, and [[react|ReAct]] interleaves with action. Gulli also positions CoT as the single-model baseline that the multi-agent [[ChainOfDebates|Chain of Debates]] / [[GraphOfDebates|Graph of Debates]] frameworks deliberately move beyond, and notes that the "thinking" of [[rlvr|RLVR]]-trained reasoning models is essentially a long, dynamic CoT (thousands of tokens) learned via training rather than prompting.

### Appendix A: prompt-level CoT
The book's [[agentic-design-patterns-appendix-a-prompting|Appendix A]] presents CoT at the prompt level with the same two-way framing as *Hands-On LLMs* Ch 6 — **zero-shot CoT** (*"Let's think step by step"*) and **few-shot CoT** (provide example chains) — and adds two best practices: present the **final answer *after* the reasoning steps** (since generating the reasoning influences the answer's token predictions), and for single-correct-answer tasks (e.g. math) set [[Temperature|temperature]] to **0** (greedy decoding) for deterministic selection. It lists CoT's advantages (low-effort, off-the-shelf, interpretable, robust across model versions) and its main cost (more reasoning tokens → higher cost and latency).
