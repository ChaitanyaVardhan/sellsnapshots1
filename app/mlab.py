import requests

base_url = 'https://api.mlab.com/api/1/'

api_key = app.config['mlab_api_key']
def read_from_mlab(params):
    r = requests.get(url)
    
