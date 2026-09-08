# Data Analysis in Pandas - Recap

> Part of **Topic 4: Data Analysis in Pandas** · source item type: WikiPage

---
This short lesson summarizes the topics we covered in this section and why they'll be important to you as a data scientist.

## Key Takeaways

In this section, we spent time getting comfortable with pandas and getting some more practice with exploratory data analysis. Some of the key takeaways:

- For non-trivial datasets you'll usually want to store your data in pandas data structures rather than native Python lists and dictionaries
- Pandas has a range of great features for easily importing data from anything from a CSV, an Excel file, JSON, SQL, or a Python dictionary

- Pandas `Series` and `DataFrame` classes have a bunch of powerful methods for munging data
- Pandas also has a range of methods for applying descriptive statistics to Series and DataFrames
- Finally, by wrapping Matplotlib, Pandas also provides some very convenient plotting capabilities for quickly visualizing data
- We also got some experience working with the Ames Housing dataset, and set up accounts on Kaggle - a really useful resource for practicing data scientists.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
