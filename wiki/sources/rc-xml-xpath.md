---
title: "XML/XPath (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, xml, xpath, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/XML/XPath
---

## Summary
This task asks the programmer to run three XPath queries against a fixed sample XML inventory document and act on the results. The point is to demonstrate how a given language parses XML and applies XPath expressions to select nodes, rather than to author bespoke parsing logic. It exercises selecting a single element by position, iterating over matched nodes, and collecting all matches of a given element name.

## Task Requirements
- Run `//item[1]` to retrieve the first `item` element in the document.
- Run `//price/text()` to act on each `price` element by printing its text value.
- Run `//name` to get an array/collection of all `name` elements.
- Operate on the provided `inventory` XML document containing nested `section` and `item` nodes (each with `name`, `price`, and `description` children).

## Language Coverage
62 languages implement this task, showing broad support across general-purpose languages with XML/XPath libraries as well as XML-native technologies. Representative implementations include Python, Java, C#, C++, Perl, Ruby, JavaScript, Tcl, Haskell, and the XML-domain languages XSLT, XQuery, and XProc.

## Connections
- [[XPath]] — the query language used to address nodes in the document
- [[XML]] — the markup format being parsed and queried
- [[DocumentObjectModel]] — the tree model most implementations navigate
- [[DeclarativeQuerying]] — selecting nodes by pattern rather than imperative traversal

## Contradictions
- None — reference task page.
