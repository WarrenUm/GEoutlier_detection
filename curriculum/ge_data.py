"""Shared data-loading helpers for the OSRS statistics -> ML curriculum.

Thin, read-only access layer over the InfluxDB 3 Enterprise store owned by the
sibling ``python_InfluxDB`` project. Connection settings are read from the
environment / a git-ignored ``.env`` (never hardcoded), and all queries are
parameterized and time-bounded, following ``.kiro/steering/data-access.md``.

Typical use from a notebook::

    from ge_data import load_series, FIRE_RUNE
    import datetime as dt

    df = load_series(FIRE_RUNE, start="2023-01-01", stop="2023-02-01", interval="1h")
    df["avgHighPrice"].plot()

This module is intentionally self-contained (it talks to InfluxDB 3 directly via
``influxdb3-python``) so the curriculum does not hard-depend on importing the
``ge_pipeline`` package from the other project. It mirrors that package's query
conventions: camelCase identifiers are double-quoted and user values are bound
as query parameters.
"""

from __future__ import annotations

import datetime as _dt
import os
from functools import lru_cache

import pandas as pd
from dotenv import load_dotenv
from influxdb_client_3 import InfluxDBClient3

__all__ = [
    "FIRE_RUNE",
    "MEASUREMENT",
    "PRICE_FIELDS",
    "get_client",
    "list_items",
    "load_series",
    "load_frame",
    "to_unix_seconds",
]

#: Measurement / table holding every price snapshot.
MEASUREMENT = "itemPrice"

#: The four price/volume fields stored per item snapshot.
PRICE_FIELDS = ("avgHighPrice", "avgLowPrice", "highPriceVolume", "lowPriceVolume")

#: High-volume reference item (Fire rune); trades in essentially every window,
#: so it is a good default for smoke tests and examples.
FIRE_RUNE = "554"

# Double-quoted identifiers keep the camelCase names case-sensitive in SQL.
_QUOTED_MEASUREMENT = f'"{MEASUREMENT}"'
_QUOTED_FIELDS = ", ".join(f'"{name}"' for name in PRICE_FIELDS)
_REQUIRED_ENV = ("INFLUXDB3_HOST_URL", "INFLUXDB3_AUTH_TOKEN", "INFLUXDB3_DATABASE_NAME")

# Supported duration suffixes for interval strings, mapped to seconds.
_DURATION_UNITS = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}


def to_unix_seconds(value: int | float | str | _dt.datetime | _dt.date) -> int:
    """Coerce a timestamp-like value into whole unix seconds (UTC).

    Args:
        value: A unix-seconds number, an ISO date/datetime string
            (e.g. ``"2023-01-01"``), a :class:`datetime.datetime`, or a
            :class:`datetime.date`. Naive datetimes are assumed to be UTC.

    Returns:
        The moment as whole unix seconds.
    """
    if isinstance(value, bool):  # guard: bool is a subclass of int
        raise TypeError("bool is not a valid timestamp")
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, _dt.datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=_dt.timezone.utc)
        return int(value.timestamp())
    if isinstance(value, _dt.date):
        return int(_dt.datetime(value.year, value.month, value.day, tzinfo=_dt.timezone.utc).timestamp())
    # Fall back to pandas for ISO strings / numpy datetimes.
    ts = pd.Timestamp(value)
    if ts.tzinfo is None:
        ts = ts.tz_localize("UTC")
    return int(ts.timestamp())


def _interval_seconds(interval: str) -> int:
    """Parse a duration string (e.g. ``"5m"``, ``"1h"``) into whole seconds."""
    text = interval.strip().lower()
    if not text:
        raise ValueError("interval must be a non-empty duration string")
    unit = text[-1]
    if unit.isdigit():
        seconds = int(text)
    else:
        if unit not in _DURATION_UNITS:
            raise ValueError(
                f"unsupported interval unit {unit!r}; expected one of "
                f"{sorted(_DURATION_UNITS)}"
            )
        seconds = int(text[:-1]) * _DURATION_UNITS[unit]
    if seconds <= 0:
        raise ValueError("interval must be a positive duration")
    return seconds


@lru_cache(maxsize=None)
def get_client() -> InfluxDBClient3:
    """Return a reusable InfluxDB 3 client built from the environment.

    Loads ``.env`` (without overriding real environment values) on first use and
    caches the client so repeated calls reuse one connection.

    Returns:
        A configured :class:`influxdb_client_3.InfluxDBClient3`.

    Raises:
        RuntimeError: If any required connection variable is unset or empty.
    """
    load_dotenv(override=False)
    missing = [name for name in _REQUIRED_ENV if not os.environ.get(name)]
    if missing:
        raise RuntimeError(
            "Missing InfluxDB 3 connection variable(s): "
            f"{', '.join(missing)}. Copy .env.example to .env and fill them in "
            "(see .kiro/steering/data-access.md)."
        )
    return InfluxDBClient3(
        host=os.environ["INFLUXDB3_HOST_URL"],
        token=os.environ["INFLUXDB3_AUTH_TOKEN"],
        database=os.environ["INFLUXDB3_DATABASE_NAME"],
    )


def _query(query: str, params: dict) -> pd.DataFrame:
    """Run a parameterized SQL query and return a pandas DataFrame."""
    result = get_client().query(query=query, language="sql", query_parameters=params)
    if result is None:
        return pd.DataFrame()
    if isinstance(result, pd.DataFrame):
        return result
    if hasattr(result, "read_all"):
        result = result.read_all()
    if hasattr(result, "to_pandas"):
        return result.to_pandas()
    return pd.DataFrame(result)


def _select_fields(interval: str | None) -> str:
    """Return the SELECT field list, averaged per bin when downsampling."""
    if interval is None:
        return _QUOTED_FIELDS
    return ", ".join(f'avg("{name}") AS "{name}"' for name in PRICE_FIELDS)


def load_series(
    item_id: str,
    start: int | float | str | _dt.datetime | _dt.date,
    stop: int | float | str | _dt.datetime | _dt.date,
    interval: str | None = "1h",
) -> pd.DataFrame:
    """Load one item's price series as a time-indexed DataFrame.

    Args:
        item_id: The ``itemID`` tag value (a string, e.g. ``"554"``).
        start: Inclusive range start (unix seconds, ISO string, or datetime).
        stop: Exclusive range end (unix seconds, ISO string, or datetime).
        interval: Downsample bin (e.g. ``"1h"``, ``"1d"``) applying a per-bin
            mean, or ``None`` for raw 5-minute data. Defaults to ``"1h"``; keep
            an interval for anything beyond a few days to stay under the store's
            query-file limit.

    Returns:
        A DataFrame indexed by UTC ``time`` with the four price/volume columns,
        sorted ascending by time. Empty when the item has no data in range.
    """
    start_s, stop_s = to_unix_seconds(start), to_unix_seconds(stop)
    params = {"item_id": item_id, "start": start_s, "stop": stop_s}
    where = (
        '"itemID" = $item_id '
        "AND time >= to_timestamp_seconds(CAST($start AS BIGINT)) "
        "AND time < to_timestamp_seconds(CAST($stop AS BIGINT))"
    )
    if interval is None:
        query = (
            f"SELECT time, {_QUOTED_FIELDS} FROM {_QUOTED_MEASUREMENT} "
            f"WHERE {where} ORDER BY time"
        )
    else:
        bin_expr = f"date_bin(INTERVAL '{_interval_seconds(interval)} seconds', time)"
        query = (
            f"SELECT {bin_expr} AS time, {_select_fields(interval)} "
            f"FROM {_QUOTED_MEASUREMENT} WHERE {where} "
            f"GROUP BY {bin_expr} ORDER BY time"
        )
    frame = _query(query, params)
    return _time_index(frame)


def load_frame(
    item_ids: list[str],
    start: int | float | str | _dt.datetime | _dt.date,
    stop: int | float | str | _dt.datetime | _dt.date,
    interval: str | None = "1h",
) -> pd.DataFrame:
    """Load several items into one long-form DataFrame.

    Args:
        item_ids: The ``itemID`` tag values to include (non-empty).
        start: Inclusive range start (unix seconds, ISO string, or datetime).
        stop: Exclusive range end (unix seconds, ISO string, or datetime).
        interval: Downsample bin (per-bin mean) or ``None`` for raw data.

    Returns:
        A long-form DataFrame with columns ``itemID``, ``time`` (UTC), and the
        four price/volume fields, sorted by ``itemID`` then ``time``. Empty when
        ``item_ids`` is empty or no rows match.
    """
    if not item_ids:
        return pd.DataFrame()
    start_s, stop_s = to_unix_seconds(start), to_unix_seconds(stop)
    placeholders = [f"id{i}" for i in range(len(item_ids))]
    params: dict = dict(zip(placeholders, item_ids))
    params["start"], params["stop"] = start_s, stop_s
    in_list = ", ".join(f"${name}" for name in placeholders)
    where = (
        f'"itemID" IN ({in_list}) '
        "AND time >= to_timestamp_seconds(CAST($start AS BIGINT)) "
        "AND time < to_timestamp_seconds(CAST($stop AS BIGINT))"
    )
    if interval is None:
        query = (
            f'SELECT "itemID", time, {_QUOTED_FIELDS} FROM {_QUOTED_MEASUREMENT} '
            f'WHERE {where} ORDER BY "itemID", time'
        )
    else:
        bin_expr = f"date_bin(INTERVAL '{_interval_seconds(interval)} seconds', time)"
        query = (
            f'SELECT "itemID", {bin_expr} AS time, {_select_fields(interval)} '
            f"FROM {_QUOTED_MEASUREMENT} WHERE {where} "
            f'GROUP BY "itemID", {bin_expr} ORDER BY "itemID", time'
        )
    frame = _query(query, params)
    if not frame.empty and "time" in frame.columns:
        frame["time"] = pd.to_datetime(frame["time"], utc=True)
    return frame.reset_index(drop=True)


def list_items(
    start: int | float | str | _dt.datetime | _dt.date,
    stop: int | float | str | _dt.datetime | _dt.date,
) -> list[str]:
    """Return distinct item ids traded within a time window.

    The scan is deliberately time-bounded so it stays under the store's
    ``--query-file-limit`` (an unbounded ``SELECT DISTINCT`` can scan the whole
    store).

    Args:
        start: Inclusive start of the window (unix seconds, ISO string, datetime).
        stop: Exclusive end of the window.

    Returns:
        A sorted list of distinct ``itemID`` values seen in the window.
    """
    params = {"start": to_unix_seconds(start), "stop": to_unix_seconds(stop)}
    query = (
        f'SELECT DISTINCT "itemID" FROM {_QUOTED_MEASUREMENT} '
        "WHERE time >= to_timestamp_seconds(CAST($start AS BIGINT)) "
        "AND time < to_timestamp_seconds(CAST($stop AS BIGINT)) "
        'ORDER BY "itemID"'
    )
    frame = _query(query, params)
    if frame.empty or "itemID" not in frame.columns:
        return []
    return [str(v) for v in frame["itemID"].tolist() if v is not None]


def _time_index(frame: pd.DataFrame) -> pd.DataFrame:
    """Return ``frame`` indexed by a UTC ``time`` column, sorted ascending."""
    if frame.empty or "time" not in frame.columns:
        return frame
    frame = frame.copy()
    frame["time"] = pd.to_datetime(frame["time"], utc=True)
    return frame.set_index("time").sort_index()
