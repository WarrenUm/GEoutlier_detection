# Bayesian Classification - Recap

> Part of **Topic 28: Bayes Classification** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- Naive Bayes algorithms extend Bayes' formula to multiple variables by assuming that features are independent of one another. This then allows you to estimate an overall probability by multiplying the conditional probabilities for each of the independent features
- This assumption (that the underlying features are independent) is why Naive Bayes algorithm is considered naive -- because this is almost never true. However, Naives Bayes can prove to be quite efficient
- Expanding to multiple features, the multinomial Bayes' formula is:

$$ \Large P(y|x*1, x*2, ..., x*n) = \frac{P(y)\prod*{i}^{n}P(x*i|y)}{P(x*1, x*2, ..., x*n)}$$

- Finally, you saw how Naive Bayes algorithm can be used for document classification by classifying YouTube videos into the appropriate topic, and classifying documents as "spam" or "no spam"

- Due to insufficient text preprocessing (which you will learn how to do in a later module), the performance of this algorithm was trivial

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
