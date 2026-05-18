---
title: "Resampling"
type: concept
tags: [pandas, time-series, groupby]
sources: [pydata-time-series]
last_updated: 2026-05-15
---

# Resampling

Time-indexed analog of [[SplitApplyCombine|groupby]] in pandas: bin a time series into fixed-frequency intervals and aggregate. Operates on a [[pandasIndex|DatetimeIndex]] / `PeriodIndex` / `TimedeltaIndex`.

## API
```python
ts.resample("M").mean()            # downsample to month-end, mean each bin
ts.resample("D").ffill()           # upsample, forward-fill missing
ts.resample("5min").ohlc()         # OHLC bars per 5-minute window
df.groupby(pd.Grouper(freq="W-MON"))  # combine with column groupby
```

## Options
- `closed="left"/"right"` — which edge of the bin is closed.
- `label="left"/"right"` — which edge labels the bin.
- `loffset=` — shift labels by an offset.

## Connections
- [[pandas]] / [[SplitApplyCombine]] — generalized groupby pattern.
- [[pandasIndex]] / [[DatetimeIndex]] — required input axis.
- [[pydata-time-series]] — chapter 11 covers depth.
