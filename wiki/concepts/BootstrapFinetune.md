---
title: "BootstrapFinetune"
type: concept
tags: [dspy, optimizer, bootstrap, finetune, weights, distillation, teleprompter]
sources: [dspy-optimizers, dspy-optimization-overview, 2407.10930-better-together, 2507.03152-medval, dspy-tutorial-classification-finetuning]
last_updated: 2026-05-24
---

# BootstrapFinetune

> **Anchor paper:** [[2407.10930-better-together|Soylu, Potts & Khattab (2024)]] uses BFT as the `FinetuneWeights` step of the [[BetterTogether]] algorithm (Algorithm 2). The paper's worked instantiation — bootstrap traces → filter by metric → replace optimized prompts with vanilla prompts → train LM via [[lora|LoRA]] (rank 32, alpha 64, lr 1e-5, 5 epochs) — is the canonical implementation reference for `BootstrapFinetune` in compound LM programs.

> **Cross-domain extension paper:** [[2507.03152-medval|Aali et al. (MedVAL, 2026)]] is the **first published clinical-NLP application of `dspy.BootstrapFinetune`** and the source of the **[[QLoRA]] integration** added to DSPy's local PEFT pipeline. Replaces the prompt-bootstrap filter with the [[GeneratorValidatorConsistency|$\mathcal{M}_\mathrm{MedVAL}$ filter]] (a problem-domain-specific consistency metric over synthetic perturbations) and demonstrates that **57% of the data outperforms unfiltered 100%** for distilled clinical validators. The output is [[MedVAL4B|MedVAL-4B]], the best open-source validator on the [[MedVALBench]] benchmark.

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

## The second Banking77 receipt: cross-model open-weights distillation ([[dspy-tutorial-classification-finetuning]])

The [[dspy-tutorial-classification-finetuning|Classification Fine-tuning tutorial]] is the wiki's **first end-to-end runnable receipt of `BootstrapFinetune`** (the [[dspy-optimizers|page 13]] receipt above is narrative). Same dataset ([[Banking77]]), but a **different architecture**:

| Axis | [[dspy-optimizers]] receipt | [[dspy-tutorial-classification-finetuning]] receipt |
|---|---|---|
| Student LM | `openai/gpt-4o-mini-2024-07-18` (API) | `meta-llama/Llama-3.2-1B-Instruct` (local) |
| Teacher LM | (same student fine-tuned on its own traces) | `openai/gpt-4o-mini` (separate API teacher) |
| Distillation regime | **Self-distillation** | **Cross-model distillation** |
| Signature | `"text, hint -> label"` with `Literal[tuple(CLASSES)]` typed-output | `f"text -> label: Literal{CLASSES}"` inline string-form |
| Training-at-runtime trick | **Yes** — `hint=CLASSES[x.label]` as input field at training | **No** — no hint mechanism; metric filter only |
| Trainset size | 2000 examples | 500 examples per stage |
| Baseline → optimized | 66% → 87% (+21 pts) | 51.5% no-metric / 55% teacher → 86.7% (+31.7 pts vs teacher) |
| Inference substrate | OpenAI fine-tuning API | [[SGLang]] local server (`LocalProvider`) |
| Fine-tuning substrate | OpenAI fine-tuning API | [[HuggingFaceTRL|TRL SFTTrainer]] + [[HuggingFacePEFT|PEFT]] |
| `metric` form | `lambda x, y, trace=None: x.label == y.label` | `lambda x, y, trace=None: x.label == y.label` (identical) |
| `dspy.settings.experimental` | not surfaced | **explicitly required** |
| LM lifecycle | (none — API) | `.launch()` / `.kill()` on fine-tuned LM |
| `DSPY_FINETUNEDIR` | not surfaced | **explicit environment knob** for checkpoint/data storage |
| `train_kwargs` surface | not enumerated | full list: `device`, `use_peft`, `num_train_epochs`, `per_device_train_batch_size`, `gradient_accumulation_steps`, `learning_rate`, `max_seq_length`, `packing`, `bf16`, `output_dir` |

**Both receipts converge on ~87% post-BFT within 0.3 points** despite radically different inference and fine-tuning substrates (API vs local 1B). The closeness suggests **BFT's metric-filter mechanism dominates the substrate choice** on closed-set classification: the same `lambda` metric carries enough signal that whether the underlying SFT runs on OpenAI's fine-tuning API or on TRL+PEFT against a 1B Llama, the program-level accuracy ends up nearly identical.

The tutorial also surfaces a **two-stage ablation** the [[dspy-optimizers|page 13]] receipt does not: Stage A (500 *unlabeled* examples, no `metric=` filter) → 51.5%; Stage B (500 *labeled* examples, with `metric=` filter) → 86.7%. The same student LM, same teacher LM, same program, same dataset size — only the metric filter and presence of labels differ. The 35-point lift is the cost of the metric filter alone, isolated.

**Inverted distillation result**: the fine-tuned 1B Llama student (86.7%) beats the GPT-4o-mini teacher (55%) by **+31.7 absolute / +57.6% relative** on the same 100-item devset. First wiki receipt where the student strictly outperforms the teacher rather than compressing the teacher's behavior — the teacher's *traces* (reasoning + answer) plus a metric filter exceed the teacher's *direct accuracy*. This is what the [[dspy-optimizers|page 13]] receipt's *"output may be stronger than the teacher"* claim looks like quantified end-to-end.

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
- [[BootstrapFewShotWithRandomSearch]] — alternative prompt-tuning predecessor; the canonical `OptimizePrompts` partner inside [[BetterTogether]].
- [[BetterTogether]] — the meta-optimizer that schedules BFT between two prompt-opt steps.
- [[2407.10930-better-together]] — the paper that establishes BFT-with-prompt-opt as the dominant strategy for compound LM programs.
- [[LiteLLM]] — the upstream provider-abstraction; BootstrapFinetune reaches provider-specific fine-tuning APIs through [[DSPyLM]] which routes through LiteLLM.
- [[openai|OpenAI]] — the fine-tuning provider in the worked Banking77 receipt (`gpt-4o-mini-2024-07-18`).
- [[KnowledgeDistillation]] — the structural pattern BootstrapFinetune realizes (prompt-based behavior → weight-internalized behavior).
- [[PromptEngineering]] — the manual discipline DSPy's optimizers automate; BootstrapFinetune is the *escape hatch* into the weight-tuning regime.
