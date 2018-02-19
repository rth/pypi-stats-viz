# pypi-stats-viz

Tools for PyPi analysis

## PyPi metadata

   A few data provided for research purposes as part of this project,

    * `pypi-metadata-2018-02-11.tar` (583 MB json gzipped, 119010 packages)


## Scripts

1. [`scripts/pypi_metadata_download.py`](./scripts/pypi_metadata_download.py) - download PyPi metadata for all packages

   The included script uses PyPi JSON API to asynchronously fetch metadata for all Python packages (~125000) uploaded to PyPi. It uses aiohttp (requires Python 3.5+) and takes ~30 min with 50 parallel download
   channels (cf [warehouse/issues/2912(Comment)](https://github.com/pypa/warehouse/issues/2912#issuecomment-364674430) for more details),
   assuming a good internet connection.

2. [`scripts/pypi_metadata_json_to_parquet.py`](./scripts/pypi_metadata_json_to_parquet.py) convert the downloaded PyPi metadata from one gzipped JSON per package to [Appache parquet format](https://en.wikipedia.org/wiki/Apache_Parquet) for more efficient analytics.
   
   



2. Convert 
