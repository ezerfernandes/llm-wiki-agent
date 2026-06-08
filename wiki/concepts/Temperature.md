---
title: "Temperature"
type: concept
tags: [sampling, inference, llm, softmax]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch06-prompt-engineering, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Temperature

A **constant used to adjust logits before the softmax transformation** during LLM sampling. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Logits are divided by temperature. For a given temperature T, the adjusted logit for the ith token is $x_i / T$. Softmax is then applied on this adjusted logit instead of on $x_i$."

## Effect

- **Higher T** → reduces probabilities of common tokens, increases probabilities of rarer tokens → **more creative, less coherent**.
- **Lower T** → concentrates probability mass on the highest-logit tokens → **more consistent, less creative ("boring")**.

## Worked example (Ch 2)

Two-token model with logits [1, 2]:

| Temperature | P(A) | P(B) |
|---|---|---|
| T = 1 (default) | 0.27 | 0.73 |
| T = 0.5 | 0.12 | 0.88 |
| T → 0 | 0 | 1 (argmax) |

## T = 0 is special

Technically temperature can never be 0 (division by zero). In practice, **T = 0 is implemented as argmax over logits** — picking the token with the largest logit without doing logit-adjustment or softmax. Equivalent to **[[GreedyDecoding|greedy decoding]]**.

## Recommended defaults

- **Most model providers clamp T to [0, 2]**.
- If you own your model, any non-negative T is fine.
- **T = 0.7** is the common creative-task default — balances creativity and predictability.

## The connection to attention

The "temperature" terminology comes from statistical physics (Boltzmann's $\exp(-E/kT)$) — the same $T$ that scales the inverse-temperature term. The attention mechanism's $\sqrt{d_k}$ scaling factor in transformers (see [[Softmax]]) is the same idea: a temperature that controls how peaked the softmax output is.

## Why fixing T doesn't fully fix [[Inconsistency|inconsistency]]

Per Ch 2:

> "Even if you fix all these variables [temperature, top-p, top-k, seed], however, there's no guarantee that your model will be consistent 100% of the time. The hardware the model runs the output generation on can also impact the output."

Hardware differences across machines can produce different outputs for the same inputs even with identical sampling settings.

## Connections
- [[Softmax]] — what temperature modifies before.
- [[Topk]] / [[Topp]] — the other two main sampling controls.
- [[Logprobs]] — log-scale probabilities.
- [[GreedyDecoding]] — what T = 0 reduces to.
- [[Inconsistency]] — the failure mode temperature partly mitigates.
- [[ai-engineering-ch02-foundation-models]] — primary source (Huyen Ch 2 — mechanistic).
- [[hands-on-llm-ch06-prompt-engineering]] — operational source (Alammar & Grootendorst Ch 6).

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 takes the **operational rather than mechanistic** framing of temperature — characterizes the behavior without the softmax-rescaling math:

> *"A higher value allows less probable words to be generated... a higher temperature (e.g., 0.8) generally results in a more diverse output while a lower temperature (e.g., 0.2) creates a more deterministic output."* — Ch 6

### Temperature × top_p use-case quadrants (Ch 6 Table 6-1)

| Use case | Temperature | top_p | Description |
|---|---|---|---|
| **Brainstorming** | High | High | Highly diverse, creative, unexpected. |
| **Email generation** | Low | Low | Predictable, focused, conservative. |
| **Creative writing** | High | Low | Creative but coherent (small candidate pool keeps variation in-vocab). |
| **Translation** | Low | High | Coherent + linguistic variety. |

This is the wiki's most practical Temperature × Top-p use-case matrix — anchored in concrete application categories rather than abstract diversity-vs-coherence axes.

### Required pipe-level flag

Ch 6's `transformers.pipeline` worked example sets `do_sample=False` for deterministic output (greedy decoding); to use temperature / top_p you must set `do_sample=True`. *"Note that every time you rerun this piece of code, the output will change! temperature introduces stochastic behavior since the model now randomly selects tokens."*

## In [[agentic-design-patterns-appendix-a-prompting|Agentic Design Patterns Appendix A]]

[[AntonioGulli|Gulli]]'s prompting survey treats temperature (with [[Topk|top-k]]/[[Topp|top-p]]) as part of the **experimentation surface** and ties it to two reasoning techniques: set **temperature 0** (greedy decoding) when using [[chainofthought|CoT]] on tasks with a single correct answer (e.g. math) for deterministic step-by-step selection; and use a **higher temperature** in [[selfconsistency|self-consistency]] to generate diverse reasoning paths before majority-voting. The best-practices checklist also pairs temperature control with managing **max token length** via model configuration.
