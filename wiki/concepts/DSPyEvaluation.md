---
title: "DSPy Evaluation"
type: concept
tags: [dspy, llm-programming, evaluation, metrics, development-set, iteration, framework]
sources: [dspy-evaluation-overview, dspy-learn-index]
last_updated: 2026-05-24
---

# DSPy Evaluation

**DSPy Evaluation** is the **middle stage** of [[DSPy]]'s three-stage [[dspy-learn-index|Programming → Evaluation → Optimization]] workflow — the *measurement discipline* that turns a runnable DSPy program (the output of the Programming stage) into a **measurable, comparable, optimizable artifact** (the input the Optimization stage consumes).

The canonical source is the [[dspy-evaluation-overview|Evaluation Overview]] (page 9 of 13 of the *Learn* section). The stage's load-bearing contract — *"it's unproductive to launch optimization runs using a poorly designed program or a bad metric"* ([[dspy-learn-index|Learn index]]) — places Evaluation **upstream** of Optimization and makes the quality of the metric and dev set load-bearing for everything that follows.

## What Evaluation produces

The Evaluation stage's deliverables are not the score itself but **three reusable artifacts** the rest of DSPy consumes:

| Artifact | What it is | Consumed by |
|---|---|---|
| **Development set** | 20–200 worked examples of the task (inputs, optionally + final outputs) | The metric (per-example) and the [[DSPyOptimizers|Optimizer]] (as the search-objective sample) |
| **Metric** | A callable `(example, prediction) -> score` — scalar for simple tasks, a [[DSPyModules|`dspy.Module`]] for long-form tasks | The Optimizer (as the function to maximize) |
| **Baseline score** | The metric's value on the dev set under the *current* (unoptimized) program | The Optimizer (as the floor any optimized program must beat) and the developer (as the qualitative diagnostic *"spot any major issues"*) |

The three artifacts are **the interface contract** between the Programming and Optimization stages: a program plus a dev set plus a metric is a complete optimization problem; without any one, optimization cannot start.

## The four-step iterative-evaluation loop

[[dspy-evaluation-overview|The Evaluation Overview]] operationalizes the stage as a four-step loop, the last of which is **recursive**:

1. **Collect an initial development set.** *"Even 20 input examples of your task can be useful, though 200 goes a long way."* The page commits the framework to a **20–200-example dev-set regime** — small enough that manual labeling is feasible, large enough to discriminate among pipeline designs. Data sourcing has four ranked options:
   - **Adjacent public datasets** — HuggingFace datasets or *"a naturally occurring source like StackExchange"*.
   - **Permissive-license re-use** — *"If there's data whose licenses are permissive enough, we suggest you use them."*
   - **Manual labeling by hand** — *"you can label a few examples by hand"*.
   - **Deployed-demo collection** — *"start deploying a demo of your system and collect initial data that way."*

2. **Define a DSPy metric.** *"A metric is a function that takes examples from your data and takes the output of your system, and returns a score."* The metric is **executable Python**, not a string description, not a static threshold. Two regimes:
   - **Simple tasks** — *"just 'accuracy', e.g. for simple classification or short-form QA tasks."* A one-line scalar function.
   - **Long-form tasks** — *"your metric will be a smaller DSPy program that checks multiple properties of the output."* The metric is itself a [[DSPyModules|`dspy.Module`]] — a multi-property checker, typically built on [[DSPyPredict|`dspy.Predict`]] or [[ChainOfThought|`dspy.ChainOfThought`]] over a rubric [[DSPySignatures|Signature]]. This is DSPy's structural operationalization of the **[[llmasjudge|LLM-as-judge]]** pattern.

3. **Run development evaluations on pipeline designs.** *"Look at the outputs and the metric scores. This will probably allow you to spot any major issues, and it will define a baseline for your next steps."* The output is **two-fold**: a **baseline score** and a **qualitative diagnostic**. The diagnostic can force a return to **Step 1 or 2** (re-collect data, re-define metric) **or** all the way back to the Programming stage (re-design the pipeline). The loop is not strictly forward.

4. **(Recursive) Optimize the metric itself.** *"If your metric is itself a DSPy program, a powerful way to iterate is to optimize your metric itself. That's usually easy because the output of the metric is usually a simple value (e.g., a score out of 5), so the metric's metric is easy to define and optimize by collecting a few examples."* When the metric is a DSPy program, it can be **optimized** by a [[DSPyOptimizers|DSPy Optimizer]] the same way the system is — the "metric of the metric" is easier to define (because the metric's output is bounded and scalar) and easier to satisfy (because a few labeled examples suffice).

## Three load-bearing commitments

The Evaluation Overview makes three non-trivial framework-level commitments the wiki has not previously recorded:

### Commitment 1: Small dev sets are sufficient

*"Even 20 input examples of your task can be useful, though 200 goes a long way."*

This is in deliberate contrast to the ML-training tradition of thousands-to-millions of examples. The Evaluation stage is **not** training; it is **diagnostic**. Twenty examples are enough to:

- Discriminate among pipeline designs (e.g. [[ChainOfThought|`dspy.ChainOfThought`]] vs [[DSPyProgramOfThought|`dspy.ProgramOfThought`]]).
- Establish a baseline score the [[DSPyOptimizers|Optimizer]] must beat.
- Surface qualitative failure modes.

The 20-example floor lowers the **start-up cost** of using DSPy for a new task — the developer can ingest a handful of examples, write a metric, and run an evaluation in a sitting. The 200-example ceiling marks the *"goes a long way"* point of diminishing returns for dev-set-scale work.

### Commitment 2: Intermediate-step labels are almost never needed

*"You almost never need labels for the intermediate steps in your program in DSPy."*

Even though a [[DSPyModules|Module]] like [[ChainOfThought|`dspy.ChainOfThought`]] produces a `reasoning` field and a [[react|`dspy.ReAct`]] agent produces a `trajectory`, the developer does **not** need to label what the correct reasoning or trajectory would have been. The metric is computed against **final outputs only**; intermediate-step quality is implicit and is the [[DSPyOptimizers|Optimizer's]] job to discover.

This is DSPy's structural answer to the *intermediate-supervision problem* in chain-of-thought training: rather than supervising every intermediate step (expensive, often arbitrary), supervise only the **final output** and let the optimizer find an intermediate-step pattern that produces it. This commitment is what makes the Evaluation stage *tractable* for typical applications — labeling 200 input/final-output pairs is feasible; labeling 200 reasoning chains is not.

### Commitment 3: The metric is itself iterative

*"Invest in defining metrics and improving them incrementally over time; it's hard to consistently improve what you aren't able to define."*

The metric is a **moving target** the developer iterates on, not a fixed contract supplied up-front. *"Getting this right on the first try is unlikely: start with something simple and iterate."* This is the [[DSPyProgrammingModel|"start simple, then grow"]] discipline from page 2 applied to the **metric layer** — and it implies:

- The metric has **versions** over the project's lifetime.
- A change in metric definition may invalidate prior baselines.
- A program optimized against metric *v1* may underperform on metric *v2*; the developer must re-evaluate after a metric change.

Combined with the **recursive optimization** in Step 4, this commitment makes Evaluation a **self-improving subsystem** within DSPy — the metric improves the program, the program informs metric refinement, the metric's metric refines the metric, and so on. No other LLM-evaluation framework the wiki has recorded makes this *recursive-self-improvement* claim explicit.

## Why Evaluation is upstream of Optimization

The [[dspy-learn-index|Learn index]] is explicit: *"it's unproductive to launch optimization runs using a poorly designed program or a bad metric."* The Evaluation Overview operationalizes the *"bad metric"* half of this discipline. Three consequences:

- **The Optimizer's objective function is the metric.** [[DSPyOptimizers|Optimizers]] like `BootstrapFewShotWithRandomSearch`, `MIPROv2`, `BootstrapFinetune` (forward references to be filled in by [[DSPyOptimizers|page-13]]) search over instructions / demonstrations / weights to **maximize the metric**. If the metric is wrong, the optimizer climbs the wrong hill.

- **The Optimizer's input is the dev set.** The 20–200 examples the Evaluation stage collects are the search-objective sample the Optimizer evaluates each candidate program against. A dev set that doesn't cover the task's failure modes will yield an optimizer that doesn't fix them.

- **The Optimizer's baseline is the Evaluation baseline.** The score the Optimizer produces is meaningful only relative to the **pre-optimization baseline** the Evaluation stage establishes. Without that baseline, "optimization" is just running the program more.

This is the same load-bearing-prerequisite structure the [[DSPyProgrammingModel|Programming Model]] establishes between Programming and Evaluation: each stage's *output* is the next stage's *input contract*.

## Position in the wiki's evaluation landscape

DSPy Evaluation is the wiki's first **framework-level operationalization** of evaluation for LLM programs (as opposed to evaluation of LLMs themselves). It sits adjacent to but distinct from several related notions already in the wiki:

- **vs. [[ModelEvaluation]] (the general concept).** Model Evaluation is *"measuring model quality on a held-out set"* — a general ML notion. DSPy Evaluation is the **DSPy-specific operationalization**: 20–200-example dev set, callable metric over `(example, prediction)`, recursive-metric-optimization escape hatch. The DSPy version is **narrower** (specific to programs over LMs) and **richer** (commits to the four-step loop).

- **vs. [[OfflineEvaluation]] / [[OnlineEvaluation]].** DSPy Evaluation is unambiguously **offline** — run against a held-out dev set, not live traffic. The Overview does not discuss [[OnlineEvaluation|online evaluation]] (A/B tests, telemetry-driven measurement); this is consistent with DSPy's pre-deployment-iteration framing but is a **scope limit** worth noting.

- **vs. [[llmasjudge|LLM-as-judge]] in the broader literature.** The Overview's *"smaller DSPy program that checks multiple properties of the output"* metric is exactly an LLM-as-judge — but DSPy's version is **structurally different from ad-hoc LLM-as-judge prompts** because (a) the judge is itself a [[DSPyModules|`dspy.Module`]] with a typed [[DSPySignatures|Signature]], (b) the judge can be **optimized** by Step 4's recursive loop, and (c) the judge's prompts are produced by DSPy's [[DSPyAdapters|Adapter]] rather than hand-written. The wiki should treat the *DSPy LLM-as-judge* as a more disciplined form of the general technique.

- **vs. evaluation discussions in the agentic-harness corpus.** [[2604.25850-agentic-harness-engineering]] argues that the load-bearing axes are tools / middleware / memory rather than prompt structure; the Evaluation Overview's framing — that the metric is the **only** signal the Optimizer climbs — is **complementary** rather than contradictory. AHE would say *the metric must measure tool-use quality, not just final-output quality*; DSPy would respond *the metric is a program; write whatever measurement you want into it.*

## Forward references this concept commits to

[[dspy-evaluation-overview|The Evaluation Overview]] motivates the next two pages of the *Learn* section. The DSPyEvaluation concept page should be **expanded in place** when each lands:

- **[[DSPyData]]** (page 10 of 13, owned by a sibling ingest) will expand Step 1 — *"collect an initial development set"* — into the [[DSPyExample|`dspy.Example`]] data structure, the dev/train/test split convention, and the data-handling API surface.
- **[[DSPyMetrics]]** (page 11 of 13, owned by a sibling ingest) will expand Step 2 — *"define a DSPy metric"* — into the `(example, prediction) -> score` contract, the sub-types of metric (scalar, multi-property, judge-program), and the metric-debugging surface.

Both pages are forward references this concept commits to. When they land, the four-step loop above gains concrete-API anchors and the recursive-optimization claim (Step 4) gets a worked example.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-conversation-history]] — names the Evaluation stage's open scope-limit for conversational applications: *"the metric for a conversational application is typically [[llmasjudge|LLM-as-judge]]"* — turn-level rubric judgments over a `history`-bearing [[DSPyExample|`dspy.Example`]].
- [[dspy-mem0-react-tutorial]] — Programming-stage-only **counter-example**: tutorial **stops before** the Evaluation stage (no metric, no dev set, no [[DSPyEvaluate|`dspy.Evaluate`]] call), making the stage-boundary explicit by its absence.
- [[dspy-rag-tutorial]] — canonical end-to-end Evaluation-stage receipt: 20–200-example dev set + [[SemanticF1]] metric ([[DSPyModules|`dspy.Module`]] [[llmasjudge|LLM-as-judge]]) + baseline (42%) → all three artifacts of the stage produced and consumed by [[MIPROv2]].

## Connections

- [[DSPy]] — the framework whose middle stage this concept operationalizes.
- [[dspy-evaluation-overview]] — the canonical source for this concept (page 9 of 13 of the *Learn* section). Mints this page.
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization workflow within which this stage sits as the middle stage.
- [[DSPyProgrammingModel]] — the design philosophy from the Programming stage; the metric layer is the **contract** between the Programming Model's four artifacts and the Optimization stage.
- [[DSPyMetrics]] — **forward reference to page 11 of 13**; will expand Step 2 of the loop into the full metric contract. Owned by a sibling ingest.
- [[DSPyData]] — **forward reference to page 10 of 13**; will expand Step 1 of the loop into the [[DSPyExample|`dspy.Example`]] data-handling API. Owned by a sibling ingest.
- [[DSPyOptimizers]] — **forward reference to page 13 of 13**; the consumer of the metric and dev set this stage produces.
- [[DSPyModules]] — when the metric is a long-form-task metric, it is itself a [[DSPyModules|`dspy.Module`]] (typically [[DSPyPredict|`dspy.Predict`]] or [[ChainOfThought|`dspy.ChainOfThought`]] over a rubric Signature).
- [[DSPyPrediction]] — the metric's second argument is a [[DSPyPrediction|`dspy.Prediction`]]; the metric reads its output fields as attributes.
- [[DSPySignatures]] — a complex metric's rubric is encoded as a [[DSPySignatures|Signature]] (e.g. `"prediction: str -> correctness: float, justification: str"`).
- [[ChainOfThought]] — multi-property long-form metrics are typically a [[ChainOfThought|`dspy.ChainOfThought`]] invocation.
- [[DSPyPredict]] — the substrate every metric-as-DSPy-program is built on.
- [[ModelEvaluation]] — the general wiki concept this DSPy-specific concept specializes.
- [[OfflineEvaluation]] — the regime DSPy Evaluation operates in; the Overview does not address [[OnlineEvaluation]].
- [[OnlineEvaluation]] — explicitly out of scope on the Overview page; DSPy Evaluation is pre-deployment.
- [[llmasjudge|LLM-as-judge]] — the long-form-task metric regime DSPy's *"smaller DSPy program that checks multiple properties of the output"* operationalizes.
- [[PromptEngineering]] — the manual discipline DSPy displaces; the Evaluation Overview's *"start with something simple and iterate"* is the structurally automated analog of the prompt-engineer's iteration loop.
- [[2604.25850-agentic-harness-engineering]] — the harness-engineering counter-position; DSPy's metric-is-the-only-signal framing is complementary rather than contradictory.
- [[LLMModuloFramework]] — natural complementary framework; DSPy [[DSPyMetrics|Metrics]] are precisely the *critic* layer in Kambhampati et al.'s generate-test loop.
