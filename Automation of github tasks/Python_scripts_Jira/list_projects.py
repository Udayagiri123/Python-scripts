import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gsnugiri.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0LND93pbP7vSLMloagXDxmbZ6LF-j7buOtLDDGbwnGfukWNy_4_cNQjtNGaww9LzA30J6B5xdrcEs4PFr_pziSmE2eY_5gOBeNAxZCFGBjlBJtkwBU2RFDVBFmg5ZVrPb7CtMhCbBYwqb7j5JiueJ60yE28xia6wmM-BNSf9h89M=5481C161"

auth = HTTPBasicAuth("gsnugiri@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

for i in output :
 print(i["name"])