# Regularization - Recap

> Part of **Topic 24: Feature Selection, Ridge and Lasso** · source item type: WikiPage

---
## Key Takeaways

- Regularization discourages overly complex models by penalizing the loss function
- Lasso and Ridge are two commonly used so-called regularization techniques
- In Ridge regression, the cost function is changed by adding a penalty term to the square of the magnitude of the coefficients
- Ridge regression is often also referred to as L2 Norm Regularization
- Lasso regression is very similar to Ridge regression, except that the magnitude of the coefficients are not squared in the penalty term
- Lasso regression is often also referred to as L1 Norm Regularization
- AIC and BIC are two measures which give you a comprehensive measure of model performace taking into account the varying number of features

- The lower the AIC and/or BIC, the better the model

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
