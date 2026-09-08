"""Per-module curriculum content: dataset guidance and supplemental sources.

This data drives two generated artifacts per lesson:

* the seeded ``work.ipynb`` task prompts (via ``DATASET_GUIDANCE``), and
* the ``SUPPLEMENTAL_READING.md`` file (via ``MODULE_SOURCES``).

Keeping this here (rather than in the generator) makes the curated, researched
content easy to review and extend module by module.

``DATASET_GUIDANCE`` maps a module folder slug to guidance about which dataset a
learner should use for that module: the OSRS price store where it fits, or a
named alternative (Kaggle / scikit-learn / seaborn built-ins) where OSRS data
does not suit the lesson (e.g. classification, image, or text topics).

``MODULE_SOURCES`` maps a module folder slug to a list of supplemental sources.
Each source is a dict: ``{"type", "title", "url", "note"}`` where ``type`` is one
of ``paper``, ``video``, ``article``, ``lesson``. These were gathered by web
search and favor authoritative, open resources (official docs, Real Python,
Khan Academy, CS50, freeCodeCamp, university pages, and journal/preprint links).

Sources were summarized/paraphrased for licensing compliance; see each link for
the full original.
"""

from __future__ import annotations

# --- Dataset guidance ------------------------------------------------------

#: Default guidance when a module has no specific entry.
DEFAULT_GUIDANCE = (
    "Use the OSRS price store via the shared `ge_data` helper where the concept "
    "fits. If the lesson needs data OSRS doesn't provide (labels, images, text), "
    "reach for a scikit-learn or seaborn built-in dataset and note the choice."
)

DATASET_GUIDANCE: dict[str, str] = {
    # Phase 1 — tooling & wrangling
    "module01_python_essentials": (
        "No dataset needed. Practice on a single OSRS item snapshot expressed as "
        "plain Python values (e.g. `item_id = '554'`, `high = 5`, `low = 4`)."
    ),
    "module02_python_loops_functions": (
        "Loop over a small hand-typed list of OSRS item ids and prices; no live "
        "data needed yet."
    ),
    "module03_getting_started_data_science": (
        "Environment/process lesson — no dataset. Frame an OSRS market question "
        "using the data-science process."
    ),
    "module04_bash_and_git": (
        "No dataset. Optionally script a small export from the FastAPI "
        "`/api/datasets/export` endpoint as a Bash exercise."
    ),
    "module05_data_analysis_base_python": (
        "Use a small OSRS export as raw CSV/JSON and parse it with only the "
        "standard library (csv, json) before using pandas."
    ),
    "module06_data_analysis_pandas": (
        "Load OSRS series with `ge_data.load_series` / `load_frame` into pandas. "
        "The folded-in lab uses the Ames Housing / Kaggle datasets — either works."
    ),
    "module07_data_cleaning_pandas": (
        "Use a multi-item OSRS frame (missing 5-minute windows are real, natural "
        "missing data to clean). The folded lab's dataset is fine too."
    ),
    "module08_getting_started_sql": (
        "InfluxDB 3 speaks SQL — query the `itemPrice` measurement directly. The "
        "folded lab ships a `data.sqlite` you can also practice on."
    ),
    "module09_sql_table_relations": (
        "Practice joins on the folded lab's relational database; relate the ideas "
        "to joining OSRS price data with item metadata."
    ),
    "module10_other_databases_nosql": (
        "Conceptual — contrast the OSRS time-series store with a document model. "
        "No dataset required."
    ),
    "module11_apis": (
        "Use the RuneScape Wiki Prices API and this project's own FastAPI query "
        "API as the worked examples."
    ),
    "module12_html_css_web_scraping": (
        "Scrape item metadata (names, categories, examine text) from the OSRS "
        "Wiki to enrich the numeric store for later NLP/recommendation modules."
    ),
}

# --- Supplemental sources (module level) -----------------------------------

# Reused authoritative sources.
_S_PY_DOCS = {
    "type": "lesson",
    "title": "The Python Tutorial — official docs",
    "url": "https://docs.python.org/3/tutorial/",
    "note": "The canonical, version-accurate Python tutorial; the reference for language basics.",
}
_S_REALPYTHON_VARS = {
    "type": "article",
    "title": "Variables in Python: Usage and Best Practices (Real Python)",
    "url": "https://realpython.com/python-variables/",
    "note": "Clear treatment of assignment, naming, dynamic typing, and scope.",
}
_S_REALPYTHON_TYPES_VIDEO = {
    "type": "video",
    "title": "Basic Data Types in Python (Real Python video series)",
    "url": "https://realpython.com/videos/python-data-types-overview/",
    "note": "Video walkthrough of ints, floats, strings, and booleans.",
}
_S_SWEIGART = {
    "type": "lesson",
    "title": "Automate the Boring Stuff with Python (free online book)",
    "url": "https://automatetheboringstuff.com/",
    "note": "Beginner-friendly, project-driven Python; strong on the Phase 1 basics.",
}

MODULE_SOURCES: dict[str, list[dict]] = {
    "module01_python_essentials": [
        _S_PY_DOCS,
        _S_REALPYTHON_VARS,
        _S_REALPYTHON_TYPES_VIDEO,
        _S_SWEIGART,
        {
            "type": "paper",
            "title": "Python for Scientific Computing (Millman & Aivazis, CiSE 2011)",
            "url": "https://ieeexplore.ieee.org/document/5725235",
            "note": "Peer-reviewed overview of why Python became a scientific-computing language.",
        },
    ],
    "module02_python_loops_functions": [
        {
            "type": "lesson",
            "title": "Defining Functions — official Python tutorial",
            "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
            "note": "Authoritative reference for loops, control flow, and functions.",
        },
        {
            "type": "article",
            "title": "Python 'for' Loops: The Pythonic Way (Real Python)",
            "url": "https://realpython.com/python-for-loop/",
            "note": "Idiomatic looping over collections, ranges, and enumerate.",
        },
        {
            "type": "video",
            "title": "Python Functions (Programming with Mosh)",
            "url": "https://www.youtube.com/watch?v=9Os0o3wzS_I",
            "note": "Video walkthrough of defining functions, arguments, and return values.",
        },
        _S_SWEIGART,
        {
            "type": "paper",
            "title": "Structured Programming (Dijkstra, 1970) / control-flow foundations",
            "url": "https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD268.html",
            "note": "The historical argument for structured control flow behind loops/functions.",
        },
    ],
    "module03_getting_started_data_science": [
        {
            "type": "paper",
            "title": "50 Years of Data Science (David Donoho, 2017)",
            "url": "https://www.tandfonline.com/doi/full/10.1080/10618600.2017.1384734",
            "note": "Widely cited framing of what data science is and the analysis process.",
        },
        {
            "type": "article",
            "title": "PEP 8 — Style Guide for Python Code",
            "url": "https://peps.python.org/pep-0008/",
            "note": "The style standard the DS-environment lesson references.",
        },
        {
            "type": "video",
            "title": "The Data Science Process (Google/《What is Data Science》 overviews)",
            "url": "https://www.youtube.com/results?search_query=data+science+process+overview",
            "note": "Search list of process-overview videos; pick a recent authoritative one.",
        },
        {
            "type": "lesson",
            "title": "Project Jupyter — running notebooks locally",
            "url": "https://docs.jupyter.org/en/latest/",
            "note": "Official Jupyter docs for the local notebook environment setup.",
        },
    ],
    "module04_bash_and_git": [
        {
            "type": "lesson",
            "title": "Pro Git (free book, Chacon & Straub)",
            "url": "https://git-scm.com/book/en/v2",
            "note": "The definitive free Git reference, from basics to branching.",
        },
        {
            "type": "article",
            "title": "The Missing Semester of Your CS Education — Shell & Git (MIT)",
            "url": "https://missing.csail.mit.edu/",
            "note": "MIT's practical lectures on the shell, scripting, and version control.",
        },
        {
            "type": "video",
            "title": "Git & GitHub Crash Course (freeCodeCamp)",
            "url": "https://www.youtube.com/watch?v=RGOj5yH7evk",
            "note": "Hands-on video walkthrough of the core Git workflow.",
        },
        {
            "type": "paper",
            "title": "A Git-based version-controlled workflow for reproducible research",
            "url": "https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668",
            "note": "Peer-reviewed case for Git in reproducible scientific workflows.",
        },
    ],
    "module05_data_analysis_base_python": [
        {
            "type": "lesson",
            "title": "csv and json — Python standard library docs",
            "url": "https://docs.python.org/3/library/csv.html",
            "note": "Reference for reading CSV/JSON without third-party libraries.",
        },
        {
            "type": "article",
            "title": "Working With JSON Data in Python (Real Python)",
            "url": "https://realpython.com/python-json/",
            "note": "Parsing, transforming, and writing JSON with the standard library.",
        },
        {
            "type": "video",
            "title": "Python File & CSV handling (Corey Schafer)",
            "url": "https://www.youtube.com/watch?v=q5uM4VKywbA",
            "note": "Clear video on file I/O and the csv module.",
        },
        {
            "type": "paper",
            "title": "The application/json Media Type (RFC 8259)",
            "url": "https://www.rfc-editor.org/rfc/rfc8259",
            "note": "The formal JSON specification behind the API responses you'll parse.",
        },
    ],
    "module06_data_analysis_pandas": [
        {
            "type": "lesson",
            "title": "10 Minutes to pandas — official docs",
            "url": "https://pandas.pydata.org/docs/user_guide/10min.html",
            "note": "The fastest authoritative intro to Series and DataFrames.",
        },
        {
            "type": "article",
            "title": "pandas DataFrame tutorial (DataCamp)",
            "url": "https://www.datacamp.com/tutorial/pandas-tutorial-dataframe-python/",
            "note": "Worked introduction to DataFrame creation, indexing, and stats.",
        },
        {
            "type": "video",
            "title": "Pandas Tutorials (Corey Schafer playlist)",
            "url": "https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS",
            "note": "Highly regarded free video series covering pandas end to end.",
        },
        {
            "type": "paper",
            "title": "Data Structures for Statistical Computing in Python (McKinney, SciPy 2010)",
            "url": "https://conference.scipy.org/proceedings/scipy2010/mckinney.html",
            "note": "The original pandas paper by its creator.",
        },
    ],
    "module07_data_cleaning_pandas": [
        {
            "type": "lesson",
            "title": "Working with missing data — pandas user guide",
            "url": "https://pandas.pydata.org/docs/user_guide/missing_data.html",
            "note": "Authoritative reference for NaN handling, fill, and interpolation.",
        },
        {
            "type": "article",
            "title": "Tidy Data principles (applied in pandas)",
            "url": "https://www.jstatsoft.org/article/view/v059i10",
            "note": "Hadley Wickham's framework for cleaning data into a tidy shape.",
        },
        {
            "type": "video",
            "title": "Pandas: Cleaning Data (Corey Schafer)",
            "url": "https://www.youtube.com/watch?v=KdmPHEnPJPs",
            "note": "Video walkthrough of cleaning and handling missing values.",
        },
        {
            "type": "paper",
            "title": "Tidy Data (Wickham, Journal of Statistical Software, 2014)",
            "url": "https://www.jstatsoft.org/article/view/v059i10",
            "note": "Peer-reviewed foundation for reshaping/cleaning tabular data.",
        },
    ],
    "module08_getting_started_sql": [
        {
            "type": "lesson",
            "title": "Intro to SQL — Khan Academy",
            "url": "https://www.khanacademy.org/computing/computer-programming/sql/",
            "note": "Free interactive course on SELECT, WHERE, GROUP BY, and joins.",
        },
        {
            "type": "lesson",
            "title": "CS50's Introduction to Databases with SQL (Harvard)",
            "url": "https://cs50.harvard.edu/sql/",
            "note": "University-level SQL course, free to audit.",
        },
        {
            "type": "article",
            "title": "An Animated Introduction to SQL (freeCodeCamp)",
            "url": "https://freecodecamp.org/news/an-animated-introduction-to-sql-learn-to-query-relational-databases",
            "note": "Visual, beginner-friendly intro to the declarative query model.",
        },
        {
            "type": "video",
            "title": "Welcome to SQL (Khan Academy video)",
            "url": "https://www.khanacademy.org/computing/hour-of-code/hour-of-sql/v/welcome-to-sql",
            "note": "Short video introduction to relational databases and SQL.",
        },
        {
            "type": "paper",
            "title": "A Relational Model of Data for Large Shared Data Banks (Codd, 1970)",
            "url": "https://dl.acm.org/doi/10.1145/362384.362685",
            "note": "The founding paper of the relational model behind SQL.",
        },
    ],
    "module09_sql_table_relations": [
        {
            "type": "lesson",
            "title": "SQL joins — Khan Academy 'Relational queries in SQL'",
            "url": "https://www.khanacademy.org/computing/computer-programming/sql/relational-queries-in-sql/",
            "note": "Interactive lessons on joins and multi-table relations.",
        },
        {
            "type": "article",
            "title": "SQL Joins Explained (SQLite docs — SELECT)",
            "url": "https://www.sqlite.org/lang_select.html",
            "note": "Authoritative reference for join syntax and semantics.",
        },
        {
            "type": "video",
            "title": "SQL Joins tutorial (freeCodeCamp full course excerpt)",
            "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
            "note": "Video coverage of inner/outer joins and subqueries.",
        },
        {
            "type": "paper",
            "title": "A Relational Model of Data for Large Shared Data Banks (Codd, 1970)",
            "url": "https://dl.acm.org/doi/10.1145/362384.362685",
            "note": "Codd's model underpins one-to-many and many-to-many relations.",
        },
    ],
    "module10_other_databases_nosql": [
        {
            "type": "lesson",
            "title": "MongoDB — official manual (Introduction)",
            "url": "https://www.mongodb.com/docs/manual/",
            "note": "Authoritative intro to a document store, contrasting relational DBs.",
        },
        {
            "type": "article",
            "title": "NoSQL Databases: a survey and decision guidance",
            "url": "https://link.springer.com/article/10.1007/s00450-016-0334-3",
            "note": "Overview of NoSQL categories (document, key-value, column, graph).",
        },
        {
            "type": "video",
            "title": "SQL vs NoSQL Explained (freeCodeCamp)",
            "url": "https://www.youtube.com/watch?v=ZS_kXvOeQ5Y",
            "note": "When to choose relational vs. document/NoSQL models.",
        },
        {
            "type": "paper",
            "title": "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al., 2007)",
            "url": "https://dl.acm.org/doi/10.1145/1323293.1294281",
            "note": "Seminal paper motivating modern NoSQL systems.",
        },
    ],
    "module11_apis": [
        {
            "type": "lesson",
            "title": "RuneScape Wiki Real-time Prices API docs",
            "url": "https://prices.runescape.wiki/",
            "note": "The upstream API this project ingests; read its usage rules.",
        },
        {
            "type": "article",
            "title": "Python's Requests library (official docs / quickstart)",
            "url": "https://requests.readthedocs.io/en/latest/user/quickstart/",
            "note": "Authoritative guide to making HTTP requests in Python.",
        },
        {
            "type": "video",
            "title": "APIs for Beginners — HTTP requests (freeCodeCamp)",
            "url": "https://www.youtube.com/watch?v=WXsD0ZgxjRw",
            "note": "Full video course on how web APIs and HTTP work.",
        },
        {
            "type": "paper",
            "title": "Architectural Styles and the Design of Network-based Software Architectures (Fielding, 2000)",
            "url": "https://ics.uci.edu/~fielding/pubs/dissertation/top.htm",
            "note": "The dissertation that defined REST, the model behind most web APIs.",
        },
    ],
    "module12_html_css_web_scraping": [
        {
            "type": "lesson",
            "title": "Beautiful Soup documentation",
            "url": "https://www.crummy.com/software/BeautifulSoup/bs4/doc/",
            "note": "Authoritative reference for parsing and navigating HTML.",
        },
        {
            "type": "article",
            "title": "Build a Web Scraper With Python (Real Python)",
            "url": "https://realpython.com/beautiful-soup-web-scraper-python/",
            "note": "End-to-end scraping walkthrough with requests + Beautiful Soup.",
        },
        {
            "type": "video",
            "title": "Web Scraping with BeautifulSoup (Corey Schafer)",
            "url": "https://www.youtube.com/watch?v=ng2o98k983k",
            "note": "Clear video walkthrough of scraping a real page.",
        },
        {
            "type": "paper",
            "title": "Web Data Extraction, Applications and Techniques: A Survey (Ferrara et al., 2014)",
            "url": "https://arxiv.org/abs/1207.0246",
            "note": "Survey of web-scraping/data-extraction methods and uses.",
        },
    ],
}


# --- Phase 2: dataset guidance ---------------------------------------------

DATASET_GUIDANCE.update({
    "module13_statistical_measures_visualization": (
        "Use OSRS returns/volume for one or more items — perfect for central "
        "tendency, dispersion, correlation, and plotting. seaborn's built-in "
        "datasets (`tips`, `penguins`) are handy for quick chart practice."
    ),
    "module14_combinatorics_probability": (
        "Use OSRS windows as events (e.g. P(price up | volume spike)). No external "
        "dataset needed; simulate with numpy where useful."
    ),
    "module15_statistical_distributions": (
        "Fit distributions to OSRS returns (heavy-tailed) and model trade counts "
        "as Poisson. scipy.stats provides the distributions."
    ),
    "module16_clt_confidence_intervals": (
        "Sample OSRS returns to show the CLT empirically and build a t-interval "
        "for an item's mean return."
    ),
    "module17_hypothesis_testing": (
        "Test OSRS price change around a known game-update date (before vs. after). "
        "OSRS data fits well."
    ),
    "module18_power_and_anova": (
        "ANOVA across OSRS item categories' returns. The folded labs ship small "
        "CSVs (e.g. ToothGrowth, salaries) that are also fine."
    ),
    "module19_ab_testing": (
        "Frame a natural OSRS experiment (weekend vs. weekday trading). For a "
        "classic A/B dataset, Kaggle's 'AB Testing' dataset works too."
    ),
    "module20_bayesian_statistics": (
        "Maintain a Bayesian belief about an OSRS item trending up as snapshots "
        "arrive. No external data required."
    ),
    "module21_intro_linear_regression": (
        "Regress one OSRS item's price on a related item's lagged price. The folded "
        "labs use Kaggle's Ames Housing / Advertising — either is fine."
    ),
    "module22_multiple_regression_validation": (
        "Build a multi-feature OSRS price model (lags, volume, calendar dummies). "
        "The folded labs' housing datasets also work for the mechanics."
    ),
    "module23_extensions_linear_models": (
        "Add interactions/polynomial terms to the OSRS price model; use the folded "
        "lab data to see bias-variance tradeoffs clearly."
    ),
    # Phase 3
    "module24_object_oriented_programming": (
        "No dataset. Wrap the OSRS loaders + a model in a `MarketModel` class."
    ),
    "module25_linear_algebra": (
        "Solve the OLS normal equations on an OSRS price model by hand with numpy. "
        "No external data."
    ),
    "module26_calculus_gradient_descent": (
        "Implement gradient descent to fit a regression on OSRS prices; visualize "
        "the cost surface. sklearn's `make_regression` gives clean synthetic data."
    ),
    "module27_feature_selection_ridge_lasso": (
        "Use many correlated OSRS lag/volume features for lasso/ridge selection. "
        "sklearn's diabetes dataset is the classic ridge/lasso demo."
    ),
    "module28_logistic_regression": (
        "Predict OSRS next-hour up/down (binary). For a labeled classic, use "
        "sklearn's breast-cancer or Kaggle's Titanic dataset."
    ),
    "module29_mle_logistic_regression": (
        "Same OSRS up/down target, coding logistic regression from scratch via MLE. "
        "sklearn's breast-cancer dataset is a good cross-check."
    ),
    "module30_k_nearest_neighbors": (
        "Classify OSRS move direction from recent-feature neighbors. sklearn's Iris "
        "is the canonical KNN teaching set."
    ),
    "module31_naive_bayes": (
        "Gaussian NB on OSRS features; for document-NB, use sklearn's "
        "20 Newsgroups text dataset."
    ),
    "module32_decision_trees": (
        "CART regression/classification on OSRS features. sklearn's Iris / "
        "breast-cancer datasets illustrate splits cleanly."
    ),
    "module33_ensemble_methods": (
        "Random forest / XGBoost on OSRS price/direction. Kaggle's Titanic or "
        "sklearn's California Housing are strong ensemble demos."
    ),
    "module34_support_vector_machines": (
        "SVM for OSRS direction. sklearn's Iris / make_classification show margins "
        "and kernels clearly (OSRS data can be noisy for SVMs)."
    ),
    "module35_ml_pipeline": (
        "Wrap OSRS feature-engineering + scaling + model in one sklearn Pipeline. "
        "Any of the sklearn built-ins work for the mechanics."
    ),
    # Phase 4
    "module36_principal_component_analysis": (
        "PCA on a panel of OSRS item returns to find market factors. sklearn's "
        "digits dataset is the classic image-PCA demo."
    ),
    "module37_clustering": (
        "Cluster OSRS items by price/volume behavior into market segments. "
        "sklearn's make_blobs / Iris are good clustering sandboxes."
    ),
    "module38_big_data_pyspark": (
        "The full multi-year OSRS history is genuinely large — a real PySpark "
        "target. Any large public CSV (e.g. NYC taxi) also works to practice Spark."
    ),
    "module39_recommendation_systems": (
        "Recommend related OSRS items from co-movement. The classic recommender "
        "dataset is MovieLens (grouplens.org) — used by the `surprise` library."
    ),
    "module40_time_series_models": (
        "OSRS price series are the core use case — decompose, difference, ARIMA. "
        "The folded labs ship time-series CSVs too."
    ),
    "module43_natural_language_processing": (
        "Use scraped OSRS item names/examine text (Topic 12). Classic NLP corpora: "
        "sklearn's 20 Newsgroups, NLTK corpora, or Kaggle's IMDb reviews."
    ),
    "module44_neural_networks": (
        "A small net for OSRS next-step price. For a first classifier, sklearn's "
        "digits or Keras's MNIST are standard."
    ),
    "module45_deep_neural_networks": (
        "Deepen the OSRS price net; Keras's MNIST/Fashion-MNIST are the standard "
        "image demos for MLP depth."
    ),
    "module46_tuning_neural_networks": (
        "Tune the OSRS price net (dropout, batch norm, early stopping). MNIST/"
        "Fashion-MNIST also show regularization effects clearly."
    ),
    "module47_convolutional_neural_networks": (
        "CNNs need image data: use Keras's MNIST/CIFAR-10. Optionally treat OSRS "
        "item×time windows as 1-D/2-D signals for a CNN experiment."
    ),
    "module48_transfer_learning": (
        "Pretrain a sequence model on high-liquidity OSRS items, fine-tune on a "
        "low-history item. For images, use Keras applications + a Kaggle image set."
    ),
    "module49_deep_nlp_sequence_models": (
        "LSTM/GRU forecasters on OSRS price windows; embeddings on item text. "
        "Classic sequence corpora: IMDb reviews, or any Kaggle text dataset."
    ),
    "module50_graph_theory_networks": (
        "Build an OSRS item co-movement graph (edges = correlated returns) with "
        "NetworkX. NetworkX also ships classic graphs (Karate Club) for practice."
    ),
    "module51_operationalizing_mlops_cloud": (
        "Package the best OSRS model behind the FastAPI service / Docker. No new "
        "dataset — this is about shipping what you built."
    ),
})


# --- Phase 2-4: supplemental sources ---------------------------------------

# Canonical reusable sources for the stats/ML/DL topics.
_ISLR = {
    "type": "lesson",
    "title": "An Introduction to Statistical Learning (free PDF + labs)",
    "url": "https://www.statlearning.com/",
    "note": "The standard undergraduate text; free PDF with Python/R labs.",
}
_STATQUEST = lambda topic, url: {  # noqa: E731
    "type": "video",
    "title": f"StatQuest: {topic} (Josh Starmer)",
    "url": url,
    "note": "StatQuest's clear, visual explanation of the topic.",
}

MODULE_SOURCES.update({
    "module13_statistical_measures_visualization": [
        {"type": "lesson", "title": "seaborn: statistical data visualization (official tutorial)",
         "url": "https://seaborn.pydata.org/tutorial.html",
         "note": "Authoritative guide to statistical plots on pandas DataFrames."},
        {"type": "article", "title": "Seaborn Statistical Data Visualization (DataCamp)",
         "url": "https://www.datacamp.com/tutorial/seaborn-python-tutorial/",
         "note": "Worked intro to the common statistical chart types."},
        _STATQUEST("Measures of central tendency & spread",
                   "https://www.youtube.com/watch?v=SzZ6GpcfoQY"),
        {"type": "paper", "title": "seaborn: statistical data visualization (Waskom, JOSS 2021)",
         "url": "https://joss.theoj.org/papers/10.21105/joss.03021",
         "note": "The peer-reviewed paper describing the seaborn library."},
    ],
    "module14_combinatorics_probability": [
        {"type": "article", "title": "Seeing Theory — visual probability (Brown University)",
         "url": "https://seeing-theory.brown.edu/",
         "note": "Interactive visual introduction to probability concepts."},
        _ISLR,
        {"type": "lesson", "title": "MIT 6.041 / Khan Academy Probability",
         "url": "https://www.khanacademy.org/math/statistics-probability/probability-library",
         "note": "Free lessons on sets, conditional probability, and combinatorics."},
        _STATQUEST("Probability is not Likelihood / Bayes",
                   "https://www.youtube.com/watch?v=pYxNSUDSFH4"),
        {"type": "paper", "title": "An Essay towards Solving a Problem in the Doctrine of Chances (Bayes, 1763)",
         "url": "https://royalsocietypublishing.org/doi/10.1098/rstl.1763.0053",
         "note": "The original paper introducing Bayes' theorem."},
    ],
    "module15_statistical_distributions": [
        {"type": "lesson", "title": "scipy.stats — statistical functions (docs)",
         "url": "https://docs.scipy.org/doc/scipy/reference/stats.html",
         "note": "Reference for the distributions you'll fit and sample."},
        {"type": "article", "title": "4 Probability Distributions Every Data Scientist Needs to Know (Built In)",
         "url": "https://builtin.com/data-science/probability-distributions-data-science",
         "note": "Relates the common distributions (normal, binomial, uniform, Poisson) and their uses."},
        _STATQUEST("The Normal Distribution, Clearly Explained",
                   "https://www.youtube.com/watch?v=rzFX5NWojp0"),
        {"type": "paper", "title": "On the mathematical foundations of theoretical statistics (Fisher, 1922)",
         "url": "https://royalsocietypublishing.org/doi/10.1098/rsta.1922.0009",
         "note": "Foundational paper on estimation and distributions."},
    ],
    "module16_clt_confidence_intervals": [
        _ISLR,
        {"type": "article", "title": "Confidence Intervals (Real Python / scipy)",
         "url": "https://realpython.com/python-statistics/",
         "note": "Computing descriptive stats and intervals in Python."},
        _STATQUEST("The Central Limit Theorem, Clearly Explained",
                   "https://www.youtube.com/watch?v=YAlJCEDH2uY"),
        {"type": "paper", "title": "The Bootstrap and confidence intervals (Efron, 1979)",
         "url": "https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full",
         "note": "Efron's bootstrap, a resampling route to confidence intervals."},
    ],
    "module17_hypothesis_testing": [
        {"type": "lesson", "title": "Khan Academy — Significance tests (hypothesis testing)",
         "url": "https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample",
         "note": "Free lessons on null hypotheses, z/t tests, and p-values."},
        {"type": "article", "title": "The ASA Statement on p-Values (Wasserstein & Lazar, 2016)",
         "url": "https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108",
         "note": "The American Statistical Association's guidance on p-value use."},
        _STATQUEST("Hypothesis Testing and the Null Hypothesis",
                   "https://www.youtube.com/watch?v=0oc49DyA3hU"),
        {"type": "paper", "title": "P-Values: Misunderstood and Misused (Frontiers in Physics, 2016)",
         "url": "https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2016.00006/full",
         "note": "Peer-reviewed review of common p-value misinterpretations."},
    ],
    "module18_power_and_anova": [
        _ISLR,
        {"type": "article", "title": "Low Power Tests Exaggerate Effect Sizes (Statistics by Jim)",
         "url": "https://statisticsbyjim.com/hypothesis-testing/low-power-studies/",
         "note": "Accessible explanation of statistical power, effect size, and sample size."},
        _STATQUEST("ANOVA, Clearly Explained",
                   "https://www.youtube.com/watch?v=0Vj2V2qRU10"),
        {"type": "paper", "title": "A power primer (Cohen, 1992)",
         "url": "https://psycnet.apa.org/record/1992-98120-001",
         "note": "Cohen's classic guide to statistical power and effect sizes."},
    ],
    "module19_ab_testing": [
        {"type": "lesson", "title": "Udacity/Google — A/B Testing (course overview)",
         "url": "https://www.udacity.com/course/ab-testing--ud257",
         "note": "Widely used free course on designing and analyzing A/B tests."},
        {"type": "article", "title": "Trustworthy Online Controlled Experiments (overview)",
         "url": "https://exp-platform.com/",
         "note": "Kohavi et al.'s resources on real-world online experimentation."},
        _STATQUEST("A/B testing and Fisher's exact test",
                   "https://www.youtube.com/watch?v=udyAvvaMjfM"),
        {"type": "paper", "title": "Controlled experiments on the web: survey and practical guide (Kohavi et al., 2009)",
         "url": "https://link.springer.com/article/10.1007/s10618-008-0114-1",
         "note": "Peer-reviewed practical guide to online A/B experiments."},
    ],
    "module20_bayesian_statistics": [
        {"type": "lesson", "title": "Think Bayes (free book, Allen Downey)",
         "url": "https://allendowney.github.io/ThinkBayes2/",
         "note": "Bayesian statistics from a programmer's perspective, in Python."},
        {"type": "article", "title": "Full Explanation of MLE, MAP and Bayesian Inference (Towards Data Science)",
         "url": "https://towardsdatascience.com/full-explanation-of-mle-map-and-bayesian-inference-1db9a7fb1d2b/",
         "note": "Clear contrast of maximum likelihood vs. maximum a posteriori vs. full Bayes."},
        _STATQUEST("Bayes' Theorem, Clearly Explained",
                   "https://www.youtube.com/watch?v=9wCnvr7Xw4E"),
        {"type": "paper", "title": "An Essay towards Solving a Problem in the Doctrine of Chances (Bayes, 1763)",
         "url": "https://royalsocietypublishing.org/doi/10.1098/rstl.1763.0053",
         "note": "The origin of Bayesian inference."},
    ],
    "module21_intro_linear_regression": [
        {"type": "article", "title": "Linear Regression — a friendly walkthrough (Towards Data Science)",
         "url": "https://towardsdatascience.com/linear-regression-explained-1b36f97b7572/",
         "note": "Approachable article on fitting and interpreting a regression line."},
        _ISLR,
        {"type": "lesson", "title": "statsmodels — Ordinary Least Squares (docs)",
         "url": "https://www.statsmodels.org/stable/regression.html",
         "note": "Reference for OLS, diagnostics, and summary output."},
        _STATQUEST("Linear Regression (Fitting a line), Clearly Explained",
                   "https://www.youtube.com/watch?v=nk2CQITm_eo"),
        {"type": "paper", "title": "Regression towards mediocrity in hereditary stature (Galton, 1886)",
         "url": "https://galton.org/essays/1880-1889/galton-1886-jaigi-regression-stature.pdf",
         "note": "Galton's original paper that named 'regression'."},
    ],
    "module22_multiple_regression_validation": [
        {"type": "article", "title": "Multicollinearity and VIF explained (Statistics by Jim)",
         "url": "https://statisticsbyjim.com/regression/multicollinearity-in-regression-analysis/",
         "note": "Practical article on diagnosing multicollinearity in multiple regression."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — cross-validation (user guide)",
         "url": "https://scikit-learn.org/stable/modules/cross_validation.html",
         "note": "Authoritative guide to validation and avoiding leakage."},
        _STATQUEST("Machine Learning Fundamentals: Cross Validation",
                   "https://www.youtube.com/watch?v=fSytzGwwBVw"),
        {"type": "paper", "title": "A study of cross-validation and bootstrap for accuracy estimation (Kohavi, 1995)",
         "url": "https://dl.acm.org/doi/10.5555/1643031.1643047",
         "note": "Classic empirical comparison of validation methods."},
    ],
    "module23_extensions_linear_models": [
        _ISLR,
        {"type": "article", "title": "Bias-Variance Tradeoff (Scott Fortmann-Roe)",
         "url": "http://scott.fortmann-roe.com/docs/BiasVariance.html",
         "note": "The go-to visual explanation of bias vs. variance."},
        _STATQUEST("Bias and Variance, Clearly Explained",
                   "https://www.youtube.com/watch?v=EuBBz3bI-aA"),
        {"type": "paper", "title": "Neural networks and the bias/variance dilemma (Geman et al., 1992)",
         "url": "https://direct.mit.edu/neco/article/4/1/1/5601",
         "note": "The paper that framed the bias-variance decomposition."},
    ],
    # Phase 3
    "module24_object_oriented_programming": [
        {"type": "lesson", "title": "Classes — official Python tutorial",
         "url": "https://docs.python.org/3/tutorial/classes.html",
         "note": "Authoritative reference for classes, instances, and methods."},
        {"type": "article", "title": "Object-Oriented Programming in Python (Real Python)",
         "url": "https://realpython.com/python3-object-oriented-programming/",
         "note": "Practical OOP walkthrough with examples."},
        {"type": "video", "title": "Python OOP Tutorials (Corey Schafer)",
         "url": "https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc",
         "note": "Highly regarded free video series on Python OOP."},
        {"type": "paper", "title": "The Object-Oriented paradigm (Stefik & Bobrow, 1985)",
         "url": "https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/508",
         "note": "Early survey framing object-oriented programming concepts."},
    ],
    "module25_linear_algebra": [
        {"type": "video", "title": "Essence of Linear Algebra (3Blue1Brown)",
         "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab",
         "note": "The canonical visual series building linear-algebra intuition."},
        {"type": "lesson", "title": "NumPy — linear algebra (numpy.linalg docs)",
         "url": "https://numpy.org/doc/stable/reference/routines.linalg.html",
         "note": "Reference for matrix ops and solving linear systems."},
        {"type": "article", "title": "Linear Algebra for Data Science (article)",
         "url": "https://www.deeplearningbook.org/contents/linear_algebra.html",
         "note": "The linear-algebra chapter of the Deep Learning book (free)."},
        {"type": "paper", "title": "The Matrix Cookbook (Petersen & Pedersen)",
         "url": "https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf",
         "note": "A dense reference of matrix identities used throughout ML."},
    ],
    "module26_calculus_gradient_descent": [
        {"type": "video", "title": "Gradient descent, how neural networks learn (3Blue1Brown)",
         "url": "https://www.youtube.com/watch?v=IHZwWFHWa-w",
         "note": "Visual intuition for gradient descent and cost surfaces."},
        {"type": "lesson", "title": "Google ML Crash Course — Gradient descent",
         "url": "https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent",
         "note": "Concise authoritative lesson on the algorithm."},
        {"type": "article", "title": "An overview of gradient descent optimization algorithms (Ruder)",
         "url": "https://www.ruder.io/optimizing-gradient-descent/",
         "note": "Widely cited survey of gradient-descent variants."},
        {"type": "paper", "title": "A Stochastic Approximation Method (Robbins & Monro, 1951)",
         "url": "https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-22/issue-3/A-Stochastic-Approximation-Method/10.1214/aoms/1177729586.full",
         "note": "The origin of stochastic gradient methods."},
    ],
    "module27_feature_selection_ridge_lasso": [
        {"type": "article", "title": "Ridge vs Lasso regression, intuitively (Towards Data Science)",
         "url": "https://towardsdatascience.com/ridge-and-lasso-regression-a-complete-guide-with-python-scikit-learn-e20e34bcbf0b/",
         "note": "Article contrasting L1/L2 regularization with code."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — Linear Models (Ridge, Lasso)",
         "url": "https://scikit-learn.org/stable/modules/linear_model.html",
         "note": "Reference for regularized regression and selection."},
        _STATQUEST("Regularization Part 1: Ridge (L2) Regression",
                   "https://www.youtube.com/watch?v=Q81RR3yKn30"),
        {"type": "paper", "title": "Regression Shrinkage and Selection via the Lasso (Tibshirani, 1996)",
         "url": "https://www.jstor.org/stable/2346178",
         "note": "The original lasso paper."},
    ],
    "module28_logistic_regression": [
        {"type": "article", "title": "Logistic Regression (Google ML Crash Course)",
         "url": "https://developers.google.com/machine-learning/crash-course/logistic-regression",
         "note": "Concise article on the logistic model, log-odds, and calibration."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — Logistic Regression (docs)",
         "url": "https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression",
         "note": "Reference for fitting and evaluating logistic models."},
        _STATQUEST("Logistic Regression, Clearly Explained",
                   "https://www.youtube.com/watch?v=yIYKR4sgzI8"),
        {"type": "paper", "title": "The regression analysis of binary sequences (Cox, 1958)",
         "url": "https://www.jstor.org/stable/2983890",
         "note": "Cox's foundational paper on logistic regression."},
    ],
    "module29_mle_logistic_regression": [
        {"type": "lesson", "title": "MLE explained (StatLect)",
         "url": "https://www.statlect.com/fundamentals-of-statistics/maximum-likelihood",
         "note": "Careful, worked treatment of maximum likelihood estimation."},
        {"type": "article", "title": "A Gentle Introduction to Maximum Likelihood Estimation (ML Mastery)",
         "url": "https://machinelearningmastery.com/what-is-maximum-likelihood-estimation-in-machine-learning/",
         "note": "MLE framed for machine-learning practitioners."},
        _STATQUEST("Maximum Likelihood, Clearly Explained",
                   "https://www.youtube.com/watch?v=XepXtl9YKwc"),
        {"type": "paper", "title": "On the mathematical foundations of theoretical statistics (Fisher, 1922)",
         "url": "https://royalsocietypublishing.org/doi/10.1098/rsta.1922.0009",
         "note": "Fisher's paper introducing maximum likelihood."},
    ],
    "module30_k_nearest_neighbors": [
        {"type": "article", "title": "A complete guide to K-Nearest Neighbors (article)",
         "url": "https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/",
         "note": "Article on KNN mechanics, distance metrics, and choosing K."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — Nearest Neighbors (docs)",
         "url": "https://scikit-learn.org/stable/modules/neighbors.html",
         "note": "Reference for KNN classification/regression and metrics."},
        _STATQUEST("K-nearest neighbors, Clearly Explained",
                   "https://www.youtube.com/watch?v=HVXime0nQeI"),
        {"type": "paper", "title": "Nearest neighbor pattern classification (Cover & Hart, 1967)",
         "url": "https://ieeexplore.ieee.org/document/1053964",
         "note": "The founding paper of nearest-neighbor classification."},
    ],
    "module31_naive_bayes": [
        {"type": "lesson", "title": "scikit-learn — Naive Bayes (docs)",
         "url": "https://scikit-learn.org/stable/modules/naive_bayes.html",
         "note": "Reference for Gaussian and multinomial naive Bayes."},
        {"type": "article", "title": "Naive Bayes for text classification (article)",
         "url": "https://sebastianraschka.com/Articles/2014_naive_bayes_1.html",
         "note": "Sebastian Raschka's careful derivation and text example."},
        _STATQUEST("Naive Bayes, Clearly Explained",
                   "https://www.youtube.com/watch?v=O2L2Uv9pdDA"),
        {"type": "paper", "title": "Idiot's Bayes — not so stupid after all? (Hand & Yu, 2001)",
         "url": "https://www.jstor.org/stable/1403452",
         "note": "Why naive Bayes works surprisingly well despite its assumptions."},
    ],
    "module32_decision_trees": [
        {"type": "article", "title": "Decision Trees explained (Towards Data Science)",
         "url": "https://towardsdatascience.com/decision-trees-explained-3ec41632ceb6/",
         "note": "Article on entropy, information gain, and tree building."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — Decision Trees (docs)",
         "url": "https://scikit-learn.org/stable/modules/tree.html",
         "note": "Reference for training, tuning, and pruning trees."},
        _STATQUEST("Decision Trees, Clearly Explained",
                   "https://www.youtube.com/watch?v=_L39rN6gz7Y"),
        {"type": "paper", "title": "Induction of Decision Trees (Quinlan, 1986)",
         "url": "https://link.springer.com/article/10.1007/BF00116251",
         "note": "Quinlan's ID3 paper on entropy and information gain."},
    ],
    "module33_ensemble_methods": [
        {"type": "article", "title": "A Gentle Introduction to Gradient Boosting (ML Mastery)",
         "url": "https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/",
         "note": "Article introducing bagging, boosting, and XGBoost."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — Ensemble methods (docs)",
         "url": "https://scikit-learn.org/stable/modules/ensemble.html",
         "note": "Reference for random forests and gradient boosting."},
        _STATQUEST("Random Forests / Gradient Boost (StatQuest series)",
                   "https://www.youtube.com/watch?v=J4Wdy0Wc_xQ"),
        {"type": "paper", "title": "Random Forests (Breiman, 2001)",
         "url": "https://link.springer.com/article/10.1023/A:1010933404324",
         "note": "Breiman's original random-forests paper."},
    ],
    "module34_support_vector_machines": [
        {"type": "article", "title": "Support Vector Machine — intuition and kernels (article)",
         "url": "https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47/",
         "note": "Article on margins and the kernel trick."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — Support Vector Machines (docs)",
         "url": "https://scikit-learn.org/stable/modules/svm.html",
         "note": "Reference for SVMs, kernels, and parameters."},
        _STATQUEST("Support Vector Machines, Clearly Explained",
                   "https://www.youtube.com/watch?v=efR1C6CvhmE"),
        {"type": "paper", "title": "Support-Vector Networks (Cortes & Vapnik, 1995)",
         "url": "https://link.springer.com/article/10.1007/BF00994018",
         "note": "The founding SVM paper."},
    ],
    "module35_ml_pipeline": [
        {"type": "lesson", "title": "scikit-learn — Pipelines and composite estimators",
         "url": "https://scikit-learn.org/stable/modules/compose.html",
         "note": "Authoritative guide to leak-safe pipelines."},
        {"type": "article", "title": "Automate ML Workflows with Pipelines (Machine Learning Mastery)",
         "url": "https://machinelearningmastery.com/automate-machine-learning-workflows-pipelines-python-scikit-learn/",
         "note": "Why and how to wrap preprocessing + model into one leak-safe object."},
        {"type": "video", "title": "scikit-learn Pipelines (video walkthrough)",
         "url": "https://www.youtube.com/watch?v=w9IGkBfOoic",
         "note": "Hands-on pipeline construction and cross-validation."},
        {"type": "paper", "title": "Scikit-learn: Machine Learning in Python (Pedregosa et al., 2011)",
         "url": "https://jmlr.org/papers/v12/pedregosa11a.html",
         "note": "The scikit-learn paper describing its API design."},
    ],
    # Phase 4
    "module36_principal_component_analysis": [
        {"type": "article", "title": "A One-Stop Shop for PCA (Towards Data Science)",
         "url": "https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c/",
         "note": "Article building PCA intuition from the covariance matrix."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — PCA / decomposition (docs)",
         "url": "https://scikit-learn.org/stable/modules/decomposition.html",
         "note": "Reference for PCA and related dimensionality reduction."},
        _STATQUEST("Principal Component Analysis (PCA), Step-by-Step",
                   "https://www.youtube.com/watch?v=FgakZw6K1QQ"),
        {"type": "paper", "title": "On lines and planes of closest fit (Pearson, 1901)",
         "url": "https://www.tandfonline.com/doi/abs/10.1080/14786440109462720",
         "note": "Pearson's original paper introducing PCA."},
    ],
    "module37_clustering": [
        {"type": "article", "title": "K-Means clustering explained (article)",
         "url": "https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/",
         "note": "Article on clustering methods and choosing the number of clusters."},
        _ISLR,
        {"type": "lesson", "title": "scikit-learn — Clustering (docs)",
         "url": "https://scikit-learn.org/stable/modules/clustering.html",
         "note": "Reference for k-means, hierarchical, and DBSCAN."},
        _STATQUEST("K-means clustering, Clearly Explained",
                   "https://www.youtube.com/watch?v=4b5d3muPQmA"),
        {"type": "paper", "title": "A density-based algorithm for discovering clusters — DBSCAN (Ester et al., 1996)",
         "url": "https://dl.acm.org/doi/10.5555/3001460.3001507",
         "note": "The DBSCAN paper for density-based clustering."},
    ],
    "module38_big_data_pyspark": [
        {"type": "lesson", "title": "PySpark — official documentation",
         "url": "https://spark.apache.org/docs/latest/api/python/",
         "note": "Authoritative PySpark API and getting-started docs."},
        {"type": "article", "title": "PySpark for Data Science (DataCamp tutorial)",
         "url": "https://www.datacamp.com/tutorial/pyspark-tutorial-getting-started-with-pyspark",
         "note": "Hands-on intro to Spark DataFrames and MLlib."},
        {"type": "video", "title": "PySpark Full Course (freeCodeCamp)",
         "url": "https://www.youtube.com/watch?v=_C8kWso4ne4",
         "note": "End-to-end video course on PySpark."},
        {"type": "paper", "title": "Resilient Distributed Datasets (Zaharia et al., 2012)",
         "url": "https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/zaharia",
         "note": "The RDD paper underpinning Spark."},
    ],
    "module39_recommendation_systems": [
        {"type": "lesson", "title": "Surprise — recommender library docs",
         "url": "https://surprise.readthedocs.io/en/stable/",
         "note": "Library for building/evaluating collaborative-filtering models."},
        {"type": "article", "title": "MovieLens datasets (GroupLens)",
         "url": "https://grouplens.org/datasets/movielens/",
         "note": "The classic recommender dataset used across the field."},
        {"type": "video", "title": "Recommender Systems (Andrew Ng, ML course excerpt)",
         "url": "https://www.youtube.com/watch?v=giIXNoiqO_U",
         "note": "Collaborative filtering and matrix factorization explained."},
        {"type": "paper", "title": "Matrix Factorization Techniques for Recommender Systems (Koren et al., 2009)",
         "url": "https://ieeexplore.ieee.org/document/5197422",
         "note": "The influential Netflix-Prize matrix-factorization paper."},
    ],
    "module40_time_series_models": [
        {"type": "article", "title": "A Gentle Introduction to ARIMA (ML Mastery)",
         "url": "https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/",
         "note": "Article on stationarity, ACF/PACF, and fitting ARIMA in Python."},
        {"type": "lesson", "title": "Forecasting: Principles and Practice (Hyndman, free online)",
         "url": "https://otexts.com/fpp3/",
         "note": "The standard open text for time-series decomposition and ARIMA."},
        {"type": "lesson", "title": "statsmodels — Time Series Analysis (tsa docs)",
         "url": "https://www.statsmodels.org/stable/tsa.html",
         "note": "Reference for ACF/PACF, ARIMA, and SARIMAX."},
        {"type": "video", "title": "Time Series Analysis (ritvikmath ARIMA series)",
         "url": "https://www.youtube.com/watch?v=DeORzP0go5I",
         "note": "Clear video series on AR, MA, ARMA, and ARIMA."},
        {"type": "paper", "title": "Time Series Analysis: Forecasting and Control (Box & Jenkins)",
         "url": "https://onlinelibrary.wiley.com/doi/book/10.1002/9781118619193",
         "note": "The Box-Jenkins methodology that defines ARIMA modeling."},
    ],
    "module43_natural_language_processing": [
        {"type": "lesson", "title": "Natural Language Processing with Python (NLTK book)",
         "url": "https://www.nltk.org/book/",
         "note": "The free NLTK book covering tokenization, tagging, classification."},
        {"type": "article", "title": "scikit-learn — Working with text data (tutorial)",
         "url": "https://scikit-learn.org/1.4/tutorial/text_analytics/working_with_text_data.html",
         "note": "TF-IDF vectorization and text classification, end to end."},
        {"type": "video", "title": "NLP Zero to Hero (TensorFlow) / NLTK tutorials",
         "url": "https://www.youtube.com/watch?v=fNxaJsNG3-s",
         "note": "Video introduction to NLP concepts and pipelines."},
        {"type": "paper", "title": "Efficient Estimation of Word Representations (word2vec; Mikolov et al., 2013)",
         "url": "https://arxiv.org/abs/1301.3781",
         "note": "The word2vec paper behind modern word embeddings."},
    ],
    "module44_neural_networks": [
        {"type": "video", "title": "But what is a neural network? (3Blue1Brown)",
         "url": "https://www.youtube.com/watch?v=aircAruvnKk",
         "note": "The canonical visual introduction to neural networks."},
        {"type": "lesson", "title": "Keras — getting started (docs)",
         "url": "https://keras.io/getting_started/",
         "note": "Authoritative quickstart for building networks in Keras."},
        {"type": "article", "title": "Deep Learning (free book) — Ch. 6 Feedforward Networks",
         "url": "https://www.deeplearningbook.org/contents/mlp.html",
         "note": "Goodfellow et al.'s chapter on feedforward networks."},
        {"type": "paper", "title": "Learning representations by back-propagating errors (Rumelhart et al., 1986)",
         "url": "https://www.nature.com/articles/323533a0",
         "note": "The backpropagation paper that made training deep nets practical."},
    ],
    "module45_deep_neural_networks": [
        {"type": "video", "title": "Neural Networks series (3Blue1Brown)",
         "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi",
         "note": "The full visual series through deeper networks and learning."},
        {"type": "lesson", "title": "Deep Learning (free book, Goodfellow/Bengio/Courville)",
         "url": "https://www.deeplearningbook.org/",
         "note": "The standard graduate reference; free to read online."},
        {"type": "article", "title": "Keras examples — MLP / image classification",
         "url": "https://keras.io/examples/",
         "note": "Runnable reference examples for deeper networks."},
        {"type": "paper", "title": "ImageNet Classification with Deep CNNs — AlexNet (Krizhevsky et al., 2012)",
         "url": "https://dl.acm.org/doi/10.1145/3065386",
         "note": "The paper that launched the modern deep-learning era."},
    ],
    "module46_tuning_neural_networks": [
        {"type": "lesson", "title": "Keras — regularization & callbacks (docs)",
         "url": "https://keras.io/api/layers/regularizers/",
         "note": "Reference for dropout, weight decay, and early stopping."},
        {"type": "article", "title": "A Recipe for Training Neural Networks (Karpathy)",
         "url": "https://karpathy.github.io/2019/04/25/recipe/",
         "note": "Karpathy's widely shared practical tuning guide."},
        {"type": "video", "title": "Regularization / tuning (deeplearning.ai excerpts)",
         "url": "https://www.youtube.com/watch?v=6g0t3Phly2M",
         "note": "Video coverage of dropout, normalization, and tuning."},
        {"type": "paper", "title": "Dropout: A Simple Way to Prevent Overfitting (Srivastava et al., 2014)",
         "url": "https://jmlr.org/papers/v15/srivastava14a.html",
         "note": "The dropout paper; also see Batch Normalization (Ioffe & Szegedy, 2015)."},
    ],
    "module47_convolutional_neural_networks": [
        {"type": "video", "title": "But what is a convolution? (3Blue1Brown)",
         "url": "https://www.youtube.com/watch?v=KuXjwB4LzSA",
         "note": "Visual intuition for the convolution operation."},
        {"type": "lesson", "title": "CS231n — Convolutional Neural Networks (Stanford)",
         "url": "https://cs231n.github.io/convolutional-networks/",
         "note": "The canonical university course notes on CNNs."},
        {"type": "article", "title": "Keras — CNN example (image classification)",
         "url": "https://keras.io/examples/vision/mnist_convnet/",
         "note": "A runnable CNN reference implementation."},
        {"type": "paper", "title": "Gradient-based learning applied to document recognition — LeNet (LeCun et al., 1998)",
         "url": "https://ieeexplore.ieee.org/document/726791",
         "note": "The foundational CNN paper."},
    ],
    "module48_transfer_learning": [
        {"type": "lesson", "title": "Keras — Transfer learning & fine-tuning (guide)",
         "url": "https://keras.io/guides/transfer_learning/",
         "note": "Authoritative guide to reusing pretrained networks."},
        {"type": "article", "title": "A Survey on Transfer Learning (overview)",
         "url": "https://machinelearningmastery.com/transfer-learning-for-deep-learning/",
         "note": "Accessible overview of when and how to transfer."},
        {"type": "video", "title": "Transfer Learning (TensorFlow tutorial video)",
         "url": "https://www.youtube.com/watch?v=LsdxvjLWkIY",
         "note": "Hands-on transfer-learning walkthrough."},
        {"type": "paper", "title": "A Survey on Transfer Learning (Pan & Yang, 2010)",
         "url": "https://ieeexplore.ieee.org/document/5288526",
         "note": "The widely cited transfer-learning survey."},
    ],
    "module49_deep_nlp_sequence_models": [
        {"type": "article", "title": "Understanding LSTM Networks (Christopher Olah)",
         "url": "https://colah.github.io/posts/2015-08-Understanding-LSTMs/",
         "note": "The definitive visual explanation of LSTMs."},
        {"type": "lesson", "title": "CS224n — NLP with Deep Learning (Stanford)",
         "url": "https://web.stanford.edu/class/cs224n/",
         "note": "University course on sequence models and embeddings."},
        {"type": "video", "title": "Recurrent Neural Networks / LSTMs (StatQuest)",
         "url": "https://www.youtube.com/watch?v=YCzL96nL7j0",
         "note": "Clear video explanation of RNNs and LSTMs."},
        {"type": "paper", "title": "Long Short-Term Memory (Hochreiter & Schmidhuber, 1997)",
         "url": "https://www.bioinf.jku.at/publications/older/2604.pdf",
         "note": "The original LSTM paper."},
    ],
    "module50_graph_theory_networks": [
        {"type": "lesson", "title": "NetworkX — tutorial & documentation",
         "url": "https://networkx.org/documentation/stable/tutorial.html",
         "note": "Authoritative guide to building and analyzing graphs in Python."},
        {"type": "article", "title": "Networks, Crowds, and Markets (Easley & Kleinberg, free book)",
         "url": "https://www.cs.cornell.edu/home/kleinber/networks-book/",
         "note": "Free textbook on graph theory and network analysis."},
        {"type": "video", "title": "Graph Theory / Network Analysis (video course)",
         "url": "https://www.youtube.com/watch?v=09_LlHjoEiY",
         "note": "Video introduction to graph theory algorithms."},
        {"type": "paper", "title": "The PageRank Citation Ranking (Page, Brin et al., 1999)",
         "url": "http://ilpubs.stanford.edu:8090/422/",
         "note": "A landmark application of node centrality on a graph."},
    ],
    "module51_operationalizing_mlops_cloud": [
        {"type": "lesson", "title": "Amazon SageMaker — developer guide",
         "url": "https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html",
         "note": "Authoritative reference for training/deploying models on AWS."},
        {"type": "article", "title": "Rules of Machine Learning: Best Practices for ML Engineering (Google)",
         "url": "https://developers.google.com/machine-learning/guides/rules-of-ml",
         "note": "Google's field guide to shipping ML systems."},
        {"type": "video", "title": "MLOps explained (video overview)",
         "url": "https://www.youtube.com/watch?v=06-AZXmwHjo",
         "note": "Overview of productionizing and operating ML models."},
        {"type": "paper", "title": "Hidden Technical Debt in Machine Learning Systems (Sculley et al., 2015)",
         "url": "https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html",
         "note": "The classic paper on the real costs of running ML in production."},
    ],
})


def guidance_for(folder_slug: str) -> str:
    """Return the dataset guidance for a module folder slug."""
    return DATASET_GUIDANCE.get(folder_slug, DEFAULT_GUIDANCE)


def sources_for(folder_slug: str) -> list[dict]:
    """Return the supplemental sources for a module folder slug (may be empty)."""
    return MODULE_SOURCES.get(folder_slug, [])
