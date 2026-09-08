# Feature and Model Selection: AIC and BIC

> Part of **Topic 24: Feature Selection, Ridge and Lasso** · source item type: WikiPage

---
## Introduction

Previously, you've seen how you can select ways of assessing your model fit metrics like MSE, SSE, and $R^2$. These values almost always improve when adding more variables, so if you only use these metrics to determine the optimal features of your model, it is highly likely that you will overfit the model to your data. In this lesson you'll be introduced to two new measures: AIC and BIC, which give you a comprehensive measure of model performace taking into account the additional variables.

## Objectives

You will be able to:

- Define AIC and BIC in the context of assessing model fit


## AIC

The formula for the AIC, invented by Hirotugu Akaike in 1973 and short for "Akaike's Information Criterion" is given by:

#### $$ \text{AIC} = -2\ln(\hat{L}) + 2k $$

Where: * $k$ : length of the parameter space (i.e. the number of features) * $\hat{L}$ : the maximum value of the likelihood function for the model

Another way to phrase the equation is:

$$ \text{AIC(model)} = - 2 * \text{log-likelihood(model)} + 2 * \text{length of the parameter space} $$

The AIC is generally used to compare each candidate model. The nice thing about the AIC is that for every model that uses Maximum Likelihood Estimation, the log-likelihood is automatically computed, and as a consequence, the AIC is very easy to calculate.

The AIC acts as a penalized log-likelihood criterion, giving a balance between a good fit (high value of log-likelihood) and complexity (complex models are penalized more than fairly simple ones). The AIC is unbounded so it can take any type of value, but the bottom line is that when comparing models, the model with the **lowest** AIC should be selected.

Note that directly comparing the values of log-likelihood maxima for different models (without including the penalty) is not good enough for model comparison because including more parameters in a model will *always* give rise to an increased value of the maximum likelihood. Due to that reason, searching for the model with maximal log-likelihood would always lead to the model with the most parameters. The AIC balances this by penalizing for the number of parameters, hence searching for models with few parameters but fitting the data well.

In Python, the AIC is built into `statsmodels` and in `sklearn` (such as `LassoLarsIC`, which you'll use in the upcoming lab).

## BIC

The BIC (Bayesian Information Criterion) is very similar to the AIC and emerged as a Bayesian response to the AIC, but can be used for the exact same purposes. The idea is to select the candidate model with the highest probability given the data. This idea can be formalized inside a Bayesian framework, involving prior probabilities on candidate models along with prior densities on all parameters in the models. The penalty is slightly changed and depends on the number of rows in the dataset:

$$ \text{BIC} = - 2\ln(\hat{L}) + \ln(n) * k $$

where:

- $\hat{L}$ and $k$ are the same as in AIC
- $n$ : the number of data points (the sample size)

Another way to phrase the equation is:

$$ \text{BIC(model)} = -2 * \text{log-likelihood(model)} + \text{log(number of observations)} * \text{(length of the parameter space)} $$

Like the AIC, the **lower** your BIC, the better your model is performing.

## Uses of AIC and BIC

- Performing feature selection: comparing models with only a few variables and more variables, computing the AIC/BIC and select the features that generated the lowest AIC or BIC
- Similarly, selecting or not selecting interactions/polynomial features depending on whether or not the AIC/BIC decreases when adding them in
- Computing the AIC and BIC for several values of the regularization parameter in Ridge/Lasso models and selecting the best regularization parameter, and many more!

## Summary

Great! In this lesson you learned about AIC and BIC, two measures that are helpful when comparing and evaluating models with varying number of features.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
