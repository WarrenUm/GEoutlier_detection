# Curriculum

New work for the OSRS statistics → ML curriculum lives here, one folder per
module. Each module follows the same pattern from the root
[`README.md`](../README.md) roadmap: **pull data → state the question → apply the
method → check assumptions → interpret in market terms.**

## Layout

```
curriculum/
├── ge_data.py                 # shared read-only data-loading helpers (import from any module)
├── module00_foundations/
│   └── 00_foundations.ipynb   # Module 0 starter: connect, load, downsample, reshape
└── module01_.../              # add later modules as folders here
```

## Getting started

1. From the repo root, copy `.env.example` to `.env` and fill in the InfluxDB 3
   connection values (see [`../.kiro/steering/data-access.md`](../.kiro/steering/data-access.md)).
2. Install the base stack: `pip install -r ../requirements.txt`.
3. Open `module00_foundations/00_foundations.ipynb` in the IDE, select the
   Python 3.12 kernel, and run all cells. It doubles as the connection smoke test.

## The `ge_data` helper

`ge_data.py` is a thin, **read-only** layer over the InfluxDB 3 store. Import it
from any module notebook:

```python
from ge_data import load_series, load_frame, list_items, FIRE_RUNE

df = load_series(FIRE_RUNE, start="2023-01-01", stop="2024-01-01", interval="1h")
```

- `load_series(item_id, start, stop, interval)` — one item, time-indexed DataFrame.
- `load_frame(item_ids, start, stop, interval)` — many items, long-form DataFrame.
- `list_items(start, stop)` — distinct item ids traded in a (bounded) window.

`start`/`stop` accept unix seconds, ISO strings (`"2023-01-01"`), or datetimes.
Pass an `interval` (e.g. `"1h"`, `"1d"`) for anything beyond a few days; use
`interval=None` for raw 5-minute data only on short windows. This project never
writes to the store — collection lives in the sibling `python_InfluxDB` project.
