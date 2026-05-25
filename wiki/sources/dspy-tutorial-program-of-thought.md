---
title: "DSPy Tutorial — ProgramOfThought (LocalSandbox + ChainOfThought failure case + MultiHopSearchWithPoT)"
type: source
tags: [dspy, tutorial, program-of-thought, code-generation, sandbox, multi-hop-retrieval, colbertv2, llama3]
date: 2026-05-24
source_file: raw/dspy-tutorial-program-of-thought.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/program_of_thought/` (`docs/docs/tutorials/program_of_thought/index.ipynb`) — **the canonical end-to-end receipt of [[DSPyProgramOfThought|`dspy.ProgramOfThought`]]** in the wiki corpus. The tutorial walks three escalating receipts: (1) [[LocalSandbox|`dspy.LocalSandbox`]] as a standalone code-execution primitive; (2) a side-by-side [[chainofthought|`dspy.ChainOfThought`]] **failure** vs. `dspy.ProgramOfThought` success on `12! / sum-of-primes(1..30)` — same `BasicGenerateAnswer` Signature, same [[LanguageModel|LM]], swap of one constructor name; (3) a `MultiHopSearchWithPoT` `dspy.Module` that composes `dspy.ChainOfThought` for query generation with `dspy.ProgramOfThought(..., max_iters=3)` for the final computational answer over [[ColBERTv2]]-retrieved Wikipedia context.

**First wiki receipt of [[LocalSandbox|`dspy.LocalSandbox`]] as a user-facing API** — `sandbox.execute(expr)` returning the value of the last expression in `expr`. **First wiki receipt of `dspy.ProgramOfThought(..., max_iters=N)`** — the iteration-cap kwarg, hidden inside the Module on prior pages. **First wiki receipt of a swap-one-constructor portability demo from `dspy.ChainOfThought` to `dspy.ProgramOfThought` with a printed failure-then-success comparison** — the operational form of the *swap-without-modifying-the-signature* claim that [[DSPyProgrammingModel]] and [[DSPyModules]] assert but did not previously demonstrate with printed receipts.

## Key Claims

- **`dspy.ProgramOfThought` automatically generates and refines Python code to solve downstream tasks.** The tutorial frames `ProgramOfThought` as the code-execution counterpart to `ChainOfThought`: instead of routing reasoning through prose, route it through Python — generate code, execute it via `dspy.LocalSandbox`, fold the execution result into the [[DSPyPrediction|Prediction]] under the user's declared output field.
- **`dspy.LocalSandbox` is a standalone, user-instantiable primitive.** `sandbox = dspy.LocalSandbox(); sandbox.execute("value = 2*5 + 4\nvalue")` returns `14`. The tutorial walks this **before** introducing `dspy.ProgramOfThought`, framing the sandbox as the underlying engine the Module calls into. This is the first wiki receipt that `LocalSandbox` is reachable as `dspy.LocalSandbox` (not buried inside the Module's internals).
- **The Module honors arbitrary user-declared [[DSPySignatures|Signatures]].** `class BasicGenerateAnswer(dspy.Signature): question = dspy.InputField(); answer = dspy.OutputField()` → `pot = dspy.ProgramOfThought(BasicGenerateAnswer); pot(question="2*5 + 4").answer == '14'`. The generalized-over-any-signature claim from [[DSPyModules]] becomes operational here.
- **ChainOfThought fails at `12! / sum-of-primes(1..30)` at the final arithmetic step.** CoT reasons correctly through `12! = 479,001,600` and the prime sum (`2+3+5+7+11+13+17+19+23+29 = 129`) but divides incorrectly: `479,001,600 / 129 = 3,710,009` (wrong). Correct: `3713190.697674419`. The tutorial explicitly verifies *"by a real calculator!"* This is the **first wiki receipt of a CoT arithmetic failure caught and contrasted with PoT on the same prompt** — concrete evidence for the *Built-in sound critic* claim on the [[DSPyProgramOfThought]] page.
- **ProgramOfThought gets `3713190.697674419` on the same prompt.** Same `BasicGenerateAnswer` Signature, same LM, swap `dspy.ChainOfThought(...)` → `dspy.ProgramOfThought(...)`. The generated code defines helper functions (`is_prime`, `factorial`) and returns the exact float — no precision loss from prose arithmetic.
- **The portability claim — *"swap one module for another without modifying the signature"* — is operationalized with printed receipts.** The same `BasicGenerateAnswer` Signature drives `cot = dspy.ChainOfThought(BasicGenerateAnswer)` and `pot = dspy.ProgramOfThought(BasicGenerateAnswer)`. Constructor name is the only change.
- **`max_iters` is a `dspy.ProgramOfThought` constructor kwarg.** The `MultiHopSearchWithPoT` example uses `dspy.ProgramOfThought(GenerateAnswer, max_iters=3)`. First wiki receipt of this kwarg — the Module retries code generation up to `max_iters` times when execution fails, otherwise it short-circuits. Default value not disclosed by the tutorial; only the override is visible.
- **`MultiHopSearchWithPoT` is a custom `dspy.Module` composing `ChainOfThought` (query generation) + `ProgramOfThought` (final answer).** Two sibling sub-modules: `self.generate_query = dspy.ChainOfThought(GenerateSearchQuery)`, `self.generate_answer = dspy.ProgramOfThought(GenerateAnswer, max_iters=3)`. The `forward()` method runs `num_hops` retrieval loops, each calling `generate_query` then `search_wikipedia(query)`, deduplicating context, then a single `generate_answer(context, question)` at the end. **First wiki receipt of a multi-hop RAG pipeline whose final answer module is `dspy.ProgramOfThought` instead of `dspy.ChainOfThought`** — the prior multi-hop receipts ([[dspy-rl-multihop-tutorial]], [[dspy-tool-use-tutorial]]) all use `ChainOfThought` or hand-rolled prose-reasoning as the answer step.
- **Multi-hop computational word-problem receipt: "Statue of Liberty atomic number + first-10-primes digit count, squared" → 2025.** Question: *"What is the square of the total sum of the atomic number of the metal that makes up the gift from France to the United States in the late 19th century and the sum of the number of digits in the first 10 prime numbers?"* The pipeline (1) retrieves Statue of Liberty and copper passages via [[ColBERTv2]], (2) extracts atomic number 29, (3) computes the digit-sum-of-first-10-primes (14) programmatically, (4) sums (43), (5) squares (2025). Demonstrates the two-domain payoff: **retrieval for factual lookup, code execution for arithmetic**.
- **Tutorial LM: Meta `Llama-3-70b-Instruct`** via `dspy.LM("openai/meta-llama/Meta-Llama-3-70b-Instruct", api_base="API_BASE", api_key="None")`. **First wiki receipt of Llama-3-70b-Instruct in a DSPy tutorial** — the OpenAI-prefix + LiteLLM-mediated open-weight pattern with placeholder `api_base`/`api_key="None"`, consistent with [[DSPyLM]]'s any-provider posture.
- **Retrieval: `dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3)`.** Same public ColBERTv2 server URL as multiple other DSPy tutorials ([[dspy-custom-module]], [[dspy-modules]]). The `wiki17_abstracts` corpus — Wikipedia 2017 first-paragraph abstracts. **Wrapped in a plain Python `search_wikipedia(query)` function**, not a `dspy.Tool` — same pattern as [[dspy-custom-module]] (per [[ColBERTv2]]'s observation that the wrapper is a retrieval **client**, not a learnable sub-module).
- **`from dspy.dsp.utils import deduplicate`** — first wiki receipt of the `dspy.dsp.utils.deduplicate` helper used in multi-hop receipts. The legacy `dspy.dsp.*` namespace (carried over from the framework's earlier name *Demonstrate-Search-Predict*) still ships utility shims that are functionally part of the public surface.

## Key Quotes

> "`dspy.ProgramOfThought` automatically generates and refines Python code to solve downstream tasks." — Section 1

> "`ProgramOfThought` integrates an adapted Python sandbox to execute code generated by LMs." — Section 1

> "With the Python interpreter executing code accurately, `ProgramOfThought` mitigates computation errors that may fail in `ChainOfThought`, improving correctness particularly for numerical and logical queries." — Section 3

> "We'll take inspiration from the Multi-Hop Search task and simply tweak the final `generate_answer` layer to use `ProgramOfThought` in place of `ChainOfThought` to ensure accurate computations given a question and retrieved context." — Section 4

> "Let's use Meta's `Llama-3-70b-Instruct`. You can easily swap this out for other providers or local models." — Section 2

## Connections

- [[DSPy]] — host framework.
- [[DSPyProgramOfThought]] — the central Module the tutorial documents end-to-end. **This tutorial is the canonical receipt page; the [[DSPyProgramOfThought]] concept page links back to it.**
- [[LocalSandbox]] — new concept page minted by this ingest. `dspy.LocalSandbox` is the user-facing Python-execution primitive the Module wraps; this tutorial is the first wiki receipt where `LocalSandbox` is instantiated directly.
- [[chainofthought|ChainOfThought]] — sibling Module used as the *failure case* in Section 3 (`12! / 129` arithmetic error) and as the *query-generation* layer in `MultiHopSearchWithPoT`.
- [[DSPyModules]] — parent abstraction.
- [[DSPyPredict]] — minimal primitive both Modules wrap.
- [[DSPySignatures]] — `BasicGenerateAnswer` and `GenerateAnswer` are the Signatures the Modules honor.
- [[DSPyPrediction]] — return object carrying the `answer` field.
- [[DSPyProgrammingModel]] — names the CoT ↔ PoT swap as the canonical portability example; this tutorial is the operational receipt.
- [[ColBERTv2]] — retrieval client wrapped in `search_wikipedia(query)` for the multi-hop word-problem demo.
- [[MultiHopRAG]] / [[MultiHopQA]] — the multi-hop pattern this tutorial extends by swapping the answer module to PoT.
- [[InspectHistory]] — `dspy.inspect_history()` is called four times in the tutorial as the sanity-check window.
- [[DSPyLM]] — `dspy.LM("openai/meta-llama/Meta-Llama-3-70b-Instruct", api_base=..., api_key="None")` is the OpenAI-prefix-via-LiteLLM open-weight receipt.
- [[Llama3]] — the LM used by the tutorial (forward reference; stub if no page).
- [[ProgramOfThought]] — the underlying Chen et al. 2022 research-paper technique the Module generalizes (forward reference; stub).
- [[LLMModuloFramework]] — code execution as sound critic; this tutorial's CoT-vs-PoT comparison is a concrete demo of the LM + sound-critic pattern.

## Contradictions

- **None with existing wiki content.** This tutorial is consistent with every prior DSPy receipt: `dspy.Predict` as minimal primitive, Modules expand Signatures, the constructor-swap portability claim. The only **new disclosure** that does not contradict but **extends** prior content is the receipt that `dspy.LocalSandbox` is user-instantiable (prior pages described code execution only as a hidden internal mechanism inside `dspy.ProgramOfThought`).
- **One self-inconsistency in the tutorial**: both Section 3 (`ChainOfThought` comparison) and Section 4 (Contextual Reasoning) are numbered `## 3)` in the source — almost certainly a copy-paste typo in the upstream document, not a wiki contradiction. Documented for posterity.
- **No cost / latency / token-budget disclosure.** Continuing gap across the DSPy tutorial corpus.
- **No metric, no eval set, no [[DSPyOptimizers|Optimizer]].** This is a *programming-stage-only* tutorial (sibling to [[dspy-ai-text-game-tutorial]], [[dspy-sample-code-generation-tutorial]], [[dspy-custom-module]]) — demonstrates the API surface, not optimization.
- **No `max_iters` ablation.** The kwarg is set to 3 in the multi-hop receipt but the tutorial does not vary it or disclose the default.
- **No security model for `LocalSandbox`.** The tutorial does not describe what "adapted Python sandbox" actually isolates — no file-system / network / process discussion. Contrast with [[dspy-mcp-tutorial]]'s explicit child-process MCP isolation and [[dspy-tool-use-tutorial]]'s `@func_set_timeout(10)` + try/except isolation (which had no isolation boundary beyond timeout). **`LocalSandbox`'s actual safety boundary is undisclosed.**
- **The `wiki17_abstracts` ColBERTv2 endpoint is a publicly-hosted shared server at `http://20.102.90.50:2017`.** Same caveats as prior tutorials using this endpoint — unauthenticated HTTP, no SLA, may go down without notice. Forward-flagged as the canonical operational risk for any reproducer.
