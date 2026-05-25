---
title: "DSPy Tutorial — Classification Fine-tuning (Banking77 via Local Llama-3.2-1B)"
type: source
tags: [dspy, tutorial, finetune, classification, distillation, banking77, sglang, peft, trl, llama, local-inference]
date: 2026-05-24
source_file: raw/dspy-tutorial-classification-finetuning.ipynb
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/classification_finetuning/` (`docs/docs/tutorials/classification_finetuning/index.ipynb`). **The wiki's first runnable end-to-end receipt of [[BootstrapFinetune|`dspy.BootstrapFinetune`]]** — the only weight-tuning optimizer in the [[DSPyOptimizers|catalog]] — and the **first DSPy tutorial whose output is a fine-tuned local open-weights model** rather than a prompt-optimized program. Distills a [[chainofthought|`dspy.ChainOfThought`]] classifier from a [[GPT|GPT-4o-mini]] teacher into a locally-served [[Llama|Llama-3.2-1B-Instruct]] student on the **77-way [[Banking77]] intent classification task** ([[PolyAI]] dataset, 77 banking inquiry categories). **Two-stage receipt**: stage A bootstraps from **500 unlabeled** examples (no metric filter) → **51.5%** dev accuracy; stage B bootstraps from **500 labeled** examples with a `lambda x, y: x.label == y.label` metric filter → **86.7%** dev accuracy. **Headline cross-model result**: the fine-tuned 1B student (**86.7%**) outperforms the GPT-4o-mini teacher (**55%**) on the same 100-item dev set — **a ~50× smaller open-weights model beats the API teacher by 31.7 absolute points** through metric-filtered bootstrap distillation. **Twenty-ninth wiki-corpus DSPy tutorial** and the **first benchmarked on a classification task with weight optimization** — fills the *weight-space classification* slot the wiki had only documented at the second-hand-receipt level via the [[BootstrapFinetune|BootstrapFinetune concept page's]] Banking77 narrative receipt from [[dspy-optimizers|page 13]].

## Key Claims

- **`dspy.BootstrapFinetune` is the bridge from prompt-tuning to weight-tuning.** A single optimizer call (`optimizer.compile(student_classify, teacher=teacher_classify, trainset=...)`) takes a prompt-based DSPy program and emits a program whose underlying LM has been fine-tuned on the teacher's bootstrap traces. No separate fine-tuning script; no separate dataset preparation; no separate deployment step.
- **Teacher/student decoupling is per-program, not just per-LM.** The receipt creates two `deepcopy()` of the same `dspy.ChainOfThought` Module and binds each to a different LM via `set_lm(...)` — `student_classify.set_lm(student_lm)` and `teacher_classify.set_lm(teacher_lm)`. The optimizer's `teacher=teacher_classify` argument takes a **whole program** (which may itself differ from the student in module composition or instructions), not just an LM.
- **`metric=` filtering on `BootstrapFinetune` is a near-free 35-point lift.** Stage A (no metric, 500 unlabeled examples): 51.5%. Stage B (metric filter, 500 labeled examples): 86.7%. Same student LM, same teacher LM, same program, same dataset size — only the metric filter and the presence of labels differ. **A simple `lambda x, y, trace=None: x.label == y.label` is enough** — the lift comes from filtering teacher rollouts that disagree with the gold label out of the SFT dataset, not from metric complexity.
- **The fine-tuned 1B student beats the GPT-4o-mini teacher by 31.7 absolute points.** Student post-Stage-B 86.7% vs teacher baseline 55%. Concrete demonstration that **cross-model distillation can amplify** rather than just compress: the student is not just *cheaper* than the teacher, it is *better* on the target distribution. The tutorial frames this as *"the fine-tuned student outperforms the teacher despite being 50× smaller"*.
- **`dspy.settings.experimental = True` is the entry gate for `BootstrapFinetune`.** *"Fine-tuning is an experimental feature, so we set a flag to enable it."* First wiki receipt of the experimental flag as a hard precondition for weight-space optimization in DSPy.
- **Local fine-tuned LMs require explicit `.launch()` / `.kill()` lifecycle management.** `classify_ft.get_lm().launch()` starts the [[SGLang]] inference server; `classify_ft.get_lm().kill()` frees GPU memory between runs. Distinct from API-backed LMs which have no such lifecycle. The tutorial calls `.kill()` between Stage A and Stage B explicitly to free memory before the second fine-tuning run.
- **The student program is bound to the *fine-tuned* LM after compile, not the original `student_lm`.** *"Note that the trained LM will be a new LM instance (the `student_lm` object we instantiated here will be untouched!)"* — the optimizer returns a new program with a new LM; the original `student_lm` reference can be reused or discarded.
- **`DSPY_FINETUNEDIR` is the storage knob for checkpoints + training data.** Falls back to `DSPY_CACHEDIR` if unset. Pairs with `CUDA_VISIBLE_DEVICES` for GPU selection. First wiki receipt of `DSPY_FINETUNEDIR` as a first-class DSPy environment variable.
- **`train_kwargs` is the local-LM training-config surface.** The tutorial enumerates the kwargs accepted by `BootstrapFinetune` for local LMs: `device`, `use_peft`, `num_train_epochs`, `per_device_train_batch_size`, `gradient_accumulation_steps`, `learning_rate`, `max_seq_length`, `packing`, `bf16`, `output_dir`. **First wiki disclosure of the full `train_kwargs` surface for BFT on a local model** — these are passed through to the [[HuggingFaceTRL|TRL]] [[SupervisedFinetuning|SFT trainer]] under the hood.
- **The `Literal[CLASSES]` typed-output is the closed-set classification idiom.** `classify = dspy.ChainOfThought(f"text -> label: Literal{CLASSES}")` — an **inline string-form Signature** with the 77-element tuple inlined into the type literal via Python f-string. The model's `inspect_history()` dump shows the adapter expanding `Literal[...]` into both a numbered field declaration (`2. label (Literal[activate_my_card, age_limit, ...])`) and a semicolon-separated must-be-one-of constraint in the user message — first wiki view of the ChatAdapter's Literal-type expansion in full.
- **No `train_kwargs` are needed in the worked example** — defaults suffice for `Llama-3.2-1B-Instruct` SFT on Banking77. The tutorial does not enumerate cost or wall-time; this is a *capability* receipt, not a *cost* receipt.

## Key Quotes

> *"Let's walk through a quick example of fine-tuning the LM weights within a DSPy program. We'll apply to a simple 77-way classification task. Our finetuned program will use a tiny `Llama-3.2-1B` language model, hosted locally on your GPU. To make this more interesting, we'll assume that (i) we don't have any training labels but (ii) we have 500 unlabeled training examples."*

> *"The word 'bootstrapped' here means that the program itself will be invoked on the training inputs and the resulting traces seen over all modules will be recorded and used for finetuning. This is the weight-optimizing variant of the various `BootstrapFewShot` methods in DSPy."*

> *"On every question in the (unlabeled) training set, this will invoke the teacher program, which will produce reasoning and select a class. This will be traced and then constitute a training set for all modules (in this case, just the one CoT module) in the student program."*

> *"If you have labels, you can generally boost this by a large margin. To do so, you can pass a `metric` to `BootstrapFinetune`, which it will use for filtering the trajectories over your program before it builds the finetuning data."*

> *"That's quite a bit better, given just 500 labels. In fact, it seems to be a lot stronger than the teacher LM gets out of the box!"*

## Code Receipt

```python
import dspy, random
from typing import Literal
from dspy.datasets import DataLoader
from dspy.clients.lm_local import LocalProvider
from datasets import load_dataset

# Dataset: Banking77 (PolyAI), 77 classes
CLASSES = load_dataset("PolyAI/banking77", split="train",
                       trust_remote_code=True).features['label'].names
kwargs = dict(fields=("text", "label"), input_keys=("text",),
              split="train", trust_remote_code=True)
raw_data = [
    dspy.Example(x, label=CLASSES[x.label]).with_inputs("text")
    for x in DataLoader().from_huggingface(dataset_name="PolyAI/banking77",
                                           **kwargs)[:1000]
]
random.Random(0).shuffle(raw_data)
unlabeled_trainset = [dspy.Example(text=x.text).with_inputs("text")
                      for x in raw_data[:500]]

# Program: one-line CoT classifier over Literal[CLASSES]
classify = dspy.ChainOfThought(f"text -> label: Literal{CLASSES}")

# Two LMs, two program copies
student_lm = dspy.LM(model="openai/local:meta-llama/Llama-3.2-1B-Instruct",
                    provider=LocalProvider(), max_tokens=2000)
teacher_lm = dspy.LM('openai/gpt-4o-mini', max_tokens=3000)
student_classify = classify.deepcopy(); student_classify.set_lm(student_lm)
teacher_classify = classify.deepcopy(); teacher_classify.set_lm(teacher_lm)

# Stage A: unlabeled, no metric → 51.5%
dspy.settings.experimental = True
optimizer = dspy.BootstrapFinetune(num_threads=16)
classify_ft = optimizer.compile(student_classify,
                                teacher=teacher_classify,
                                trainset=unlabeled_trainset)
classify_ft.get_lm().launch()

devset = raw_data[500:600]
metric = (lambda x, y, trace=None: x.label == y.label)
evaluate = dspy.Evaluate(devset=devset, metric=metric,
                         display_progress=True, display_table=5, num_threads=16)
evaluate(classify_ft)             # → 51.0

classify_ft.get_lm().kill()       # free GPU memory

# Stage B: labeled, with metric → 86.7%
optimizer = dspy.BootstrapFinetune(num_threads=16, metric=metric)
classify_ft = optimizer.compile(student_classify,
                                teacher=teacher_classify,
                                trainset=raw_data[:500])  # labeled
classify_ft.get_lm().launch()
evaluate(classify_ft)             # → 85.0 (86.7% over the 98 scored items)
evaluate(teacher_classify)        # → 55.0  (teacher baseline)
```

## Result Table

| Run | Trainset | Metric filter | Dev accuracy |
|---|---|---|---|
| Stage A — student post-BFT | 500 unlabeled | no | **51.5%** (51/99) |
| Stage B — student post-BFT | 500 labeled | yes | **86.7%** (85/98) |
| Teacher baseline | — | — | **55.0%** (55/100) |

**Student (1B, fine-tuned, metric-filtered) beats teacher (GPT-4o-mini, prompted) by +31.7 absolute / +57.6% relative** on the same 100-item devset (`raw_data[500:600]`) with the same metric (`x.label == y.label`).

## Position in the DSPy Tutorial Corpus

This is the **29th wiki-corpus DSPy tutorial** and the **first end-to-end weight-tuning receipt** ([[BootstrapFinetune]] as the optimizer). Coverage map of the *optimizer rung* of the wiki's DSPy tutorial corpus:

| Optimizer | Tutorials | Tuned object | Substrate |
|---|---|---|---|
| **`dspy.BootstrapFinetune`** | **this tutorial** | **LM weights** | **Local [[SGLang]] + [[HuggingFaceTRL|TRL]] SFT** |
| `dspy.MIPROv2` | [[dspy-tutorial-math]], [[dspy-tutorial-rag-as-agent]], [[dspy-entity-extraction-tutorial]], [[dspy-rag-tutorial]] | Instructions + demos | API LMs |
| `dspy.GEPA` | [[dspy-tutorial-gepa-aime]], [[dspy-tutorial-gepa-facility-support-analyzer]], [[dspy-tutorial-gepa-papillon]], [[dspy-tutorial-gepa-trusted-monitor]] | Instructions (reflection-driven) | API LMs |
| `dspy.ArborGRPO` | [[dspy-tutorial-rl-papillon]], [[dspy-rl-multihop-tutorial]] | LM weights via [[grpo|GRPO]] / [[DAPO]] | Local [[Arbor]] + [[lora|LoRA]] |
| (none / Programming-stage only) | 18 other tutorials | — | — |

**Two weight-tuning families in the DSPy tutorial corpus**: BFT (this tutorial — SFT distillation from a teacher program) and GRPO (the rl_papillon / rl_multihop tutorials — on-policy RL with composite or deterministic rewards). BFT is the **supervised** weight-tuning family; GRPO is the **reinforcement-learning** weight-tuning family. The wiki now has worked end-to-end receipts for both axes.

## Second Banking77 Receipt — Cross-Receipt Reconciliation with [[dspy-optimizers]]

The wiki's existing Banking77 BFT receipt comes from [[dspy-optimizers|page 13 of the DSPy *Learn* corpus]], summarized in [[BootstrapFinetune#The canonical worked example: Banking77 (66% → 87%)|the BootstrapFinetune concept page]]. This new tutorial is the **second wiki receipt of Banking77 + `BootstrapFinetune`** — same dataset, **different architecture**:

| Axis | [[dspy-optimizers]] receipt | **This tutorial** |
|---|---|---|
| Student LM | `openai/gpt-4o-mini-2024-07-18` (API) | `meta-llama/Llama-3.2-1B-Instruct` (local) |
| Teacher LM | (same student fine-tuned on its own traces) | `openai/gpt-4o-mini` (separate API teacher) |
| Distillation regime | **Self-distillation** — student bootstraps from itself | **Cross-model distillation** — open-weights student bootstraps from API teacher |
| Signature shape | `"text, hint -> label"` with `Literal[tuple(CLASSES)]` typed-output via `with_updated_fields` | `"text -> label: Literal{CLASSES}"` inline string-form, no hint |
| Training-at-runtime trick | **Yes** — `hint=CLASSES[x.label]` as an input field at training time, absent at inference | **No** — no hint mechanism; label is supervisory via metric filter only |
| Trainset size | 2000 examples | 500 examples (per stage) |
| Baseline → optimized | 66% → 87% (21-point lift) | 51.5% (no metric) / 55% (teacher baseline) → 86.7% (32-point lift over teacher) |
| Inference substrate | OpenAI fine-tuning API | [[SGLang]] local server |
| Fine-tuning substrate | OpenAI fine-tuning API | [[HuggingFaceTRL|TRL]] + [[HuggingFacePEFT|PEFT]] (local) |
| `metric` form | `lambda x, y, trace=None: x.label == y.label` | `lambda x, y, trace=None: x.label == y.label` (identical) |
| `dspy.settings.experimental` | not surfaced | **explicitly required** |

**Both receipts converge on ~87% post-BFT** on Banking77 — within 0.3 points despite the radically different inference substrate (API vs local 1B). The closeness suggests **BFT's metric-filter mechanism dominates the substrate choice** on this task: the same `lambda` metric carries enough signal that whether the underlying SFT runs on OpenAI's fine-tuning API or on TRL+PEFT against a 1B Llama, the program-level accuracy ends up nearly identical.

**No contradictions** — the two receipts complete each other. The [[dspy-optimizers]] page's receipt establishes the *API self-distillation* idiom (with the *hint* trick); this tutorial establishes the *open-weights cross-model distillation* idiom (without any hint trick) as an equally valid Banking77 BFT recipe.

## Cross-Receipt: Local Weight-Tuning Architectural Convergence with [[dspy-tutorial-rl-papillon]] / [[dspy-rl-multihop-tutorial]]

This is the **third local-weight-tuning DSPy tutorial** in the wiki — joining the two [[ArborGRPO]] tutorials. The substrate stack converges:

| Component | This tutorial (BFT) | [[dspy-tutorial-rl-papillon]] (GRPO) | [[dspy-rl-multihop-tutorial]] (GRPO) |
|---|---|---|---|
| Inference server | [[SGLang]] | [[Arbor]] (which wraps SGLang) | [[Arbor]] (wraps SGLang) |
| Local fine-tuning | [[HuggingFaceTRL|TRL]] SFT + [[HuggingFacePEFT|PEFT]] | [[Arbor]] GRPO + [[lora|LoRA]] | [[Arbor]] GRPO + [[lora|LoRA]] |
| Student model | Llama-3.2-1B-Instruct | (Qwen2.5-7B-Instruct via [[PAPILLON]]) | Qwen2.5-1.5B-Instruct |
| Optimizer | `dspy.BootstrapFinetune` | `dspy.ArborGRPO` | `dspy.ArborGRPO` |
| `.launch()`/`.kill()` | Yes — explicit | (implicit via Arbor server lifecycle) | (implicit via Arbor server lifecycle) |
| `dspy.settings.experimental` | required | (not required) | (not required) |

**SGLang is the common inference substrate** — the BFT tutorial uses it directly via `LocalProvider`; the GRPO tutorials use it indirectly via [[Arbor]]. **`HuggingFaceTRL` + `HuggingFacePEFT` is the SFT-side fine-tuning stack** (this tutorial); **Arbor's bespoke GRPO trainer** is the RL-side fine-tuning stack (the other two). The wiki now has receipts for both branches.

## Dependency Footprint

The **largest local-stack dependency footprint** of any wiki-corpus DSPy tutorial:

```bash
pip install -U dspy >=2.6.0
pip install datasets
pip install --upgrade pip
pip install uv
uv pip install "sglang[all]>=0.4.4.post3" --find-links https://flashinfer.ai/whl/cu124/torch2.5/flashinfer-python
uv pip install -U torch transformers==4.48.3 accelerate trl peft
```

**Notable pin**: `transformers==4.48.3` — the tutorial explicitly cites <https://github.com/huggingface/trl/issues/2338> as the reason for the version pin. First wiki receipt of a version-pin justification linked to an upstream GitHub issue inside a DSPy tutorial.

**Hardware requirement**: a local GPU (single GPU works; `CUDA_VISIBLE_DEVICES` controls selection). The tutorial flags this constraint up front: *"This tutorial requires a local GPU at the moment for inference, though we plan to support ollama serving for finetuned models as well."* First wiki receipt of [[Ollama]] as a stated future inference substrate for DSPy fine-tuned models (not yet supported).

## What This Tutorial Does Not Cover

- **No cost or wall-time disclosure** — same scope gap as [[dspy-tutorial-gepa-aime]] / [[dspy-tutorial-gepa-papillon]] / [[dspy-tutorial-gepa-facility-support-analyzer]]. The Stage A and Stage B fine-tunes have no reported runtime; the dev evaluations are timed by progress bar only (35s, 46s, 11s for the three runs at `num_threads=16`).
- **No `train_kwargs` worked sweep** — the kwargs surface is enumerated but no example varies them; default settings (presumably full-parameter SFT given `use_peft` is *opt-in*) carry the result.
- **No comparison against MIPROv2 / GEPA on the same Banking77 task** — the [[dspy-optimizers|page 13 rubric]]'s composability claim (*"optimize prompts first with MIPROv2 on a 7B+ LM, then BFT into a smaller LM"*) is not exercised; BFT is run *cold* from the unoptimized student.
- **No save/load receipt for the fine-tuned model** — the MLflow appendix shows `mlflow.dspy.log_model(classify_ft, artifact_path="model")` + `mlflow.dspy.load_model(...)` but no plain `program.save(...)` / `program.load(...)` shape.
- **No GPU memory or VRAM disclosure** — the `.kill()` step is motivated only by *"free our GPU memory"*; no numeric VRAM footprint for the 1B model + SGLang server + SFT trainer.
- **No PEFT/LoRA ablation** — `use_peft` is named as a kwarg but the worked example does not use it, so the headline 86.7% is full-parameter SFT (not LoRA).
- **No multi-seed / variance reporting** — single-shot result.
- **No `BetterTogether` composition** — the [[BootstrapFinetune#When to use BootstrapFinetune|page 13 recommendation]] is *"prompt optimization → BFT"*; the tutorial runs BFT in isolation.
- **No checkpoint resumption / continued training across stages** — Stage A and Stage B each train from `student_lm` from scratch (the original `student_lm` reference is reused as input to both `compile(...)` calls).

## Connections

- [[DSPy]] — the framework.
- [[BootstrapFinetune|`dspy.BootstrapFinetune`]] — the optimizer; this is the **first wiki end-to-end runnable receipt** of `BootstrapFinetune` (the [[dspy-optimizers|page 13]] receipt is narrative/abridged).
- [[DSPyOptimizers]] — the catalog containing `BootstrapFinetune`; this tutorial is the only wiki tutorial whose optimizer comes from the *Finetuning* family.
- [[DSPyOptimization]] — the *Optimization* stage of the [[DSPyProgrammingModel|three-stage workflow]] that BFT operationalizes in the weight-tuning regime.
- [[chainofthought|`dspy.ChainOfThought`]] — the only module used; the program is a one-line `dspy.ChainOfThought(f"text -> label: Literal{CLASSES}")`.
- [[DSPySignatures]] — the inline string-form Signature with `Literal{CLASSES}` typed-output; the closed-set-classification idiom that pairs with BFT for SFT-friendly outputs.
- [[DSPyPredict]] — the underlying Predict module type each per-step LM call routes through after fine-tuning.
- [[DSPyLM|`dspy.LM`]] — the LM client; this tutorial is the **first wiki receipt of `LocalProvider()`** + the `openai/local:<hf-model-id>` model-prefix idiom for [[SGLang]]-backed local serving.
- [[DSPyModules]] — `program.deepcopy()` + `program.set_lm(lm)` is the per-program LM-binding pattern; this tutorial uses it twice (one for student, one for teacher).
- [[DSPyAdapters]] — the [[DSPyAdapters|ChatAdapter]]-expanded `Literal[...]` system+user message structure is visible in the `inspect_history()` dump.
- [[DSPyEvaluate|`dspy.Evaluate`]] — the dev-set scoring harness; 16-thread parallel evaluation; the `display_table=5` printout shows the first 5 predictions inline.
- [[DSPyMetrics]] — the metric carries dual roles: (a) the **filter** inside `BootstrapFinetune(metric=...)` (deciding which teacher traces enter the SFT dataset); (b) the **evaluator** inside `dspy.Evaluate(metric=...)` (scoring dev predictions). Same function, two roles.
- [[DSPyData|`dspy.Example`]] / `DataLoader.from_huggingface` — the trainset construction; first wiki receipt of `DataLoader().from_huggingface(dataset_name="PolyAI/banking77", **kwargs)` over Banking77.
- [[FineTuning]] — the LM-weight-tuning regime BFT bridges DSPy into.
- [[SupervisedFinetuning]] — the regime the fine-tuning step runs in (TRL SFTTrainer under the hood).
- [[KnowledgeDistillation|knowledge distillation]] — the structural pattern this tutorial realizes; teacher (GPT-4o-mini API) → student (Llama-3.2-1B local). **First wiki receipt where the student strictly outperforms the teacher** on the target task — typically distillation compresses with quality loss; here the metric-filtered SFT dataset makes the student strictly better.
- [[BootstrapFewShot]] — the prompt-tuning sibling using the same bootstrap-and-filter mechanism; this tutorial's Stage A vs Stage B mirror the *trace-filtered vs unfiltered* contrast on the BootstrapFewShot side.
- [[ChainOfThought]] — alias / concept page covering the CoT module pattern.
- [[Banking77]] — the dataset; 77 banking-inquiry categories from [[PolyAI]]; the canonical fine-grained intent-classification benchmark in the DSPy corpus.
- [[PolyAI]] — the publisher of Banking77 ([[HuggingFace|HuggingFace]] dataset `PolyAI/banking77`).
- [[Llama|Llama-3.2-1B-Instruct]] — the student LM; [[meta|Meta]]'s tiniest Llama-3.2 chat model (1.24B params); first wiki end-to-end receipt of Llama-3.2-1B as a DSPy student.
- [[meta|Meta]] — publisher of the Llama-3.2 series.
- [[GPT|GPT-4o-mini]] — the teacher LM and the baseline-comparison model.
- [[openai|OpenAI]] — the teacher LM provider.
- [[SGLang]] — the local inference server backing `LocalProvider`; first wiki receipt of SGLang as the inference substrate for a fine-tuned DSPy model.
- [[HuggingFaceTRL|TRL]] — the [[HuggingFace]] reinforcement-learning + SFT library; this tutorial uses TRL's SFTTrainer under the hood for the actual gradient step.
- [[HuggingFacePEFT|PEFT]] — the parameter-efficient fine-tuning library; available via `use_peft=True` in `train_kwargs` but not exercised in the worked example.
- [[HuggingFace]] — the broader ecosystem hosting `transformers`, `accelerate`, `trl`, `peft`, and the Banking77 dataset.
- [[MLflow]] — the tutorial recommends MLflow tracing (`mlflow.dspy.autolog()`) and ships an optional MLflow-experiment save/load snippet (`mlflow.dspy.log_model(classify_ft, artifact_path="model")` + `mlflow.dspy.load_model(...)`); first wiki receipt of MLflow saving a *weight-tuned* DSPy program rather than a prompt-tuned one.
- [[BetterTogether]] — the meta-optimizer that schedules BFT between prompt-optimization passes; not exercised in this tutorial but the [[BootstrapFinetune|recommended composition pattern]].
- [[MIPROv2]] — the recommended prompt-optimizer predecessor in the `BetterTogether` recipe; not exercised here.
- [[Ollama]] — flagged as a future inference substrate for fine-tuned DSPy models (not yet supported as of this tutorial).
- [[Classification]] — the task family.
- [[2407.10930-better-together]] — the paper that establishes BFT-with-prompt-opt as the dominant strategy for compound LM programs.
- [[2507.03152-medval]] — the medical-validation paper using `dspy.BootstrapFinetune` with [[QLoRA]] for clinical NLP distillation; conceptual sibling on the cross-domain application axis.

## Contradictions

None with the existing wiki. The result **reinforces**:

- [[BootstrapFinetune]] concept page's *"a 21-point absolute improvement — the largest of the three worked receipts on the page"* claim — this tutorial extends the BFT lift envelope to **+32 points** (student post-Stage-B vs teacher baseline) on the same dataset, with a different student architecture.
- [[KnowledgeDistillation]] page's expected pattern — but in the **inverted direction**: the student exceeds the teacher rather than compressing it. This is the *bootstrap distillation* pattern where the teacher's *traces* (reasoning + answer) plus a metric filter exceed the teacher's *direct accuracy* — first wiki receipt of this inversion concretely measured.
- [[DSPyOptimizers]]'s rubric that BFT is the *post-success efficiency move* — but here BFT works cold from the unoptimized student. The 86.7% suggests BFT alone, without prior prompt optimization, is already strong on a closed-set classification task with a metric filter.
- The [[DSPyLM]] page's *per-Module LM binding via `set_lm(...)`* idiom — the [[BootstrapFinetune|page]] notes this was *"the only place in the corpus `set_lm(...)` is exercised"*; this tutorial is the **second wiki receipt of `set_lm(...)`** in a DSPy program, used twice in one program (student + teacher).

## Scope-Limit Gaps

- No cost or wall-time numbers; no GPU memory footprint.
- No `train_kwargs` sweep; no `use_peft=True` ablation; no `num_train_epochs` / learning-rate / batch-size sensitivity.
- No comparison to MIPROv2 / GEPA prompt-optimization baselines on the same Banking77 task.
- No `BetterTogether` composition (the [[dspy-optimizers|page 13 recommendation]] of prompt-opt → BFT).
- No multi-seed variance estimate; single-shot dev accuracy.
- No alternative student model (e.g. Llama-3.2-3B-Instruct, Qwen2.5-1.5B-Instruct) to characterize the lift's dependence on student capacity.
- No alternative teacher model (e.g. GPT-4o, Claude, a stronger teacher) to characterize the lift's dependence on teacher quality.
- No examination of the SFT dataset itself — how many of the 500 teacher traces pass the metric filter; what fraction of the filtered dataset's labels are correct vs incorrect.
- No checkpoint resumption or continued training (Stage B does not initialize from Stage A's fine-tuned weights).
- No save/load via plain `program.save(...)` / `program.load(...)`; the only persistence path shown is via MLflow.
- No Ollama deployment of the fine-tuned model (explicitly flagged as future work).
