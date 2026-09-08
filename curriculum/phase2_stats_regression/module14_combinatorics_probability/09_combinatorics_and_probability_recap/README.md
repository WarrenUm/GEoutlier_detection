# Combinatorics and Probability - Recap

> Part of **Topic 11: Combinatorics and Probability** · source item type: WikiPage

---
## Introduction

In this section, you learned about the concepts of combinatorics and probability.

## Key Takeaways

In this section, we dug into a number of foundational concepts - from NumPy to the basics of Probability * Probability is "how likely" it is that an event will happen * Sets in Python are unordered collections of unique elements * A sample space is a collection of every single possible outcome in a trial * The inclusion exclusion principle is a counting technique used to calculate the number of elements in a collection of sets with overlapping elements * Factorials provide the basis for calculating permutations * The difference between permutations and combinations is that with combinations, order is not important * The "sum rule" of probability states that $P(A\cup B) = P(A) + P(B) - P(A \cap B) $

- Independent events don't affect each other - e.g. consecutive coin tosses
- Dependent events do affect each other - e.g. picking consecutive colored marbles from a bag
- The product rule is useful when the conditional probability is easy to compute, but the probability of intersections of events is not.
- The chain rule (also called the general product rule) permits the calculation of any member of the joint distribution of a set of random variables using only conditional probabilities.
- Bayes theorem describes the probability of an event based on prior knowledge of conditions that might be related to the event
- The law of total probability states that the probability for a sample space is the sum of the probabilities for partitions of that sample space

In this section, we introduced the ideas of combinatorics and probability. In the next section, you'll use this knowledge and take it a step further by learning about statistical distributions and their applications!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
