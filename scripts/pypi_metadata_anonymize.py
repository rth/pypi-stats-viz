import gzip
from pathlib import Path
from glob import glob
from tqdm import tqdm
import toolz

import json


if __name__ == '__main__':

    data_dir = Path('..') / 'data' / 'pypi-metadata-2018-02-11'
    out_dir = Path('..') / 'data' / 'pypi-metadata-anonymized-2018-02-11'

    def anonymize(record):
        del record['info']['author_email']
        return record

    def load(path):
        with gzip.open(path, 'r') as fh:
            return json.load(fh)

    def save(record):
        name = record['info']['name']
        with gzip.open(str(out_dir / (str(name) + '.json.gz')), 'wt') as fh:
            json.dump(record, fh)

    if not out_dir.exists():
        out_dir.mkdir()

    pipe = toolz.compose(save, anonymize, load)

    for path in tqdm(glob(str(data_dir / '*.json.gz'))):
        pipe(path)
