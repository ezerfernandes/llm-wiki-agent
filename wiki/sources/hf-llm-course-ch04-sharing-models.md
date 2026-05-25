---
title: "HuggingFace LLM Course — Ch 4: Sharing models and tokenizers"
type: source
tags: [hf-llm-course, course, hub, model-cards, sharing]
date: 2026-05-23
source_file: raw/hf-llm-course/ch04-sharing-models.md
---

## Summary
Chapter 4 of the HuggingFace LLM Course covers the [[HuggingFaceHub]] as the canonical platform for discovering, using, and sharing pretrained models. It walks through loading checkpoints (e.g. `camembert-base`) via `pipeline()` or `Auto*`/`TFAuto*` classes, then details three complementary paths to publish: (1) the high-level `push_to_hub` API integrated into `Trainer`/Keras `PushToHubCallback` and on `model`/`tokenizer` objects, (2) the [[HuggingFaceHubLibrary]] (`create_repo`, `upload_file`, `Repository` class), and (3) the raw [[Git]] + [[GitLFS]] workflow. The chapter closes with a deep treatment of the [[ModelCard]] — README.md with YAML metadata (language, license, datasets) — grounded in Mitchell et al.'s "Model Cards for Model Reporting" paper, and section 5 marks the end of Part 1 of the course.

## Key Claims
- Every Hub repository is a Git repo, enabling versioning and reproducibility; publishing also auto-deploys a hosted Inference API widget.
- The Hub is framework-agnostic (Transformers, Flair, AllenNLP, Asteroid, pyannote, timm) with 10,000+ public models; sharing/usage is free, with paid plans for private hosting.
- `Auto*` / `TFAuto*` classes are preferred over architecture-specific classes (`CamembertForMaskedLM`, `TFCamembertForMaskedLM`) because they are architecture-agnostic and make checkpoint switching trivial.
- A checkpoint must match the task head: loading `camembert-base` into `fill-mask` works; loading it into `text-classification` yields nonsense because the head is wrong.
- Authentication is required for writes — via `notebook_login()` in notebooks or `huggingface-cli login` in a terminal — and the token is cached locally.
- Three creation paths exist: `push_to_hub` API, `huggingface_hub` Python library, and the web interface (`huggingface.co/new`).
- `Trainer` with `push_to_hub=True` in `TrainingArguments` auto-uploads every save and auto-generates a model card with hyperparameters and eval results; `hub_model_id` overrides the repo name and supports `"org/repo"` form.
- Keras users get equivalent behavior via the `PushToHubCallback` passed to `model.fit()`.
- The Hub file system uses Git for regular files and Git-LFS for large files; `.gitattributes` is auto-configured by the web interface to LFS-track extensions like `.bin` and `.h5`.
- `upload_file` is HTTP-POST-based, requires neither git nor git-lfs, but caps individual files at 5 GB.
- The `Repository` class wraps git: `git_pull`, `git_add`, `git_commit`, `git_push`, `git_tag` — the recommended workflow is `git_pull` → `save_pretrained` → `git_add` → `git_commit` → `git_push`.
- [[ModelCard]] sections (per Mitchell et al. 2018): Model description, Intended uses & limitations, How to use, Limitations and bias, Training data, Training procedure, Variable and metrics, Evaluation results.
- Model card YAML frontmatter (`language`, `license`, `datasets`, `tags`, `metrics`) drives Hub filtering and discovery; `camembert-base` example: `language: fr`, `license: mit`, `datasets: [oscar]`.
- Model cards are not required to publish, but documentation directly improves downstream reproducibility, fairness, and reusability.
- Section 5 closes Part 1: users should be able to fine-tune a pretrained model on a text classification task and upload it to the Hub.

## Key Quotes
> "Each of these models is hosted as a Git repository, which allows versioning and reproducibility." — Section 1
> "Sharing a model on the Hub automatically deploys a hosted Inference API for that model." — Section 1
> "The only thing you need to watch out for is that the chosen checkpoint is suitable for the task it's going to be used for." — Section 2
> "We recommend using the `Auto*` classes instead, as these are by design architecture-agnostic." — Section 2
> "When using a pretrained model, make sure to check how it was trained, on which datasets, its limits, and its biases. All of this information should be indicated on its model card." — Section 2 TIP
> "The system to manage files on the Hugging Face Hub is based on git for regular files, and git-lfs (which stands for Git Large File Storage) for larger files." — Section 3
> "A limitation of this approach is that it doesn't handle files that are larger than 5GB in size." — Section 3 (`upload_file`)
> "The model card is a file which is arguably as important as the model and tokenizer files in a model repository." — Section 4
> "Model cards are not a requirement when publishing models... However, explicit documentation of the model can only benefit future users." — Section 4

## Code & Patterns (push_to_hub, Repository, model cards, license fields)

### Loading via pipeline / Auto classes
```py
from transformers import pipeline
camembert_fill_mask = pipeline("fill-mask", model="camembert-base")

from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("camembert-base")
model = AutoModelForMaskedLM.from_pretrained("camembert-base")
```

### Authentication
```python
from huggingface_hub import notebook_login
notebook_login()
```
```bash
huggingface-cli login
```

### Trainer integration
```py
from transformers import TrainingArguments
training_args = TrainingArguments(
    "bert-finetuned-mrpc", save_strategy="epoch", push_to_hub=True
)
# trainer.train()  -> auto-uploads each save; trainer.push_to_hub() finalizes
# Override repo name: hub_model_id="a_different_name" or "my_org/my_repo"
```

### Keras integration
```py
from transformers import PushToHubCallback
callback = PushToHubCallback("bert-finetuned-mrpc", save_strategy="epoch", tokenizer=tokenizer)
# model.fit(..., callbacks=[callback])
```

### Object-level push_to_hub
```py
model.push_to_hub("dummy-model")
tokenizer.push_to_hub("dummy-model")
tokenizer.push_to_hub("dummy-model", organization="huggingface")
tokenizer.push_to_hub("dummy-model", organization="huggingface", use_auth_token="<TOKEN>")
```

### huggingface_hub library — repo management
```python
from huggingface_hub import (
    login, logout, whoami,
    create_repo, delete_repo, update_repo_visibility,
    list_models, list_datasets, list_metrics, list_repo_files,
    upload_file, delete_file,
)
create_repo("dummy-model")
create_repo("dummy-model", organization="huggingface")
# create_repo kwargs: private=True/False, token=..., repo_type="dataset"|"space"
```

### upload_file (HTTP, no git, 5 GB cap)
```py
from huggingface_hub import upload_file
upload_file(
    "<path_to_file>/config.json",
    path_in_repo="config.json",
    repo_id="<namespace>/dummy-model",
)
```

### Repository class workflow
```py
from huggingface_hub import Repository
repo = Repository("<path_to_dummy_folder>", clone_from="<namespace>/dummy-model")
repo.git_pull()
model.save_pretrained("<path_to_dummy_folder>")
tokenizer.save_pretrained("<path_to_dummy_folder>")
repo.git_add()
repo.git_commit("Add model and tokenizer files")
repo.git_push()
# also: repo.git_tag()
```

### Raw git + git-lfs path
```bash
git lfs install
git clone https://huggingface.co/<namespace>/<your-model-id>
# save_pretrained dumps config.json, pytorch_model.bin (~400MB), tokenizer files, sentencepiece.bpe.model
git add .
git status        # confirm files staged
git lfs status    # confirm .bin / .h5 / .bpe.model are LFS-tracked
git commit -m "First model version"
git push          # LFS upload progress shown
```

### Model card YAML metadata (camembert-base example)
```yaml
---
language: fr
license: mit
datasets:
- oscar
---
```
Recognized fields per the [hub-docs modelcard spec](https://github.com/huggingface/hub-docs/blame/main/modelcard.md): `language`, `license`, `tags`, `datasets`, `metrics`, plus structured evaluation results.

### Model card section template
1. Model description (architecture, version, paper, author, copyright)
2. Intended uses & limitations
3. How to use (pipeline / model+tokenizer examples)
4. Limitations and bias
5. Training data
6. Training procedure (preprocessing, epochs, batch size, LR)
7. Variable and metrics
8. Evaluation results (with decision threshold if applicable)

### Reference model cards
- `bert-base-cased`, `gpt2`, `distilbert-base-uncased`

## Connections
- [[HuggingFaceHub]] — central platform; this chapter is the primary how-to for it.
- [[HuggingFaceTransformers]] — provides `pipeline()`, `Auto*` classes, `Trainer.push_to_hub`.
- [[HuggingFaceHubLibrary]] — the `huggingface_hub` Python package backing `push_to_hub` and `Repository`.
- [[ModelCard]] — README.md + YAML metadata; section 4 is essentially a treatise on it.
- [[ModelCardsForModelReporting]] — Mitchell et al. 2018 paper, origin of the model card concept.
- [[MargaretMitchell]] — first author of the model cards paper.
- [[CamemBERT]] — running example checkpoint (`camembert-base`); also the YAML example.
- [[BERT]] — exercise checkpoint (`bert-base-cased`) and reference model card.
- [[GPT2]] — reference model card example.
- [[DistilBERT]] — reference model card example.
- [[Git]] / [[GitLFS]] — storage substrate for Hub repos; LFS for files >a few MB and >5GB pushes.
- [[Trainer]] — `push_to_hub=True` in `TrainingArguments` for automatic uploads.
- [[Keras]] — `PushToHubCallback` for `model.fit()`.
- [[FillMask]] — task used for the camembert demo.
- [[InferenceAPI]] — auto-deployed widget on every public model page.
- [[OscarDataset]] — dataset referenced in the camembert-base model card metadata.
- [[Reproducibility]] — repeatedly cited as the rationale for cards + git versioning.
- [[ResponsibleAI]] / [[ModelBias]] — model cards as the disclosure surface for limitations and bias.
- [[FineTuning]] — prerequisite chapters; section 5 frames sharing as the natural post-fine-tuning step.

## Contradictions
- None apparent vs. prior wiki content. Chapter 4 reinforces the `Auto*` recommendation from Chapter 2 and the `Trainer.push_to_hub` mention from Chapter 3 rather than contradicting them.
- Minor staleness: `use_auth_token` parameter and `organization` kwarg on `push_to_hub` have since been renamed (`token`, `repo_id` namespace prefix) in newer `huggingface_hub` versions; the `Repository` class is now deprecated in favor of `HfApi` / `upload_folder`. Course text reflects the pre-deprecation API.
