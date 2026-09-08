# Multiple Regression and Model Validation - Recap

> Part of **Topic 19: Multiple Regression and Model Validation** · source item type: WikiPage

---
## Introduction

In this section you extended your knowledge of building regression models by adding additional predictive variables and subsequently validating those models using train-test-split and cross validation.

## Multiple Regression

You saw a number of techniques and concepts related to regression. This included the idea of using multiple predictors in order to build a stronger estimator. That said, there were caveats to using multiple predictors. For example, multicollinearity between variables should be avoided. One option for features with particularly high correlation is to only use one of these features. This improves model interpretability. In addition, linear regression is also most effective when features are of a similar scale. Typically, feature scaling and normalization are used to achieve this. There are also other data preparation techniques such as creating dummy variables for categorical variables, and transforming non-normal distributions using functions such as logarithms. Finally, in order to validate models it is essential to always partition your dataset such as with train-test splits or k-fold cross validation.

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
- `ames.csv` — supporting data/helper file for the exercise.
- `data_description.txt` — supporting data/helper file for the exercise.
- `overfit_underfit.png` — supporting data/helper file for the exercise.
