# Coding Standards

Standards for the analysis and modeling work in this project. The focus is
reproducible, readable notebooks and scripts that read from the InfluxDB 3 store
and apply statistics / ML methods.

## Python Style

- Target Python 3.11+. Follow PEP 8 (snake_case for functions and variables).
- Add type hints to reusable function signatures; use `X | None` unions.
- Add short docstrings (summary, Args, Returns) to shared/helper functions.
- Keep functions focused and single-purpose; factor repeated notebook logic into
  a small local module rather than copy-pasting across notebooks.

## Data Access

- Read price data only from the InfluxDB 3 store — see
  `.kiro/steering/data-access.md`. Do not build new work on the legacy
  `geitems.db` or `prices/*.csv` files.
- Prefer the `ge_pipeline` read helpers or the FastAPI query API over hand-rolled
  SQL. When writing raw InfluxDB 3 SQL, double-quote the camelCase identifiers
  and bind item ids / time bounds as query parameters — never interpolate them.
- Always bound time ranges; downsample with an `interval` for long-range or
  plotting queries. Avoid unbounded whole-store scans.
- This project is read-only against the store. Never write or delete price data.

## Configuration

- Never hardcode secrets, tokens, hosts, or file paths in notebooks or source.
- Load connection settings from the environment / a git-ignored `.env`
  (`INFLUXDB3_HOST_URL`, `INFLUXDB3_AUTH_TOKEN`, `INFLUXDB3_DATABASE_NAME`).
- Document required keys in a placeholder `.env.example`.

## Notebooks

- Notebooks are the primary deliverable for curriculum topics. Each should:
  read data → apply the method → **interpret the result in market terms**.
- Keep a clear narrative: markdown cells stating the question, the method, and
  the takeaway. Show assumptions and how they were checked.
- Restart-and-run-all should reproduce the notebook top to bottom. No reliance
  on hidden out-of-order state.
- Set random seeds for any stochastic step (sampling, train/test split, model
  init) so results are reproducible.
- Keep heavy data pulls parameterized (item ids, date range, interval) near the
  top so a notebook is easy to re-point at a different item or window.
- Do not commit large data dumps or rendered heavy outputs; prefer re-pulling
  from the store.

## Modeling Discipline

- State and check model assumptions (e.g. stationarity for ARIMA, linearity /
  homoscedasticity for OLS) before trusting results.
- For any predictive model, use a **time-aware** train/validation/test split
  (no shuffling across time); never let future data leak into training.
- Report a sensible baseline (e.g. naive / seasonal-naive forecast) alongside
  every model so improvements are measured against it.
- Use appropriate metrics (RMSE/MAE/MAPE for forecasts; accuracy/precision/recall
  /ROC-AUC for classification) and say why.
- Prefer established libraries — `statsmodels`, `scikit-learn`, `pmdarima`,
  `pandas`, `numpy`, `matplotlib`/`plotly` — over re-implementing standard
  methods, except where re-implementing is the learning exercise (then keep it
  clearly labeled as pedagogical).

## Project Hygiene

- Keep new curriculum work separate from the legacy CSV/SQLite notebooks so the
  two are not confused.
- Pin dependencies (a modern `requirements.txt` or `pyproject.toml`); the
  existing `requirements.txt` predates this direction and should be refreshed
  before reuse.
- Use the `logging` module for operational messages in scripts; `print` is fine
  inside exploratory notebook cells.
- Remove dead / commented-out code; rely on git history instead.
