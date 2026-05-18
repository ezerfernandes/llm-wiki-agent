---
title: "DataModule"
type: concept
tags: [training, framework, d2l]
sources: [d2l-linear-regression]
last_updated: 2026-05-16
---

# DataModule (D2L)

Base class for **datasets** in the [[d2l-preface|D2L]] [[ObjectOrientedDesign|OO]] scaffold ([[d2l-linear-regression]] §3.2). Encapsulates dataset download, preprocessing, and the `train_dataloader()` / `val_dataloader()` generators that yield minibatches into a [[Module]]'s `training_step` / `validation_step`. Inspired by [[PyTorchLightning|PyTorch Lightning]]'s `LightningDataModule`.

## Minimal API

```python
class DataModule(d2l.HyperParameters):
    def __init__(self, root='../data', num_workers=4):
        self.save_hyperparameters()
    def get_dataloader(self, train):   # subclass overrides this
        raise NotImplementedError
    def train_dataloader(self):
        return self.get_dataloader(train=True)
    def val_dataloader(self):
        return self.get_dataloader(train=False)
```

Subclasses (e.g., `SyntheticRegressionData`, the running dataset of the chapter) override `get_dataloader` to yield `(features, labels)` minibatches.

## Why separate from `Module`

[[d2l-linear-regression]]: "Data loaders are a convenient way of abstracting out the process of loading and manipulating data. This way the same machine learning *algorithm* is capable of processing many different types and sources of data without the need for modification." The same `LinearRegression` `Module` can train on synthetic data, real housing prices, or images by swapping only the `DataModule`.

## Connections

- [[d2l-linear-regression]] — §3.2 canonical reference; introduces `SyntheticRegressionData` as the running `DataModule` subclass.
- [[Module]] — sibling class for the model itself.
- [[Trainer]] — orchestrates `fit(model, data)` consuming the `DataModule`'s loaders.
- [[DataLoader]] — the underlying [[PyTorch]] / framework primitive `get_tensorloader` wraps.
- [[PyTorchLightning]] — named inspiration.
- [[D2LPackage]] — `DataModule` is `#@save`-persisted and reused by every later chapter.
