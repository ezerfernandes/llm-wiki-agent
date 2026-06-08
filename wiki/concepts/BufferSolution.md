---
title: "Buffer Solution"
type: concept
tags: [chemistry, general-chemistry, acids-bases, equilibrium]
sources: [chemistry-2e-ch14-acid-base-equilibria]
last_updated: 2026-06-07
---

# Buffer Solution

A **buffer solution** (buffer) is a solution containing appreciable amounts of a weak [[ConjugateAcidBasePair|conjugate acid-base pair]]. It **resists changes in [[pHScale|pH]]** when small amounts of strong acid or strong base are added. Two common forms:
- a weak acid plus its salt (e.g. acetic acid + sodium acetate, CH₃CO₂H / CH₃CO₂⁻);
- a weak base plus its salt (e.g. ammonia + ammonium chloride, NH₃ / NH₄⁺).

## How it works

The conjugate pair supplies both a proton acceptor and a proton donor. In an acetic acid / acetate buffer,
$$\mathrm{CH_3CO_2H(aq) + H_2O(l) \rightleftharpoons H_3O^+(aq) + CH_3CO_2^-(aq)},$$
added strong base is consumed by the weak acid (equilibrium shifts right) and added strong acid is consumed by the conjugate base (shifts left). The added strong acid/base is effectively converted into the weak acid/base of the pair, so [H₃O⁺] barely moves.

## Buffer capacity

**Buffer capacity** is the amount of acid or base that can be added before the pH changes significantly (usually by one unit). It depends on the **concentrations** of both components: a 1.0 M acetic acid/acetate buffer has greater capacity than a 0.10 M one. Practical selection rules:
1. A good buffer has roughly **equal** concentrations of its two components; it loses usefulness once one component drops below ~10% of the other.
2. Weak-acid/salt pairs buffer best at pH < 7; weak-base/salt pairs at pH > 7. The buffer is most effective near pH = pKa.

## Quantitative treatment

The pH of a buffer is given by the [[HendersonHasselbalch|Henderson-Hasselbalch equation]], pH = pKa + log([A⁻]/[HA]).

## Biological role

Blood is buffered near pH 7.4 by the carbonic acid-bicarbonate system (CO₂ + 2H₂O ⇌ H₂CO₃ ⇌ HCO₃⁻ + H₃O⁺), with [HCO₃⁻] ≈ 0.024 M and [H₂CO₃] ≈ 0.0012 M. Normal blood-pH swings are < 0.1; changes of 0.4 or more are likely fatal. Respiration assists regulation by adjusting CO₂.

## Connections
- [[ConjugateAcidBasePair]] — a buffer is an appreciable amount of one
- [[HendersonHasselbalch]] — computes buffer pH
- [[AcidIonizationConstant]] — pKa sets the buffer's working pH
- [[pHScale]] — what a buffer stabilizes
- [[AcidBaseTitration]] — the buffer region lies before the equivalence point of a weak-acid titration
- [[LeChatelierPrinciple]] — the equilibrium shifts that absorb added acid/base
- [[chemistry-2e-ch14-acid-base-equilibria]] — source chapter (§14.6)

> Disambiguation: chemistry buffer *solution* — not a memory/data buffer (see computing pages such as [[BufferOverflow]]).
