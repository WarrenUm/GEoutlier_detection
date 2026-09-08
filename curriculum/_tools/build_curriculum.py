"""Generate the self-contained curriculum folder tree from the source exports.

Reads the Flatiron-style course export (``course-data.js``) and emits, per phase,
one folder per module and one sub-folder per lesson. Each lesson folder gets:

* ``README.md``   — the lesson explanation, converted from the source lesson HTML
                    to clean markdown (self-contained; no dependency on the
                    original export afterwards).
* ``work.ipynb``  — a starter notebook for the learner's own work.
* ``test_work.py``— a pytest that executes ``work.ipynb`` and checks it runs.

The HTML->markdown conversion uses only the Python standard library so the
generator has no third-party dependencies. Run it from the repo root:

    python3 curriculum/_tools/build_curriculum.py --phase 1

Idempotent for READMEs/tests (regenerated each run); ``work.ipynb`` is only
written if missing, so re-running never clobbers your work.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
import sys
import uuid
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import phase_content  # noqa: E402  (local content data module)

# --- Paths -----------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
CURRICULUM = REPO_ROOT / "curriculum"
# The source exports live one level up from the repo, in the workspace.
SOURCE_JS = (
    REPO_ROOT.parent
    / "Data-Science-Full-Curriculum-2021-Jul-07_00-26-59"
    / "viewer"
    / "course-data.js"
)
# The illumidesk lesson/lab repos (one folder per lesson, exercises + data).
ILLUMIDESK = REPO_ROOT.parent / "illumidesk_files"

# --- Phase -> source module mapping ----------------------------------------
# Values are indices into course-data.js "modules". Module 0 (foundations) is
# authored by hand, not generated. Each phase maps its README topics to the
# source modules that supply their lesson content.
PHASES: dict[int, dict] = {
    1: {
        "slug": "phase1_tooling",
        "title": "Phase 1 - Data-science tooling & data wrangling",
        # (topic_number, folder_slug, source_module_index)
        "modules": [
            (1, "module01_python_essentials", 0),
            (2, "module02_python_loops_functions", 1),
            (3, "module03_getting_started_data_science", 5),
            (4, "module04_bash_and_git", 6),
            (5, "module05_data_analysis_base_python", 7),
            (6, "module06_data_analysis_pandas", 8),
            (7, "module07_data_cleaning_pandas", 9),
            (8, "module08_getting_started_sql", 10),
            (9, "module09_sql_table_relations", 11),
            (10, "module10_other_databases_nosql", 12),
            (11, "module11_apis", 13),
            (12, "module12_html_css_web_scraping", 14),
        ],
    },
    2: {
        "slug": "phase2_stats_regression",
        "title": "Phase 2 - Probability, statistics & regression",
        "modules": [
            # Topic 13 merges the source's Statistical Measures (2) and Data
            # Visualization (3) modules; handled via extra source modules below.
            (13, "module13_statistical_measures_visualization", 2),
            (14, "module14_combinatorics_probability", 16),
            (15, "module15_statistical_distributions", 17),
            (16, "module16_clt_confidence_intervals", 18),
            (17, "module17_hypothesis_testing", 19),
            (18, "module18_power_and_anova", 20),
            (19, "module19_ab_testing", 21),
            (20, "module20_bayesian_statistics", 22),
            (21, "module21_intro_linear_regression", 23),
            (22, "module22_multiple_regression_validation", 24),
            (23, "module23_extensions_linear_models", 25),
        ],
        # Modules that append their lessons onto an already-created module dir.
        "append": [
            ("module13_statistical_measures_visualization", 3),  # Data Visualization
        ],
    },
    3: {
        "slug": "phase3_ml_foundations",
        "title": "Phase 3 - Math & machine-learning foundations",
        "modules": [
            (24, "module24_object_oriented_programming", 27),
            (25, "module25_linear_algebra", 28),
            (26, "module26_calculus_gradient_descent", 29),
            (27, "module27_feature_selection_ridge_lasso", 30),
            (28, "module28_logistic_regression", 31),
            (29, "module29_mle_logistic_regression", 32),
            (30, "module30_k_nearest_neighbors", 33),
            (31, "module31_naive_bayes", 34),
            (32, "module32_decision_trees", 35),
            (33, "module33_ensemble_methods", 36),
            (34, "module34_support_vector_machines", 37),
            (35, "module35_ml_pipeline", 38),
        ],
    },
    4: {
        "slug": "phase4_advanced_ml_dl",
        "title": "Phase 4 - Advanced ML, deep learning & operations",
        "modules": [
            (36, "module36_principal_component_analysis", 39),
            (37, "module37_clustering", 40),
            (38, "module38_big_data_pyspark", 41),
            (39, "module39_recommendation_systems", 42),
            (40, "module40_time_series_models", 43),
            # Topics 41 (forecasting/GARCH) and 42 (anomaly detection) are
            # project-specific extensions with no single source module; authored
            # as README-only modules (no source lessons to fold).
            (43, "module43_natural_language_processing", 44),
            (44, "module44_neural_networks", 45),
            (45, "module45_deep_neural_networks", 46),
            (46, "module46_tuning_neural_networks", 47),
            (47, "module47_convolutional_neural_networks", 50),
            (48, "module48_transfer_learning", 51),
            (49, "module49_deep_nlp_sequence_models", 52),
            (50, "module50_graph_theory_networks", 49),
            (51, "module51_operationalizing_mlops_cloud", 48),
        ],
    },
}

# Illumidesk folder contents that are boilerplate and never folded in.
_SKIP_NAMES = {
    ".git",
    ".ipynb_checkpoints",
    ".learn",
    ".canvas",
    ".gitignore",
    "CONTRIBUTING.md",
    "LICENSE.md",
    "index_files",
    "README.md",  # lesson README comes from course-data; keep source separate
}
# Words dropped when building keyword sets for fuzzy folder matching.
_STOP_WORDS = {
    "introduction", "to", "the", "a", "an", "and", "with", "in", "of", "for",
    "using", "codealong", "code", "along", "lab", "v2", "1", "intro", "recap",
    "101",
}


# --- HTML -> Markdown (stdlib only) ----------------------------------------


class _MarkdownConverter(HTMLParser):
    """Minimal HTML->Markdown converter for the lesson content tags.

    Handles h1-h6, p, br, ul/ol/li, strong/b, em/i, code, pre, blockquote, a,
    img, hr, and tables. Unknown tags are ignored but their text is kept.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self._list_stack: list[str] = []  # 'ul' or 'ol'
        self._ol_counters: list[int] = []
        self._in_pre = False
        self._in_code = False
        self._href: str | None = None
        self._pending_link_text: list[str] = []
        self._capturing_link = False
        self._in_blockquote = False

    # -- helpers --
    def _emit(self, text: str) -> None:
        self.out.append(text)

    def handle_starttag(self, tag: str, attrs: list) -> None:
        a = dict(attrs)
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._emit("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self._emit("\n\n> " if self._in_blockquote else "\n\n")
        elif tag == "br":
            self._emit("  \n")
        elif tag == "hr":
            self._emit("\n\n---\n")
        elif tag == "ul":
            # A top-level list needs a blank line before it so the first item is
            # not glued to preceding inline text (e.g. "You will be able to:").
            if not self._list_stack:
                self._emit("\n")
            self._list_stack.append("ul")
        elif tag == "ol":
            if not self._list_stack:
                self._emit("\n")
            self._list_stack.append("ol")
            self._ol_counters.append(0)
        elif tag == "li":
            indent = "  " * (len(self._list_stack) - 1)
            if self._list_stack and self._list_stack[-1] == "ol":
                self._ol_counters[-1] += 1
                self._emit(f"\n{indent}{self._ol_counters[-1]}. ")
            else:
                self._emit(f"\n{indent}- ")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "pre":
            self._in_pre = True
            self._emit("\n\n```python\n")
        elif tag == "code":
            if not self._in_pre:
                self._in_code = True
                self._emit("`")
        elif tag == "blockquote":
            self._in_blockquote = True
            self._emit("\n\n")
        elif tag == "a":
            self._href = a.get("href")
            self._capturing_link = True
            self._pending_link_text = []
        elif tag == "img":
            src = a.get("src", "")
            alt = a.get("alt", "image")
            self._emit(f"\n\n![{alt}]({src})\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in ("ul", "ol"):
            if self._list_stack:
                popped = self._list_stack.pop()
                if popped == "ol" and self._ol_counters:
                    self._ol_counters.pop()
            self._emit("\n")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "pre":
            self._in_pre = False
            self._emit("\n```\n")
        elif tag == "code":
            if self._in_code:
                self._in_code = False
                self._emit("`")
        elif tag == "blockquote":
            self._in_blockquote = False
            self._emit("\n")
        elif tag == "a":
            text = "".join(self._pending_link_text).strip()
            self._capturing_link = False
            if self._href and text:
                self._emit(f"[{text}]({self._href})")
            elif text:
                self._emit(text)
            self._href = None
            self._pending_link_text = []

    def handle_data(self, data: str) -> None:
        if self._in_pre:
            # Preserve code verbatim (indentation, newlines).
            target = self._pending_link_text if self._capturing_link else self.out
            target.append(data)
            return
        # Outside <pre>, collapse any run of whitespace (including source
        # newlines) to a single space so inline text and list items don't
        # fragment across lines.
        collapsed = re.sub(r"\s+", " ", data)
        if self._capturing_link:
            self._pending_link_text.append(collapsed)
        else:
            self._emit(collapsed)


def html_to_markdown(html: str) -> str:
    """Convert a lesson's HTML ``content`` into cleaned markdown text."""
    conv = _MarkdownConverter()
    conv.feed(html or "")
    md = "".join(conv.out)
    # Collapse runs of blank lines and trim trailing spaces on lines.
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.strip()
    # The lesson README supplies its own H1 title, so drop a leading duplicate
    # top-level heading from the converted content to avoid two H1s.
    md = re.sub(r"^#\s+.*\n+", "", md, count=1)
    md = _fix_inline_objectives(md)
    return md.strip() + "\n"


def _fix_inline_objectives(md: str) -> str:
    """Turn a source "You will be able to: - a - b" line into a bullet list.

    A handful of source lessons author their objectives as one inline paragraph
    with literal ``-`` separators instead of a real ``<ul>``. Split those into a
    proper markdown list. Only triggered by the explicit objectives lead-in so
    ordinary prose containing dashes is left untouched.
    """

    def _replace(match: "re.Match[str]") -> str:
        items = [part.strip() for part in match.group("items").split(" - ")]
        items = [it for it in items if it]
        bullets = "\n".join(f"- {it}" for it in items)
        return f"{match.group('lead')}\n\n{bullets}\n"

    pattern = re.compile(
        r"(?P<lead>You will be able to:)\s*-\s*(?P<items>.+)$",
        re.MULTILINE,
    )
    return pattern.sub(_replace, md)


# --- Slug / naming ---------------------------------------------------------


def slugify(text: str) -> str:
    """Return a filesystem-safe lowercase slug for a lesson title."""
    s = text.strip().lower()
    s = s.replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_") or "item"


# --- Emitters --------------------------------------------------------------


def _cell_id() -> str:
    """Return a short unique cell id (satisfies nbformat 4.5+)."""
    return uuid.uuid4().hex[:12]


def _md_cell(lines: list[str]) -> dict:
    return {"cell_type": "markdown", "id": _cell_id(), "metadata": {}, "source": lines}


def _code_cell(lines: list[str]) -> dict:
    return {
        "cell_type": "code",
        "id": _cell_id(),
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines,
    }


def starter_notebook(
    topic_title: str,
    lesson_title: str,
    guidance: str,
    has_lab: bool,
) -> dict:
    """Return a seeded starter notebook with OSRS/alt-dataset task prompts.

    The notebook is intentionally runnable as-is (its scaffolding executes so the
    lesson test passes immediately), while giving the learner a clear, tailored
    set of tasks and the right dataset pointer for the topic.
    """
    lab_line = (
        "This lesson has a folded-in `lab.ipynb` (the original exercise) plus its "
        "data files — work through it, or pull pieces into this notebook.\n"
        if has_lab
        else "There is no folded-in lab for this lesson; work the tasks below directly.\n"
    )
    return {
        "cells": [
            _md_cell([
                f"# {lesson_title}\n",
                "\n",
                f"*{topic_title}*\n",
                "\n",
                "Read `README.md` in this folder for the lesson, then do your work here.\n",
                "See `SUPPLEMENTAL_READING.md` for papers, videos, and articles.\n",
                "\n",
                f"**Dataset for this lesson:** {guidance}\n",
                "\n",
                lab_line,
            ]),
            _md_cell([
                "## Setup\n",
            ]),
            _code_cell([
                "import sys\n",
                "from pathlib import Path\n",
                "\n",
                "# Make the shared curriculum helpers importable from any lesson folder.\n",
                "CURRICULUM = Path.cwd()\n",
                "while CURRICULUM.name != 'curriculum' and CURRICULUM != CURRICULUM.parent:\n",
                "    CURRICULUM = CURRICULUM.parent\n",
                "if str(CURRICULUM) not in sys.path:\n",
                "    sys.path.insert(0, str(CURRICULUM))\n",
                "\n",
                "# Uncomment when you need market data:\n",
                "# from ge_data import load_series, load_frame, list_items, FIRE_RUNE\n",
            ]),
            _md_cell([
                "## Tasks\n",
                "\n",
                "Work through the lesson's exercises here. Suggested steps:\n",
                "\n",
                "1. Reproduce the key idea from the lesson README on a small example.\n",
                "2. Apply it to the dataset noted above (OSRS via `ge_data`, or the\n",
                "   suggested alternative).\n",
                "3. Interpret the result in plain terms — what does it tell you?\n",
                "\n",
                "Add `assert` cells to check your own results; `pytest` runs this\n",
                "notebook, so passing asserts = a passing lesson.\n",
            ]),
            _code_cell([
                "# Your work here\n",
            ]),
            _md_cell([
                "## Self-check\n",
                "\n",
                "Add assertions that capture what a correct result looks like, e.g.:\n",
            ]),
            _code_cell([
                "# Example self-check (replace with your own):\n",
                "# assert result is not None\n",
            ]),
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.12"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def supplemental_reading(topic_title: str, lesson_title: str, sources: list[dict]) -> str:
    """Return the SUPPLEMENTAL_READING.md body for a lesson.

    Groups the module's curated sources by type (paper / video / article /
    lesson) so each lesson offers all four kinds of supplement.
    """
    lines = [
        f"# Supplemental reading — {lesson_title}",
        "",
        f"Curated outside resources for **{topic_title}**. Use these to go beyond the",
        "lesson README: read a paper for depth, watch a video for intuition, and skim",
        "an article or another lesson for a second explanation.",
        "",
    ]
    if not sources:
        lines += [
            "> No curated external sources are listed for this module yet. Good starting",
            "> points: the official docs for the library in use, Real Python, Khan",
            "> Academy, and a relevant survey paper on Google Scholar.",
            "",
        ]
        return "\n".join(lines)

    order = [("paper", "Scientific papers"), ("video", "Videos"),
             ("article", "Articles"), ("lesson", "Other lessons & docs")]
    by_type: dict[str, list[dict]] = {}
    for s in sources:
        by_type.setdefault(s["type"], []).append(s)

    for key, heading in order:
        items = by_type.get(key, [])
        if not items:
            continue
        lines.append(f"## {heading}")
        lines.append("")
        for s in items:
            lines.append(f"- [{s['title']}]({s['url']})")
            lines.append(f"  — {s['note']}")
        lines.append("")

    lines += [
        "---",
        "",
        "*Sources gathered via web search and summarized for licensing compliance;",
        "follow each link for the full original. Suggestions welcome — add more in this",
        "file as you find them.*",
        "",
    ]
    return "\n".join(lines)


def test_file(lesson_title: str) -> str:
    """Return the pytest source that executes a lesson's notebooks.

    The generated test executes ``work.ipynb`` (always) and ``lab.ipynb`` (the
    folded-in exercise notebook, when present) end-to-end from the lesson folder,
    so ``pytest`` validates both. Any ``assert`` cells the learner adds run here
    too. Requires ``nbclient`` and ``nbformat`` (both pulled in by JupyterLab in
    requirements.txt); the test is skipped cleanly if they are absent.
    """
    escaped = lesson_title.replace('"', "'")
    return f'''"""Validates this lesson\'s notebooks so `pytest` checks your work.

Two checks:

* ``work.ipynb`` (your work) is **executed** end-to-end from this folder, so
  relative data paths resolve and any ``assert`` cells you add are enforced.
  This is the pass/fail contract for the lesson.
* ``lab.ipynb`` (the original, folded-in exercise), when present, is only checked
  for validity — it is intentionally *incomplete* (fill-in-the-blank), so running
  it top-to-bottom is expected to fail until you complete it. Execute it yourself
  as you work through the exercise, or copy the parts you want into ``work.ipynb``.
"""

from pathlib import Path

import pytest

nbformat = pytest.importorskip("nbformat")
nbclient = pytest.importorskip("nbclient")

HERE = Path(__file__).parent


def _execute(notebook: Path) -> None:
    nb = nbformat.read(notebook, as_version=4)
    # resources path=HERE so relative data paths (e.g. "ames.csv") resolve.
    client = nbclient.NotebookClient(
        nb, timeout=300, kernel_name="python3",
        resources={{"metadata": {{"path": str(HERE)}}}},
    )
    client.execute()


def test_work_notebook_runs() -> None:
    """{escaped}: the work notebook executes without error."""
    _execute(HERE / "work.ipynb")


@pytest.mark.skipif(
    not (Path(__file__).parent / "lab.ipynb").exists(),
    reason="no folded-in lab.ipynb for this lesson",
)
def test_lab_notebook_is_valid() -> None:
    """{escaped}: the folded-in exercise notebook is a valid notebook.

    Not executed: the lab is an incomplete exercise by design. Complete it in
    ``work.ipynb`` (which *is* executed).
    """
    nbformat.read(HERE / "lab.ipynb", as_version=4)
'''


def module_readme(topic_num: int, topic_title: str, source_module: dict, lessons: list[tuple]) -> str:
    """Return the module-level README linking to each lesson sub-folder."""
    lines = [
        f"# Module {topic_num:02d} — {topic_title}",
        "",
        f"Adapted from the source curriculum module **{source_module['name']}**,",
        "re-grounded in OSRS market data. Work each lesson in order; open the",
        "lesson `README.md`, then do your work in that lesson's `work.ipynb`.",
        "",
        "See the root [README](../../../README.md) for where this module sits in the",
        "overall roadmap.",
        "",
        "## Lessons",
        "",
    ]
    for slug, title in lessons:
        lines.append(f"- [`{slug}/`]({slug}/README.md) — {title}")
    lines.append("")
    lines.append("## How to work a lesson")
    lines.append("")
    lines.append("1. Read the lesson `README.md`.")
    lines.append("2. Do the work in `work.ipynb` (load OSRS data via `ge_data` where it fits).")
    lines.append("3. Run `pytest` in the lesson folder — it executes your notebook.")
    lines.append("")
    return "\n".join(lines)


def lesson_readme(
    topic_title: str,
    title: str,
    content_md: str,
    item_type: str,
    fold: dict | None = None,
) -> str:
    """Return a lesson README: converted content plus a work/lab/test footer."""
    header = [
        f"# {title}",
        "",
        f"> Part of **{topic_title}** · source item type: {item_type}",
        "",
        "---",
        "",
    ]
    footer = [
        "",
        "---",
        "",
        "## Your work",
        "",
        "Do this lesson's exercises in `work.ipynb` in this folder. Where the concept",
        "applies to market data, load it with the shared `ge_data` helper and interpret",
        "the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in",
        "this folder runs the notebook (and your asserts) end-to-end.",
        "",
    ]
    fold = fold or {}
    if fold.get("lab") or fold.get("files"):
        footer += [
            "## Folded-in exercise material",
            "",
            "This lesson includes the original hands-on material, converted for local use:",
            "",
        ]
        if fold.get("lab"):
            footer.append(
                "- [`lab.ipynb`](lab.ipynb) — the original exercise notebook. Work through"
            )
            footer.append(
                "  it, or copy the parts you want into `work.ipynb`. `pytest` runs it too."
            )
        for name in fold.get("files", []):
            footer.append(f"- `{name}` — supporting data/helper file for the exercise.")
        footer.append("")
    return "\n".join(header) + content_md + "\n".join(footer)


# --- Illumidesk lab matching & folding -------------------------------------


def _folder_slug(title: str) -> str:
    """Slugify a lesson title the way the illumidesk folders are named."""
    s = title.strip().lower().replace("&", "and")
    s = re.sub(r"\(.*?\)", "", s)  # drop parenthetical asides
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def _keyset(slug: str) -> set[str]:
    """Return the significant keyword set of a slug for fuzzy matching."""
    return {w for w in slug.split("-") if w and w not in _STOP_WORDS}


def _list_illumidesk() -> list[str]:
    """Return the ``dsc-*`` lesson/lab folder names available to fold in."""
    if not ILLUMIDESK.exists():
        return []
    return [
        p.name
        for p in ILLUMIDESK.iterdir()
        if p.is_dir() and p.name.startswith("dsc-")
    ]


def match_illumidesk(title: str, folders: list[str]) -> list[str]:
    """Return illumidesk folders for a lesson (lesson + lab + codealong).

    Tries exact slug variants first, then a conservative keyword-Jaccard match
    (>= 0.6), then a high-cutoff difflib fallback. Returns every related folder
    found (e.g. both ``dsc-x`` and ``dsc-x-lab``) so data files and the exercise
    notebook are both available. An empty list means no confident match — the
    lesson is treated as narrative-only.
    """
    slug = _folder_slug(title)
    folder_set = set(folders)
    variants = [
        f"dsc-{slug}",
        f"dsc-{slug}-lab",
        f"dsc-{slug}-codealong",
        f"dsc-{slug}-lab-v2-1",
        f"dsc-{slug}-codealong-v2-1",
    ]
    found = [v for v in variants if v in folder_set]
    if found:
        return found

    # Keyword-Jaccard fallback (conservative threshold to avoid false matches).
    ks = _keyset(slug)
    if ks:
        scored = sorted(
            (
                (len(ks & _keyset(f[4:])) / len(ks | _keyset(f[4:])), f)
                for f in folders
                if _keyset(f[4:])
            ),
            reverse=True,
        )
        if scored and scored[0][0] >= 0.6:
            return [scored[0][1]]

    close = difflib.get_close_matches(f"dsc-{slug}", folders, n=1, cutoff=0.74)
    return close


def fold_illumidesk(lesson_dir: Path, folder_names: list[str]) -> dict:
    """Copy an illumidesk lesson/lab's exercise notebook and data into a lesson.

    From the matched folder(s), copies the exercise notebook as ``lab.ipynb``
    (preferring a ``-lab`` folder) and any data/helper files (``.csv``, ``.txt``,
    ``.py``, ``.json``, ``.db``, ``.sqlite``, images) alongside it, skipping
    boilerplate. Existing files are overwritten so a regen refreshes source
    material, but the learner's ``work.ipynb`` is written elsewhere and untouched.

    Args:
        lesson_dir: The destination lesson folder.
        folder_names: The matched illumidesk folder names (may be empty).

    Returns:
        A dict describing what was folded: ``{"lab": bool, "files": [names]}``.
    """
    result = {"lab": False, "files": []}
    if not folder_names:
        return result

    # Prefer a -lab folder for the exercise notebook; keep all for data files.
    ordered = sorted(folder_names, key=lambda n: (not n.endswith("-lab"), n))
    data_exts = {".csv", ".txt", ".py", ".json", ".db", ".sqlite",
                 ".png", ".jpg", ".jpeg", ".xlsx", ".tsv"}

    lab_written = False
    for name in ordered:
        src = ILLUMIDESK / name
        if not src.exists():
            continue
        # Exercise notebook -> lab.ipynb (first/best folder wins).
        nb = src / "index.ipynb"
        if nb.exists() and not lab_written:
            shutil.copyfile(nb, lesson_dir / "lab.ipynb")
            result["lab"] = True
            lab_written = True
        # Data + helper files.
        for f in src.iterdir():
            if f.name in _SKIP_NAMES or f.is_dir():
                continue
            if f.suffix.lower() in data_exts and f.name != "index.ipynb":
                shutil.copyfile(f, lesson_dir / f.name)
                if f.name not in result["files"]:
                    result["files"].append(f.name)
    result["files"].sort()
    return result


def _emit_lessons(
    module_dir: Path,
    module_slug: str,
    src_module: dict,
    topic_title: str,
    illumidesk: list[str],
    start_order: int,
    used_slugs: set[str],
) -> tuple[list[tuple], int]:
    """Emit each lesson folder for one source module; return (lessons, folded).

    ``lessons`` is the list of ``(slug, title)`` for the module README index;
    ``folded`` counts how many lessons had illumidesk exercise material attached.
    """
    lessons: list[tuple] = []
    folded = 0
    for offset, item in enumerate(src_module.get("items", [])):
        order = start_order + offset
        title = item.get("title", "").strip()
        base = slugify(title)
        slug = f"{order:02d}_{base}"
        while slug in used_slugs:
            slug += "_x"
        used_slugs.add(slug)
        content_md = html_to_markdown(item.get("content", ""))

        lesson_dir = module_dir / slug
        lesson_dir.mkdir(exist_ok=True)

        matches = match_illumidesk(title, illumidesk)
        fold = fold_illumidesk(lesson_dir, matches)
        if fold["lab"] or fold["files"]:
            folded += 1

        (lesson_dir / "README.md").write_text(
            lesson_readme(topic_title, title, content_md, item.get("type", ""), fold),
            encoding="utf-8",
        )
        (lesson_dir / "test_work.py").write_text(test_file(title), encoding="utf-8")
        (lesson_dir / "SUPPLEMENTAL_READING.md").write_text(
            supplemental_reading(topic_title, title, phase_content.sources_for(module_slug)),
            encoding="utf-8",
        )
        nb_path = lesson_dir / "work.ipynb"
        if not nb_path.exists():
            nb_path.write_text(
                json.dumps(
                    starter_notebook(
                        topic_title,
                        title,
                        phase_content.guidance_for(module_slug),
                        has_lab=fold["lab"],
                    ),
                    indent=1,
                ),
                encoding="utf-8",
            )
        lessons.append((slug, title))
    return lessons, folded


def phase_readme(phase: dict, module_titles: list[tuple]) -> str:
    """Return the phase-level README indexing its modules."""
    lines = [
        f"# {phase['title']}",
        "",
        "Adapted from the source bootcamp syllabus and re-grounded in OSRS market",
        "data. See the root [README](../../README.md) for how this phase fits the",
        "overall roadmap, and [Phase 1](../phase1_tooling/README.md) for the full",
        "folder convention and how to run the lesson tests.",
        "",
        "## Modules",
        "",
    ]
    for folder_slug, topic_num, topic_title in module_titles:
        lines.append(
            f"{topic_num}. [`{folder_slug}/`]({folder_slug}/README.md) — {topic_title}"
        )
    lines += [
        "",
        "## Working a lesson",
        "",
        "Each lesson folder has a `README.md` (the lesson), a `work.ipynb` (your",
        "notebook), and a `test_work.py` (runs your notebook under `pytest`). Lessons",
        "that had hands-on exercises also include a folded-in `lab.ipynb` and its data",
        "files. Run the whole phase with `pytest curriculum/" + phase["slug"] + "`.",
        "",
    ]
    return "\n".join(lines)


def build_phase(phase_num: int, data: dict) -> None:
    """Generate the folder tree for one phase, folding in illumidesk material."""
    phase = PHASES[phase_num]
    phase_dir = CURRICULUM / phase["slug"]
    phase_dir.mkdir(parents=True, exist_ok=True)
    modules = data["modules"]
    illumidesk = _list_illumidesk()

    # Modules that append extra source modules onto an existing module folder.
    appends: dict[str, list[int]] = {}
    for folder_slug, extra_idx in phase.get("append", []):
        appends.setdefault(folder_slug, []).append(extra_idx)

    total_lessons = total_folded = 0
    module_titles: list[tuple] = []
    for topic_num, folder_slug, src_idx in phase["modules"]:
        src_module = modules[src_idx]
        topic_title = src_module["name"]
        module_titles.append((folder_slug, topic_num, topic_title))
        module_dir = phase_dir / folder_slug
        module_dir.mkdir(exist_ok=True)

        used_slugs: set[str] = set()
        lessons, folded = _emit_lessons(
            module_dir, folder_slug, src_module, topic_title, illumidesk, 1, used_slugs
        )
        # Append any extra source modules' lessons into the same folder.
        for extra_idx in appends.get(folder_slug, []):
            extra = modules[extra_idx]
            more, more_folded = _emit_lessons(
                module_dir, folder_slug, extra, topic_title, illumidesk,
                len(lessons) + 1, used_slugs,
            )
            lessons += more
            folded += more_folded

        (module_dir / "README.md").write_text(
            module_readme(topic_num, topic_title, src_module, lessons),
            encoding="utf-8",
        )
        total_lessons += len(lessons)
        total_folded += folded
        print(f"  module {folder_slug}: {len(lessons)} lessons ({folded} with lab)")

    # Write the phase README only if absent, so a hand-authored one (Phase 1)
    # is preserved across regenerations.
    phase_readme_path = phase_dir / "README.md"
    if not phase_readme_path.exists():
        phase_readme_path.write_text(phase_readme(phase, module_titles), encoding="utf-8")

    print(
        f"Phase {phase_num}: {total_lessons} lesson folders "
        f"({total_folded} with folded-in labs) under {phase_dir}"
    )


def load_source() -> dict:
    """Load and parse the course-data.js export into a dict."""
    raw = SOURCE_JS.read_text(encoding="utf-8")
    return json.loads(raw[raw.index("{"):].rstrip().rstrip(";"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--phase",
        default="1",
        help="Phase number to generate, or 'all' (default: 1).",
    )
    args = parser.parse_args()
    if not SOURCE_JS.exists():
        raise SystemExit(f"Source export not found at {SOURCE_JS}")
    data = load_source()

    if args.phase == "all":
        for phase_num in sorted(PHASES):
            build_phase(phase_num, data)
        return

    phase_num = int(args.phase)
    if phase_num not in PHASES:
        raise SystemExit(f"No mapping for phase {phase_num}; known: {sorted(PHASES)}")
    build_phase(phase_num, data)


if __name__ == "__main__":
    main()
