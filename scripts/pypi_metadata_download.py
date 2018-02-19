import sys
import asyncio
import gzip
import json
from pathlib import Path
import xmlrpc.client

from aiohttp import ClientSession


# adapted from https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html  # noqa


def get_packages():
    client = xmlrpc.client.ServerProxy('https://pypi.python.org/pypi')
    packages = client.list_packages()
    return packages


async def fetch(out_dir, name, session):
    BASE_URL = "https://pypi.org/pypi/{}/json"
    url = BASE_URL.format(name)
    async with session.get(url) as response:
        sys.stdout.write('.')
        sys.stdout.flush()
        if response.status != 200:
            return
        try:
            res = await response.json()
            with gzip.open(str(out_dir / name) + ".json.gz", 'wt') as fh:
                json.dump(res, fh)
        except:  # noqa
            print(f'{name} failed')
            raise


async def bound_fetch(sem, out_dir, name, session):
    # Getter function with semaphore.
    async with sem:
        await fetch(out_dir, name, session)


async def run(packages, n_channels, out_dir):
    tasks = []
    # create instance of Semaphore
    # to limit the number of concurent calls
    sem = asyncio.Semaphore(n_channels)

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        for name in packages:
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(
                    bound_fetch(sem, out_dir, name, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses

if __name__ == '__main__':

    # number of parallel downloads
    n_channels = 50
    out_dir = Path('..') / 'data' / 'pypi_metadata'

    if not out_dir.exists():
        out_dir.mkdir(parents=True)

    packages = get_packages()
    print('Downloaded a list of %s PyPi packages...' % len(packages))

    print('Starting PyPi metadata download with %s parallel connections...'
          % n_channels)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(packages, n_channels, out_dir))
    loop.run_until_complete(future)
