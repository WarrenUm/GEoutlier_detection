# Multiple Regression and Model Validation - Introduction

> Part of **Topic 19: Multiple Regression and Model Validation** · source item type: WikiPage

---
## Introduction

In this section, you'll start to see more advanced regression models which employ multiple predictors. With that, you'll also start to investigate how to validate your models to ensure they are neither overfit nor underfit, and will generalize well to future cases.

## Multiple Linear Regression

In the last section, you learned how to perform a basic linear regression with a single predictor variable. Here, you'll explore how to perform linear regressions using **multiple** independent variables to better predict a target variable.

## Improving a Baseline Model

Over the next few lessons, you'll see some ways to improve basic regression models using different combinations of features as well as some feature engineering. Often, a simple linear regression can be used as a "baseline model" upon which new features can be added to improve the predictions. Any decisions on how to change features should be compared against a simpler model to see if the changes have improved the model or not. This section will give an introduction to many of the techniques which can improve a regression model.

## Dealing with Categorical Variables

Up to this point you've only seen continuous predictor variables. Here, you'll get a further look at how to identify and then transform categorical variables to utilize them as predictors of our target variable.

## Multicollinearity of Features

While multiple predictors will ultimately increase model performance and yield better predictions, there are also possible negative effects when using multiple predictors that have a high correlation with each other. This is known as multicollinearity and can muddy model interpretation.

## Feature Scaling and Normalization

Another consideration when using multiple predictors in any model is the scale of those features. For example, a dataset surrounding households might have a "number of children" feature and an "income" feature. These two variables are of vastly different scales and as such, simply having a feature like income which is on a much larger scale can impact its influence over the model. To avoid this, it is best practice to normalize the scale of all features before feeding the data to a machine learning algorithm.

## Multiple Linear Regression in Statsmodels

After covering a lot of the key theory, you'll then get some hands-on practice in performing multiple linear regressions using the Statsmodels and Scikit-Learn libraries.

## Model Fit and Validation

You'll continue the section by looking at how we can analyze the results of a regression, and learn the importance of splitting data into training and test sets to determine how well a model predicts "unknown" values (the test dataset). Finally, you'll wrap up the section by looking at how k-fold cross-validation can be used to get additional model validations on a limited data set by taking multiple splits of training and testing data.

## Summary

In this section, you'll continue to bolster your understanding of linear regression so that you can solve a wider range of problems more accurately. Many of the principles covered in this section will also apply in later modules as you move onto working with other machine learning models.

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
