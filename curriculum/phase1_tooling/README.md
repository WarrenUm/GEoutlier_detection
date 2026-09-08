# Phase 1 — Data-science tooling & data wrangling

The programming, environment, and data-access foundations for the curriculum,
adapted from the source bootcamp syllabus and re-grounded in OSRS market data.
See the root [README](../../README.md) for how this phase fits the overall
roadmap.

## Modules

1. [`module01_python_essentials/`](module01_python_essentials/README.md)
2. [`module02_python_loops_functions/`](module02_python_loops_functions/README.md)
3. [`module03_getting_started_data_science/`](module03_getting_started_data_science/README.md)
4. [`module04_bash_and_git/`](module04_bash_and_git/README.md)
5. [`module05_data_analysis_base_python/`](module05_data_analysis_base_python/README.md)
6. [`module06_data_analysis_pandas/`](module06_data_analysis_pandas/README.md)
7. [`module07_data_cleaning_pandas/`](module07_data_cleaning_pandas/README.md)
8. [`module08_getting_started_sql/`](module08_getting_started_sql/README.md)
9. [`module09_sql_table_relations/`](module09_sql_table_relations/README.md)
10. [`module10_other_databases_nosql/`](module10_other_databases_nosql/README.md)
11. [`module11_apis/`](module11_apis/README.md)
12. [`module12_html_css_web_scraping/`](module12_html_css_web_scraping/README.md)

## Folder convention

```
phase1_tooling/
└── moduleNN_<name>/
    ├── README.md              # module overview + lesson index
    └── NN_<lesson>/
        ├── README.md          # the lesson, converted to markdown (self-contained)
        ├── work.ipynb         # YOUR notebook — do the exercises here
        └── test_work.py       # pytest that executes work.ipynb (and your asserts)
```

Each lesson `README.md` is a standalone conversion of the original lesson content
— once generated, nothing depends on the `illumidesk_files` or
`Data-Science-Full-Curriculum` folders anymore.

## Working a lesson

1. Read the lesson `README.md`.
2. Do the exercises in `work.ipynb`. Where a concept applies to market data, load
   it with the shared [`ge_data`](../ge_data.py) helper and interpret the result
   in OSRS terms.
3. Add `assert` cells to check yourself.
4. Run the tests:
   ```
   pytest curriculum/phase1_tooling            # whole phase
   pytest curriculum/phase1_tooling/module01_python_essentials/01_introduction_to_variables_variable_assignment
   ```
   Each `test_work.py` executes that lesson's `work.ipynb` top-to-bottom, so a
   notebook that runs cleanly (with your asserts passing) makes the test pass.

## Regenerating

These folders are generated from the source exports (the course export plus the
`illumidesk_files` lesson/lab repos) by
[`../_tools/build_curriculum.py`](../_tools/build_curriculum.py). Re-running it
refreshes each lesson's `README.md`, `test_work.py`, and folded-in `lab.ipynb` +
data files, but **never overwrites an existing `work.ipynb`**, so your work is
safe:

```
python3 curriculum/_tools/build_curriculum.py --phase 1     # one phase
python3 curriculum/_tools/build_curriculum.py --phase all   # all four phases
```

Once generated, the lessons are fully self-contained — nothing depends on the
`illumidesk_files` or `Data-Science-Full-Curriculum` folders anymore.

## Checking the supplemental-reading links

Every lesson's `SUPPLEMENTAL_READING.md` links are curated in
`../_tools/phase_content.py`. A stdlib-only checker validates them:

```
python3 curriculum/_tools/check_links.py             # check the curated source URLs
python3 curriculum/_tools/check_links.py --markdown  # scan the generated .md files
```

It reports OK / REDIRECT / BROKEN and exits non-zero if any link is broken (so it
can gate CI). 403/429 responses are treated as reachable (some hosts bot-block
automated checkers). Fix any broken links in `phase_content.py`, then regenerate.
