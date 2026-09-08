# Data Access

This project is a **read-only consumer** of the InfluxDB 3 Enterprise store owned
by the sibling `python_InfluxDB` project. This file is the reference for how to
connect and pull OSRS Grand Exchange price data into analysis notebooks and
scripts. Never write price data from this project — collection and storage are
`python_InfluxDB`'s job.

## The store

- **Engine:** InfluxDB 3 Enterprise (free At-Home license), Docker container.
- **Endpoint:** HTTP API + Flight/gRPC share one port, `:8181`.
- **Default host:** the live deployment is on the remote server
  `http://192.168.1.85:8181`. `http://localhost:8181` is the portable
  single-host fallback. Always confirm which host a process targets by its
  `INFLUXDB3_HOST_URL` rather than assuming `localhost`.
- **Database:** `GEItemPrices`.
- **Auth:** local dev runs `--without-auth`, so **any non-empty token** is
  accepted. Still pass a token string; never commit real secrets.

## Schema

| Element | Value |
|---------|-------|
| Measurement / table | `itemPrice` |
| Tag | `itemID` (string) |
| Fields | `avgHighPrice`, `avgLowPrice`, `highPriceVolume`, `lowPriceVolume` |
| Timestamp | unix **seconds**, 5-minute granularity |
| History | from ~2021-03-14 onward |

InfluxDB 3 SQL is case-sensitive for these camelCase identifiers, so they must be
**double-quoted** in raw SQL (e.g. `"itemPrice"`, `"itemID"`, `"avgHighPrice"`).
Always bind user values (item ids, time bounds) as **query parameters** — never
interpolate them into query strings.

## Configuration

Connection settings come from the environment (use a git-ignored `.env`, mirror
`python_InfluxDB`'s keys):

```
INFLUXDB3_HOST_URL=http://192.168.1.85:8181
INFLUXDB3_AUTH_TOKEN=any-non-empty-token
INFLUXDB3_DATABASE_NAME=GEItemPrices
```

Keep `.env` git-ignored and document keys in a placeholder `.env.example`.

## Recommended read paths

Prefer, in order:

1. **Reuse `ge_pipeline` read helpers** (from the `python_InfluxDB` project).
   These are already parameterized, memory-bounded, and return tidy pandas
   frames — ideal as analysis inputs:
   - `ge_pipeline.influx.get_client(settings)` — reusable `InfluxDBClient3`.
   - `query_price_series(client, item_id, start, stop, interval)` — one item, a
     time-ascending list of point dicts; `interval` (e.g. `"1h"`) applies
     `date_bin` mean downsampling.
   - `query_chunk(client, item_ids, start, stop, interval)` — many items, a
     combined `DataFrame`.
   - `data_access.build_feature_frame(client, item_ids, start, stop, interval)`
     — a wide, time-indexed, **ML-ready** `DataFrame` (per-item feature columns).
   - `data_access.get_price_page(...)` / `iter_time_chunks(...)` /
     `stream_dataset(...)` — cursor pagination and streaming export for large
     ranges.
   - `list_item_ids(client)` — distinct item ids (time-bound it on large stores).

2. **FastAPI query API** (`ge-pipeline serve` in `python_InfluxDB`) when you
   want a language-agnostic HTTP boundary or the outlier annotations:
   - `GET /api/items`, `GET /api/items/{id}/prices`, `.../prices/page`,
     `.../outliers`, `GET /api/datasets/export` (ndjson/csv/parquet),
     `GET /api/outlier-methods`.
   - Range params like `range=7d` or `range=all`; `interval` like `1h`.
   - Ranges wider than ~7 days require an explicit `interval` (server downsamples).

3. **Direct InfluxDB 3 SQL** via `influxdb3-python` only when the helpers above
   do not cover the query. Follow the double-quote + parameter-binding rules.

## Scale and query-file-limit awareness

The store holds years of 5-minute data. Follow the same discipline the platform
uses:

- **Bound your time ranges.** Whole-store scans (unbounded `SELECT DISTINCT`,
  `COUNT(*)`, `MIN/MAX(time)`) can hit InfluxDB 3's `--query-file-limit`.
  Time-bounded queries are fine.
- **Downsample** with an `interval` for long-range or plotting queries; keep raw
  5-minute resolution only when a method genuinely needs it.
- **Generate time chunks lazily** and stream large exports chunk-by-chunk rather
  than materializing the full history in memory.
- For cheap long-range dashboards, an optional pre-aggregated `itemPrice_1h`
  rollup measurement may exist; pass it as the `measurement` argument to the
  read helpers when present.

## Reference items

Item `554` (Fire rune) is the platform's high-volume reference item and a good
default for smoke tests, since it trades in essentially every 5-minute window.

## Visualizing in the IDE

Exploration happens in notebooks opened directly in Kiro/VS Code. Select the
project's Python 3.12 kernel; `matplotlib`/`seaborn` render inline and `plotly`
renders interactively (via `nbformat` + `ipywidgets`, both in `requirements.txt`).
Prefer this over standing up an external dashboard — Grafana and the React SPA in
`python_InfluxDB` already cover operational dashboards.
