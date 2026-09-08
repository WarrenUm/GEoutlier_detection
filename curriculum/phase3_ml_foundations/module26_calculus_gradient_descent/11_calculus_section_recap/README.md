# Calculus - Section Recap

> Part of **Topic 23: Calculus, Cost Function and Gradient Descent** · source item type: WikiPage

---
## Introduction

Congratulations! You have learned about one of the most fundamental concepts at the core machine learning, calculus. In this section, you started with the basics of derivatives and moved all the way to coding out gradient descent with multiple variables.

## Key Takeaways

In this section, we both learned how to traverse a cost function graph to find the local minima to solve a linear regression by using gradient descent and covered some of the foundational calculus that will help you to understand many of the other machine learning models you'll encounter as a professional data scientist.

Key takeaways include:

- A derivative is the "instantaneous rate of change" of a function - or it can be thought of as the "slope of the curve" at a point in time
- A derivative can also be thought of as a special case of the rate of change over a period of time - as that period of time is zero.
- If you calculate the rate of change over a period of time and keep reducing the period of time, it usually tends to a limit - which is the value of that derivative
- The power rule, constant factor rule, and addition rule are key tools for calculating derivatives for various kinds of functions
- The chain rule can be a useful tool for calculating the derivate of composite functions
- A derivative can be useful for identifying local maxima or minima as in both cases, the derivative tends to zero
- A cost curve can be used to plot the values of a cost function (in the case of linear regression) for various values of offset and slope for the best fit line.
- Gradient descent can be used to move towards the local minimum on the cost curve and thus the ideal values for the y-intercept and slope to minimize the selected cost function when performing a linear regression.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
