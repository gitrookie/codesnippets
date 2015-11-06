import json
import logging
import os
from pathlib import Path
import urllib
from urllib.request import urlopen, Request


req = Request("https://api.launchpad.net/devel/hplip",
              method="findSimilarQuestions")
# req = Request("https://api.launchpad.net/devel/bugs/1512166", method="GET")
https://api.launchpad.net/devel/hplip/+question/59808
with urlopen(req) as resp:
    data = json.loads(resp.readall().decode('utf-8'))
print(data)
