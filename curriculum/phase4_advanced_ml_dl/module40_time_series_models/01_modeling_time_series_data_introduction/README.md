# Modeling Time Series Data - Introduction

> Part of **Topic 38: Time Series Models** · source item type: WikiPage

---
## Introduction

In this section, you'll learn about modeling for time series data.

## Time Series Modeling

In the previous section, we introduced the idea of time series data and provided some best practices for importing, managing, and visualizing time series data along with a number of techniques for removing trends and/or seasonality from a time series dataset. In this section, we're going to look at various types of models for time series data.

### Basic Time Series Models

We start off by introducing two basic time series models -- the white noise and random walk models.

### Correlation, Autocorrelation, and Partial Autocorrelation

We will then move on to the concept of correlation as it relates to time series datasets, and plot the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) for a time series.

### ARMA Models

We then move on to introduce two other key time series models that are widely used for predicting future values for time series data - the auto regressive (AR) and moving average (MA) models.

## Summary

Let's get started! This section wraps up our introduction to time series analysis, giving you the modeling tools required to effectively forecast time series data.

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
