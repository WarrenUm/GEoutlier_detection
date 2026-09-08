# Modeling Time Series Data - Recap

> Part of **Topic 38: Time Series Models** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- A white noise model has a fixed and constant mean and variance, and no correlation over time

- A random walk model has no specified mean or variance, but has a strong dependence over time

- The Pandas `.corr()` method can be used to return the correlation between various time series in the DataFrame

- Autocorrelation allows us to identify how strongly each time series observation is related to previous observations

- The Autocorrelation Function (ACF) is a function that represents autocorrelation of a time series as a function of the time lag

- The Partial Autocorrelation Function (or PACF) gives the partial correlation of a time series with its own lagged values, controlling for the values of the time series at all shorter lags

- ARMA (Autoregressive and Moving Average) modeling is a tool for forecasting time series values by regressing the variable on its own lagged (past) values

- ARMA models assume that you've already detrended your data and that there is no seasonality

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.

## Folded-in exercise material

This lesson includes the original hands-on material, converted for local use:

- [`lab.ipynb`](lab.ipynb) — the original exercise notebook. Work through
  it, or copy the parts you want into `work.ipynb`. `pytest` runs it too.
- `min_temp.csv` — supporting data/helper file for the exercise.
- `temp.csv` — supporting data/helper file for the exercise.
