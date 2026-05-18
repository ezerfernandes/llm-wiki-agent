---
title: "Confidence Momentum Controller (CMC)"
type: concept
tags: [test-time-scaling, controller, discovered-algorithm]
sources: [2605.08083-autotts]
last_updated: 2026-05-15
---

# Confidence Momentum Controller (CMC)

The TTS controller **discovered by [[AutoTTS]]** in [[2605.08083-autotts]] after a five-round, $39.9 search loop. CMC governs all width × depth decisions (BRANCH / CONTINUE / PROBE / PRUNE / ANSWER) over a [[2602.03845-parallel-probe|Parallel-Probe]]-style offline trajectory pool, and exposes only a single scalar $\beta\in[0,1]$ ([[BetaParameterization|beta parameterization]]).

## Four Non-Obvious Mechanisms

1. **Trend-based stopping (EMA momentum).** Track `ema_conf = (1−α)·ema_prev + α·new_conf` of pool [[selfconsistency|Beta-majority confidence]] over the last `T_ema` rounds. Gate fires only when BOTH `ema_conf ≥ conf_thresh` AND `delta ≥ −delta_slack` (non-deteriorating momentum). Prevents premature termination on single-step confidence spikes — a structural improvement over baselines' instantaneous gates (IBC, SCR, DGCC, Parallel-Probe).

2. **Coupled width–depth control via shared EMA delta.** The same EMA-delta signal that drives the stopping gate *also* drives the widening decision: large positive delta ⇒ confidence is accelerating, no widening; small or negative delta ⇒ plateau or regression, widen by `widen_burst` new branches. Creates a closed feedback loop absent in all hand-crafted baselines.

3. **Alignment-aware depth allocation.** Three-tier branch classification each round after `warm_up`:
   - `aligned`: latest answer matches pool winner → multiplier = `burst_aligned` (extra probe steps).
   - `neutral`: no pool winner yet, or first round of disagreement → multiplier = 1.
   - `deviant`: latest answer disagrees with pool winner → multiplier = 1, abandonment counter starts.

   Probe budget per round is distributed across active branches via a priority queue sorted by `probe_count` ascending — most-invested branches served first (up to `burst_senior` extra steps), then remaining budget to less-invested branches. Concentrates depth on near-completion branches while still advancing younger ones.

4. **Conservative branch abandonment.** A deviant branch is abandoned only after *persistent* disagreement for `abandon_patience` consecutive rounds, AND with the guarantee that ≥2 active branches are always preserved. Prevents the [[InverseWisdomLaw]]-style collapse where transient noise prunes the right answer.

## Beta Schedule (App. D)

All hyperparameters are smooth analytic functions of $b=\beta$:

```
n_init           = max(2, round(2 + 6b))            # initial branches
max_branch_use   = min(64, round(4 + 60b))           # ceiling on widening
warm_up          = max(2, round(2 + 8b))             # rounds before tiering
abandon_patience = max(3, round(3 + 9b))             # persistence threshold

T_ema     = max(2, round(2 + 6b))                    # EMA window
ema_alpha = 0.70 − 0.40·b                            # NON-INCREASING (more inertia at high β)

conf_thresh  = 0.85 + 0.12·b                         # stopping floor [0.85, 0.97]
delta_slack  = 0.04 − 0.03·b                         # momentum tolerance

burst_aligned = max(1, round(1 + 2b))                # extra probes for aligned branches
widen_burst   = max(1, round(1 + 3b))                # new branches per widening event
trend_thresh  = 0.04 − 0.03·b                        # EMA-delta floor for widening
min_complete  = max(2, round(2 + 3b))                # min completed branches before gate
```

## Empirical Results

(Held-out, avg across Qwen3-0.6B / 1.7B / 4B / 8B.)

| $\beta$ | Acc | Tokens | Notes |
|---|---|---|---|
| 0.5 | 45.3 | 334K | ~69.5% token reduction vs SC@64 at matched accuracy |
| 1.0 | 46.6 | 621K | Peak accuracy beyond all handcrafted baselines in 5/8 cases |

Generalizes:
- DeepSeek-R1-Distill-Llama-8B on HMMT25: AutoTTS(β=1) reaches 27.2 acc vs SC@64's 26.7 at half the tokens.
- Qwen3-1.7B on GPQA-Diamond (non-math): AutoTTS(β=0.5) 41.6 / 151.0K vs SC@64 41.3 / 510.0K.

## How CMC Differs from Seeds

| Seed | Stopping signal | Widening | Depth |
|---|---|---|---|
| ASC / ESC | full reads, no incremental probing | — | — |
| Parallel-Probe | fixed cohort, instantaneous majority | none after warm-up | uniform |
| IBC (round 1) | instantaneous pool confidence | uniform 1-step | none |
| SCR (round 2) | instantaneous gate | plateau-triggered widening | asymmetric burst (aligned) |
| DGCC (round 3) | dual gate (primary + soft corroboration) | vote-gap proportional | lazy sleeping |
| **CMC (round 5)** | **EMA-momentum (level + non-deteriorating)** | **trend-coupled** | **probe-age priority + alignment burst** |

CMC replaces all instantaneous gates with a single EMA-momentum gate; introduces probe-age priority (neither uniform nor burst-aligned only); and links width and depth via confidence-trend feedback — a feedback loop absent in all prior controllers.

## Connections

- [[2605.08083-autotts]] — discovery paper.
- [[AutoTTS]] — discovery framework.
- [[BetaParameterization]] — the single-knob discipline CMC obeys.
- [[2602.03845-parallel-probe|Parallel-Probe]] — closest seed; replaced by EMA-momentum.
- [[selfconsistency|Self-Consistency / SC@64]] — handcrafted baseline.
- [[WidthDepthSearch]] — the control space CMC navigates.
- [[testtimescaling|Test-Time Scaling]] — parent problem.
- [[2402.01817-llm-modulo|LLM-Modulo]] — CMC fits as an external-critic instance: the controller decides termination via EMA-gating, not via the base LLM's [[SelfVerification|self-verification]].
