# Bayesians vs Frequentists

> Part of **Topic 17: Bayesian Statistics** · source item type: WikiPage

---
## Introduction

Up until now, all of the statistical theory you have encountered has been through the lens of a Frequentist. This has included discussions of z-tests, t-tests, p-values, and ANOVA; all are from the Frequentist perspective. In this lesson, you'll start to explore an alternative perspective donned by Bayesians.

## Objectives

You will be able to:

- Compare the Bayesian v. Frequentist statistical frameworks


## Philosophical Interpretations

A natural place to start when outlining the differences between Bayesians and Frequentists is to talk of their interpretation of probability itself. For Frequentists, the probability of an event is the limit of the rate of occurrences of the event if the same scenario including context and assumptions were repeated ad infinitum. In contrast, Bayesians interpret probability as the level of confidence, or belief, in a particular event occurring. In many ways, this makes a more natural interpretation for rare events that cannot possibly reoccur in the same context and circumstances.

## Practical Implications

The practical implications of Bayesians versus Frequentists rest upon making assumptions about unknown quantities. In the Bayesian framework, you make assumptions about unknown variables which you are attempting to estimate. For example, you might assume that the number of individuals who will buy a product can be represented by a binomial variable with parameter $p$. In contrast, the Frequentist perspective does not allow embedding of prior beliefs such as this into statistical experiments and analyses.

## Summary

In this lesson, you started to learn about the differences in Bayesian versus Frequentist statistical perspectives. Keep in mind that there are not always rigid lines between these modes of thought. Nonetheless, the discussion is a worthwhile one in considering which approach you wish to take in your research and analysis.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
