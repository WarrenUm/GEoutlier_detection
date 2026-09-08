# Central Limit Theorem and Confidence Intervals - Recap

> Part of **Topic 13: Central Limit Theorem and Confidence Intervals** · source item type: WikiPage

---
## Introduction

This short lesson summarizes the topics we covered in this section and why they'll be important to you as a data scientist.

## Key Takeaways

This section was all about building further on your statistics foundations by introducing the Central Limit Theorem and confidence intervals. Some of the key takeaways include:

- The Central Limit Theorem states that often, independent random variables summed together will converge to a normal distribution as the number of variables increases
- Using the Central Limit Theorem, we can work with non-normally distributed data sets as if they were normally distributed
- The Standard Error is a measure of spread - it is the standard deviation of samples from the sample mean
- If you take repeated samples and compute the 95% confidence interval for a given parameter for each sample, 95% of the intervals would contain the population parameter.
- The $z$-critical value is the number of standard deviations you'd have to go from the mean of the normal distribution to capture the proportion of the data associated with the desired confidence level.
- If you don't know the standard deviation for a population, you need to use t-distributions to compute the margin of error for calculating a confidence interval.

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
- `non_normal_dataset.csv` — supporting data/helper file for the exercise.
- `output_16_1.png` — supporting data/helper file for the exercise.
- `output_18_1.png` — supporting data/helper file for the exercise.
- `output_20_1.png` — supporting data/helper file for the exercise.
- `output_5_1.png` — supporting data/helper file for the exercise.
