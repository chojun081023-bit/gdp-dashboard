"""Smoke tests: the whole Streamlit script runs headlessly without raising."""

from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parent.parent / 'streamlit_app.py')


def run_app():
    at = AppTest.from_file(APP, default_timeout=30)
    at.run()
    return at


def test_app_runs_without_exception():
    at = run_app()
    assert not at.exception


def test_default_selection_renders_one_metric_per_country():
    at = run_app()
    selected = at.multiselect[0].value
    assert len(selected) == 6
    assert len(at.metric) == len(selected)
