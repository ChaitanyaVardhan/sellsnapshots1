import logging

import boto3

import os

import json

import requests

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') 

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

MLAB_API_KEY = os.environ.get('MLAB_API_KEY')

DIR = 'tmp'

class s3_mlab_upload():

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.s3 = boto3.client('s3')
        self.BUCKET_NAME = os.environ.get('BUCKET_NAME')

    def get_files(self, dir_name):
        self.path = os.path.join(os.getcwd(),dir_name)
        self.files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

    def s3_upload(self, infile):
        file_name = os.path.join(self.path, infile)
        key_name = 'trublu/' + infile
        self.logger.info('Uploading photo to s3')
        with open(file_name, 'rb') as f:
            self.s3.upload_fileobj(f, self.BUCKET_NAME, key_name, ExtraArgs={'ACL': 'public-read', 'ContentType': 'image/jpeg'}, Callback=None)
            self.mlab_upload(key_name)

    def mlab_upload(self, key_name):
        self.logger.info('Uploading photo data to mlab')
        image_url = 'https://s3.amazonaws.com/' + self.BUCKET_NAME + '/' + key_name
        image_data = dict(image_url=image_url)
        api_key = MLAB_API_KEY
        url = 'https://api.mlab.com/api/1/databases/sellsnapshots-test/collections/photos?apiKey=' + api_key
        headers = {'content-type': 'application/json; charset=utf-8'}
        data = json.dumps(image_data)
        response = requests.post(url, data=data, headers=headers)

if __name__ == '__main__':
    s3_mlab_upload = s3_mlab_upload()
    s3_mlab_upload.get_files(DIR)
    s3_mlab_upload.logger.info(len(s3_mlab_upload.files))    
    count = 0
    for f in s3_mlab_upload.files:
        s3_mlab_upload.logger.info(f)
        s3_mlab_upload.s3_upload(f)
        ++count
    s3_mlab_upload.logger.info('no of files uploaded: ' + str(count))
