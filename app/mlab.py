import requests
import json
import logging
import sys

from config import MLAB_API_KEY

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def read_from_mlab(**kwargs):
    q = {}
    if kwargs.get('caption'):
        q['caption'] = kwargs.get('caption')
    if kwargs.get('description'):
        q['description'] = kwargs.get('description')
    if kwargs.get('image_url'):
        q['image_url'] = kwargs.get('image_url')

    api_key = MLAB_API_KEY
    url_base = 'https://api.mlab.com/api/1/databases/sellsnapshots-test/collections/photos?q='
    url = url_base  + json.dumps(q) + '&apiKey='+ api_key

    logging.info("Read api call to mlab")
    response = requests.get(url)
    search_results = response.json()
    status_code = response.status_code
    logging.info("status code of read:" + str(status_code))

    return search_results, status_code
