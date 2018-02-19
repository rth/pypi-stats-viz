import dask.bag as db
from dask.diagnostics import ProgressBar
from pathlib import Path

import json


if __name__ == '__main__':

    data_dir = Path('..') / 'data' / 'pypi-metadata-2018-02-19'

    js_raw = (db.read_text(str(data_dir / '*.json.gz'))
                .map(json.loads).repartition(10))

    with ProgressBar():
        js = js_raw.pluck('info')
        df = js.to_dataframe()
        df['requires_dist'] = df['requires_dist'].apply(','.join)
        # comma is used in one of the classifiers,
        # so can't use it as a delimiter
        df['classifiers'] = df['classifiers'].apply(';'.join)

        # drop email for privacy reasons
        del df['author_email']
        # downloads fields is empty anyway
        del df['downloads']

        df.to_parquet(str(data_dir) + '.parq',
                      compression='snappy', engine='pyarrow')
