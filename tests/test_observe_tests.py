import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / '.claude/skills/test-observer/scripts/observe_tests.py'
spec = importlib.util.spec_from_file_location('observe_tests', SCRIPT)
observe_tests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(observe_tests)


def test_summarize_reads_counts_and_failed_tests():
    output = (
        'FAILED tests/test_a.py::test_x - AssertionError\n'
        'ERROR tests/test_b.py::test_y - ValueError\n'
        '1 failed, 3 passed, 1 error in 0.50s\n'
    )
    s = observe_tests.summarize(output)
    assert s['counts'] == {'failed': 1, 'passed': 3, 'error': 1}
    assert s['failed'] == ['tests/test_a.py::test_x', 'tests/test_b.py::test_y']


def test_shrink_keeps_short_output_and_error_line_in_long_output():
    assert observe_tests.shrink('short') == 'short'
    long = '\n'.join(f'INFO step {i} ok' for i in range(3000)) + '\nE   AssertionError: boom'
    out = observe_tests.shrink(long)
    assert len(out) < len(long)
    assert 'AssertionError: boom' in out
