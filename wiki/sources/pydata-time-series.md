---
title: "Python for Data Analysis 3E — Ch.11: Time Series"
type: source
tags: [book, pandas, time-series, datetime, resampling, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/time-series.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/time-series.html
chapter: 11
---

## Summary
Time-series tooling in [[pandas]] — the substrate that made it appealing for finance work in the first place. Covers `datetime`/`timedelta`, string⇄datetime conversion (`pd.to_datetime`, `dateutil.parser.parse`, `strftime`/`strptime`), `DatetimeIndex` selection and slicing, `pd.date_range` with frequencies (`"D"`, `"H"`, `"T"`, `"M"`, `"BM"`, `"WOM-2FRI"`, …) and shifts (`shift(n, freq=...)`), time zone localization / conversion via `pytz`/`zoneinfo`, `Period` and `PeriodIndex` for fixed periods, **resampling** (downsample / upsample / period resampling / `Grouper`), and moving-window functions (`rolling(window=).mean()`, `.std()`, EWMA, binary-window correlations).

## Key Claims
- **datetime stdlib** — `datetime.datetime`, `datetime.timedelta`; `datetime.now()`; `strftime("%Y-%m-%d")` for formatting, `strptime` for parsing fixed format; `dateutil.parser.parse("Jan 31, 1997 10:45 PM")` for flexible parsing.
- **`pd.to_datetime`** — vectorized parser; accepts strings, ints (epoch), arrays; returns `DatetimeIndex`/`Timestamp`.
- **DatetimeIndex selection** — `ts["1/10/2011":"1/31/2011"]` slices by date strings; `ts["2011"]` selects entire year; `ts["2011-05"]` selects month; `ts.truncate(after="...")`.
- **`pd.date_range`** — generate fixed-frequency timestamp index: `pd.date_range("2012-04-01", periods=20, freq="D")`. Frequency aliases: `"D"` daily, `"B"` business day, `"H"` hourly, `"T"`/`"min"` minute, `"S"` second, `"M"` month-end, `"BM"` business month-end, `"MS"` month-start, `"WOM-2FRI"` 2nd Friday of month, `"Q-DEC"` quarter-end in Dec, `"A-DEC"` year-end.
- **shift** — `ts.shift(2)` shifts values forward 2 periods; `ts.shift(2, freq="M")` advances the index by 2 months instead of values.
- **Time zones** — `ts.tz_localize("UTC")` to make naive timestamps tz-aware; `ts.tz_convert("America/New_York")` to convert. Operations between differently-zoned series align in UTC.
- **Period** — fixed period (not instantaneous); `pd.Period("2012", freq="A-DEC")`; `pd.period_range(...)`; `.asfreq("M", how="start"/"end")` converts frequency.
- **Resampling** — `ts.resample("M").mean()` downsamples; `ts.resample("D").ffill()` upsamples with forward-fill. Bin labels controlled by `closed=`, `label=`, `loffset=`. OHLC aggregation: `.resample("5min").ohlc()`.
- **GroupBy + time** — `df.groupby(pd.Grouper(freq="W-MON"))` mixes column groupby with time bucketing.
- **Rolling windows** — `s.rolling(window=20, min_periods=...).mean()` / `.std()`; `s.ewm(span=30).mean()` for exponentially-weighted; binary window funcs like `s1.rolling(60).corr(s2)`.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[pandas]] — time-series API.
- [[DatetimeIndex]] / [[PeriodIndex]] — labeled time axes.
- [[Resampling]] — time-bucketed groupby.
- [[pydata-modeling]] — chapter 12 next.

## Contradictions
- None.
