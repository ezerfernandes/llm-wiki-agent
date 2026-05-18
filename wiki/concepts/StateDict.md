---
title: "State Dict"
type: concept
tags: [deep-learning, framework, d2l, pytorch, serialization]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# State Dict

A flat Python `OrderedDict` mapping *every* parameter name (hierarchical, dot-separated — e.g. `"hidden.weight"`, `"hidden.bias"`, `"output.weight"`) to its tensor value. The portable, framework-native snapshot format for [[PyTorch]] models ([[d2l-builders-guide]] §`read-write.md`).

## Save / load idiom

```python
torch.save(net.state_dict(), 'mlp.params')      # save

clone = MLP()                                    # rebuild architecture in code
clone.load_state_dict(torch.load('mlp.params'))  # restore parameters
clone.eval()                                     # switch to eval mode
```

## Architecture is not in the state dict

This is the most important property of the format:

> "An important detail to note is that this saves model *parameters* and not the entire model. … The models themselves can contain arbitrary code, hence they cannot be serialized as naturally. Thus, in order to reinstate a model, we need to generate the architecture in code and then load the parameters from disk." — [[d2l-builders-guide]]

Practical implication: deployment artifacts must ship **both** the parameter file *and* the Python class definition. Pickling the whole `nn.Module` is possible (`torch.save(net, path)`) but discouraged — it embeds the import path of every class and breaks when refactored.

## Why this design

- Modules contain arbitrary Python (`if`, `while`, custom math). Serializing arbitrary code reliably is hard; serializing tensors is trivial.
- Loose coupling between architecture (versioned in source control) and weights (versioned as binary artifacts).
- Cross-version forward-portability — name-keyed dict survives small refactors as long as parameter names stay stable.

## Selective loading

```python
sd = torch.load('mlp.params')
# Keep only encoder weights, discard classifier head
encoder_sd = {k: v for k, v in sd.items() if k.startswith('encoder.')}
new_net.load_state_dict(encoder_sd, strict=False)
```

This is the standard mechanism for [[TransferLearning|transfer learning]] — load a pretrained backbone, attach a new head.

## Cross-framework analogues

| Framework | Save | Load |
|---|---|---|
| [[PyTorch]] | `torch.save(net.state_dict(), path)` | `clone.load_state_dict(torch.load(path))` |
| [[MXNet]] | `net.save_parameters('mlp.params')` | `clone.load_parameters('mlp.params')` |
| [[TensorFlow]] | `net.save_weights('mlp.params')` | `clone.load_weights('mlp.params')` |
| [[JAX]] / Flax | `checkpoints.save_checkpoint(dir, params, step)` | `checkpoints.restore_checkpoint(dir, target=None)` |

## Connections

- [[d2l-builders-guide]] — §`read-write.md` canonical reference.
- [[NeuralNetworkModule]] — what `state_dict()` is a method of.
- [[ParameterAccess]] — `state_dict()` is `named_parameters()` materialized into a dict.
- [[Parameter]] — the tensors named by the dict.
- [[Checkpoint]] — the saved-state-dict file is the checkpoint.
- [[FileIO]] — `torch.save` / `torch.load` are the I/O verbs.
- [[TransferLearning]] — selective loading enables backbone reuse.
- [[adapterlayers|Adapter Layers]] — pretrained-state-dict + extra small modules is the parameter-efficient fine-tuning template.
