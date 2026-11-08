"""Run pytest and print a short report: counts, failing tests, and compressed failure output."""

import os
import re
import subprocess
import sys

MAX_RAW_CHARS = 4000  # below this, show pytest output as is


def summarize(output: str) -> dict:
    counts = {k: int(n) for n, k in re.findall(r'(\d+) (passed|failed|error|errors|skipped)', output)}
    failed = re.findall(r'^(?:FAILED|ERROR) (\S+)', output, flags=re.M)
    return {'counts': counts, 'failed': failed}


def shrink(output: str) -> str:
    if len(output) <= MAX_RAW_CHARS:
        return output
    # pytest's 'E ' lines carry the assertion text; headroom may fold them into a count, so keep them
    errors = '\n'.join([line for line in output.splitlines() if line.startswith('E ')][:50])
    os.environ.setdefault('HEADROOM_OFFLINE', '1')  # no update check or downloads
    try:
        from headroom import compress
    except ImportError:
        # shortcut: tail only without headroom, install requirements-dev.txt for error-aware compression
        return output[-MAX_RAW_CHARS:] + '\n--- E lines ---\n' + errors
    call = {'id': 'pytest', 'type': 'function', 'function': {'name': 'pytest', 'arguments': '{}'}}
    msgs = [
        {'role': 'user', 'content': 'Which tests failed and why?'},
        {'role': 'assistant', 'content': None, 'tool_calls': [call]},
        {'role': 'tool', 'tool_call_id': 'pytest', 'content': output},
    ]
    compressed = str(compress(msgs, model='gpt-4o').messages[-1]['content'])
    return compressed + '\n--- E lines ---\n' + errors


def main() -> int:
    args = [sys.executable, '-m', 'pytest', '-q', '-rfE', *sys.argv[1:]]
    proc = subprocess.run(args, capture_output=True, text=True)
    output = proc.stdout + proc.stderr
    s = summarize(output)
    counts = ' · '.join(f'{n} {k}' for k, n in s['counts'].items()) or 'no summary line'
    print(f'pytest exit {proc.returncode}: {counts}')
    for name in s['failed']:
        print(f'  FAIL {name}')
    if proc.returncode != 0:
        print('--- output ---')
        print(shrink(output))
    return proc.returncode


if __name__ == '__main__':
    sys.exit(main())
