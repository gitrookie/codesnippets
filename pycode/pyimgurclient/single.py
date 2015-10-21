import logging
import os
from time import time

 from download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s -%(levelname)s -\
                    %(message)s")
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    print("In Main")
    ts = time()
    download_dir = setup_download_dir()
    links = [l for l in get_links('c53645e1e12ad62') if l.endswith('.jpg')]
    for link in links:
        download_link(download_dir, link)
    print('Took {}s'.format(time() -ts))

# if __name__ == "main":
main()
