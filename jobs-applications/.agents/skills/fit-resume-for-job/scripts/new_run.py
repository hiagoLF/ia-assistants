#!/usr/bin/env python3
"""Return versioned paths under the project generated directory."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import secrets
import unicodedata
from zoneinfo import ZoneInfo

def slug(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    value = re.sub(r'[^a-z0-9]+', '-', value).strip('-')[:100]
    if not value:
        raise ValueError('Company and job must produce a nonempty slug')
    return value

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--company', required=True)
    parser.add_argument('--job', required=True)
    parser.add_argument('--kind', choices=['resume', 'cover-letter', 'interview'], action='append',
                        help='Output kind; repeat as needed. Defaults to resume and cover-letter.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[4] / 'generated'
    folder = root / slug(args.company) / slug(args.job)
    folder.mkdir(parents=True, exist_ok=True)
    while True:
        run = datetime.now(ZoneInfo('America/Bahia')).strftime('%Y%m%d-%H%M%S%z') + '-' + secrets.token_hex(4)
        kinds = list(dict.fromkeys(args.kind or ['resume', 'cover-letter']))
        paths = {kind: str(folder / f"{kind}-{run}.{'md' if kind == 'interview' else 'pdf'}")
                 for kind in kinds}
        if not any(Path(p).exists() for p in paths.values()):
            break
    print(json.dumps({'run': run, 'paths': paths}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
