---
title: "Regression Testing"
type: concept
tags: [testing, quality]
sources: [madewithml-testing, fuzzingbook-02-intro-testing, fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Regression Testing

Re-running tests to confirm that new changes have not broken previously working behavior. In ML contexts, extends to dataset and model output stability, run via [[Pytest]] in CI.

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] makes the case for regression testing as a payoff of [[TestAutomation|automation]]: once a test is automated, "we can run it again and again" and "repeat this test with every single change," reinforcing confidence that prior behavior still holds. The chapter's [[Assertion|assert]]-based [[TestOracle|oracle]] over generated inputs is exactly the kind of cheap check meant to be re-run after every edit.

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]]'s `ResultCarver` exercise extends [[TestCarving|carving]] to regression testing: by subclassing [[Carver|`CallCarver`]] to record `return` events alongside calls, it can synthesize `assert call == recorded_result` checks (demonstrated on `urllib.parse.urlparse()`/`urlsplit()`), forming a regression suite that flags when a code change alters previously observed behavior. The chapter notes the [[RecordReplay|replay]] caveat that values depending on time, randomness, or external state may legitimately differ, so such carved assertions suit functionality that abstracts from those details.
