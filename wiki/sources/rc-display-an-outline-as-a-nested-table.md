---
title: "Display an outline as a nested table (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, tree-data-structure, parsing, html]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Display_an_outline_as_a_nested_table
---

## Summary
The task asks the programmer to convert an indented text outline into a nested table rendered as WikiTable or HTML markup, with `colspan` values on parent cells. The key insight is that an indented outline is really a tree, and the `colspan` of any node equals the number of leaves descending from it: a leaf has width 1 and a parent's width is the sum of its children's widths. Producing the table requires measuring indentation, building the tree, padding it to uniform depth, and emitting one table row per tree level.

## Task Requirements
- Parse an outline with at least three levels of indentation into a tree by measuring each line's indent.
- Translate the indentation into a nested structure and pad the tree so every branch reaches even (uniform) depth.
- Count leaves under each node: leaf width = 1, parent width = sum of children's widths.
- Emit a nested table (WikiTable markup or HTML) attaching `colspan` values to parent nodes where needed.
- Extra credit: assign each level-two subtree a consistent background color to visually distinguish the main stages.

## Language Coverage
18 languages implement this task, spanning functional, imperative, and array styles. Representative entries include Haskell, J, Java, JavaScript, Python, Perl, Raku, Go, Julia, Nim, Phix, Wren, jq, and ALGOL 68.

## Connections
- [[TreeDataStructure]] — the outline is parsed into a tree before rendering
- [[TreeTraversal]] — leaf counting and width sums require walking the tree
- [[Recursion]] — computing parent widths as sums of child widths is naturally recursive
- [[TextParsing]] — indentation depth is measured to recover hierarchy
- [[HTML]] — output target using `colspan` on table cells

## Contradictions
- None — reference task page.
