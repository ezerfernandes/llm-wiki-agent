---
title: "MIPROv2"
type: concept
tags: [dspy, optimizer, mipro, bayesian-optimization, instruction-tuning, few-shot, teleprompter]
sources: [2406.11695-mipro, dspy-optimizers, dspy-optimization-overview, 2507.19457-gepa, 2407.10930-better-together, 2604.14585-prompt-optimization-coin-flip, dspy-rag-tutorial, dspy-tutorial-rag-as-agent, dbreunig-pipelines-prompt-optimization-dspy, dspy-entity-extraction-tutorial, dspy-optimizer-tracking-tutorial, dspy-audio-tutorial, papillon-colab-tutorial, dspy-multihop-search-tutorial]
last_updated: 2026-05-24
---

> **Canonical primary source — [[2406.11695-mipro|Opsahl-Ong, Ryan, Purtell, Broman, Potts, Zaharia & Khattab (EMNLP 2024)]]**: *"Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs"* (arXiv:2406.11695v2). The paper formalizes the [[PromptOptimization|prompt-optimization]] problem for multi-stage [[LMProgram|LM programs]] (Algorithm 1), identifies the two structural challenges — the **proposal challenge** (intractable string space) and the **credit-assignment challenge** (no per-module labels) — proposes three proposal strategies (bootstrap demos / grounding / learning-to-propose) and three credit-assignment strategies (greedy / surrogate / history-based), and instantiates the whole framework as MIPRO + several baselines. **MIPRO wins on 5/7 tasks** of the [[DSPyOptimizerBenchmark]] (HotPotQA / HotPotQA-Conditional / Iris / Iris-Typo / Heart Disease / ScoNe / HoVer) by up to **13% absolute accuracy** with [[Llama3_8BInstruct|Llama-3-8B]] as the task LM and GPT-3.5 as the proposer.

> **2026 update (from [[2507.19457-gepa]]):** MIPROv2 is the **prior leading prompt optimizer that [[GEPA]] outperforms by >10%** across six benchmarks (HotpotQA, IFBench, HoVer, PUPA, AIME-2025, LiveBench-Math) on both Qwen3 8B and GPT-4.1 Mini. GEPA's prompts are also up to **9.2× shorter** than MIPROv2's because GEPA optimizes *only instructions* whereas MIPROv2 jointly optimizes instructions + multiple few-shot demonstrations. The paper notes this represents *"an exciting shift in this trend"* — earlier work (Wan et al. 2024) found instruction optimization mostly improved by producing quasi-exemplars; the 2026 finding is that **declarative natural-language instructions** now beat exemplars, attributed to improved LLM instruction-following + self-reflection.

> **External application: clinical QA at BioNLP 2025.** [[2025-bionlp-archehr-qa-neural|Reddy et al. (Neural team, University of Chicago)]] use MIPROv2 to optimize both stages of a two-stage [[EvidenceGroundedQA|evidence-grounded clinical-QA]] pipeline on [[ArchEHRQA2025|ArchEHR-QA 2025]] — Stage 1 (sentence-level evidence ID) optimized to maximize F1; Stage 2 (answer synthesis) optimized over a 6-metric composite reward ($[[bleu|BLEU]]+[[ROUGE]]+[[SARI]]+[[BERTScore]]+[[AlignScore]]+[[MEDCON]]$, mean, plus length+format indicators). Backbone [[GPT4_1|GPT-4.1]], 20-dev-case training set. Result: **2nd place, overall 51.5 — beats few-shot by 10 and zero-shot by 20 points**. The first peer-reviewed shared-task placement to use MIPROv2 in clinical NLP.

> **2026 empirical caveat (from [[2604.14585-prompt-optimization-coin-flip|Zhang, Wang, Cui, Qiu, Li, Zhu & He 2026]]):** MIPROv2's premise of [[JointOptimization|joint optimization]] across [[CompoundAISystem|compound AI system]] modules is *empirically untested* in the [[2406.11695-mipro|original paper]] and the [[2407.10930-better-together|BetterTogether]] / [[2507.19457-gepa|GEPA]] follow-ups. Zhang et al. supply the first controlled test on two-agent feed-forward pipelines and find the **$A \times B$ interaction term non-significant** in all six tested model×task conditions ($p > 0.52$, all $F < 1.0$, 0.18–2.15% of total variance). MIPRO's within-module joint optimization of *instructions × demonstrations* is not directly challenged — but its **across-module joint optimization** assumption is. The wiki's MIPRO successes ([[HotPotQAConditional]] 6 → 23.3, [[2025-bionlp-archehr-qa-neural|ArchEHR-QA]] zero-shot+20) are now best read as evidence for the [[CanButDoesntPattern|"can but doesn't" pattern]] (conditional-rule / citation-format output structure the model does not zero-shot default to) rather than evidence for cross-module coupling. See [[CompoundAIDiagnostic]] for the cheap pre-test the [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] framework recommends before invoking MIPROv2 on a new pipeline.


# MIPROv2

**`dspy.MIPROv2`** is [[DSPy]]'s **reference optimizer** — the algorithm the [[dspy-optimizers|Optimizers page]] uses as its canonical example of "how a non-trivial DSPy optimizer works". It is **the only optimizer in [[DSPyOptimizers|the catalog]] that jointly tunes both instructions and demonstrations** in the same run, and the only one that uses **[[BayesianOptimization|Bayesian Optimization]]** as its discrete-search procedure. Recommended for runs with **200+ training examples and 40+ trials**.

The acronym **MIPRO** stands for **M**ulti-prompt **I**nstruction **PR**oposal **O**ptimizer; `v2` is the second-generation version.

The canonical source is the **MIPRO paper** ([[2406.11695-mipro|Opsahl-Ong et al., EMNLP 2024]]); the catalog-level description on [[dspy-optimizers|page 13 of the DSPy *Learn* corpus]] is the user-facing documentation derived from it.

## Algorithm 1 — the generic framework

The MIPRO paper opens with a generic optimizer template that every concrete optimizer in the [[DSPyOptimizers|catalog]] implements:

```
Initialize(D, θ)              # consume trainset + proposer hyperparams
for k = 1 to I:
    (V ↦ S_k) ← Propose(θ)            # generate candidate prompt assignment
    D_k ← sample mini-batch of size B from D
    σ ← mean over D_k of μ(Φ_{V↦S_k}(x), x')   # validate assignment
    Update(V ↦ S_k, σ)                # update internal state
(V ↦ S_k) ← ExtractOptimizedSets()
return Φ_{V↦S}
```

MIPRO is the framework's **most general instantiation**: bootstrap demos × Bayesian-surrogate ([[TreeStructuredParzenEstimator|TPE]] via [[Optuna]]) joint search over (instruction, demo-set) per module + mini-batch evaluation.

## Family of optimizers introduced in the [[2406.11695-mipro|MIPRO paper]]

| Optimizer | Tunes | Credit assignment | Notes |
|---|---|---|---|
| [[BootstrapRandomSearch]] | Demos only | None (full-batch eval) | Demos-only baseline; Khattab et al. 2024. |
| **Bayesian Bootstrap** | Demos only | Surrogate over demo-set choice | MIPRO restricted to demos-only. |
| [[ModuleLevelOPRO]] | Instructions only | History-based ([[OPRO]]) | Per-module program-score-as-proxy. |
| **0-Shot MIPRO** | Instructions only | Surrogate | MIPRO restricted to instructions-only. |
| **0-Shot MIPRO++** | Proposer hyperparameters | Surrogate | Learns *how to propose* per task. |
| **MIPRO** | Joint (demos + instructions) | Surrogate | **Wins 5/7 [[DSPyOptimizerBenchmark|benchmark tasks]].** |
| Program-Level OPRO | Joint | History-based | Strong LM-credit-assignment assumption. |
| CA-OPRO | Joint (greedy) | Greedy per-module | Rejected on cost/gain ratio. |

## The three-stage mechanism

[[dspy-optimizers|The page]] describes MIPROv2 as a three-stage algorithm — this decomposition is the **structural template** the rest of the [[DSPyOptimizers|optimizer catalog]] can be read against:

### 1. Bootstrapping stage

> *"MIPRO starts with the bootstrapping stage. It takes your program, which may be unoptimized at this point, and runs it many times across different inputs to collect traces of input/output behavior for each one of your modules. It filters these traces to keep only those that appear in trajectories scored highly by your metric."*

Structurally similar to [[BootstrapFewShot]]'s demo-collection step — run the program on training inputs, collect per-module traces, filter by the [[DSPyMetrics|metric]] in `trace is not None` mode.

### 2. Grounded proposal stage

> *"MIPRO enters its grounded proposal stage. It previews your DSPy program's code, your data, and traces from running your program, and uses them to draft many potential instructions for every prompt in your program."*

The **distinctive contribution** of MIPROv2: the proposer doesn't draft instructions in a vacuum — it inspects the **actual Python code** of the program, the **training data**, and the **traces** from running the program. This is where DSPy's *"writing code instead of strings"* discipline ([[DSPyProgrammingModel|the Programming Model]]) pays off — the optimizer can read the program's structure to ground its instruction proposals.

### 3. Discrete search stage

> *"MIPRO launches the discrete search stage. It samples mini-batches from your training set, proposes a combination of instructions and traces to use for constructing every prompt in the pipeline, and evaluates the candidate program on the mini-batch. Using the resulting score, MIPRO updates a surrogate model that helps the proposals get better over time."*

[[BayesianOptimization|Bayesian Optimization]] surrogate-model-based search: the optimizer maintains a model of *which (instruction, demo-set) combinations score well*, samples promising combinations, evaluates them on mini-batches, and updates the surrogate.

## Parameters

| Parameter | Type | Default | Role |
|---|---|---|---|
| `metric` | callable | required | The optimization objective; consumed in `trace is None` mode for evaluation and `trace is not None` mode for demo filtering. |
| `auto` | str | (none) | Preset configuration: `"light"` / `"medium"` / `"heavy"` — trades off optimization budget for quality. |
| `num_threads` | int | (default) | Parallelism for evaluation; matches [[DSPyEvaluate|`dspy.Evaluate`]]'s thread-parallel harness. |
| `max_bootstrapped_demos` | int | (default) | Max demos generated by the teacher (bootstrapping stage). |
| `max_labeled_demos` | int | (default) | Max ground-truth demos sampled from `trainset`. |
| `prompt_model` | `dspy.LM` | (defaults to the configured LM) | LM used by the **grounded-proposal stage** to draft candidate instructions. Splitting from `task_model=` lets a larger model draft prompts evaluated against a smaller task LM. |
| `task_model` | `dspy.LM` | (defaults to the configured LM) | LM the candidate (instruction, demo-set) assignments are evaluated against in the **discrete-search stage**. |

### Asymmetric `prompt_model` / `task_model` split

When the deployed program needs to run on a small / cheap LM but a more capable LM is available offline for the optimization run, [[MIPROv2|MIPROv2]] supports a **proposer ≠ evaluator** configuration: `dspy.MIPROv2(..., prompt_model=<big>, task_model=<small>)`. The big model writes instruction candidates that the small model is graded on. [[dbreunig-pipelines-prompt-optimization-dspy|Breunig (2024-12-12)]] is the wiki's canonical receipt for this idiom — `prompt_model=Llama 3.3 70b`, `task_model=Llama 3.2 1b`, both via [[Ollama]]; the split yields *qualitatively better, less overfit* instructions at slightly lower validation accuracy (62%) than the single-model configuration (63.0%), trading a small numerical loss for better generalization.

## The `auto` presets

The `auto="light"/"medium"/"heavy"` kwarg is MIPROv2's **compute-budget knob** — three preset configurations that bundle the multiple internal hyperparameters into a single user-facing dial. [[dspy-optimizers|The page]] demonstrates `auto="light"` for HotPotQA and `auto="medium"` for RAG.

## Two worked receipts on the page

[[dspy-optimizers|The page]] uses MIPROv2 as the optimizer for **two of its three worked end-to-end receipts** (the third uses [[BootstrapFinetune]] for weight-tuning):

### Receipt 1: `dspy.ReAct` agent on HotPotQA (24% → 51%)

```python
import dspy
from dspy.datasets import HotPotQA

dspy.configure(lm=dspy.LM('openai/gpt-4o-mini'))

def search(query: str) -> list[str]:
    """Retrieves abstracts from Wikipedia."""
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3)
    return [x['text'] for x in results]

trainset = [x.with_inputs('question') for x in HotPotQA(train_seed=2024, train_size=500).train]
react = dspy.ReAct("question -> answer", tools=[search])
tp = dspy.MIPROv2(metric=dspy.evaluate.answer_exact_match, auto="light", num_threads=24)
optimized_react = tp.compile(react, trainset=trainset)
```

> *"An informal run similar to this on DSPy 2.5.29 raises ReAct's score from 24% to 51%."*

Setup: [[react|`dspy.ReAct`]] + Wikipedia search via `dspy.ColBERTv2`; GPT-4o-mini; 500 train examples; `dspy.evaluate.answer_exact_match` metric; **`auto="light"`**.

### Receipt 2: RAG module on StackExchange (53% → 61%)

```python
class RAG(dspy.Module):
    def __init__(self, num_docs=5):
        self.num_docs = num_docs
        self.respond = dspy.ChainOfThought('context, question -> response')

    def forward(self, question):
        context = search(question, k=self.num_docs)
        return self.respond(context=context, question=question)

tp = dspy.MIPROv2(metric=dspy.SemanticF1(), auto="medium", num_threads=24)
optimized_rag = tp.compile(RAG(), trainset=trainset, max_bootstrapped_demos=2, max_labeled_demos=2)
```

> *"It improves the quality of a RAG system over a subset of StackExchange communities from 53% to 61%."*

Setup: [[ChainOfThought|`dspy.ChainOfThought`]]-based RAG module; `dspy.SemanticF1()` ([[SemanticF1]]) as the metric (an [[llmasjudge|LLM-as-judge]] DSPy module — the **recursive-metric-optimization** claim from [[DSPyMetrics|Step 4 of the four-step Evaluation loop]] is exercised here); **`auto="medium"`**; explicit `max_bootstrapped_demos=2`, `max_labeled_demos=2`.

### Receipt 1b: `dspy.ReAct` agent on HoVer (3-hop) with GPT-4o teacher + Llama-3.2-3B student (8% → 41.67%)

The [[dspy-tutorial-rag-as-agent|Building RAG as Agent tutorial]] supplies the **first wiki receipt that decouples teacher and student models in a single MIPROv2 run**:

```python
llama3b = dspy.LM('<provider>/Llama-3.2-3B-Instruct', temperature=0.7)
gpt4o = dspy.LM('openai/gpt-4o', temperature=0.7)
dspy.configure(lm=llama3b)  # student is the global LM

react = dspy.ReAct(signature, tools=[search_wikipedia, lookup_wikipedia], max_iters=20)

kwargs = dict(teacher_settings=dict(lm=gpt4o), prompt_model=gpt4o, max_errors=999)
tp = dspy.MIPROv2(metric=top5_recall, auto="medium", num_threads=16, **kwargs)
optimized_react = tp.compile(react, trainset=trainset,
                             max_bootstrapped_demos=3, max_labeled_demos=0)
```

Two kwargs do the decoupling: **`teacher_settings=dict(lm=gpt4o)`** sets the **demo-bootstrapping teacher** (which model runs the program to collect successful traces); **`prompt_model=gpt4o`** sets the **instruction proposer** in the grounded-proposal stage. Both default to the configured task LM if unset. The tutorial uses GPT-4o for both — the *all-teacher-where-it-matters* pattern.

Additional kwargs the tutorial surfaces for the first time in the wiki:
- **`max_errors=999`** — operational knob for brittle students; small open-weights models misformat / loop / fail to terminate often enough during exploration that the default error budget aborts optimization.
- **`max_bootstrapped_demos=3, max_labeled_demos=0`** — the *small-student / GPT-4o-teacher* preset. Three demos is what fits in the brittle student's context; zero labeled demos because the dataset has no chain-of-thought labels, only `(claim, gold_titles)` pairs.

**Headline result: 8% → ~41.67% top5_recall, ~5× improvement on the same 3B student.** Larger lift than the [[2406.11695-mipro|MIPRO paper's]] HoVer result (30.2 → 44.7, 1.5×) because the paper used [[Llama3_8BInstruct|Llama-3-8B]] as the task LM (more headroom in the 3B case). This is the canonical wiki receipt for *"the expensive model writes the prompts; the cheap model runs them"*.

### Receipt 3: Single-step CoT on [[MATH-benchmark|MATH]] algebra (74.0% → 88.57%)

The [[dspy-tutorial-math|DSPy Math Reasoning tutorial]] supplies the **first wiki MIPROv2 receipt on a symbolic / numerical reasoning task** — and the **first wiki receipt where [[chainofthought|`dspy.ChainOfThought`]] is the entire program** (no retrieval, no tools, no history):

```python
gpt4o_mini = dspy.LM('openai/gpt-4o-mini', max_tokens=2000)
gpt4o     = dspy.LM('openai/gpt-4o',      max_tokens=2000)
dspy.configure(lm=gpt4o_mini)

from dspy.datasets import MATH
dataset = MATH(subset='algebra')                       # 350 train, 350 dev

module = dspy.ChainOfThought("question -> answer")     # the entire program

kwargs = dict(num_threads=24, teacher_settings=dict(lm=gpt4o), prompt_model=gpt4o_mini)
optimizer = dspy.MIPROv2(metric=dataset.metric, auto="medium", **kwargs)
optimized = optimizer.compile(module, trainset=dataset.train,
                              max_bootstrapped_demos=4, max_labeled_demos=4)
```

Setup: GPT-4o-mini student + GPT-4o teacher; **`auto="medium"`**; **`max_bootstrapped_demos=4, max_labeled_demos=4`** (double the 2+2 used in Receipts 2/2b — the MATH dataset includes worked-solution `answer` labels, so labeled demos are usable); 24 threads.

**Headline result: 74.0% → 88.57% on the 350-example dev set** (+14.6 pts absolute, ~20% relative).

Three structural firsts:
- **First MIPROv2 receipt on math reasoning** — prior receipts cover RAG (1, 2, 2b), agents (1b), and NER ([[dspy-entity-extraction-tutorial|CoNLL-2003]]). MATH fills the symbolic-reasoning slot.
- **First receipt where the program is one line of DSPy** — `dspy.ChainOfThought("question -> answer")` with no surrounding `dspy.Module` subclass.
- **First receipt of `dspy.datasets.MATH(subset=...)` as an in-framework dataset loader** with a built-in `dataset.metric`.

### Receipt 4: PAPILLON privacy-delegation on PUPA (authors-of-record Colab — number not printed)

The [[papillon-colab-tutorial|Columbia-NLP-Lab Colab tutorial]] supplies the **first wiki MIPROv2 receipt on a [[CompoundAISystem|compound AI program with an external untrusted LM call]]** — and the first MIPROv2 receipt written by the program's *paper authors themselves* (rather than DSPy.ai documentation derived from it). Trains the two-module [[PAPILLON]] system on the [[PUPA]] benchmark:

```python
local_lm = dspy.LM('openai/sglang/Llama-3.1-8B-Instruct',
                   api_base=f"http://127.0.0.1:{PORT_NUMBER}/v1",
                   api_key="", max_tokens=4000)
dspy.configure(lm=local_lm)
openai_lm = dspy.LM(model="openai/gpt-4o-mini", max_tokens=4000)

models = dict(prompt_model=openai_lm, task_model=local_lm)
optimizer = dspy.MIPROv2(metric=compute_overall_score, auto="medium",
                         num_threads=16, **models)
opt_papillon = optimizer.compile(
    zeroshot, trainset=trainset,
    minibatch_size=35, max_bootstrapped_demos=5, max_labeled_demos=0,
)
```

Setup: **Llama-3.1-8B-Instruct** (local trusted, served via [[SGLang]] on a single GPU) + **GPT-4o-mini** (untrusted external *and* prompt-proposer *and* judge LM — three roles collapsed); `dspy-ai==2.5.41` (pinned to the pre-3.0 era contemporaneous with the original PAPILLON paper); **`auto="medium"`**; **`minibatch_size=35`** (first wiki receipt of this kwarg); **`max_bootstrapped_demos=5, max_labeled_demos=0`** (the most-bootstrapped / zero-labeled MIPROv2 configuration in the wiki — driven by PUPA's lack of chain-of-thought labels); 150 train / 150 dev / remainder test from `pupa_new["train"]`; **expected runtime 30–60 min on one GPU**.

**Headline result: not printed** — the notebook commits seven `evaluate(...)` calls (zero-shot, paper-era loaded, and optimized; each evaluated for quality and leakage) but the output cells are *not* committed to the repo. **This receipt closes the API-surface gap** (MIPROv2 runs end-to-end on a compound AI system with an external LM call) but **leaves the headline-number gap open** between the [[2507.19457-gepa|GEPA paper Table 4]]'s paper-scale MIPROv2-on-PUPA cell (81.55 Qwen3 8B / 85.37 GPT-4.1 Mini) and a tutorial-grade replication.

Three structural firsts:
- **First MIPROv2 receipt on a compound AI program with an external untrusted LM call** — Receipts 1/1b/2/2b/3 are all single-module or single-module-with-tools programs. The PAPILLON program reaches *outside* the trainable LM to GPT-4o-mini, which the optimizer does not control.
- **First MIPROv2 receipt with [[SGLang]] as the explicit serving backend** for a DSPy compound system (the [[SGLang]] entity page documents the framework abstractly via [[dspy-language-models]]; this is the first concrete-tutorial receipt).
- **First MIPROv2 receipt with the `prompt_model` ≠ `task_model` split + a separate per-module `set_lm(...)` binding for the judge** (gated on `dspy.configure(experimental=True)`).

Tutorial also demonstrates `loaded_papillon.load('papillon/optimized_prompts/llama_31_8b_instruct_prompt.json', use_legacy_loading=True)` — the **first wiki receipt of `use_legacy_loading=True`** as a DSPy 2.4 → 2.5 save-format backwards-compat shim — for loading the paper-era pre-optimized prompts shipped with the repo.

### Receipt 2b: RAG module on [[RAGQAArenaTech|RAG-QA Arena Tech]] (42% → 55.5% → 61.1%)

The [[dspy-rag-tutorial|DSPy RAG tutorial]] supplies a **second worked instance** of the Receipt 2 pattern — same `auto="medium"`, same `max_bootstrapped_demos=2 / max_labeled_demos=2`, same gpt-4o-mini, same [[SemanticF1]] metric — on a different dataset ([[RAGQAArenaTech]], ~1K technical-domain QA pairs) and a different retriever ([[openai|OpenAI]] `text-embedding-3-small` over a 28K-doc local technical corpus, `k=5`). **Performance ladder**: baseline [[chainofthought|CoT]] (no retrieval) 42% → un-optimized RAG 55.5% → MIPROv2-optimized RAG **61.1%**. The +6-point optimization gain at ~**$1.50, ~20–30 min** matches Receipt 2's 53→61 envelope almost exactly — **two independent benchmarks now converge on ~61% [[SemanticF1]] as the post-optimization ceiling** for a single-hop CoT-based RAG on gpt-4o-mini with `auto="medium"`.

## The 0-shot mode

[[dspy-optimizers|The page]]'s five-rule rubric carves out a **0-shot configuration** for MIPROv2:

> *"If you prefer to do **instruction optimization only** (i.e. you want to keep your prompt 0-shot), use `MIPROv2` configured for 0-shot optimization."*

Setting `max_bootstrapped_demos=0` and `max_labeled_demos=0` (presumably) makes MIPROv2 tune **only the instructions**, leaving the prompt as 0-shot — useful when the deployed program needs to fit a small token budget or run against an LM that doesn't handle long few-shot prompts well.

## Position in the catalog's getting-started flow

```
~10 examples       → BootstrapFewShot
50+ examples       → BootstrapFewShotWithRandomSearch
200+ examples      → MIPROv2 (this page)
0-shot prompts     → MIPROv2 (0-shot mode)
post-success       → BootstrapFinetune
```

MIPROv2 is the **default for serious optimization runs** — the rubric's "200+ examples and 40+ trials" threshold aligns with the [[DSPyOptimization|workflow page's]] *300-example target*.

## What MIPROv2 reveals about the catalog

MIPROv2's three-stage decomposition is the **structural template** for non-trivial DSPy optimizers:

| Step | MIPROv2's choice | Other optimizers' alternatives |
|---|---|---|
| **(a) Collect** | Bootstrap traces, metric-filter | [[BootstrapFewShot]]'s identical step; [[GEPA]]'s trajectory collection; [[BootstrapFinetune]]'s identical step |
| **(b) Propose** | Grounded proposal from code + data + traces | `COPRO`'s instruction refinement; `SIMBA`'s self-reflective rules; [[GEPA]]'s LM reflection on what worked |
| **(c) Search** | [[BayesianOptimization\|Bayesian Optimization]] | `COPRO`'s coordinate ascent; [[BootstrapFewShotWithRandomSearch]]'s random search; `KNNFewShot`'s k-NN ranking; `SIMBA`'s mini-batch stochastic search |

MIPROv2 is the **only optimizer that occupies a distinctive position at every step** (a)+(b)+(c) — the most general-purpose optimizer in the catalog, and the most computationally expensive.

## Five lessons from the [[2406.11695-mipro|original paper]]

1. **Optimizing bootstrapped demonstrations is essential** — demos-only beats instructions-only on most tasks.
2. **Joint optimization of both is best overall** — MIPRO wins on 5/7 tasks with Wilcoxon significance.
3. **Instruction optimization is most important for tasks with conditional rules** not expressible via a small number of few-shot examples ([[HotPotQAConditional]], [[IrisTypo]], [[HeartDisease]]).
4. **Grounding helps for instruction proposal overall, but the best proposal strategy varies by task** — grounding hurts on [[ScoNe]]; [[BayesianOptimization|Bayesian]] learning over the proposer's hyperparameters (0-Shot MIPRO++) recovers per-task optimal strategies.
5. **More to learn about LM-program optimizers** — different optimizers may dominate at different compute budgets; current rankings are budget-conditional.

## Observability via [[MLflow]] autologging

The [[dspy-optimizer-tracking-tutorial|DSPy Optimizer Tracking tutorial]] is the wiki's canonical source for **MIPROv2's internal trial structure surfaced through an external tracking system**. With `mlflow.dspy.autolog(log_compiles=True, log_evals=True, log_traces_from_compile=True)`, an MIPROv2 `teleprompter.compile(...)` call materializes as a two-level [[MLflow]] run tree:

- **Parent run** — config (`auto` preset, `metric`, `max_bootstrapped_demos`, etc.), final optimized program JSON, training data, metric-progression curve across all trials.
- **Child runs** — one per intermediate `(instruction, demo-set)` candidate the [[BayesianOptimization|Bayesian surrogate]] sampled; each carries the candidate's instructions + demos, the per-mini-batch metric values, and the full LM-call trace tree for that attempt.

This makes the three-stage algorithm (bootstrap → grounded proposal → discrete search) **navigable** rather than opaque — every instruction the grounded-proposal stage drafted and every demo combination the discrete-search stage sampled becomes a clickable artifact in the MLflow UI. The tutorial's worked example exercises **MIPROv2 `auto="light"` on [[GSM8K]] with `gpt-4o` as the task LM** (first wiki MIPROv2 receipt on GSM8K via DSPy's in-framework `dspy.datasets.gsm8k.GSM8K` loader + built-in `gsm8k_metric`), without reporting a headline accuracy — the tutorial's scope is the tracking surface, not the optimization gain. Heavy-trace caveat: `log_traces_from_compile=True` storage cost grows linearly in (trials × demos × dataset size); the tutorial recommends `log_traces_from_compile=False` for large datasets.

## Connections

- [[2406.11695-mipro]] — **canonical primary source** (Opsahl-Ong et al., EMNLP 2024).
- [[dspy-optimizer-tracking-tutorial]] — **canonical wiki source for MIPROv2 observability via [[MLflow]]** — three-kwarg autolog (`log_compiles` / `log_evals` / `log_traces_from_compile`), parent/child run hierarchy mirroring MIPROv2's discrete-search trajectory, model-loading round-trip via `mlflow.artifacts.download_artifacts(...) + program.load(...)`. Also the first wiki MIPROv2 receipt on [[GSM8K]] with the built-in `gsm8k_metric`.
- [[dspy-rag-tutorial]] — second worked RAG receipt: 42% / 55.5% / **61.1%** [[SemanticF1]] on [[RAGQAArenaTech]] with `auto="medium"` — converges with Receipt 2 (53% → 61% on StackExchange) on ~61% as the post-optimization ceiling.
- [[papillon-colab-tutorial]] — **first MIPROv2 receipt on a compound AI program with an external untrusted LM call** (PAPILLON on PUPA); first `minibatch_size=35` receipt; first `max_bootstrapped_demos=5, max_labeled_demos=0` receipt; first SGLang-as-serving-backend MIPROv2 receipt; first `use_legacy_loading=True` receipt for paper-era pre-optimized prompts. **Headline number not printed** — the notebook commits the API-surface receipt without the output cells.
- [[dbreunig-pipelines-prompt-optimization-dspy]] — **third-party single-stage classification receipt**, `auto="light"` 0-shot mode (`max_labeled_demos=0, max_bootstrapped_demos=0`), [[Llama|Llama 3.2 1b]] via [[Ollama]] **51.9% → 63.0%**; also the wiki's canonical receipt for the **asymmetric `prompt_model` / `task_model` split** (proposer Llama 3.3 70b ≠ evaluator Llama 3.2 1b — reduces overfitting at slight validation-accuracy cost, 62%).
- [[dspy-tutorial-rag-as-agent]] — **first wiki receipt with teacher/student decoupling**: [[Llama|Llama-3.2-3B]] student + [[OpenAI|GPT-4o]] teacher (`teacher_settings=dict(lm=gpt4o), prompt_model=gpt4o, max_errors=999`) lifts [[react|`dspy.ReAct`]] on [[HoVer]] three-hop from 8% → 41.67% top5_recall (5×) with `auto="medium"`, `max_bootstrapped_demos=3, max_labeled_demos=0`.
- [[SemanticF1]] — the [[llmasjudge|LLM-as-judge]] metric used in both RAG receipts.
- [[RAGQAArenaTech]] — the dataset for the tutorial-anchored RAG receipt.
- [[2025-bionlp-archehr-qa-neural]] — external clinical-NLP application (BioNLP 2025 shared task, 2nd place).
- [[2603.19247-prompt-optimization-jailbreaking]] — **adversarial application**: MIPROv2 used to *maximize* danger judge score on [[HarmfulQA]] + [[JailbreakBench]] seeds. Lifts mean danger by 2–8× across four target LLMs; placed *second* of three optimizers (behind [[SIMBA]], ahead of [[GEPA]] on LLaMA-4 / Qwen-3). The cell where MIPROv2 most narrowly trails SIMBA is LLaMA-4 Maverick (0.581 vs 0.623, $\Delta = 0.04$).
- [[DSPy]] — the framework.
- [[DSPyOptimizers]] — the catalog this optimizer belongs to; MIPROv2 is the **reference example** the page uses to explain how optimizers work.
- [[DSPyOptimization]] — the workflow this optimizer operationalizes.
- [[dspy-optimizers]] — the canonical source page.
- [[BayesianOptimization]] — the surrogate-model-based search algorithm used in the discrete-search stage.
- [[DSPyMetrics]] — the metric is the optimizer's input; dual-purpose `trace` argument used in both modes.
- [[DSPyPredict]] — the per-Module learnable parameter site; MIPROv2 mutates each Predict's **`signature`** (instructions) **and** **`demos`** (demonstrations) attributes.
- [[DSPyPrediction]] — the typed return object the metric consumes.
- [[DSPyModules]] — the program input/output type.
- [[DSPyData]] / [[DSPyExample]] — the training set primitive.
- [[DSPyProgrammingModel]] — the *"writing code instead of strings"* discipline that makes the grounded-proposal stage possible (the optimizer reads the program's actual code).
- [[ChainOfThought]] — used in the RAG worked receipt as the default Module.
- [[react|ReAct]] — used in the HotPotQA worked receipt as the tool-using agent.
- [[llmasjudge]] — `dspy.SemanticF1()` in the RAG receipt is an LLM-as-judge metric.
- [[BootstrapFewShot]] — structurally similar bootstrapping stage; demos-only sibling.
- [[BootstrapFewShotWithRandomSearch]] — random-search alternative for smaller data budgets.
- [[GEPA]] — alternative instruction-tuning optimizer using LM-reflection instead of Bayesian search.
- [[BootstrapFinetune]] — the weight-tuning sibling; MIPROv2's output can be fed into BootstrapFinetune (the composability claim).
- [[BetterTogether]] — the meta-optimizer that composes prompt-opt + BFT; [[2407.10930-better-together|Soylu et al. (2024)]] use the simpler [[BootstrapFewShotWithRandomSearch|BFRS]] in their canonical benchmark (this paper precedes MIPROv2's release).
- [[2407.10930-better-together]] — earlier paper in the same Stanford/Khattab DSPy-optimizer line.
- [[HotpotQA]] — the dataset used in the HotPotQA worked receipt.
- [[OPRO]] — the history-based credit-assignment family the paper compares against.
- [[ModuleLevelOPRO]] — multi-stage extension of OPRO; instructions-only baseline.
- [[BootstrapRandomSearch]] — demos-only baseline; sibling to [[BootstrapFewShotWithRandomSearch]].
- [[BootstrapDemonstrations]] — the metric-filtered trace-collection step.
- [[TreeStructuredParzenEstimator]] — the [[BayesianOptimization|Bayesian]] surrogate MIPRO uses.
- [[Optuna]] — the underlying TPE implementation.
- [[LMProgram]] — the multi-stage target $\Phi$.
- [[CreditAssignment]] — the structural problem MIPRO's surrogate solves.
- [[DSPyOptimizerBenchmark]] — the seven-task benchmark MIPRO is evaluated on.

## Non-textual InputFields — `data_aware_proposer=False`

[[dspy-audio-tutorial]] is the **first wiki receipt of the `data_aware_proposer=False` kwarg**. MIPROv2's dataset-summarizer proposer (the *grounding* proposal strategy from the [[2406.11695-mipro|MIPRO paper]]) reads the training set's input fields to inject dataset-aware context into proposed instructions. When any `InputField` is a non-textual primitive — [[DSPyAudio|`dspy.Audio`]], `dspy.Image`, `dspy.Video` — the summarizer cannot consume the data and the kwarg **must be disabled**:

```python
optimizer = dspy.MIPROv2(metric=..., auto="light", prompt_model=gpt_4o_mini)
optimized_program = optimizer.compile(
    spoken_qa, trainset=trainset,
    max_bootstrapped_demos=2, max_labeled_demos=2,
    data_aware_proposer=False,   # required for dspy.Audio InputFields
)
```

The [[dspy-audio-tutorial|tutorial]] also models the cost discipline for audio: *"audio tokens can be costly"* → keep `max_bootstrapped_demos` / `max_labeled_demos` at **0–2** and use `auto="light"`. Same headline-lift ballpark (~10% absolute on Spoken-SQuAD with a `gpt-4o-mini-audio-preview-*` task LM) as the text-task MIPROv2 receipts in the corpus.
- [[KristaOpsahlOng]] / [[MichaelJRyan]] / [[JoshPurtell]] / [[DavidBroman]] / [[ChristopherPotts]] / [[MateiZaharia]] / [[OmarKhattab]] — paper authors.
