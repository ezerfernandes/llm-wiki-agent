---
title: "Distance and Bearing (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, geospatial, trigonometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Distance_and_Bearing
---

## Summary
Given an airplane's position as a latitude/longitude pair, the task is to find the 20 nearest airports and report the great-circle distance and compass bearing to each. The reference dataset is openflights.org's `airports.dat`, and the key insight is computing distances on a sphere using the haversine formula and initial bearing from the trigonometric forward-azimuth formula, then sorting the airports by distance to pick the closest twenty.

## Task Requirements
- Read the openflights.org `airports.dat` dataset as reference.
- For the query position (latitude 51.514669, longitude 2.198581), determine the 20 nearest airports.
- For each, report Name (col 2), Country (col 4), ICAO code (col 6), and the computed distance and bearing using Latitude (col 7) and Longitude (col 8).
- Distance in nautical miles (NM) at 0.1 NM resolution.
- Bearing in degrees (0/360 = north, 90 = east, 180 = south, 270 = west) at 1 degree resolution.

## Language Coverage
20 languages implement this task, spanning systems and scripting languages with a notable presence of BASIC dialects; representative solutions include C, C++, Fortran, Go, Java, Julia, Python, Perl, Raku, Ruby, and even a SQL/PostgreSQL version.

## Connections
- [[HaversineFormula]] — computes great-circle distance between two lat/long points
- [[GreatCircleDistance]] — the spherical-geometry distance being measured
- [[Bearing]] — initial forward azimuth between two geographic points
- [[Trigonometry]] — sine/cosine/atan2 underpin both distance and bearing
- [[Geocoding]] — working with the openflights airport coordinate dataset

## Contradictions
- None — reference task page.
