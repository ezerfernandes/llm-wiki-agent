---
title: "Bitmap/Read a PPM file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, file-io, image-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Read_a_PPM_file
---

## Summary
The task asks the programmer to read an image from a PPM (Portable Pixmap) file into the in-memory raster bitmap type defined in the Basic Bitmap Storage task, with the binary P6 variant preferred over the ASCII P3 variant. The key insight is parsing the PPM header (magic number, width, height, max color value) and then reading the raw RGB pixel triples that follow. As a follow-on, the result is combined with the write-PPM and grayscale-image solutions to convert a color image to grayscale.

## Task Requirements
- Read an image from a PPM file into the raster image storage type from the Basic Bitmap Storage task.
- Support the binary P6 format (preferred); ASCII P3 may also be handled.
- Correctly parse the PPM header: magic number, dimensions, and maximum color value.
- Combine with the write-PPM and grayscale solutions to convert a color image to grayscale.

## Language Coverage
52 languages implement this task, spanning systems languages, functional languages, and scripting languages. Representative implementations include C, C#, Rust, Go, Java, Haskell, OCaml, Python, Ruby, Perl, and Common Lisp.

## Connections
- [[PortablePixmapFormat]] — the Netpbm PPM file format being parsed
- [[RasterGraphics]] — bitmap storage model the image is read into
- [[BinaryFileParsing]] — reading the P6 header and raw RGB byte stream
- [[GrayscaleConversion]] — downstream use combining color-to-grayscale

## Contradictions
- None — reference task page.
