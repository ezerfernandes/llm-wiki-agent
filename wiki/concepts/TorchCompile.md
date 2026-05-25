---
title: "torch.compile"
type: concept
tags: [llm-engineering]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## Definition
PyTorch graph capture and fusion tool producing optimized kernels.

## In LLM Engineer's Handbook
PyTorch 2.x graph-capture-and-fusion tool that traces Python model code into an FX graph and compiles into fused, optimized kernels (TorchInductor / Triton on GPU). For LLM inference the chief constraint is shape-stability, which is why pairing it with a [[StaticKVCache]] is necessary and yields up to 4x forward-pass speedup per [[leh-ch08-inference-optimization]].
