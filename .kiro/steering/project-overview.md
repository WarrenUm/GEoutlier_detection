# Project Overview

`GEoutlier_detection` is the **analysis and modeling** half of a two-project OSRS
(Old School RuneScape) Grand Exchange data-science stack. Its sibling project,
`python_InfluxDB` (open in this workspace), owns **data collection and storage**:
it ingests 5-minute Grand Exchange price snapshots from the RuneScape Wiki Prices
API into an **InfluxDB 3 Enterprise** time-series database. This project reads
from that store and uses the data as the running example for a **complete
data-science curriculum** — a four-phase adaptation of a full bootcamp syllabus
(53 topics) covering Python and tooling foundations, SQL/APIs/scraping,
probability and statistics, regression, the core machine-learning algorithm
suite, time-series forecasting, and deep learning (including NLP, graphs, and
MLOps), all re-grounded in OSRS market data.

> **Goal:** learn and demonstrate the full data-science stack end to end, using
> real OSRS market data as the worked example throughout. The README holds the
> phased topic roadmap; each numbered topic becomes a notebook or script in
> `curriculum/` that pulls data from InfluxDB, applies the method, and interprets
> the result in market terms.

## Two-project split

| Project | Role | Owns |
|---------|------|------|
| `python_InfluxDB` | **Data platform** | Ingestion pipeline (`ge_pipeline`), InfluxDB 3 Enterprise store, FastAPI query API, Grafana, React SPA |
| `GEoutlier_detection` (this) | **Analysis / modeling** | Notebooks and scripts that read the store and work the full data-science curriculum (tooling → statistics → ML → deep learning); the phased learning roadmap |

This project does **not** ingest or write price data. It is a **read-only
consumer** of the store that `python_InfluxDB` maintains. Any need to change how
data is collected, stored, or served belongs in `python_InfluxDB`, not here.

## Where the data comes from

The single source of truth is the InfluxDB 3 Enterprise database `GEItemPrices`
managed by `python_InfluxDB`. See `.kiro/steering/data-access.md` for exact
connection details, the schema, and the recommended read paths. Summary:

- **Engine / endpoint:** InfluxDB 3 Enterprise, HTTP + Flight/gRPC on `:8181`.
  Default to the remote server `http://192.168.1.85:8181` for the live
  deployment; `http://localhost:8181` is the portable single-host default.
- **Database:** `GEItemPrices`.
- **Schema:** measurement `itemPrice`; tag `itemID` (string); fields
  `avgHighPrice`, `avgLowPrice`, `highPriceVolume`, `lowPriceVolume`; unix-second
  timestamps at 5-minute granularity; history from ~March 2021 onward.
- **Auth:** local dev runs `--without-auth`, so any non-empty token is accepted.

## Curriculum source

The roadmap's phase-and-topic structure is a complete adaptation of a full
data-science bootcamp syllabus (a Flatiron-School-style Canvas/LMS export,
*Data Science Full Curriculum*, ~53 topics across four phases) present in the
workspace. Every source topic is represented in the README and re-grounded in
OSRS market data; the README's Sources section credits it. Two project-specific
topics — financial-econometrics/GARCH forecasting depth and anomaly/outlier
detection — extend the source to match this project's focus.

> A separate workspace folder named **`osrs market data`** contains only Windows
> PowerShell launcher scripts and an older nested copy of `python_InfluxDB`. It
> is **data-platform tooling, not curriculum**, and should not be treated as a
> source for analysis work here.

## History (legacy code)

This repo began as an exploratory project that fetched snapshots from the
RuneScape Wiki API and stored them in CSV files (`prices/`) and a SQLite
database via a scheduler. The **fetch and DB-update code has been removed** —
data collection and storage now live entirely in `python_InfluxDB`. Only
exploratory analysis notebooks (`notebooks/`, `old ntbks/`) and raw CSV
snapshots (`prices/`) remain, as historical reference:

- Do **not** build new analysis on the `prices/*.csv` files or reintroduce the
  legacy Wiki-API fetch / SQLite code.
- New work reads from InfluxDB 3 through the paths in `data-access.md` and lives
  in `curriculum/`.
- Dependencies are pinned in `requirements.txt` (base) and `requirements-dl.txt`
  (deep-learning extras), targeting Python 3.12.

## Layout

```
GEoutlier_detection/
├── README.md              # the statistics -> ML learning roadmap (TOC + sources)
├── requirements.txt       # base analysis/modeling stack (Modules 0-11)
├── requirements-dl.txt    # deep-learning extras (Module 12)
├── .env.example           # InfluxDB 3 connection variables (copy to .env)
├── curriculum/            # new work: one folder per module (start here)
├── notebooks/             # legacy exploratory notebooks (historical reference)
├── old ntbks/             # older notebooks (historical reference)
├── prices/                # legacy CSV snapshots (historical reference)
└── .kiro/steering/        # project steering (this folder)
```

New curriculum work lives in `curriculum/`, organized by module, so it is not
confused with the legacy material.
