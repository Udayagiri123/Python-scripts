# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gsnugiri.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0LND93pbP7vSLMloagXDxmbZ6LF-j7buOtLDDGbwnGfukWNy_4_cNQjtNGaww9LzA30J6B5xdrcEs4PFr_pziSmE2eY_5gOBeNAxZCFGBjlBJtkwBU2RFDVBFmg5ZVrPb7CtMhCbBYwqb7j5JiueJ60yE28xia6wmM-BNSf9h89M=5481C161"

auth = HTTPBasicAuth("gsnugiri@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira tckt",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10046"
    },
    "project": {
      "id": "10034"
    },
    "summary": "Main order flow broken",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))