---
title: "PyTorch Lightning"
type: entity
tags: [framework, training, pytorch]
sources: [d2l-linear-regression]
last_updated: 2026-05-16
---

# PyTorch Lightning

Open-source training framework built on [[PyTorch]] (Lightning AI; pytorchlightning.ai). Wraps the PyTorch training loop into three concerns — `LightningModule` (model + loss + optimizer config), `LightningDataModule` (data loaders), and `Trainer` (orchestration, GPUs, callbacks, logging). Eliminates boilerplate and standardizes distributed training, mixed-precision, checkpointing, and experiment logging.

## Why it matters to this wiki

[[d2l-preface|D2L]]'s [[ObjectOrientedDesign|OO]] scaffold ([[d2l-linear-regression]] §3.2) is **explicitly inspired by PyTorch Lightning**: D2L's [[Module]] / [[DataModule]] / [[Trainer]] map directly onto Lightning's namesake classes. Every D2L architecture from linear regression onward uses this trio.

## Connections

- [[d2l-linear-regression]] — names PyTorch Lightning as the inspiration for D2L's OO design.
- [[PyTorch]] — the underlying framework.
- [[Module]] / [[DataModule]] / [[Trainer]] — D2L's Lightning-shaped classes.
