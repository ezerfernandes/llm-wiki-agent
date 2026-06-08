---
title: "Bitmap/Write a PPM file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, file-format, image-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Write_a_PPM_file
---

## Summary
This task asks the programmer to serialize an in-memory raster image (the bitmap storage type defined in the companion Basic bitmap storage task) out to a PPM file on disk. The preferred encoding is the binary P6 variant of the Netpbm portable pixmap format. The key insight is the simplicity of the format: a short ASCII header (magic number, width, height, and maximum color value) followed by raw RGB triplets, one byte per channel.

## Task Requirements
- Use the raster image data storage type from the Basic bitmap storage task.
- Write that image out to a PPM file.
- Use the binary P6 encoding in preference to the ASCII P3 variant.
- Conform to the Netpbm PPM file definition (magic number `P6`, whitespace-separated width/height/maxval header, then binary pixel data).

## Language Coverage
68 languages implement this task, reflecting broad coverage across systems, scripting, and functional languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Perl, Ruby, and Fortran.

## Connections
- [[NetpbmFormat]] — the family of portable image formats (PBM/PGM/PPM) this task targets.
- [[RasterGraphics]] — the pixel-grid image model being serialized.
- [[BinaryFileIO]] — writing raw byte streams rather than text for the P6 variant.
- [[ImageSerialization]] — encoding an in-memory bitmap to a persistent file format.

## Contradictions
- None — reference task page.
