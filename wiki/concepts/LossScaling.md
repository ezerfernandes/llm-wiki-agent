---
title: "Loss Scaling"
type: concept
tags: [mixed-precision, training, numerical-stability, fp16]
sources: [mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

# Loss Scaling

A numerical-stability technique in [[MixedPrecisionTraining|mixed-precision training]] that **amplifies the loss by a large factor (typically $2^8$ to $2^{14}$) before backpropagation**, so that small gradients stay within [[FP16]]'s representable range, then unscales the gradients before the optimizer step.

Necessary because FP16's 5-bit exponent cannot represent values below ~$6.1 \times 10^{-5}$ (its minimum normal value), and many accelerators flush subnormals to zero — so gradients that fall below this floor underflow to zero and vanish. Scaling the loss shifts the whole gradient distribution above the FP16 floor; dividing it back out after the backward pass recovers the correct magnitudes.

## Key Points

- Per [[mlsysbook-ch08-model-training|mlsysbook Ch 8]], loss scaling is step 3 of the six-step mixed-precision cycle (cast → forward → **scale** → backprop → copy-to-FP32-and-unscale → update).
- **[[AutomaticMixedPrecision|PyTorch AMP]]'s `GradScaler`** adjusts the scaling factor dynamically (raising it when no overflow occurs, backing off on `inf`/`nan`).
- **[[BF16]] eliminates the need for loss scaling** entirely: its 8-bit exponent matches FP32's dynamic range, so gradients spanning $10^{-10}$ to $10^3$ (typical for transformers) never underflow. This is the main reason BF16 is the default for transformer training despite fewer mantissa bits.
- Forgetting loss scaling (or mis-tuning it) is a common cause of FP16 training divergence — a model can train fine for 10,000+ steps then diverge from accumulated numerical error.

## Connections

- [[MixedPrecisionTraining]] — the technique loss scaling makes numerically safe.
- [[AutomaticMixedPrecision]] — `torch.cuda.amp` automates loss scaling.
- [[FP16]] — the format whose limited dynamic range loss scaling compensates for.
- [[BF16]] — the format that makes loss scaling unnecessary.
- [[mlsysbook-ch08-model-training]] — defining source.
