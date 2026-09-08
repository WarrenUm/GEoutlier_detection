# Bayesian Statistics - Introduction

> Part of **Topic 17: Bayesian Statistics** · source item type: WikiPage

---
## Introduction

In this section, you'll investigate the Bayesian statistical framework. Bayesian statistics are an alternative perspective to classical Frequentist approaches which you've seen thus far. Bayesian statistics applies reasoning to unknown probabilities in a manner in which the Frequentist approach does not allow.

## Thomas Bayes

Bayesian statistics owes its name to the famous mathematician Thomas Bayes. Born (sometime) in the early 1700s, he bucked many academic traditions of his time due to his families religious beliefs. Cambridge and Oxford were known for the most prestigious mathematics of the time, but Bayes was a Presbytarien barring him from these universities which had ties to the Church of England.

## Bayes' theorem

Bayes' theorem is a method for rewriting conditional probabilities. The formula is:

### $$ P(A|B) = \dfrac{P(B|A)P(A)}{P(B)}$$

In the following lessons, you'll learn more about two traditional interpretations of this formula. The first provides an intuitive understanding, viewing the numerator as the probability of both A and B occuring:

### $$ P(A|B) = \dfrac{P(A \cap B)}{P(B)}$$

This should make perfect sense: the probability that A is true, given B is true, is the probability that A and B are both true, divided by the probability that B was true in the first place.

The second interpretation of Bayes theorem leads straight into the Bayesian statistical framework itself, bringing about discussions of priors, likelihoods, and posterior probabilities.

## Summary

Get ready to jump in! This section provides an exciting introduction to Bayes theorem and Bayesian statistics, further rounding out your statistical toolbox!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
