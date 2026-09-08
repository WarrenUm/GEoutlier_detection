# Regularization - Introduction

> Part of **Topic 24: Feature Selection, Ridge and Lasso** · source item type: WikiPage

---
## Introduction

In an attempt to fit a good model to data, we often tend to overfit. In this section, you will learn about Regularization, a technique used to avoid overfitting. Regularization discourages overly complex models by penalizing the loss function.

## Ridge and Lasso

Ridge and Lasso regression are two examples of penalized estimation. Penalized estimation makes some or all of the coefficients smaller in magnitude (closer to zero). Some of the penalties have the property of performing both variable selection (setting some coefficients exactly equal to zero) and shrinking the other coefficients.

In Ridge regression, the cost function is changed by adding a penalty term to the square of the magnitude of the coefficients.

$$ \text{cost*function*ridge}= \sum*{i=1}^n(y*i - \hat{y})^2 = \sum*{i=1}^n(y*i - \sum*{j=1}^k(m*jx*{ij})-b)^2 + \lambda \sum*{j=1}^p m_j^2$$

Lasso regression is very similar to Ridge regression, except that the magnitude of the coefficients are not squared in the penalty term.

$$ \text{cost*function*lasso}= \sum*{i=1}^n(y*i - \hat{y})^2 = \sum*{i=1}^n(y*i - \sum*{j=1}^k(m*jx*{ij})-b)^2 + \lambda \sum*{j=1}^p \mid m_j \mid$$

## AIC and BIC

In this section you'll also be introduced to two new measures: AIC and BIC, which give you a comprehensive measure of model performace taking into account the additional variables.

The formula for the AIC, invented by Hirotugu Akaike in 1973 and short for "Akaike's Information Criterion" is given by:

$$ \text{AIC(model)} = - 2 * \text{log-likelihood(model)} + 2 * \text{length of the parameter space} $$

The BIC (Bayesian Information Criterion) is very similar to the AIC and emerged as a Bayesian response to the AIC, but can be used for the exact same purposes.

$$ \text{BIC(model)} = -2 * \text{log-likelihood(model)} + \text{log(number of observations)} * \text{(length of the parameter space)} $$

Lower the values of AIC and BIC, the better your model is performing.

## Generating Data

Finally, you will also see how you can generate practice datasets that allow testing and debugging of algorithms.

## Summary

Regularization helps prevent overfitting your models. It is also useful when performing feature selection. On the other hand, if you are comparing multiple models with varying number of features, you can use the AIC and BIC measures. Remember that the lower the AIC (or BIC), the better the model.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
