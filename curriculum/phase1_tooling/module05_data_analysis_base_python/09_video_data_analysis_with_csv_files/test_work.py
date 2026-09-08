"""Validates this lesson's notebooks so `pytest` checks your work.

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
        resources={"metadata": {"path": str(HERE)}},
    )
    client.execute()


def test_work_notebook_runs() -> None:
    """🎬 Video: Data Analysis with CSV Files: the work notebook executes without error."""
    _execute(HERE / "work.ipynb")


@pytest.mark.skipif(
    not (Path(__file__).parent / "lab.ipynb").exists(),
    reason="no folded-in lab.ipynb for this lesson",
)
def test_lab_notebook_is_valid() -> None:
    """🎬 Video: Data Analysis with CSV Files: the folded-in exercise notebook is a valid notebook.

    Not executed: the lab is an incomplete exercise by design. Complete it in
    ``work.ipynb`` (which *is* executed).
    """
    nbformat.read(HERE / "lab.ipynb", as_version=4)
