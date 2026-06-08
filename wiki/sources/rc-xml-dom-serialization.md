---
title: "XML/DOM serialization (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, xml, serialization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/XML/DOM_serialization
---

## Summary
This task asks the programmer to construct a simple in-memory Document Object Model (DOM) tree — a root element containing a child element that holds some text — and then serialize it back out to a well-formed XML string with the XML declaration. The key insight is exercising the round trip from a programmatic node tree to its textual representation, rather than parsing XML.

## Task Requirements
- Build a DOM (or equivalent node tree) representing `<root><element>Some text here</element></root>`.
- Serialize that DOM to an XML string that includes the `<?xml version="1.0" ?>` declaration.
- Produce well-formed, properly nested output matching the given structure.

## Language Coverage
57 languages implement this task, spanning systems languages, scripting languages, functional languages, and XML-native tooling. Representative implementations include C, C++, C#, Java, Python, Ruby, Perl, Go, Haskell, JavaScript, and the XML-specific XProc, XQuery, and XSLT.

## Connections
- [[DocumentObjectModel]] — the in-memory tree abstraction being built and walked
- [[Serialization]] — converting the structured object tree into a textual byte stream
- [[XML]] — the target markup format and its declaration/nesting rules
- [[TreeTraversal]] — emitting nodes in document order to render the output

## Contradictions
- None — reference task page.
