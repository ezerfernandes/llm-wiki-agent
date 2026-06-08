---
title: "Motor (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, geometric-algebra, linear-algebra]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Motor
---

## Summary
A motor is the operator in geometric algebra that represents a general rigid-body
motion — a combined rotation and translation, i.e. a screw motion. The task asks the
programmer to implement a motor type, typically as a pairing of a rotor (the rotation
part) and a screw/translation part, and to construct motors from geometric primitives
such as pairs of points, lines, or planes. The key insight is that a single motor object
can compose and apply rigid transformations uniformly, generalizing the quaternion-based
rotor by adding a translational component.

## Task Requirements
- Define a motor data type that bundles a rotor part with a screw (translation) part.
- Provide constructors that build a motor from geometric inputs (e.g. two points, two lines, two planes).
- Support unitization/normalization of the motor.
- Allow the motor to compose with other motors and act on geometric elements.

## Language Coverage
7 languages implement this task — a small set, reflecting that it is an advanced
geometric-algebra exercise. Representative implementations include C, C++, FreeBASIC,
Julia, Phix, Pluto, and Wren.

## Connections
- [[GeometricAlgebra]] — the algebraic framework defining motors and their products
- [[Rotor]] — the rotation-only operator that a motor extends with translation
- [[Quaternion]] — closely related rotation representation underlying rotors
- [[ScrewMotion]] — the rigid motion (rotation + translation along an axis) a motor encodes
- [[Bivector]] — the geometric-algebra element used to express rotations and the motor's structure

## Contradictions
- None — reference task page.
