# Logistic Regression - Recap

> Part of **Topic 25: Introduction to Logistic Regression** · source item type: WikiPage

---
## Key Takeaways

- In this section you learned about a different supervised learning technique: classification! Specifically, you practiced building a very basic classification model from scratch - a logistic regression model
- Logistic regression uses a sigmoid function which helps to plot an "s"-like curve that enables a linear function to act as a binary classifier
- You can evaluate logistic regression models using some combination of precision, recall, and accuracy
- A confusion matrix is another common way to visualize the performance of a classification model
- Receiver Operating Characteristic (ROC) curve and the Area Under the Curve (AUC) can be used to help determine the best precision-recall tradeoff for a given classifier
- Class weights, under/oversampling, and SMOTE can be used to deal with class imbalance problems

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
- `salaries_final.csv` — supporting data/helper file for the exercise.
