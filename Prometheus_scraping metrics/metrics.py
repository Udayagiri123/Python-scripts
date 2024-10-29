import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://52.91.25.244:9090/graph"

response = requests.request(
   "GET",
   url
)

print(response.text)