# Hypothesis Testing - Introduction

> Part of **Topic 14: Hypothesis Testing** · source item type: WikiPage

---
## Introduction

In this section, you'll learn about experimental design and hypothesis testing. All scientific research that comes out of universities uses hypothesis testing to determine if the results of an experiment are significant or not. As a data scientist, you might be tasked with designing, performing, and analyzing the results of an experiment. Finally, you'll also learn about resampling methods, which are modern statistical techniques that involve taking repeated subsamples from a sample and help better estimate the precision of your sample statistics.

## Hypothesis Testing

In this section, you'll be looking at experimental design, effect size, T-tests, Type 1 and Type 2 errors, and resampling techniques like the jackknife, bootstrap, and permutation tests.

### Experimental Design

Without good experimental design, it's very easy to draw the wrong conclusions from your experiments. Because of that, you'll kick this section off by looking at the scientific method and the key elements of good experimental design - forming **alternative** and **null hypotheses**, conducting an experiment, analyzing the results for statistical significance and drawing conclusions.

### Effect Size

We then look at how to calculate and interpret the size of the difference between control and test groups. We'll see how the "Effect Size" can be used to communicate the practical significance of experimental results, to perform meta-analyses of multiple studies, and to perform power analysis to determine the number of participants that a study would require to achieve a certain probability of finding a true effect.

### One and Two Sample T-tests

Next, you'll also look at t-tests and how they can be used to compare two averages to see how significant the differences are between one or two samples once we have defined the experimental design.

### Type 1 and Type 2 Errors

From there, you'll learn about **type 1 (false positive)** and **type 2 (false negative) errors** and the inherent tradeoff between them.

### Jackknife, Bootstrap, and Permutation Tests

We'll look at techniques for taking repeated subsamples from a sample using bootstrapping, jackknife and permutation tests to better estimate the precision of your sample statistics or validate models by using random subsets.

## Summary

Without a good understanding of experimental design, it's easy to end up confusing spurious correlations for meaningful results or placing too much (or too little) weight on the results of any given test. In this section, we cover a range of tools and techniques to ensure that you design your experiments rigorously and interpret them thoughtfully.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
