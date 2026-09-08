# What is Probability?

> Part of **Topic 11: Combinatorics and Probability** · source item type: WikiPage

---
## Introduction

As an aspiring data scientist, it's important to know the foundations of probability and combinatorics, as these areas form the backbone of many concepts in data science. In the following lessons and labs, you'll get a gentle introduction to several concepts that are related to probability, such as sets, combinations, and permutations.

## Objectives

You will be able to:

- Define probability


## What is probability, and how does it relate to data science?

Probability is the chance that a certain event will happen, in other words, how "likely" it is that some event will happen.

As data science often uses *statistical inference* to analyze or predict certain events or trends, knowing probability and its applications is important because statistical inference uses probability distributions of the data. Although it might take a little more time for you to understand just how important the foundations of probability are for data science, by the end of the first part of the probability section, you'll be able to answer questions like:

-

How likely is it to end up with heads when flipping a coin once? (the answer here is 50% - not very surprising)
-

How likely is it to end up with exactly 2 x heads and 3 x tails when flipping a coin 5 times?
-

How likely is it to throw tails first, then heads, then tails, then heads, then tails when flipping a coin 5 times?
-

If you throw 5 dice, what is the probability of throwing a ["full house"](http://grail.sourceforge.net/demo/yahtzee/rules.html)?
-

What is the probability of drawing 2 consecutive aces from a standard deck of cards?

## Summary

Now, let's dive deeper into the understanding of sets. Getting these concepts will make calculating your first probabilities much easier!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
