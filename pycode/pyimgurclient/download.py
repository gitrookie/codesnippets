import json
import logging
import os
from pathlib import Path
import urllib
from urllib.request import urlopen, Request

# logger objects are never instantiated directly, but always through module
# level function logging.getLogger(name) as follows
logger = logging.getLogger(__name__)

# Authorization is standard http header(like Host, Content-Type) which specifies
# credentials for http authentication.
def get_links(client_id):
    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    req = Request("https://api.imgur.com/3/gallery/", headers=headers,
                  method="GET")
    with urlopen(req) as resp:
        data = json.loads(resp.readall().decode('utf-8'))
    return map(lambda item: item['link'], data['data'])


def download_link(directory, link):
    logger.info("Downloading %s", link)
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.readall())


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir
