---
title: "Checkpoint"
type: concept
tags: [training, mlops]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# Checkpoint

A serialized snapshot of model parameters (and often optimizer state) saved during training so runs can resume, fork, or be evaluated retrospectively. Required for [[EarlyStopping]], [[DistributedTraining]] fault tolerance, and producing the artifacts consumed by [[ExperimentTracking]] tools.

[[d2l-builders-guide]] §`read-write.md` is the canonical reference for the *mechanic*: `torch.save(net.state_dict(), 'mlp.params')` writes a [[StateDict|state-dict]] file; `clone = MLP(); clone.load_state_dict(torch.load('mlp.params'))` rebuilds the architecture in code and restores the parameters. The architecture is *not* in the file — see [[StateDict]] for the reasoning.

D2L's motivation quote: "the best practice is to periodically save intermediate results … to ensure that we do not lose several days' worth of computation if we trip over the power cord of our server." See [[FileIO]] for the broader save/load API including raw tensors and dicts.
