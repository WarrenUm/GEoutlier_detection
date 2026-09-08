# Data Cleaning in Pandas - Introduction

> Part of **Topic 5: Data Cleaning in Pandas** · source item type: Assignment

---
## Introduction

In this section, you will learn invaluable skills that will form the foundation of your data processing work. Before you can apply machine learning algorithms or do interesting analyses, you often must clean and transform your data into a suitable format. Such initial data wrangling processes are often referred to as Extract Transform Load (ETL). Our primary tool of choice for performing ETL and basic analyses will be the Pandas package.

## Why ETL?

ETL is an essential first step to data analysis and data science. It also will form the foundation for exploratory data analysis. Often, you will be thrown a dataset that you have little to no information about. In these cases, your first step is to explore the data and get familiar with it. What are the columns? How many observations do you have? Are there missing values? Any outliers? If we have user-level data, how can we explore aggregate trends along features like gender, race, or geography? All of these can be answered by applying ETL to transform raw datasets into alternative useful views.

## Quick ETL Example

While you'll see complete examples and explanations for all of these techniques (and more), here's a quick preview of some ETL techniques covered in this section! For more details, continue on to future lessons!

### Import data

```python
import pandas as pd
df = pd.read_csv('Yelp_Reviews.csv', index_col=0)
df.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      business_id cool date funny review_id stars text useful user_id     1 pomGBqfbxcqPv14c3XH-ZQ 0 2012-11-13 0 dDl8zu1vWPdKGihJrwQbpw 5 I love this place! My fiance And I go here atl... 0 msQe1u7Z_XuqjGoqhB0J5g   2 jtQARsP6P-LbkyjbO1qNGg 1 2014-10-23 1 LZp4UX5zK3e-c5ZGSeo3kA 1 Terrible. Dry corn bread. Rib tips were all fa... 3 msQe1u7Z_XuqjGoqhB0J5g   4 Ums3gaP2qM3W1XcA5r6SsQ 0 2014-09-05 0 jsDu6QEJHbwP2Blom1PLCA 5 Delicious healthy food. The steak is amazing. ... 0 msQe1u7Z_XuqjGoqhB0J5g   5 vgfcTvK81oD4r50NMjU2Ag 0 2011-02-25 0 pfavA0hr3nyqO61oupj-lA 1 This place sucks. The customer service is horr... 2 msQe1u7Z_XuqjGoqhB0J5g   10 yFumR3CWzpfvTH2FCthvVw 0 2016-06-15 0 STiFMww2z31siPY7BWNC2g 5 I have been an Emerald Club member for a numbe... 0 TlvV-xJhmh7LCwJYXkV-cg

```python
df.shape
```

```python
(2610, 9)
```

### Apply lambda functions

```python
df['Review_Word_Length'] = df['text'].map(lambda x: len(x.split()))
df.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      business_id cool date funny review_id stars text useful user_id Review_Word_Length     1 pomGBqfbxcqPv14c3XH-ZQ 0 2012-11-13 0 dDl8zu1vWPdKGihJrwQbpw 5 I love this place! My fiance And I go here atl... 0 msQe1u7Z_XuqjGoqhB0J5g 58   2 jtQARsP6P-LbkyjbO1qNGg 1 2014-10-23 1 LZp4UX5zK3e-c5ZGSeo3kA 1 Terrible. Dry corn bread. Rib tips were all fa... 3 msQe1u7Z_XuqjGoqhB0J5g 30   4 Ums3gaP2qM3W1XcA5r6SsQ 0 2014-09-05 0 jsDu6QEJHbwP2Blom1PLCA 5 Delicious healthy food. The steak is amazing. ... 0 msQe1u7Z_XuqjGoqhB0J5g 30   5 vgfcTvK81oD4r50NMjU2Ag 0 2011-02-25 0 pfavA0hr3nyqO61oupj-lA 1 This place sucks. The customer service is horr... 2 msQe1u7Z_XuqjGoqhB0J5g 82   10 yFumR3CWzpfvTH2FCthvVw 0 2016-06-15 0 STiFMww2z31siPY7BWNC2g 5 I have been an Emerald Club member for a numbe... 0 TlvV-xJhmh7LCwJYXkV-cg 32

```python
df.shape # Previously this was (2610, 9), now we have added a column
```

```python
(2610, 10)
```

### Group data

```python
df.groupby('business_id')['stars'].mean().head()
```

```python
business_id
-050d_XIor1NpCuWkbIVaQ    5.0
-0qht1roIqleKiQkBLDkbw    1.0
-3zffZUHoY8bQjGfPSoBKQ    5.0
-6tvduBzjLI1ISfs3F_qTg    5.0
-9nai28tnoylwViuJVrYEQ    5.0
Name: stars, dtype: float64
```

### Check for duplicates

Check how many we have:

```python
df.duplicated().value_counts()
```

```python
False    2277
True      333
dtype: int64
```

Visually inspect them:

```python
# Use keep=False to keep all duplicates and sort_values to put duplicates next to each other
df[df.duplicated(keep=False)].sort_values(by='business_id')
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      business_id cool date funny review_id stars text useful user_id Review_Word_Length     1729 -GY2fx-8udXPY8qn2HVBCg 0 2016-08-30 0 yQ6P1_CvM94wMLYw1T0UWA 5 Just opened a new account today. So far I am ... 1 sZfZGrI592euyacKUcwQYg 55   1729 -GY2fx-8udXPY8qn2HVBCg 0 2016-08-30 0 yQ6P1_CvM94wMLYw1T0UWA 5 Just opened a new account today. So far I am ... 1 sZfZGrI592euyacKUcwQYg 55   754 -LRlx2j9_LB3evsRRcC9MA 0 2017-10-07 0 kUqPsZmWwLIMSstGHhWssA 5 The vet took the time to explain what was poss... 0 VgaYZ7004pTwEDSDWR6u4Q 33   754 -LRlx2j9_LB3evsRRcC9MA 0 2017-10-07 0 kUqPsZmWwLIMSstGHhWssA 5 The vet took the time to explain what was poss... 0 VgaYZ7004pTwEDSDWR6u4Q 33   2767 -MKWJZnMjSit406AUKf7Pg 0 2015-01-03 2 rJhrQD3-b9GjTso0dxIkwg 1 Drove 37 miles on a Saturday at 12:30pm for lu... 0 kzP96uX8TUMmmvLtd-I3RQ 18   ... ... ... ... ... ... ... ... ... ... ...   2193 zKw09ftu1730wEIZBZPoFg 3 2015-01-04 0 JV-yxKxMFp-d0rLDc_2_6w 5 So relaxing combined with the meditation and ... 5 3mZFkwfa6XV0BBazRTva9w 31   496 zg5rJfgT4jhzg1d6r2twnA 0 2014-06-21 0 Zbj0HgdN3AT4l-mbH-EfjA 3 Burger week\r\n\r\n1. Blazing Pineapple Burger... 0 UGW-9bbBEB3eP1o6mWD_WA 62   496 zg5rJfgT4jhzg1d6r2twnA 0 2014-06-21 0 Zbj0HgdN3AT4l-mbH-EfjA 3 Burger week\r\n\r\n1. Blazing Pineapple Burger... 0 UGW-9bbBEB3eP1o6mWD_WA 62   988 ziv21pDfyrgdhlrlNIgDfg 0 2016-08-11 0 fus9odxu9bjE2lSxfwNfdw 5 Get this!!! Wow Karlo is amazing and best cus... 2 ywjqPgnMrDZKOhA33v92Cw 62   988 ziv21pDfyrgdhlrlNIgDfg 0 2016-08-11 0 fus9odxu9bjE2lSxfwNfdw 5 Get this!!! Wow Karlo is amazing and best cus... 2 ywjqPgnMrDZKOhA33v92Cw 62

666 rows × 10 columns

### Remove duplicates

```python
df = df.drop_duplicates()
df.shape # Previously this was (2610, 10), now we have dropped duplicate rows
```

```python
(2277, 10)
```

### Recheck for duplicates

```python
df.duplicated().value_counts()
```

```python
False    2277
dtype: int64
```

```python
# Duplicates should no longer exist
df[df.duplicated(keep=False)].sort_values(by='business_id')
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      business_id cool date funny review_id stars text useful user_id Review_Word_Length

### Create pivot tables

```python
# This transforms the data into a person by person spreadsheet and what stars they gave various restaurants
# Most values are NaN (null or missing) because people only review a few restaurants of those that exist
usr_reviews = df.pivot(index='user_id', columns='business_id', values='stars')
usr_reviews.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }     business_id -050d_XIor1NpCuWkbIVaQ -0qht1roIqleKiQkBLDkbw -3zffZUHoY8bQjGfPSoBKQ -6tvduBzjLI1ISfs3F_qTg -9nai28tnoylwViuJVrYEQ -C8sSrFqaCxp51pyo-fQLQ -Dnh48f029YNugtMKkkI-Q -FLnsWAa4AGEW4NgE8Fqew -G7MPSNBpxRJmtrJxdwt7A -GY2fx-8udXPY8qn2HVBCg ... zdE82PiD6wquvjYLyhOJNA zdd3hyxB8ylYV6RcNe347Q zg5rJfgT4jhzg1d6r2twnA ziv21pDfyrgdhlrlNIgDfg zkhBU5qW_zCy0q4OEtIrsA ztP466jMUMtqLwwHqXbk9w zw9_mqWBn1QCfZg88w0Exg zwNLJ2VglfEvGu7DDZjJ4g zzYaAiC0rLNSDiFQlMKOEQ zzgSiOnuUjnBnmfR-ZG4ww   user_id                          -0biHfjE0soSptbU5G3nug NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN   -2K0yp7lBT_JUOzGkpdJ_g NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN   -Opvc9hAWllZSSPDUsD7NA NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN   -Zdxj4wuj4D_899B7tPE3g NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN   -_iULENf28RbqL2k0ja5Xw NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN

5 rows × 2192 columns

## Summary

In this brief introduction, you learned the acronym ETL and got to preview a few examples of ETL processes using pandas. In the upcoming lessons you'll get a much richer understanding of these and other techniques for wrangling your data!

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
- `titanic.csv` — supporting data/helper file for the exercise.
