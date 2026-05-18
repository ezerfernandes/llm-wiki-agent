---
title: "Dive into Deep Learning — Builders' Guide"
type: source
tags: [textbook, d2l, builders-guide, pytorch, modules, gpu, parameters]
date: 2026-05-16
source_file: raw/d2l-en/chapter_builders-guide/
---

## Summary

[[AstonZhang|Zhang]], [[ZacharyLipton|Lipton]], [[MuLi|Li]] & [[AlexanderSmola|Smola]]'s seven-section "power-user" chapter of [[d2l-preface|D2L]] — the bridge from *end user* to *library implementer*. Peels back the abstractions used so far: the **[[NeuralNetworkModule|module / block]]** abstraction ([[PyTorch]] `nn.Module`, [[MXNet]] `nn.Block`, Keras `tf.keras.Model`, [[JAX]]/Flax `linen.Module`) and how `Sequential` is just a thin daisy-chain subclass; **[[ParameterAccess|parameter access]]** (`state_dict()`, `named_parameters()`, indexing into submodules) and **[[ParameterSharing|tied / shared parameters]]** across layers; **[[ParameterInitialization|built-in + custom initialization]]** ([[XavierInitialization|Xavier]], normal, constant, custom `nn.init` schemes); **[[LazyInitialization|lazy initialization]]** (`nn.LazyLinear`) that defers shape inference until first forward pass; **[[CustomLayer|custom layers]]** with and without learnable [[Parameter|Parameters]]; **[[FileIO|file I/O]]** for tensors and entire model `state_dict` checkpoints (architecture is *not* serialized — code re-creates it); and **[[GPU|GPU usage]]** — device specification (`torch.device('cuda:i')`), tensor placement, model-to-device transfer (`net.to(device)`), and the cardinal rule that **all operands of an op must live on the same device** (no implicit copies; transfers are slow). Zero new mathematical content — entirely a practical operations chapter that every subsequent D2L architecture (CNNs, RNNs, Transformers) silently relies on.

## Key Claims

- **Modules are the universal abstraction.** Every layer, every multi-layer block, and the entire model are subclasses of a common base class ([[PyTorch]] `nn.Module`, [[MXNet]] `nn.Block`, Keras `tf.keras.Model`, Flax `linen.Module`). A module needs only (i) a `forward` method describing the input→output computation, (ii) storage for parameters; backpropagation is handled automatically by [[Autograd]]. "Individual layers can be modules. Many layers can comprise a module. Many modules can comprise a module" — recursive composition is the entire programming model.
- **`Sequential` is *not* magic.** It is a 20-line subclass of `nn.Module` that maintains an ordered list of submodules and whose `forward` chains them: `for m in self.children(): X = m(X); return X`. Net is registered by `add_module` (or `*args`), which is what makes the framework discover its parameters. Re-implementing `MySequential` from scratch is the canonical exercise.
- **Custom `forward` enables arbitrary Python control flow inside the network.** Once you subclass `Module` you can intersperse `if` statements, `while` loops, NumPy-style math, even non-learnable "constant parameters" (`self.rand_weight = torch.rand((20,20))` — no `nn.Parameter` wrapper, no gradient) — `FixedHiddenMLP` demos a `while X.abs().sum() > 1: X /= 2` loop and parameter reuse (the same `nn.Linear` called twice = parameter sharing across layers).
- **Parameter access is dictionary-like, recursive, and uniform across frameworks.** `net[idx]` indexes into a `Sequential`; `.state_dict()`, `.named_parameters()`, and `.parameters()` walk the entire submodule tree. Each parameter is a *complex object* containing `.data` (the tensor value) and `.grad` (the gradient, `None` until backward is called). Operations on "all parameters at once" use these recursive accessors.
- **Parameter tying (sharing) is created by reusing the same `nn.Linear` instance in multiple places.** `shared = nn.LazyLinear(8); net = nn.Sequential(..., shared, ..., shared, ...)` makes the second and third hidden layer *exactly the same tensor* — mutating one mutates the other. Gradients of the tied locations are *summed* during backprop, so weight sharing is implemented for free by the autograd graph.
- **Lazy initialization defers shape inference until the first forward pass.** Layers like `nn.LazyLinear(256)` are declared without an input dimension; the framework records the desired output size, allocates no weight tensor, and waits. The first `net(X)` call infers `n_in` from `X.shape[-1]`, allocates the weight, and runs default init. This eliminates one common source of architecture-modification bugs and is *essential* for [[CNN|convolutional]] / pooling stacks where input resolution determines downstream shapes.
- **Initialization is composable per submodule.** `net.apply(fn)` recursively applies a (typically type-guarded) init function to every submodule: `if type(m) == nn.Linear: nn.init.xavier_uniform_(m.weight); nn.init.zeros_(m.bias)`. Per-layer overrides work the same way (`net[0].apply(init_xavier); net[2].apply(init_42)`). Custom initializers are just Python functions that mutate `module.weight.data` in-place — there is nothing "framework-blessed" about them.
- **Custom layers are written by subclassing `Module`.** Parameter-free layers (e.g. `CenteredLayer` doing `X - X.mean()`) need only override `forward`. Layers *with* learnable parameters wrap their tensors in `nn.Parameter(torch.randn(in_units, units))`, which is what the framework discovers as a tracked parameter (added to `named_parameters()`, initialized, saved by `state_dict`, moved by `.to(device)`).
- **`state_dict` saves *parameters*, not architecture.** `torch.save(net.state_dict(), 'mlp.params')` serializes only the parameter dictionary. To load: re-construct the `MLP()` class in code, then `clone.load_state_dict(torch.load('mlp.params'))`. The architecture *must* be regenerable from code because modules can contain arbitrary Python — "the models themselves can contain arbitrary code, hence they cannot be serialized as naturally." This is why frozen production deployments ship both code and weights.
- **Checkpointing is essential for long training runs.** "When running a long training process, the best practice is to periodically save intermediate results … to ensure that we do not lose several days' worth of computation if we trip over the power cord of our server." Individual tensors are saved with `torch.save(x, path)` / `torch.load(path)`; dicts of tensors work too — that is exactly what `state_dict` is.
- **GPUs are referenced by device handles.** [[PyTorch]] uses `torch.device('cpu')` and `torch.device(f'cuda:{i}')`. `cpu` represents *all* CPU cores and the entire main memory; `cuda:i` represents *one* GPU card and its memory. Multiple GPUs are addressed `cuda:0`, `cuda:1`, etc. `torch.cuda.device_count()` queries availability; the D2L `try_gpu(i)` helper falls back to CPU gracefully.
- **Tensors must live on the same device for any binary op.** `X.cuda(1)` (or `.to(device=...)`) returns a *copy* on the target device — explicit, never implicit. "If we sum two tensors, we need to make sure that both arguments live on the same device — otherwise the framework would not know where to store the result." Models are moved with `net = net.to(device=try_gpu())`; when input and parameters are co-resident the computation stays on-device.
- **Cross-device transfer is *slow* — much slower than computation.** D2L's rule of thumb: "Many small operations are much worse than one big operation … several operations at a time are much better than many single operations interspersed in the code." Logging GPU losses to CPU per minibatch triggers the GIL and stalls all GPUs — keep logs on-device, transfer in bulk at the end of an epoch. Even `print(tensor)` and NumPy conversion are silent device→CPU copies.

## Key Quotes

> "Individual layers can be modules. Many layers can comprise a module. Many modules can comprise a module. A module can contain code. Modules take care of lots of housekeeping, including parameter initialization and backpropagation." — `model-construction.md` §Summary

> "Lazy initialization can be convenient, allowing the framework to infer parameter shapes automatically, making it easy to modify architectures and eliminating one common source of errors. We can pass data through the model to make the framework finally initialize parameters." — `lazy-init.md` §Summary

> "An important detail to note is that this saves model *parameters* and not the entire model. … The models themselves can contain arbitrary code, hence they cannot be serialized as naturally. Thus, in order to reinstate a model, we need to generate the architecture in code and then load the parameters from disk." — `read-write.md` §Loading and Saving Model Parameters

> "If we sum two tensors, we need to make sure that both arguments live on the same device — otherwise the framework would not know where to store the result or even how to decide where to perform the computation." — `use-gpu.md` §Tensors and GPUs

> "People use GPUs to do machine learning because they expect them to be fast. But transferring variables between devices is slow: much slower than computation. So we want you to be 100% certain that you want to do something slow before we let you do it." — `use-gpu.md` §Side Notes

## Connections

- [[d2l-preface]] — pedagogical thesis (concepts / context / code, just-in-time).
- [[d2l-preliminaries]] — `nn.Module` is to layers what `ndarray` is to data.
- [[d2l-linear-regression]] — first chapter to use `nn.Linear` / `nn.Sequential`; this chapter retroactively explains *what they are*.
- [[d2l-multilayer-perceptrons]] — uses `apply(init_xavier)`, `state_dict` and `to(device)` operationally; this chapter explains the mechanics.
- [[Module]] — D2L's training-loop base class — distinct from but built on `nn.Module`.
- [[NeuralNetworkModule]] — the framework-level abstraction (newly created).
- [[ParameterAccess]] — `state_dict` / `named_parameters` / index access (newly created).
- [[ParameterSharing]] — tied weights as multi-reference to the same tensor (newly created).
- [[LazyInitialization]] — deferred shape inference (newly created).
- [[CustomLayer]] — subclassing `Module` for new operators (newly created).
- [[StateDict]] — the framework's portable parameter-snapshot format (newly created).
- [[GPU]] — compute device for tensors and parameters (newly created).
- [[Parameter]] — `nn.Parameter` wrapping a tensor as a tracked, optimizable variable (newly created).
- [[PyTorch]] / [[MXNet]] / [[TensorFlow]] / [[JAX]] — the four framework targets compared throughout.
- [[CUDA]] — the GPU compute platform `cuda:i` refers to.
- [[NVIDIA]] — vendor of the GPUs `nvidia-smi` queries (newly created entity).
- [[WeightInitialization]] / [[XavierInitialization]] / [[HeInitialization]] — concrete init schemes invoked.
- [[Checkpoint]] — the parameter-snapshot artifact `state_dict` produces.
- [[Autograd]] — handles backward automatically once `forward` is defined.
- [[Tensor]] — what lives on a device.
- [[gpumemoryhierarchy]] — why cross-device transfers are slow.

## Contradictions

- **None direct.** Reaffirms (rather than contradicts): [[WeightInitialization]]'s framework-defaults table (Xavier for tanh, He for ReLU, LeCun for SELU/Flax); [[Checkpoint]]'s definition ("serialized snapshot of model parameters … so runs can resume"); [[gpumemoryhierarchy]]'s "transfers are slow" cost model — D2L now provides the concrete API for what the wiki previously described abstractly. No tension with [[d2l-preliminaries]] (tensors / autograd), [[d2l-linear-regression]] (which uses `nn.LazyLinear` already), or [[d2l-multilayer-perceptrons]] (which uses `apply(init_xavier)` operationally).
