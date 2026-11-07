"""Smoke tests: the whole Streamlit script runs headlessly without raising."""

import tomllib
from pathlib import Path

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parent.parent
APP = str(ROOT / 'streamlit_app.py')


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


def test_missing_gdp_shows_na_not_nan():
    at = run_app()
    at.multiselect[0].set_value(['AFG']).run()  # AFG has no 2022 value
    assert not at.exception
    assert at.metric[0].value == 'n/a'


def test_empty_selection_warns_and_stops():
    at = run_app()
    at.multiselect[0].set_value([]).run()
    assert not at.exception
    assert len(at.warning) == 1
    assert len(at.metric) == 0


def test_mobile_css_is_injected():
    at = run_app()
    css = (ROOT / 'assets/mobile.css').read_text()
    assert any(css.strip() in h.proto.body for h in at.get('html'))


def test_theme_defines_light_and_dark():
    # A bare [theme] block forces light mode; both variants keep the phone's dark mode working.
    config = tomllib.loads((ROOT / '.streamlit/config.toml').read_text())
    assert config['theme']['light']['primaryColor']
    assert config['theme']['dark']['primaryColor']
