---
title: "Made With ML — Utilities"
type: source
tags: [foundations, made-with-ml, deep-learning, training-loop]
date: 2026-05-15
source_file: raw/madewithml/foundations-utilities.md
---

## Summary
Refactoring lesson that consolidates the ad-hoc training code from earlier chapters into reusable PyTorch utilities: a `set_seeds` helper, a `Dataset` / `DataLoader` for batched iteration, device-aware tensor movement (CPU vs CUDA), a `Trainer` class with `train_step` / `eval_step` / `predict_step`, learning-rate scheduling, early stopping on validation loss, and model saving / loading. These utilities then become the standard scaffolding reused by every deep-learning chapter (CNN, embeddings, RNN, attention, transformer).

## Key Claims
- Reproducibility requires seeding NumPy, Python's `random`, PyTorch CPU, and PyTorch CUDA (single- and multi-GPU) — the lesson packages this in a single `set_seeds` function.
- A custom `Dataset` plus a `DataLoader` cleanly separates data representation from batching and shuffling, and supports collate functions for variable-length sequences in later lessons.
- Device handling should be explicit: `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")`, and every input tensor + model is `.to(device)`.
- The `Trainer` class encapsulates the standard loop: forward, loss, zero grads, backward, step, accumulate metrics — and exposes train/eval/predict modes that toggle `model.train()` / `model.eval()` and `torch.inference_mode()`.
- Learning-rate schedulers (e.g. `ReduceLROnPlateau`) adapt the step size based on validation loss, helping convergence without manual tuning per epoch.
- Early stopping monitors validation loss and stops training after a fixed `patience` of non-improving epochs, keeping the best model seen.
- Model checkpoints save `state_dict()` (weights only, not the full Python object) for robust portable reload via `model.load_state_dict(torch.load(path))`.
- These utilities are the contract that downstream lessons rely on — every later architecture plugs into the same `Trainer`.

## Key Quotes
> "We're having to set a lot of seeds for reproducibility now, so let's wrap it all up in a function." — Set up

> Early-stopping loop: `if val_loss < best_val_loss: best_val_loss = val_loss; best_model = self.model; _patience = patience  # reset` — Trainer.train

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — framework
- [[DataLoader]] — batched iteration abstraction
- [[Dataset]] — sample-level data abstraction
- [[Trainer]] — reusable training-loop class introduced here
- [[EarlyStopping]] — validation-loss-based stopping criterion
- [[LearningRateScheduler]] — adaptive learning-rate adjustment
- [[Reproducibility]] — seeding discipline
- [[ModelCheckpoint]] — state-dict save/load pattern
- [[Adam]] — optimizer used by default
- [[CrossEntropyLoss]] — loss used by default
- [[NeuralNetwork]] — what the Trainer trains

## Contradictions
- None identified.
