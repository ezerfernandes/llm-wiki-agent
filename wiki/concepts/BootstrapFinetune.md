---
title: "BootstrapFinetune"
type: concept
tags: [dspy, optimizer, bootstrap, finetune, weights, distillation, teleprompter]
sources: [dspy-optimizers, dspy-optimization-overview]
last_updated: 2026-05-17
---

# BootstrapFinetune

**`dspy.BootstrapFinetune`** is the **only weight-tuning optimizer** in [[DSPy]]'s [[DSPyOptimizers|catalog]] — the bridge between DSPy's prompt-tuning regime (every other optimizer) and the underlying LM's [[FineTuning|fine-tuning]] regime. It **distills a prompt-based DSPy program into weight updates**, producing a program whose steps are the same but whose per-step LM is now a fine-tuned model instead of a prompted one.

The canonical source is [[dspy-optimizers|page 13 of the DSPy *Learn* corpus]].

## Mechanism

[[dspy-optimizers|The page]]'s definition:

> *"Distills a prompt-based DSPy program into weight updates. The output is a DSPy program that has the same steps, but where each step is conducted by a finetuned model instead of a prompted LM."*

The two-step mechanism:

1. **Bootstrap traces, metric-filter** — structurally identical to [[BootstrapFewShot]]'s collection step. Run the program on training inputs; collect per-module traces; filter by the [[DSPyMetrics|metric]] in `trace is not None` mode; keep only traces that pass.

2. **Fine-tune the LM on the filtered traces.** The metric-passing traces become a **supervised fine-tuning dataset** for the underlying LM. The result is a fine-tuned model that has internalized the program's prompt-driven behavior into its weights.

The output is a [[DSPyModules|`dspy.Module`]] of the same class as the input, but each per-step LM call now routes to the fine-tuned model rather than the original prompted one.

## Parameters

| Parameter | Type | Default | Role |
|---|---|---|---|
| `metric` | callable | required | Validates bootstrapped traces in `trace is not None` mode; only metric-passing traces enter the fine-tuning dataset. |
| `num_threads` | int | (default) | Parallelism for evaluation. |

The [[dspy-optimizers|page]]'s worked Banking77 receipt uses a simple lambda metric (`lambda x, y, trace=None: x.label == y.label`) — the simplest possible metric form, demonstrating that BootstrapFinetune doesn't require a complex metric.

## The canonical worked example: Banking77 (66% → 87%)

[[dspy-optimizers|The page]]'s third worked end-to-end receipt — **the only weight-tuning receipt in the corpus**:

```python
import dspy
from typing import Literal

lm = dspy.LM('openai/gpt-4o-mini-2024-07-18')

# Define the DSPy module for classification. It will use the hint at training time, if available.
signature = dspy.Signature("text, hint -> label").with_updated_fields('label', type_=Literal[tuple(CLASSES)])
classify = dspy.ChainOfThought(signature)
classify.set_lm(lm)

# Optimize via BootstrapFinetune.
optimizer = dspy.BootstrapFinetune(metric=(lambda x, y, trace=None: x.label == y.label), num_threads=24)
optimized = optimizer.compile(classify, trainset=trainset)
optimized(text="What does a pending cash withdrawal mean?")
```

Setup: PolyAI Banking77 dataset (2000 examples, 77 classes); [[ChainOfThought|`dspy.ChainOfThought`]] over a `Literal[tuple(CLASSES)]`-typed [[DSPySignatures|Signature]] (a closed-set-classification idiom); per-Module LM binding via `classify.set_lm(lm)` (the **only place in the corpus** `set_lm(...)` is exercised); a simple lambda metric.

> *"An informal run similar to this on DSPy 2.5.29 raises GPT-4o-mini's score 66% to 87%."*

A **21-point absolute improvement** — the largest of the three worked receipts on the page, and a concrete demonstration that weight-tuning the LM can outperform prompt-tuning when sufficient data (2000 examples) is available.

## The training-at-runtime trick

The Banking77 example includes a subtle data-preparation move:

```python
trainset = [
    dspy.Example(x, hint=CLASSES[x.label], label=CLASSES[x.label]).with_inputs("text", "hint")
    for x in DataLoader().from_huggingface(dataset_name="PolyAI/banking77", **kwargs)[:2000]
]
```

The `hint` field is **the ground-truth label, attached as an input** for the training run. The [[DSPySignatures|Signature]] is `"text, hint -> label"` — so during training the program receives the answer as a hint and learns to **produce the label conditioned on the hint**. At inference time, no hint is provided, and the fine-tuned model is expected to produce the label from `text` alone — having learned the *text-to-label* mapping despite the hint being supervisory signal during fine-tuning.

This is a **distillation-style trick** — the hint provides strong supervision during fine-tuning that the model internalizes; the resulting fine-tuned weights produce the label even when the hint is absent at inference time.

## When to use BootstrapFinetune

[[dspy-optimizers|The page]]'s five-rule rubric makes BootstrapFinetune the **post-success efficiency move**:

> *"If you have been able to use one of these with a large LM (e.g., 7B parameters or above) and need a very **efficient program**, finetune a small LM for your task with `BootstrapFinetune`."*

The recommended workflow:

1. First optimize the program's **prompts** with [[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]] / [[MIPROv2]] using a **large LM** (7B+).
2. Once the prompt-optimized program **works well** on the large LM, use BootstrapFinetune to **distill** the behavior into a smaller LM via fine-tuning.
3. Deploy the fine-tuned small LM for inference efficiency.

This is the **composability** claim ([[DSPyOptimizers|operationalized via]] `dspy.BetterTogether`) realized as a concrete two-step recipe: prompt optimization → weight optimization. The [[dspy-optimizers|page]]'s composability example names exactly this sequence: *"You can run `dspy.MIPROv2` and use the produced program ... to `dspy.BootstrapFinetune` to get better results. This is partly the essence of `dspy.BetterTogether`."*

## Position in the catalog

| Family | Optimizers | What's tuned |
|---|---|---|
| Few-Shot | `LabeledFewShot`, [[BootstrapFewShot]], [[BootstrapFewShotWithRandomSearch]], `KNNFewShot` | Demonstrations |
| Instruction | `COPRO`, [[MIPROv2]], `SIMBA`, [[GEPA]] | Instructions |
| **Finetuning** | **`BootstrapFinetune`** (this page) | **LM weights** |
| Program Transformation | `Ensemble` | Composition |
| Meta-Optimizer | `BetterTogether` | Sequence of optimizers |

**BootstrapFinetune is the only entry in the Finetuning family.** Every other optimizer tunes the *prompts* (instructions, demos); BootstrapFinetune tunes the *underlying model*. This is what makes DSPy a **both-axes** optimization framework — the third portability claim of [[DSPyProgrammingModel|the Programming Model]] (*"run prompt-optimization or weight fine-tuning against the same program"*) is realized in this single optimizer.

## Implications for the 20/80 train/val split

[[dspy-optimization-overview|The Optimization Overview]]'s inverted 20/80 train/val split is recommended for *most prompt optimizers* because *"prompt optimizers tend to overfit on small training sets."* BootstrapFinetune is **not** a prompt optimizer — it tunes weights — so the rationale (small prompt-search space → easy memorization) **doesn't apply** in the same way. The page doesn't explicitly carve BootstrapFinetune out of the 20/80 recommendation, but the rationale leaves it implicit: weight-tuning's conventional ML data hygiene (80/20 train/val, 2000+ examples) is the regime BootstrapFinetune naturally operates in.

## Connections

- [[DSPy]] — the framework.
- [[DSPyOptimizers]] — the catalog this optimizer belongs to.
- [[DSPyOptimization]] — the workflow this optimizer operationalizes.
- [[dspy-optimizers]] — the canonical source page; ships the only weight-tuning worked receipt in the corpus.
- [[FineTuning]] — the LM-weight-tuning regime BootstrapFinetune bridges DSPy into; the *"or weights"* half of the [[DSPyOptimization|three-input contract]]'s *"tune the prompts or weights"* commitment.
- [[DSPyMetrics]] — the dual-purpose `trace` argument's `trace is not None` branch is what the demo-validation step uses to filter the fine-tuning dataset.
- [[DSPyLM]] — the LM client; this is the only optimizer that targets the LM's **weights**. The Banking77 receipt's `classify.set_lm(lm)` is the only `set_lm(...)` exercise in the entire *Learn* corpus.
- [[DSPyModules]] / [[DSPyPredict]] — the program input/output type; each per-step LM call routes to the fine-tuned model after compilation.
- [[DSPySignatures]] — the stable interface; the `text, hint -> label` Banking77 Signature uses `Literal[tuple(CLASSES)]` typed-output (the closed-set-classification idiom from [[dspy-signatures]]).
- [[DSPyData]] / [[DSPyExample]] — the training set primitive; BootstrapFinetune typically benefits from larger datasets (2000+ examples in the worked receipt).
- [[ChainOfThought]] — the Module used in the Banking77 worked receipt.
- [[BootstrapFewShot]] — the prompt-tuning sibling using the same bootstrap-and-filter mechanism.
- [[MIPROv2]] — the recommended prompt optimizer to run **before** BootstrapFinetune (the prompt → weight composition pattern).
- [[BootstrapFewShotWithRandomSearch]] — alternative prompt-tuning predecessor.
- [[LiteLLM]] — the upstream provider-abstraction; BootstrapFinetune reaches provider-specific fine-tuning APIs through [[DSPyLM]] which routes through LiteLLM.
- [[openai|OpenAI]] — the fine-tuning provider in the worked Banking77 receipt (`gpt-4o-mini-2024-07-18`).
- [[KnowledgeDistillation]] — the structural pattern BootstrapFinetune realizes (prompt-based behavior → weight-internalized behavior).
- [[PromptEngineering]] — the manual discipline DSPy's optimizers automate; BootstrapFinetune is the *escape hatch* into the weight-tuning regime.
