# Inference versus Prediction

> Part of **Topic 19: Multiple Regression and Model Validation** · source item type: WikiPage

---
## Introduction

In the last few lessons, you have seen how to deal with categorical variables and why multicollinearity can be an issue with regression analysis. You also learned about log transformations, feature scaling, and normalization in order to accurately determine the coefficients of your features and to improve the model accuracy. Before we proceed further, it is important to discuss two different modeling approaches that you should keep in mind when working with data: modeling for *inference* and modeling for *prediction*. Are you asking yourself "aren't they the same thing"? Well, no! In this lesson you will see why and how.

## Objectives

- Explain the difference between modeling for inference and prediction

## Inference

When you are modeling for *inference*, you are asking the question "How does X (independent variables or features) affect Y (dependent or target or outcome variable)?". So, in essence, you are trying to figure out which features affect your outcome **and** how your outcome changes when these features change.

When modeling for *inference*, you are typically focused on only a subset of features because you are trying to understand how the outcome changes when you vary these features. As a result, great emphasis is given to the coefficients of these features as opposed to the overall accuracy of the model.

Hence, when you are modeling for inference, you typically choose *simpler* models, that is, models that are interpretable. Linear regression is a very good example of a model that is interpretable. With some basic training, anyone can understand how the features affect the outcome by observing the coefficients of these features. Some other interpretable models that you will learn later are logistic regression, decision trees, linear SVMs etc.

## Prediction

When you are modeling for *prediction*, you are asking the question "How well can I use X (independent variables or features) to predict Y (dependent or target or outcome variable)?" Thus, in this case, you are less concerned about how and which features impact Y as opposed to how you can efficiently use them to predict Y.

When modeling for *prediction*, you typically use all available features (and most likely engineer new features) because you are trying to accurately predict Y, at all costs. As a result, you are less concerned about the coefficients of these features and instead focus on the overall accuracy of the model.

Hence, when you are modeling for prediction, you typically choose more *complex* models. In the upcoming modules, as you learn about various Machine Learning models, you will notice that your sole focus is on improving the predictive accuracy of your models. That is, given some data, your job will be to build a model that best predicts the future (your target variable). This can often mean you will be dealing with *black box* models -- models that are difficult to interpret. Given the independent variables, these models can do a great job of predicting the target, but its inner workings will be very very difficult (almost impossible) to understand. These models can include SVMs with radial kernels, random forests, neural networks, and other techniques such regularization, cross-validation, grid search etc.

## Additional Resources

- [Inference vs Prediction - Roger Peng](https://www.youtube.com/watch?v=5mcCOdyr5w4)
- [Inference vs Prediction - R for Data Science Blog](https://www.datascienceblog.net/post/commentary/inference-vs-prediction/)

## Summary

Remember that how you build your models depends on what question you are asking of your data:

- Are you solely interested in how you can use the data to predict the future? If so, you are most likely *modeling for prediction*
- Or, are you interested in understanding how a given set of features affect your outcome? If so, you are most likely *modeling for inference*

Depending on what questions you ask, your modeling approaches will vary significatly, and hence it is very important to first understand the context of your problem and ask yourself what is the end goal of your analysis before you set out building any models.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
