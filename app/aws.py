import requests
from flask import current_app
from flask_login import current_user
import boto3
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def get_presigned_url(image_name):
    s3 = boto3.client('s3')
    presigned_url = s3.generate_presigned_url(
        ClientMethod = 'delete_object',
        Params = {
            'Bucket': current_app.config['S3_BUCKET'],
            'Key':current_user.user_url + '/' + image_name
        }
    )

    return presigned_url    

def delete_from_s3(image_name):
    logging.info('in delete_from_s3')
    presigned_url = get_presigned_url(image_name)
    logging.info('presigned url is {}'.format(presigned_url))
    r = requests.delete(presigned_url)
    logging.info('delete status code: {}'.format(r.status_code))
    return r.status_code

