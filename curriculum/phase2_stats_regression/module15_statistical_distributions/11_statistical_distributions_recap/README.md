# Statistical Distributions - Recap

> Part of **Topic 12: Statistical Distributions** · source item type: WikiPage

---
## Introduction

You have now completed the second of two foundational statistics sections! In the following section you will apply this knowledge of statistical distributions to begin finding *inferential* statistics.

This short lesson summarizes the topics we covered in this section.

## Key Takeaways

In this section, we dug into statistical distributions.

Key takeaways include:

- There are two ways we categorize distributions: discrete and continuous
  - **Discrete** distributions have a distinct, non-infinite number of possible values. For example, the number of bedrooms in a house is discrete. We describe discrete distributions using **probability mass function**s (PMFs).
  - **Continuous** distributions have effectively an infinite number of possible values (subject to measurement and/or storage precision). For example, a person's height is continuous. We describe continuous distributions using **probability density function**s (PDFs) and **cumulative distribution function**s (CDFs).

- Highlighting some specific distributions:
  - Bernoulli Trials deal with a series of boolean events, which is a type of discrete distribution
  - The **normal** distribution is the classic "bell curve" with 68% of the probability mass within 1 SD (standard deviation) of the mean, 95% within 2 SDs, and 99.7% within 3 SDs.
  - The **standard normal** distribution is a standardized version of the normal distribution, where the mean is 0 and the SD is 1

- Insights regarding distributions:
  - The **z-score** can be used to understand how extreme a certain result is
  - **Skewness** and **kurtosis** can be used to measure how different a given distribution is from a normal distribution

## Appendix

Recall that there is additional material in the Appendix for you to review if you have time. In particular:

- The uniform distribution, which represents processes where each outcome is equally likely, like rolling dice
- The Poisson distribution, which can be used to represent the likelihood of a given number of successes over a given time period
- The exponential distribution, which can be used to represent the amount of time it may take before an event occurs

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
