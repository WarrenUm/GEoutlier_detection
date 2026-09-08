# Recommendation Systems

> Part of **Phase 4 Appendix: Graph Theory** · source item type: Assignment

---
## Introduction

In this lesson, you'll investigate a very different take on networks and investigate how recommendation systems can be built off of networks.

## Objectives

You will be able to:

- Demonstrate how to create a simple collaborative filtering recommender system
- Use graph-based similarity metrics to create a collaborative filtering recommender system


## Motivating Ideas

When recommending items to a user whether they be books, music, movies, restaurants or other consumer products, one is typically trying to find the preferences of other users with similar tastes who can provide useful suggestions for the user in question. With this, examining the relationships amongst users and their previous preferences can help identify which users are most similar to each other. Alternatively, one can examine the relationships between the items themselves. These two perspectives underlying the two predominant means to recommendation systems: item-based and people-based.

## Collaborative Filtering

One popular implementation of this intuition is collaborative filtering. This starts by constructing a matrix of user or item similarities. For example, you might calculate the distance between users based on their mutual ratings of items. From there, you then select the top $n$ similar users or items. Finally, in the case of users, you then project an anticipated rating for other unreviewed items of the user based on the preferences of these similar users. Once sorted, these projections can be then used to serve recommendations to other users.

## Importing a Dataset

To start, you'll need to import a dataset as usual. For this lesson, you'll take a look at the Movie-Lens dataset which contains movie reviews for a large number of individuals. While the dataset is exclusively older movies, it should still make for an interesting investigation.

```python
import pandas as pd
df = pd.read_csv('ml-100k/u.data', delimiter='\t',
                 names=['user_id' , 'item_id' , 'rating' , 'timestamp'])
df.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      user_id item_id rating timestamp     0 196 242 3 881250949   1 186 302 3 891717742   2 22 377 1 878887116   3 244 51 2 880606923   4 166 346 1 886397596

As you can see, this dataset could easily be represented as a bimodal weighted network graph connecting user nodes with movies nodes with rating weights. Let's also import some metadata concerning the movies to bring the scenario to life.

```python
col_names = ['movie_id' , 'movie_title' , 'release_date' , 'video_release_date' ,
             'IMDb_URL' , 'unknown', 'Action', 'Adventure', 'Animation',
             'Childrens', 'Comedy', 'Crime' , 'Documentary', 'Drama', 'Fantasy',
             'Film-Noir', 'Horror', 'Musical', 'Mystery' , 'Romance' , 'Sci-Fi',
             'Thriller', 'War' ,'Western']
movies = pd.read_csv('ml-100k/u.item', delimiter='|', encoding='latin1', names=col_names)
movies.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      movie_id movie_title release_date video_release_date IMDb_URL unknown Action Adventure Animation Childrens ... Fantasy Film-Noir Horror Musical Mystery Romance Sci-Fi Thriller War Western     0 1 Toy Story (1995) 01-Jan-1995 NaN http://us.imdb.com/M/title-exact?Toy%20Story%2... 0 0 0 1 1 ... 0 0 0 0 0 0 0 0 0 0   1 2 GoldenEye (1995) 01-Jan-1995 NaN http://us.imdb.com/M/title-exact?GoldenEye%20(... 0 1 1 0 0 ... 0 0 0 0 0 0 0 1 0 0   2 3 Four Rooms (1995) 01-Jan-1995 NaN http://us.imdb.com/M/title-exact?Four%20Rooms%... 0 0 0 0 0 ... 0 0 0 0 0 0 0 1 0 0   3 4 Get Shorty (1995) 01-Jan-1995 NaN http://us.imdb.com/M/title-exact?Get%20Shorty%... 0 1 0 0 0 ... 0 0 0 0 0 0 0 0 0 0   4 5 Copycat (1995) 01-Jan-1995 NaN http://us.imdb.com/M/title-exact?Copycat%20(1995) 0 0 0 0 0 ... 0 0 0 0 0 0 0 1 0 0

5 rows × 24 columns

## Transforming the Data

```python
user_ratings = df.pivot(index='user_id', columns='item_id', values='rating')
user_ratings.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }     item_id 1 2 3 4 5 6 7 8 9 10 ... 1673 1674 1675 1676 1677 1678 1679 1680 1681 1682   user_id                          1 5.0 3.0 4.0 3.0 3.0 5.0 4.0 1.0 5.0 3.0 ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN   2 4.0 NaN NaN NaN NaN NaN NaN NaN NaN 2.0 ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN   3 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN   4 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN   5 4.0 3.0 NaN NaN NaN NaN NaN NaN NaN NaN ... NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN

5 rows × 1682 columns

## Filling Missing Values

```python
for col in user_ratings:
    mean = user_ratings[col].mean()
    user_ratings[col] = user_ratings[col].fillna(value=mean)
user_ratings.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }     item_id 1 2 3 4 5 6 7 8 9 10 ... 1673 1674 1675 1676 1677 1678 1679 1680 1681 1682   user_id                          1 5.000000 3.000000 4.000000 3.000000 3.000000 5.000000 4.000000 1.000000 5.000000 3.000000 ... 3.0 4.0 3.0 2.0 3.0 1.0 3.0 2.0 3.0 3.0   2 4.000000 3.206107 3.033333 3.550239 3.302326 3.576923 3.798469 3.995434 3.896321 2.000000 ... 3.0 4.0 3.0 2.0 3.0 1.0 3.0 2.0 3.0 3.0   3 3.878319 3.206107 3.033333 3.550239 3.302326 3.576923 3.798469 3.995434 3.896321 3.831461 ... 3.0 4.0 3.0 2.0 3.0 1.0 3.0 2.0 3.0 3.0   4 3.878319 3.206107 3.033333 3.550239 3.302326 3.576923 3.798469 3.995434 3.896321 3.831461 ... 3.0 4.0 3.0 2.0 3.0 1.0 3.0 2.0 3.0 3.0   5 4.000000 3.000000 3.033333 3.550239 3.302326 3.576923 3.798469 3.995434 3.896321 3.831461 ... 3.0 4.0 3.0 2.0 3.0 1.0 3.0 2.0 3.0 3.0

5 rows × 1682 columns

## Creating a User Matrix

To create a user matrix, you must calculate the distance between users. Choosing an appropriate distance metric for this is crucial. In this instance, a simple Euclidean distance is apt to be appropriate, but in other instances an alternative metric such as cosine distance might be a more sensible choice.

```python
import numpy as np
import datetime
```

```python
u1 = user_ratings.iloc[1]
u2 = user_ratings.iloc[2]
def distance(v1,v2):
    return np.sqrt(np.sum((v1-v2)**2))
distance(u1,u2)
```

```python
11.084572689977236
```

```python
# ⏰ Expect this cell to take several minutes to run
start = datetime.datetime.now()
user_matrix = []
for i, row in enumerate(user_ratings.index):
    u1 = user_ratings[row]
    # Matrix is symetric, so fill in values for previously examined users
    user_distances = [entry[i] for entry in user_matrix]
    for j, row2 in enumerate(user_ratings.index[i:]):
        u2 = user_ratings[row2]
        d = distance(u1,u2)
        user_distances.append(d)
    user_matrix.append(user_distances)
user_similarities = pd.DataFrame(user_matrix)

end = datetime.datetime.now()
elapsed = end - start
print(elapsed)

user_similarities.head()
```

```python
0:02:12.766052
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      0 1 2 3 4 5 6 7 8 9 ... 933 934 935 936 937 938 939 940 941 942     0 0.000000 29.936426 34.042510 25.599772 27.165580 22.301547 26.215828 23.496667 25.937816 21.335516 ... 36.156616 26.799824 19.717999 25.405054 36.780720 21.812402 51.343159 32.668768 23.666899 24.014478   1 29.936426 0.000000 16.182447 19.619520 13.942961 17.161477 28.271802 29.750381 30.305192 23.904303 ... 16.059514 11.520504 25.495994 14.214126 15.803102 17.058759 28.922541 13.417856 14.396717 14.214562   2 34.042510 16.182447 0.000000 24.390253 16.425187 20.838161 32.394615 35.050119 33.991216 28.574367 ... 13.944501 13.948331 30.359617 17.340413 13.335128 21.472178 24.388253 13.221221 19.026807 18.205507   3 25.599772 19.619520 24.390253 0.000000 18.809007 15.341923 24.285722 23.233123 24.219603 18.588349 ... 24.992752 16.263677 18.954594 16.038223 25.407118 14.828270 39.984010 22.005445 14.904607 15.217085   4 27.165580 13.942961 16.425187 18.809007 0.000000 13.840300 25.698150 27.076469 26.955596 20.865873 ... 16.513384 9.004673 21.955017 11.236040 16.516795 13.212617 31.007449 13.597272 12.242182 11.385938

5 rows × 943 columns

## Calculating Recommendations

Now on to the recommendations! To do this, you'll select the top $n$ users who are similar to the user in question. From there, you'll then predict the current user's rating of a movie based on the average of the closest users ratings. Finally, you'll then sort these ratings from highest to lowest and remove movies that the current user has already rated and seen.

```python
def recommend_movies(user, user_similarities, user_ratings, df, n_users=20, n_items=10):
    """n is the number of similar users who you wish to use to generate recommendations."""
    # User_Similarities Offset By 1 and Must Remove Current User
    top_n_similar_users = user_similarities[user-1].drop(user-1).sort_values().index[:n_users]
    # Again, fixing the offset of user_ids
    top_n_similar_users = [i+1 for i in top_n_similar_users]
    already_watched = set(df[df.user_id == 0].item_id.unique())
    unwatched = set(df.item_id.unique()) - already_watched
    projected_user_reviews = user_ratings[user_ratings.index.isin(top_n_similar_users)].mean()[list(unwatched)].sort_values(ascending=False)
    return projected_user_reviews[:n_items]
```

```python
recommend_movies(1, user_similarities, user_ratings, df)
```

```python
item_id
1122    5.0
814     5.0
1500    5.0
1536    5.0
1653    5.0
1599    5.0
1467    5.0
1189    5.0
1201    5.0
1293    5.0
dtype: float64
```

## Summary

In this lesson you got a proper introduction to recommendation systems using collaborative filtering!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
