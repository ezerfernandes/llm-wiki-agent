---
title: "File I/O (Tensors & Models)"
type: concept
tags: [deep-learning, framework, d2l, serialization]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# File I/O (Tensors & Models)

How [[PyTorch]] / [[MXNet]] / [[TensorFlow]] / [[JAX]] persist tensors and entire model states to disk and reload them — the substrate of [[Checkpoint|checkpointing]], deployment, and reproducibility ([[d2l-builders-guide]] §`read-write.md`).

## Three granularities

| Granularity | PyTorch save | PyTorch load |
|---|---|---|
| Single tensor | `torch.save(x, 'x-file')` | `x2 = torch.load('x-file')` |
| List / dict of tensors | `torch.save([x, y], 'x-files')` / `torch.save({'x':x,'y':y}, 'mydict')` | `torch.load('x-files')` |
| Entire model | `torch.save(net.state_dict(), 'mlp.params')` | `clone.load_state_dict(torch.load('mlp.params'))` |

The dict form is what the framework's `state_dict` uses internally — `state_dict()` is a `dict[str, Tensor]` from parameter names to values.

## Why checkpoint

[[d2l-builders-guide]]: "When running a long training process, the best practice is to periodically save intermediate results (checkpointing) to ensure that we do not lose several days' worth of computation if we trip over the power cord of our server." Modern foundation-model training writes a checkpoint every $N$ steps; the [[2205.14135-flashattention|FlashAttention]] / [[1706.03762-attention-is-all-you-need|Transformer]] training loops all assume crash-resumable checkpoints.

## What you actually save

For a checkpoint to fully restore training you need:

1. **Model `state_dict`** — parameters.
2. **Optimizer `state_dict`** — momentum buffers, Adam moments, step counter.
3. **Scheduler state** — current learning rate, last epoch.
4. **Random-state** — torch / numpy / python RNG seeds for exact reproducibility.
5. **Step / epoch counter** — where to resume the loop.

Idiomatic PyTorch:

```python
torch.save({
    'epoch': epoch,
    'model_state_dict': net.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
}, f'ckpt_{epoch}.pt')
```

## Architecture not included

[[d2l-builders-guide]] is explicit: `state_dict` saves *parameters only*. The architecture must be rebuilt in code: `clone = MLP(); clone.load_state_dict(torch.load('mlp.params'))`. See [[StateDict]] for the full reasoning. Pickling the whole module is possible but brittle across refactors.

## Cross-framework analogues

| Framework | Tensor save | Model save |
|---|---|---|
| [[PyTorch]] | `torch.save(x, p)` | `torch.save(net.state_dict(), p)` |
| [[MXNet]] | `npx.save(p, x)` | `net.save_parameters(p)` |
| [[TensorFlow]] | `np.save(p, x.numpy())` | `net.save_weights(p)` |
| [[JAX]] / Flax | `jnp.save(p, x)` | `checkpoints.save_checkpoint(dir, params, step)` |

## Connections

- [[d2l-builders-guide]] — §`read-write.md` canonical reference.
- [[StateDict]] — the dict format model saves use.
- [[Checkpoint]] — the artifact this produces.
- [[NeuralNetworkModule]] — what is being serialized.
- [[Parameter]] — the tensors inside.
- [[TransferLearning]] — partial-load via `strict=False`.
- [[ExperimentTracking]] — checkpoints flow to MLflow / W&B / Comet artifact stores.
