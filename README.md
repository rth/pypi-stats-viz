# pypi-stats-viz

Tools for PyPi analysis

## PyPi metadata

   PyPi metadata (including project description, release information etc) for all ~130000 Python packages uploaded to PyPi are  provided for research purposes as part of this project. Files are provided in a gzip compressed JSON format.


* February 11th, 2018 - <a href="https://s3-eu-west-1.amazonaws.com/public-sym/pypi-stats-viz/pypi-metadata-anonymized-2018-02-11.tar.xz" rel="nofollow">`pypi-metadata-anonymized-2018-02-11.tar.xz`</a> (309 MB xz compressed, 119008 packages)
* February 19th, 2018 - <a href="https://s3-eu-west-1.amazonaws.com/public-sym/pypi-stats-viz/pypi-metadata-anonymized-2018-02-19.tar.xz" rel="nofollow">`pypi-metadata-anonymized-2018-02-11.tar.xz`</a> (318 MB xz compressed, 128712 packages)

 These datasets are obtained by running the `pypi_metadata_download.py` download script (see below), followed by `pypi_metadata_anonymize.py` script to remove author email information for privacy reasons.


## Scripts

1. [`pypi_metadata_download.py`](./scripts/pypi_metadata_download.py) - download PyPi metadata for all packages

   The included script uses PyPi JSON API to asynchronously fetch metadata for all Python packages (~130000) uploaded to PyPi. It uses aiohttp (requires Python 3.5+) and takes ~30 min with 50 parallel download
   channels (cf [warehouse/issues/2912(Comment)](https://github.com/pypa/warehouse/issues/2912#issuecomment-364674430) for more details),
   assuming a good internet connection.

2. [`pypi_metadata_json_to_parquet.py`](./scripts/pypi_metadata_json_to_parquet.py) convert the downloaded PyPi metadata from one gzipped JSON per package to Appache parquet format for more efficient analytics.
   
   
2. [`pypi_metadata_anonymize.py`](./scripts/pypi_metadata_anonymize.py) remove the `author_email` fields from the individual jsons.


## Notebooks

1. [`pypi_spam_url_blacklist_matching.ipynb`](./notebooks/pypi_spam_url_blacklist_matching.ipynb): following the [PyPi spam incident in February 2018](https://status.python.org/incidents/mgjw1g5yjy5j) this notebook is a somewhat unsuccessful attempt to detect spam in the uploaded Python packages by matching links contained in the description against blacklisted domain names. 


## Contributing

Please open an issue or a Pull Request for any comments about this repository.
