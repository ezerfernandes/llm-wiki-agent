---
name: Explainability
title: "Explainability"
type: concept
tags: [responsible-ai, interpretability, transparency, regulation]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Explainability

The ability to articulate **which input features drove a specific prediction**, enabling human oversight, debugging, and regulatory compliance. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], explainability is *post-hoc* — added without changing the model ([[SHAP]], [[LIME]]) — and is distinct from [[Interpretability|interpretability]], an *intrinsic* model property.

## Requirements vary by domain
| Domain | Level |
|---|---|
| Credit decisions | Individual explanation required (adverse-action notices) |
| Medical diagnosis | Clinical reasoning support |
| Content moderation | Appeal-supporting |
| Recommendation | Optional ("because you watched X") |
| Fraud detection | Internal-only (explanations may enable gaming) |

## Methods and the interpretability spectrum
- **Post-hoc**: [[SHAP]] ([[ShapleyValues|Shapley values]]), [[LIME]] (local surrogate), [[SaliencyMap|saliency maps]].
- **Inherently interpretable**: linear/logistic regression, decision trees, attention.
- **Concept-based** explanations map behavior to human-understandable concepts.
The spectrum runs decision trees / linear models (auditable, lower capacity) → random forests → neural nets / CNNs (higher accuracy, require post-hoc tools). Pick the most interpretable model that meets accuracy needs.

Regulatory force: [[EUAIAct|EU AI Act]] demands "meaningful information about the logic involved"; [[GDPR]] Article 15(1)(h) grants access to automated-decision logic; US adverse-action notices require disclosing denial factors. The "hospital shortcut" (Zech et al. 2018) shows interpretability tools are QA gates, not polish.

## Connections
- [[Interpretability]] — the intrinsic counterpart.
- [[SHAP]] / [[LIME]] / [[ShapleyValues]] / [[SaliencyMap]] — post-hoc methods.
- [[EUAIAct]] / [[GDPR]] — regulatory drivers.
- [[ShortcutLearning]] — what interpretability tools detect.
- [[ResponsibleAIEngineering]] — the discipline.
- [[mlsysbook-ch15-responsible-engineering]] — source.
