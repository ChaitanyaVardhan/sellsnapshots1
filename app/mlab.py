import requests
import json
import logging
import sys

from config import MLAB_API_KEY
from config import MLAB_DB_BASE_URL

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def read_from_mlab(coll=None, **kwargs):
    q = {}

    for key in kwargs:
        q[key] = kwargs[key]

    api_key = MLAB_API_KEY
    url_base = MLAB_DB_BASE_URL
    url = url_base + coll + '?q='  + json.dumps(q) + '&apiKey='+ api_key

    logging.info("Read api call to mlab")
    logging.info("url: " + url)
    response = requests.get(url)
    search_results = response.json()
    status_code = response.status_code
    logging.info("status code of read:" + str(status_code))

    return search_results, status_code
