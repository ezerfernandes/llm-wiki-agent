# DSPy Optimization Overview

**Source URL:** https://dspy.ai/learn/optimization/overview/
**Breadcrumb:** Get Started > Learn DSPy > DSPy Optimization
**Page 12 of 13** of the DSPy *Learn* documentation; **opens the Optimization stage** of the three-stage Programming → Evaluation → Optimization model. Last sibling: Optimizers (page 13).

---

## DSPy Optimization

Once you have a system and a way to evaluate it, you can use DSPy optimizers to tune the prompts or weights in your program.

Now that you have some data and a metric, you're ready to optimize the program you built. You can iterate fast by trying out different optimizers. You may also want to collect more data for optimization at this stage. For instance, you may want to expand your data collection to include training, development, and test sets. **You can often get substantial value out of 30 examples, but aim for at least 300 examples.**

For most prompt optimizers, **we recommend allocating 20% of your data for training and 80% for validation**, contrary to typical deep learning conventions. This is because prompt optimizers tend to overfit on small training sets. However, the GEPA optimizer follows standard ML practice — maximizing the training set size while keeping the validation set sufficiently sized to represent the downstream task distribution.

Now, before getting started with an optimizer, it's useful to think about whether your task is well-defined, whether you have sufficient data, whether your metric is appropriate, and whether you're using a sufficiently sophisticated optimizer. The questions to revisit during this iteration include:

- Is your task well-defined?
- Have you collected enough data?
- Is your metric appropriate?
- Are you using the most sophisticated optimizer that fits your needs?
- Could DSPy Assertions or other advanced features help?
- Is your program structured optimally — e.g. should you decompose, or simplify?

**Iterative development is key. DSPy gives you the pieces to do that incrementally.** Improving your data, your program structure, your metric, or the DSPy optimizer you use.

This is an emerging paradigm for optimizing LM programs, and the community is here to help. Join the [Discord server](https://discord.gg/XCGy2WDCQB) for discussions and support.

---

## Inputs an optimizer takes

An optimizer takes three inputs:

1. **A program** — the DSPy program (signatures + modules + LM wiring) you've built.
2. **A metric** — a function that measures program quality, defined per the [Metrics page](https://dspy.ai/learn/evaluation/metrics/).
3. **A training set** — a small set of input examples (some optimizers also use a separate validation set).

The output is **an optimized program** whose prompts (instructions, few-shot demonstrations) and/or weights have been refined so the metric improves.

---

## Next step

Continue to **Optimizers** (the next page) for the concrete catalog of optimization algorithms — `BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`, `MIPROv2`, `BootstrapFinetune`, `GEPA`, and others — and the per-optimizer decision rubric (when to pick which).
