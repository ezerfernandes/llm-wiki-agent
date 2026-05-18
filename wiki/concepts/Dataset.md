---
title: "Dataset"
type: concept
tags: [data, training]
sources: []
last_updated: 2026-05-15
---

# Dataset

A collection of examples (rows, images, documents) used for training and evaluation, typically wrapped in a framework abstraction (PyTorch `Dataset`, HuggingFace `datasets.Dataset`). Consumed by a [[DataLoader]] and partitioned via [[DataSplitting]] into train/val/[[HoldoutDataset]] subsets.
