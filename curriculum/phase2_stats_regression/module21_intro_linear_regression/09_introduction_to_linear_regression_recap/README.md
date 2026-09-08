# Introduction to Linear Regression - Recap

> Part of **Topic 18: Introduction to Linear Regression** · source item type: WikiPage

---
## Introduction

This short lesson summarizes the topics we covered in this section and why they'll be important to you as a data scientist.

## Key Takeaways

In this section, the nominal focus was on how to perform a linear regression, but the real value was learning how to think about the application of machine learning models to data sets.

Key takeaways include:

- Statistical learning theory deals with the problem of finding a predictive function based on data
- A loss function calculates how well a given model represents the relationship between data values
- A linear regression is simply a (straight) line of best fit for predicting a continuous value (y = mx + c)
- The Coefficient of Determination (R Squared) can be used to determine how well a given line fits a given data set
- Certain assumptions must hold true for a least squares linear regression to be useful - linearity, normality and heteroscedasticity
- Q-Q plots can check for normality in residual errors
- The Jarque-Bera test can be used to test for normality - especially when the number of data points is large
- The Goldfeld-Quant test can be used to check for homoscedasticity

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
