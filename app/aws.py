from requests import request

def delete_from_s3(presigned_url):
    r = request.delete(presigned_url)
    return r.status_code
