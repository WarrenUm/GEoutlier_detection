# GEoutlier_detection — OSRS Market Data as a Full Data-Science Curriculum

This project uses real Old School RuneScape (OSRS) Grand Exchange market data as
the running example for a **complete, undergraduate-level data-science
curriculum** — from Python and tooling foundations, through probability,
statistics, and regression, into the full machine-learning and deep-learning
stack. Every topic is worked on the same live dataset so the math and code stay
concrete.

The curriculum structure mirrors a full data-science bootcamp syllabus (53
topics across four phases; see [Sources](#sources--further-reading)) and adapts
**every** topic to OSRS market data. Data collection and storage are owned by the
sibling project **`python_InfluxDB`**, which ingests 5-minute Grand Exchange
price snapshots from the RuneScape Wiki Prices API into an **InfluxDB 3
Enterprise** time-series database. This project is a **read-only consumer** of
that store: it pulls data, applies a method, and interprets the result in market
terms.

> New here? Read [How to use this roadmap](#how-to-use-this-roadmap), then start
> at [Phase 1](#phase-1--data-science-tooling--data-wrangling).

---

## Table of Contents

- [Why OSRS market data?](#why-osrs-market-data)
- [The dataset](#the-dataset)
- [How to use this roadmap](#how-to-use-this-roadmap)
- [Prerequisites](#prerequisites)
- [Curriculum roadmap](#curriculum-roadmap)
  - [Module 0 — Foundations: the data and the toolbox](#module-0--foundations-the-data-and-the-toolbox)
  - [Phase 1 — Data-science tooling & data wrangling](#phase-1--data-science-tooling--data-wrangling)
    - [1. Python essentials](#1-python-essentials)
    - [2. Python loops & functions](#2-python-loops--functions)
    - [3. Getting started with data science](#3-getting-started-with-data-science)
    - [4. Bash and Git](#4-bash-and-git)
    - [5. Data analysis in base Python](#5-data-analysis-in-base-python)
    - [6. Data analysis in pandas](#6-data-analysis-in-pandas)
    - [7. Data cleaning in pandas](#7-data-cleaning-in-pandas)
    - [8. Getting started with SQL](#8-getting-started-with-sql)
    - [9. SQL table relations](#9-sql-table-relations)
    - [10. Other database structures (NoSQL)](#10-other-database-structures-nosql)
    - [11. APIs](#11-apis)
    - [12. HTML, CSS & web scraping](#12-html-css--web-scraping)
  - [Phase 2 — Probability, statistics & regression](#phase-2--probability-statistics--regression)
    - [13. Statistical measures & visualization](#13-statistical-measures--visualization)
    - [14. Combinatorics and probability](#14-combinatorics-and-probability)
    - [15. Statistical distributions](#15-statistical-distributions)
    - [16. Central limit theorem & confidence intervals](#16-central-limit-theorem--confidence-intervals)
    - [17. Hypothesis testing](#17-hypothesis-testing)
    - [18. Statistical power and ANOVA](#18-statistical-power-and-anova)
    - [19. A/B testing](#19-ab-testing)
    - [20. Bayesian statistics](#20-bayesian-statistics)
    - [21. Introduction to linear regression](#21-introduction-to-linear-regression)
    - [22. Multiple regression & model validation](#22-multiple-regression--model-validation)
    - [23. Extensions to linear models](#23-extensions-to-linear-models)
  - [Phase 3 — Math & machine-learning foundations](#phase-3--math--machine-learning-foundations)
    - [24. Object-oriented programming](#24-object-oriented-programming)
    - [25. Linear algebra](#25-linear-algebra)
    - [26. Calculus, cost functions & gradient descent](#26-calculus-cost-functions--gradient-descent)
    - [27. Feature selection, ridge & lasso](#27-feature-selection-ridge--lasso)
    - [28. Logistic regression](#28-logistic-regression)
    - [29. MLE and logistic regression](#29-mle-and-logistic-regression)
    - [30. K-nearest neighbors](#30-k-nearest-neighbors)
    - [31. Naive Bayes classification](#31-naive-bayes-classification)
    - [32. Decision trees](#32-decision-trees)
    - [33. Ensemble methods](#33-ensemble-methods)
    - [34. Support vector machines](#34-support-vector-machines)
    - [35. Building a machine-learning pipeline](#35-building-a-machine-learning-pipeline)
  - [Phase 4 — Advanced ML, deep learning & operations](#phase-4--advanced-ml-deep-learning--operations)
    - [36. Principal component analysis](#36-principal-component-analysis)
    - [37. Clustering](#37-clustering)
    - [38. Big data in PySpark](#38-big-data-in-pyspark)
    - [39. Recommendation systems](#39-recommendation-systems)
    - [40. Time-series models](#40-time-series-models)
    - [41. Forecasting & financial econometrics](#41-forecasting--financial-econometrics)
    - [42. Anomaly & outlier detection](#42-anomaly--outlier-detection)
    - [43. Natural language processing](#43-natural-language-processing)
    - [44. Neural networks](#44-neural-networks)
    - [45. Deep neural networks](#45-deep-neural-networks)
    - [46. Tuning neural networks](#46-tuning-neural-networks)
    - [47. Convolutional neural networks](#47-convolutional-neural-networks)
    - [48. Transfer learning](#48-transfer-learning)
    - [49. Deep NLP & sequence models](#49-deep-nlp--sequence-models)
    - [50. Graph theory & networks](#50-graph-theory--networks)
    - [51. Operationalizing code, MLOps & the cloud](#51-operationalizing-code-mlops--the-cloud)
  - [Capstone](#capstone)
- [Suggested schedule](#suggested-schedule)
- [Environment setup](#environment-setup)
- [Repository layout](#repository-layout)
- [Sources & further reading](#sources--further-reading)

---

## Why OSRS market data?

The OSRS Grand Exchange is a virtual commodity market with millions of daily
trades. It has the statistical texture of real financial data — trends,
seasonality, volatility clustering, shocks around game updates, and cross-item
correlations — but it is free of the licensing, cost, and access barriers of
equities or crypto feeds. That makes it an ideal teaching dataset:

- **Every method has a natural question.** "Is this price spike an outlier or a
  real move?" "Does one item predict another's demand?" "Can I forecast
  tomorrow's price?"
- **Multiple series, one schema.** Thousands of items share an identical
  structure, so the same code generalizes from a single item to a panel.
- **High frequency, long history.** 5-minute snapshots since 2021 give enough
  data for both fine-grained volatility work and long-horizon forecasting.
- **Rich side data.** Item metadata (names, examine text, categories) supports
  the NLP, recommendation, and graph modules too.

## The dataset

Data lives in InfluxDB 3 (`GEItemPrices`). Full connection details are in
[`.kiro/steering/data-access.md`](.kiro/steering/data-access.md). Schema summary:

| Element | Value |
|---------|-------|
| Measurement | `itemPrice` |
| Tag | `itemID` (string) |
| Fields | `avgHighPrice`, `avgLowPrice`, `highPriceVolume`, `lowPriceVolume` |
| Timestamp | unix seconds, 5-minute granularity |
| History | ~2021-03-14 → present |

You read it through the shared [`curriculum/ge_data.py`](curriculum/ge_data.py)
helpers, the `ge_pipeline` helpers, or the FastAPI query API. A good smoke-test
item is `554` (Fire rune), which trades in essentially every window.

## How to use this roadmap

- Work the phases **in order** — each builds on the last. Do not skip the
  statistics and regression phases; the assumption-checking and uncertainty
  habits carry through everything after.
- **Each numbered topic becomes one notebook** (or a small script) in
  `curriculum/`. The pattern is always the same: *pull data → state the question
  → apply the method → check assumptions → interpret the result in market terms.*
- Every topic lists its **key concepts** and a concrete **OSRS application**.
- Difficulty is flagged 🟢 introductory · 🟡 intermediate · 🔴 advanced.
- This roadmap is a **complete adaptation** of a full data-science bootcamp
  syllabus (see [Sources](#sources--further-reading)); every source topic is
  represented and re-grounded in OSRS market data.

## Prerequisites

- **Programming:** none assumed — Phase 1 starts from Python variables. Prior
  coding experience lets you move quickly through Topics 1–2.
- **Math:** single-variable calculus and basic linear algebra help from Phase 3
  on; Topics 25–26 build the pieces you need. High-school algebra is enough to
  start.

---

## Curriculum roadmap

### Module 0 — Foundations: the data and the toolbox
🟢 *Goal: connect to the store and load OSRS data into pandas comfortably.*

The starter module and connection smoke test. See
[`curriculum/module00_foundations/`](curriculum/module00_foundations/).

**Key concepts:** time-series data model, tags vs. fields, unix timestamps, tidy
vs. wide data, resampling/downsampling, reproducible notebooks.

**OSRS application:** connect via `ge_data`, pull a year of Fire rune (`554`)
prices, downsample raw 5-minute data to hourly/daily, load multiple items, and
detect missing windows.

---

## Phase 1 — Data-science tooling & data wrangling

Programming, environment, and data-access skills. This phase produces the
reusable loaders and cleaning code the rest of the curriculum leans on.

### 1. Python essentials
🟢 **Key concepts:** variable assignment, strings, numeric types and booleans,
conditionals, lists, dictionaries, built-in operators/functions/methods.
**OSRS application:** store a single item snapshot in variables and dicts;
compute a price margin with arithmetic and conditionals.

### 2. Python loops & functions
🟢 **Key concepts:** looping over collections, `while` loops, `break`/`continue`,
nested loops, defining functions, arguments, user input/output.
**OSRS application:** loop over a list of item ids and write a `price_margin()`
function; build the first version of a reusable loader.

### 3. Getting started with data science
🟢 **Key concepts:** the data-science process, problems DS can solve, PEP 8,
data privacy and ethics, professional environment setup (Anaconda, Git,
Jupyter), running notebooks locally.
**OSRS application:** stand up the project environment, adopt PEP 8, and frame a
market question using the DS process; note the ethics of market-manipulation
detection.

### 4. Bash and Git
🟢 **Key concepts:** the Bash shell, version control 101, staging/committing,
branches, collaboration, resolving conflicts.
**OSRS application:** manage this repo with Git; script a small Bash pipeline to
export a dataset via the FastAPI `/api/datasets/export` endpoint.

### 5. Data analysis in base Python
🟢 **Key concepts:** file I/O, CSV, JSON, working with known JSON schemas,
exploring/transforming JSON.
**OSRS application:** parse a raw RuneScape Wiki API JSON response (and the
NDJSON export) with only the standard library before reaching for pandas.

### 6. Data analysis in pandas
🟢 **Key concepts:** Python libraries, Series and DataFrames, indexing/accessing
data, importing data, statistical methods, plotting with pandas.
**OSRS application:** load an item series into a DataFrame with `ge_data`,
compute summary stats, and make first plots.

### 7. Data cleaning in pandas
🟡 **Key concepts:** lambda functions, `groupby`, combining/merging DataFrames,
pivot tables, missing data handling.
**OSRS application:** clean and align multi-item frames; handle the missing
5-minute windows of low-volume items; pivot long→wide per item.

### 8. Getting started with SQL
🟢 **Key concepts:** selecting, filtering and ordering, grouping/aggregation,
DB admin basics, data types.
**OSRS application:** InfluxDB 3 speaks SQL — write `SELECT`/`WHERE`/`GROUP BY`
queries with `date_bin` downsampling directly against `itemPrice` (double-quoted
identifiers, parameterized values).

### 9. SQL table relations
🟡 **Key concepts:** joins, one-to-many and many-to-many, subqueries, using SQL
with pandas, a cumulative lab.
**OSRS application:** join price data to item metadata; use subqueries to find,
e.g., items whose volume exceeds their trailing average, then load results into
pandas.

### 10. Other database structures (NoSQL)
🟡 **Key concepts:** NoSQL vs. relational, document stores, MongoDB.
**OSRS application:** contrast the time-series store with a document model; sketch
how item metadata could live in a document store and why time-series data does not.

### 11. APIs
🟡 **Key concepts:** the client–server model, HTTP request/response cycle, OAuth,
reading API docs, consuming a real API.
**OSRS application:** read the RuneScape Wiki Prices API docs and the project's
own FastAPI query API; fetch series over HTTP and handle rate limits/headers.

### 12. HTML, CSS & web scraping
🟡 **Key concepts:** HTML structure, CSS selectors, Beautiful Soup, scraping
pages and images, semantic elements.
**OSRS application:** scrape item metadata (names, categories, examine text) from
the OSRS Wiki to enrich the numeric store for the NLP and recommendation modules.

---

## Phase 2 — Probability, statistics & regression

The statistical core: describe data, quantify uncertainty, test hypotheses, and
model relationships.

### 13. Statistical measures & visualization
🟢 **Key concepts:** NumPy basics, measures of central tendency, measures of
dispersion, covariance and correlation; matplotlib and seaborn; visualization
best practices and common mistakes.
**OSRS application:** profile price/return/volume distributions per item; compute
the covariance/correlation matrix across related items and visualize it honestly.

### 14. Combinatorics and probability
🟢 **Key concepts:** sets, probability fundamentals, permutations and factorials,
combinations, conditional probability, the law of total probability.
**OSRS application:** compute the probability that a randomly sampled window shows
a price increase; use conditional probability to relate volume spikes to price moves.

### 15. Statistical distributions
🟡 **Key concepts:** sampling, PMF/PDF/CDF, Bernoulli/binomial, normal and
standard-normal, uniform, Poisson, exponential distributions, skewness and kurtosis.
**OSRS application:** fit candidate distributions to returns (heavy tails!) and
model trade arrivals per window as Poisson; quantify skew/kurtosis of returns.

### 16. Central limit theorem & confidence intervals
🟡 **Key concepts:** the CLT, confidence intervals with the t-distribution,
introduction to statistical significance.
**OSRS application:** show the CLT empirically by sampling mean returns; build a
t-based confidence interval for an item's mean return.

### 17. Hypothesis testing
🟡 **Key concepts:** experimental design, z-score and p-value testing, the null
hypothesis, one-sample z-test, effect sizes, t-tests, Type I/II errors,
resampling methods.
**OSRS application:** test whether mean price changed before vs. after a known
game update, reporting effect size and being explicit about error types.

### 18. Statistical power and ANOVA
🟡 **Key concepts:** statistical power, Welch's t-test, the multiple-comparisons
problem, Goodhart's law, the Kolmogorov–Smirnov test, ANOVA, chi-square.
**OSRS application:** ANOVA across several item categories' returns; correct for
multiple comparisons when scanning many items for a post-update effect.

### 19. A/B testing
🟡 **Key concepts:** A/B test design and analysis, metric tracking.
**OSRS application:** frame a natural experiment (e.g. weekend vs. weekday trading)
as an A/B test; design it, then analyze it with the tools from Topics 17–18.

### 20. Bayesian statistics
🟡 **Key concepts:** Bayesian vs. frequentist views, Bayes' theorem, maximum
likelihood estimation (MLE), maximum a posteriori (MAP), multinomial Bayes.
**OSRS application:** maintain a Bayesian belief about "is this item trending up,"
updating as new snapshots arrive; compare MLE vs. MAP parameter estimates.

### 21. Introduction to linear regression
🟡 **Key concepts:** statistical learning theory, simple linear regression, the
coefficient of determination (R²), regression assumptions, OLS in statsmodels,
regression diagnostics, interpreting significance and p-values.
**OSRS application:** regress an item's price on a related item's lagged price;
run full residual diagnostics and interpret the slope in market terms.

### 22. Multiple regression & model validation
🟡🔴 **Key concepts:** multiple regression, categorical variables, multicollinearity
(VIF), log transformations, feature scaling/normalization, inference vs.
prediction, model fit, regression validation, cross-validation, pickling models.
**OSRS application:** build a multi-feature price model (lags, volume, calendar
dummies), check VIF, and validate with time-aware cross-validation; persist the model.

### 23. Extensions to linear models
🔴 **Key concepts:** interaction terms, polynomial regression, the bias–variance
trade-off, feature selection and engineering, model validation.
**OSRS application:** add interactions and polynomial terms to the price model and
show where added flexibility helps vs. overfits.

---

## Phase 3 — Math & machine-learning foundations

The math under the models, then the core supervised-learning algorithms.

### 24. Object-oriented programming
🟡 **Key concepts:** classes and instances, instance methods.
**OSRS application:** wrap the data loaders and a model in a small `MarketModel`
class with `fit`/`predict`/`plot` methods.

### 25. Linear algebra
🟡 **Key concepts:** motivation for LA in DS, systems of linear equations;
scalars, vectors, matrices, tensors; matrix multiplication; solving systems with
NumPy; regression via linear algebra; computational complexity (OLS → gradient descent).
**OSRS application:** solve the OLS normal equations by hand with NumPy on a
price model and confirm they match statsmodels.

### 26. Calculus, cost functions & gradient descent
🔴 **Key concepts:** derivatives, derivatives of non-linear functions, rules for
derivatives, gradient descent, step sizes, gradient descent in 3D, the gradient,
gradient of a cost function.
**OSRS application:** implement gradient descent from scratch to fit a regression
on OSRS prices; visualize the cost surface and the effect of the learning rate.

### 27. Feature selection, ridge & lasso
🔴 **Key concepts:** regularization, ridge and lasso regression, AIC/BIC, feature
selection methods.
**OSRS application:** with many correlated item/lag features, use lasso to select
predictors and ridge to stabilize a price model; compare by AIC/BIC and CV error.

### 28. Logistic regression
🟡 **Key concepts:** supervised learning, linear→logistic, logistic regression in
scikit-learn, confusion matrices, evaluation metrics, ROC/AUC, class imbalance.
**OSRS application:** predict whether an item's next-hour price rises; evaluate
with a confusion matrix and ROC-AUC against a majority/last-direction baseline.

### 29. MLE and logistic regression
🔴 **Key concepts:** MLE review, the link to logistic regression, gradient descent
review, coding logistic regression from scratch, model comparisons, a cumulative lab.
**OSRS application:** derive and code logistic regression via MLE + gradient
descent from scratch, then match it to scikit-learn on the "will it rise?" task.

### 30. K-nearest neighbors
🟡 **Key concepts:** distance metrics, KNN, choosing the best K, KNN in scikit-learn.
**OSRS application:** classify next-move direction from recent-feature neighbors;
tune K and discuss why scaling matters for distance-based methods.

### 31. Naive Bayes classification
🟡 **Key concepts:** Bayesian classifiers, Gaussian naive Bayes, document
classification with naive Bayes.
**OSRS application:** Gaussian NB on engineered price features; later, document-NB
on scraped item descriptions to predict item category.

### 32. Decision trees
🟡 **Key concepts:** decision trees, entropy and information gain, trees in
scikit-learn, hyperparameter tuning and pruning, regression (CART) trees.
**OSRS application:** a CART regression tree for next-hour price and a
classification tree for direction; inspect splits and prune to control overfit.

### 33. Ensemble methods
🔴 **Key concepts:** bagging, random forests, `GridSearchCV`, gradient boosting
and weak learners, XGBoost.
**OSRS application:** random forest and XGBoost models for price/direction, tuned
via `GridSearchCV`; compare against the single tree and the linear baselines.

### 34. Support vector machines
🔴 **Key concepts:** SVMs, the kernel trick.
**OSRS application:** an SVM classifier for price-move direction with an RBF
kernel; discuss margins and the effect of `C`/`gamma`.

### 35. Building a machine-learning pipeline
🟡 **Key concepts:** scikit-learn pipelines, refactoring code into pipelines.
**OSRS application:** refactor the feature-engineering + scaling + model steps into
a single leak-safe `Pipeline` that can be cross-validated as one object.

---

## Phase 4 — Advanced ML, deep learning & operations

Unsupervised learning, time-series/forecasting (the project's core), sequence and
image deep learning, graphs, and shipping models.

### 36. Principal component analysis
🔴 **Key concepts:** unsupervised learning, the curse of dimensionality, PCA in
scikit-learn, covariance matrix and eigendecomposition, image PCA.
**OSRS application:** PCA on a panel of item returns to extract common "market
factors"; interpret the leading components economically.

### 37. Clustering
🔴 **Key concepts:** k-means, hierarchical agglomerative clustering, common
clustering pitfalls, market segmentation, semi-supervised/look-alike models.
**OSRS application:** cluster items by price/volume behavior into market segments
(stable commodities vs. speculative items); characterize each cluster.

### 38. Big data in PySpark
🔴 **Key concepts:** big data, MapReduce, Spark analytics, PySpark setup with
Docker, ML with Spark.
**OSRS application:** process the full multi-year, all-item history in PySpark
(the raw store is hundreds of millions of points); compute distributed aggregates
and fit a Spark ML model.

### 39. Recommendation systems
🔴 **Key concepts:** recommenders, collaborative filtering, SVD, `Surprise`,
matrix factorization with ALS.
**OSRS application:** "items like this" — recommend related items from co-movement
patterns via matrix factorization on an item×time returns matrix.

### 40. Time-series models
🟡🔴 **Key concepts:** time-series basics, correlation and autocorrelation (ACF/PACF),
stationarity and differencing, AR/MA/ARMA, ARMA/ARIMA in statsmodels, seasonal ARIMA.
**OSRS application:** the Box–Jenkins loop end to end — decompose an item series,
test stationarity, read ACF/PACF, fit and diagnose a (S)ARIMA model.

### 41. Forecasting & financial econometrics
🔴 **Key concepts:** forecasting workflow, baselines (naive/seasonal-naive/drift),
exponential smoothing (ETS/Holt-Winters), backtesting with rolling/expanding
windows, error metrics (MAE/RMSE/MAPE/MASE); log returns, volatility clustering,
ARCH/GARCH, VaR, cointegration, Granger causality.
**OSRS application:** a forecasting harness that backtests baselines, ETS, and
ARIMA against the seasonal-naive baseline; a GARCH volatility model and a
cointegration/pairs study on two related items.
*(Extends the source's Time-Series topic with the financial-econometrics depth
this project targets.)*

### 42. Anomaly & outlier detection
🟡🔴 **Key concepts:** statistical outliers (z-score, modified z-score, IQR),
rolling/robust thresholds, STL-residual outliers, Isolation Forest, Local Outlier
Factor, changepoint detection.
**OSRS application:** the project's original theme — reproduce and extend the
platform's z-score/IQR detectors (`/api/outlier-methods`), add STL and Isolation
Forest, and compare methods on labeled spike events.
*(Project-specific topic; the reason this repo exists.)*

### 43. Natural language processing
🔴 **Key concepts:** word vectorization, NLTK, regular expressions, feature
engineering for text, context-free grammars and POS tagging, text classification.
**OSRS application:** with scraped item names/examine text (Topic 12), classify
items into categories and extract features from descriptions with regex + TF-IDF.

### 44. Neural networks
🔴 **Key concepts:** neural network fundamentals, introduction to Keras.
**OSRS application:** a small feed-forward network for next-step price prediction;
compare it honestly against the classical baselines.

### 45. Deep neural networks
🔴 **Key concepts:** deeper networks, image classification with MLPs.
**OSRS application:** deepen the price network; discuss when extra depth helps vs.
overfits on tabular market features.

### 46. Tuning neural networks
🔴 **Key concepts:** regularization, normalization, tuning strategy.
**OSRS application:** apply dropout, batch norm, and early stopping to the price
network; track the effect on validation error.

### 47. Convolutional neural networks
🔴 **Key concepts:** CNNs, building a CNN from scratch, visualizing intermediate
activations.
**OSRS application:** 1-D CNNs over price windows for pattern detection/forecasting;
optionally treat multi-item "images" (item × time) as 2-D input.

### 48. Transfer learning
🔴 **Key concepts:** using pretrained networks.
**OSRS application:** pretrain a sequence model on high-liquidity items, then
fine-tune on a low-liquidity item with little history.

### 49. Deep NLP & sequence models
🔴 **Key concepts:** word embeddings, Word2Vec, classification with embeddings,
sequence-model use cases, RNNs, LSTMs and GRUs.
**OSRS application:** LSTM/GRU forecasters over multivariate price windows,
benchmarked against ARIMA/ETS/gradient boosting from Topics 40–41; embeddings for
item descriptions.

### 50. Graph theory & networks
🔴 **Key concepts:** graph theory, NetworkX, simple and shortest paths, node
centrality, network clustering, graph-based recommendation.
**OSRS application:** build an item co-movement graph (edges = correlated
returns); find central "hub" items and communities via network clustering.

### 51. Operationalizing code, MLOps & the cloud
🔴 **Key concepts:** DS/ML engineering, the AWS ecosystem, SageMaker,
productionizing a model with Docker and SageMaker.
**OSRS application:** package the best model behind the existing FastAPI service
(and/or Docker), schedule periodic re-training, and outline a cloud deployment.

---

## Capstone
🔴 Tie it together: pick a market question (forecast, anomaly system, pairs/
trading-signal backtest, or recommender), pull data from InfluxDB, engineer
features, train and rigorously evaluate several models with proper walk-forward
validation, and write up the findings — mirroring the source curriculum's
end-to-end capstone project, grounded in OSRS data.

---

## Suggested schedule

The source curriculum is organized in four phases; a full-time bootcamp runs
~one phase per five weeks, a self-paced learner longer:

| Phase | Topics | Theme |
|-------|--------|-------|
| Phase 1 | Module 0 + Topics 1–12 | Tooling & data wrangling (Python, Bash/Git, SQL, APIs, scraping) |
| Phase 2 | Topics 13–23 | Probability, statistics, hypothesis testing, regression |
| Phase 3 | Topics 24–35 | Math foundations + core supervised ML |
| Phase 4 | Topics 36–51 + capstone | Unsupervised, time-series/forecasting, deep learning, graphs, MLOps |

Do not skip Phase 2 — the assumption-checking and uncertainty habits underpin
everything after.

## Environment setup

1. Ensure the InfluxDB 3 store from `python_InfluxDB` is reachable (see
   [`.kiro/steering/data-access.md`](.kiro/steering/data-access.md)).
2. Create a git-ignored `.env` with the connection variables:
   ```
   INFLUXDB3_HOST_URL=http://192.168.1.85:8181
   INFLUXDB3_AUTH_TOKEN=any-non-empty-token
   INFLUXDB3_DATABASE_NAME=GEItemPrices
   ```
3. Use a Python 3.12 virtual environment (see `runtime.txt`). Install the base
   stack, then the deep-learning extras when you reach Phase 4's neural modules:
   ```
   pip install -r requirements.txt
   pip install -r requirements-dl.txt   # Topics 44-49 (torch is large)
   ```
   The base stack covers everything through classical ML and forecasting:
   `pandas`, `numpy`, `scipy`, `statsmodels`, `statsforecast`, `arch`,
   `scikit-learn`, `xgboost`/`lightgbm`, `shap`, `ruptures`, and plotting
   (`matplotlib`, `seaborn`, `plotly`). Some later topics use additional
   libraries (`nltk`, `networkx`, `pyspark`, `surprise`) — install those per
   module as you reach them.
4. **Visualizing in the IDE:** open a notebook (`.ipynb`) in Kiro/VS Code and
   select the project's Python 3.12 kernel. `matplotlib`/`seaborn` render inline,
   and `plotly` figures render interactively via `nbformat` + `ipywidgets`
   (both included). This is the recommended way to explore the OSRS data here.

## Repository layout

```
GEoutlier_detection/
├── README.md              # this roadmap
├── requirements.txt       # base stack (Phases 1-3 + classical ML/forecasting)
├── requirements-dl.txt    # deep-learning extras (Phase 4 neural modules)
├── .env.example           # InfluxDB 3 connection variables (copy to .env)
├── .kiro/steering/        # project steering (overview, coding standards, data access)
├── curriculum/            # the curriculum (start here)
│   ├── ge_data.py         # shared read-only data loaders
│   ├── _tools/            # generator that builds the phase folders from the sources
│   ├── module00_foundations/          # starter + connection smoke test
│   ├── phase1_tooling/                # Topics 1-12: one folder per module, per lesson
│   ├── phase2_stats_regression/       # Topics 13-23
│   ├── phase3_ml_foundations/         # Topics 24-35
│   └── phase4_advanced_ml_dl/         # Topics 36-51
│       └── moduleNN_.../NN_<lesson>/  # README.md + work.ipynb + test_work.py (+ lab.ipynb/data)
├── pytest.ini             # runs the per-lesson notebook tests
├── notebooks/             # legacy exploratory notebooks (historical reference only)
├── old ntbks/             # older notebooks (historical reference only)
└── prices/                # legacy CSV snapshots (historical reference only)
```

The legacy Wiki-API fetch and SQLite DB-update code has been removed — data
collection and storage live in the sibling `python_InfluxDB` project. New
curriculum work goes in `curriculum/`, organized by topic, and reads from the
InfluxDB 3 store. The remaining `notebooks/`, `old ntbks/`, and `prices/` are
kept only as historical reference and should not seed new analysis.

---

## Sources & further reading

The curriculum **structure** (four phases; the 53 topics in Phases 1–4) is a
direct adaptation of a full data-science bootcamp syllabus, re-grounded in OSRS
market data. Each topic below is also backed by a canonical open reference.

**Curriculum structure**
- *Data Science Full Curriculum* — a Flatiron-School-style bootcamp syllabus
  export (53 topics / ~404 items across four phases), covering Python, SQL,
  APIs, statistics, regression, the ML algorithm suite, deep learning, NLP,
  graphs, and MLOps. Provided in the workspace as a Canvas/LMS export; its topic
  list defines the phase and topic structure used above.

**Probability & statistics**
- MIT OpenCourseWare, *18.05 Introduction to Probability and Statistics*. https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
- American Statistical Association, *Curriculum Guidelines for Undergraduate Programs in Statistical Science*. https://www.amstat.org/education/2000-curriculum-guidelines-for-undergraduate-programs-in-statistical-science-

**Regression & econometrics**
- James, Witten, Hastie & Tibshirani, *An Introduction to Statistical Learning* (ISLR). https://www.statlearning.com/
- Jeffrey Wooldridge, *Introductory Econometrics: A Modern Approach*.

**Time series & forecasting**
- Rob J. Hyndman & George Athanasopoulos, *Forecasting: Principles and Practice* (3rd ed.). https://otexts.com/fpp3/ (Python edition: https://otexts.com/fpppy/)
- J. Michael Steele, *Stat 434: Financial Time Series* (Wharton) — ARIMA, cointegration, ARCH/GARCH. http://www-stat.wharton.upenn.edu/~steele/Courses/434/434Syllabus.html

**Machine learning & deep learning**
- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning* (ESL). https://hastie.su.domains/ElemStatLearn/
- Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — practical scikit-learn/Keras coverage matching Topics 28–47.
- Ian Goodfellow, Yoshua Bengio & Aaron Courville, *Deep Learning*. https://www.deeplearningbook.org/
- University of Warwick, *CS342 Machine Learning* outline. https://courses.warwick.ac.uk/modules/2024/CS342-15.pdf

**SQL, NLP, big data, graphs & tooling**
- *SQL* — the InfluxDB 3 SQL reference (the store's query language). https://docs.influxdata.com/influxdb3/
- Bird, Klein & Loper, *Natural Language Processing with Python* (the NLTK book). https://www.nltk.org/book/
- *Apache Spark / PySpark* documentation. https://spark.apache.org/docs/latest/api/python/
- *NetworkX* documentation (graph theory). https://networkx.org/documentation/stable/

**Data source**
- RuneScape Wiki, *Real-time Prices API* documentation — the upstream source of the 5-minute Grand Exchange snapshots. https://prices.runescape.wiki/

*Content from these sources was summarized and rephrased for compliance with
their licensing; consult the originals for full treatment.*
