<!-- Source: https://hypothesis.readthedocs.io/en/latest/explanation/domain.html
     Captured 2026-06-05 via Claude Code WebFetch (agent-converted markdown, not byte-verbatim). -->

# Domain and Distribution

## Overview

Hypothesis distinguishes between two key concepts in property-based testing:

**Domain**: The complete set of possible inputs a strategy can generate. For example, `lists(integers())` has a domain of all integer lists.

**Distribution**: The probability with which different domain elements are generated — whether small or large lists, positive or negative numbers, etc.

## Core Philosophy

Hypothesis maintains a deliberate design stance: "while users may be responsible for selecting the domain, the property-based testing library — not the user — should be responsible for selecting the distribution."

## How to Choose a Domain

The documentation recommends selecting "the most-general strategy for your test, so that it can in principle generate any edge case for which the test should pass." Overly restrictive domains risk excluding bug-triggering values.

Size limitations should only be implemented after observing substantial performance slowdowns. The documentation notes that "Far better to find bugs slowly, than not find them at all" and suggests using settings like `phases` or `max_examples` for performance management instead.

## Why Distribution Control Is Excluded

Three primary reasons explain this design choice:

1. **Human limitations**: People tend to over-tune for known bugs while under-preparing for unknown ones.
2. **Context dependency**: Optimal distributions vary based on both the codebase and specific property being tested.
3. **Implementation flexibility**: Distribution remains an internal detail, allowing Hypothesis to improve without breaking public APIs.

The documentation notes that alternative backends like `hypofuzz` and `crosshair` better serve users needing distribution control.

## Distribution Details

Hypothesis employs a complex, multi-faceted approach optimized for bug discovery rather than uniform or realistic input generation, including static strategy design, dynamic engine features, source code analysis, and swarm testing techniques.
