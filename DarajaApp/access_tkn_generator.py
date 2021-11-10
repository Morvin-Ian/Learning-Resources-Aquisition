import requests
from requests.auth import HTTPBasicAuth
from .credentials import acess_token_url,consumer_key,consumer_secrete

def generate_access_token():
    response = requests.request("GET", acess_token_url, auth=HTTPBasicAuth(consumer_key,consumer_secrete))    
    res_json = response.json()
    #Filtering out the expiry date that is returned together with the access as a response 
    filtered_access_token = res_json['access_token'] 
    return filtered_access_token