import logging

class s3_mlab_upload():

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def s3_upload(self):
        self.logger.info('Uploading photo to s3')

    def mlab_upload(self):
        self.logger.info('Uploading photo data to mlab')

if __name__ == '__main__':
    s3_mlab_upload = s3_mlab_upload()
    s3_mlab_upload.s3_upload()
    s3_mlab_upload.mlab_upload()
